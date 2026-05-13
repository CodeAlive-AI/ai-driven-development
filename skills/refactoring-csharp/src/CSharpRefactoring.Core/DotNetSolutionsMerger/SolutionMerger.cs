using System.Globalization;
using Microsoft.VisualStudio.SolutionPersistence.Model;
using Microsoft.VisualStudio.SolutionPersistence.Serializer;

namespace DotNetSolutionsMerger;

public enum MissingProjectPolicy
{
    SkipWithWarning,
    Error
}

public enum DuplicateProjectPolicy
{
    MergeMetadata,
    Skip,
    Error
}

public sealed record SolutionMergeOptions
{
    public bool IncludeStandaloneProjectsWhenExpandingDirectories { get; init; } = true;
    public bool GroupProjectsBySourceSolution { get; init; } = true;
    public bool PreserveInputSolutionFolders { get; init; } = true;
    public bool GroupStandaloneProjectsByDirectory { get; init; } = true;
    public bool DistillProjectConfigurations { get; init; } = true;
    public bool ValidateRoundTrip { get; init; } = true;
    public MissingProjectPolicy MissingProjectPolicy { get; init; } = MissingProjectPolicy.SkipWithWarning;
    public DuplicateProjectPolicy DuplicateProjectPolicy { get; init; } = DuplicateProjectPolicy.MergeMetadata;
    public IEqualityComparer<string> PathComparer { get; init; } = StringComparer.OrdinalIgnoreCase;
    public IReadOnlySet<string> ExcludedDirectoryNames { get; init; } = new HashSet<string>(StringComparer.OrdinalIgnoreCase)
    {
        ".git", ".hg", ".svn", ".vs", ".idea", ".vscode", "bin", "obj", "node_modules", "packages"
    };
    public Action<string>? Log { get; init; }
}

public sealed record SolutionMergeResult(
    string OutputPath,
    int SourceSolutionCount,
    int AddedProjectCount,
    int DuplicateProjectCount,
    IReadOnlyList<string> AddedProjects,
    IReadOnlyList<string> SkippedProjects,
    IReadOnlyList<string> Warnings);

public sealed class SolutionMerger
{
    private static readonly HashSet<string> SolutionExtensions = new(StringComparer.OrdinalIgnoreCase)
    {
        ".sln", ".slnx"
    };

    private static readonly HashSet<string> ProjectExtensions = new(StringComparer.OrdinalIgnoreCase)
    {
        ".csproj", ".vbproj", ".fsproj", ".vcxproj", ".shproj", ".sqlproj", ".dbproj", ".wixproj", ".wapproj", ".esproj", ".njsproj", ".proj"
    };

    private readonly IReadOnlyList<string> _inputs;
    private readonly string _outputPath;
    private readonly SolutionMergeOptions _options;

    public SolutionMerger(IEnumerable<string> inputs, string outputPath, SolutionMergeOptions? options = null)
    {
        ArgumentNullException.ThrowIfNull(inputs);
        ArgumentException.ThrowIfNullOrWhiteSpace(outputPath);

        _inputs = inputs.Where(static p => !string.IsNullOrWhiteSpace(p)).ToArray();
        if (_inputs.Count == 0)
        {
            throw new ArgumentException("At least one input solution, project, or directory is required.", nameof(inputs));
        }

        _outputPath = outputPath;
        _options = options ?? new SolutionMergeOptions();
    }

    public static Task<SolutionMergeResult> MergeDirectoryAsync(
        string inputDirectory,
        string outputSolutionPath,
        SolutionMergeOptions? options = null,
        CancellationToken cancellationToken = default)
    {
        ArgumentException.ThrowIfNullOrWhiteSpace(inputDirectory);
        return new SolutionMerger(new[] { inputDirectory }, outputSolutionPath, options).MergeAsync(cancellationToken);
    }

    public static Task<SolutionMergeResult> MergeAsync(
        IEnumerable<string> inputs,
        string outputSolutionPath,
        SolutionMergeOptions? options = null,
        CancellationToken cancellationToken = default)
    {
        return new SolutionMerger(inputs, outputSolutionPath, options).MergeAsync(cancellationToken);
    }

    public async Task<SolutionMergeResult> MergeAsync(CancellationToken cancellationToken = default)
    {
        string outputFullPath = NormalizeAbsolutePath(EnsureSupportedOutputExtension(_outputPath));
        string outputDirectory = Path.GetDirectoryName(outputFullPath)
            ?? throw new InvalidOperationException($"Unable to determine the output directory for '{outputFullPath}'.");

        Directory.CreateDirectory(outputDirectory);

        List<string> warnings = [];
        List<string> addedProjects = [];
        List<string> skippedProjects = [];
        List<SourceSolution> sourceSolutions = [];
        List<StandaloneProjectSource> standaloneProjects = [];

        foreach (DiscoveredInput input in DiscoverInputs(outputFullPath))
        {
            cancellationToken.ThrowIfCancellationRequested();

            string extension = Path.GetExtension(input.FilePath);
            if (SolutionExtensions.Contains(extension))
            {
                sourceSolutions.Add(await LoadSolutionAsync(input.FilePath, cancellationToken).ConfigureAwait(false));
            }
            else if (ProjectExtensions.Contains(extension))
            {
                standaloneProjects.Add(new StandaloneProjectSource(input.FilePath, input.ScanRoot));
            }
            else
            {
                warnings.Add($"Unsupported input ignored: {input.FilePath}");
            }
        }

        if (sourceSolutions.Count == 0 && standaloneProjects.Count == 0)
        {
            throw new InvalidOperationException("No .sln, .slnx, or supported project files were found.");
        }

        SolutionModel merged = new()
        {
            Description = "Merged solution generated by DotNetSolutionsMerger."
        };

        MergeProjectTypes(merged, sourceSolutions);
        MergeSolutionBuildDimensions(merged, sourceSolutions);

        Dictionary<string, SolutionProjectModel> projectsByAbsolutePath = new(_options.PathComparer);
        Dictionary<SolutionProjectModel, SolutionProjectModel> sourceToTargetProject = [];
        HashSet<string> usedTopLevelFolders = new(StringComparer.OrdinalIgnoreCase);

        foreach (SourceSolution source in sourceSolutions)
        {
            string sourceDirectory = Path.GetDirectoryName(source.FilePath)
                ?? throw new InvalidOperationException($"Unable to determine the source directory for '{source.FilePath}'.");

            string? sourceRootFolder = null;
            if (_options.GroupProjectsBySourceSolution)
            {
                string baseFolderName = SafeSolutionFolderSegment(Path.GetFileNameWithoutExtension(source.FilePath));
                sourceRootFolder = CreateUniqueFolderPath(baseFolderName, usedTopLevelFolders);
            }


            foreach (SolutionProjectModel sourceProject in source.Model.SolutionProjects)
            {
                cancellationToken.ThrowIfCancellationRequested();

                SolutionFolderModel? targetFolder = GetTargetFolder(merged, sourceProject.Parent, sourceRootFolder);
                SolutionProjectModel? targetProject = AddOrMergeProject(
                    merged,
                    sourceProject,
                    sourceDirectory,
                    outputDirectory,
                    targetFolder,
                    projectsByAbsolutePath,
                    addedProjects,
                    skippedProjects,
                    warnings);

                if (targetProject is not null)
                {
                    sourceToTargetProject[sourceProject] = targetProject;
                }
            }
        }

        foreach (SourceSolution source in sourceSolutions)
        {
            foreach (SolutionProjectModel sourceProject in source.Model.SolutionProjects)
            {
                if (!sourceToTargetProject.TryGetValue(sourceProject, out SolutionProjectModel? targetProject) ||
                    sourceProject.Dependencies is null)
                {
                    continue;
                }

                foreach (SolutionProjectModel sourceDependency in sourceProject.Dependencies)
                {
                    if (sourceToTargetProject.TryGetValue(sourceDependency, out SolutionProjectModel? targetDependency) &&
                        !ReferenceEquals(targetProject, targetDependency))
                    {
                        targetProject.AddDependency(targetDependency);
                    }
                }
            }
        }

        foreach (StandaloneProjectSource standalone in standaloneProjects)
        {
            cancellationToken.ThrowIfCancellationRequested();

            AddOrMergeStandaloneProject(
                merged,
                standalone,
                outputDirectory,
                projectsByAbsolutePath,
                addedProjects,
                skippedProjects,
                warnings);
        }

        if (_options.DistillProjectConfigurations)
        {
            merged.DistillProjectConfigurations();
        }

        await SaveAtomicallyAsync(merged, outputFullPath, warnings, cancellationToken).ConfigureAwait(false);

        int duplicateCount = skippedProjects.Count(static item => item.Contains("duplicate", StringComparison.OrdinalIgnoreCase));
        return new SolutionMergeResult(
            outputFullPath,
            sourceSolutions.Count,
            addedProjects.Count,
            duplicateCount,
            addedProjects.AsReadOnly(),
            skippedProjects.AsReadOnly(),
            warnings.AsReadOnly());
    }

    private async Task<SourceSolution> LoadSolutionAsync(string solutionPath, CancellationToken cancellationToken)
    {
        _options.Log?.Invoke($"Reading solution: {solutionPath}");

        var serializer = SolutionSerializers.GetSerializerByMoniker(solutionPath)
            ?? throw new NotSupportedException($"Unsupported solution file extension: '{solutionPath}'.");

        try
        {
            SolutionModel model = await serializer.OpenAsync(solutionPath, cancellationToken).ConfigureAwait(false);
            return new SourceSolution(solutionPath, model);
        }
        catch (SolutionException ex)
        {
            throw new InvalidOperationException($"Failed to parse solution '{solutionPath}': {ex.Message}", ex);
        }
    }

    private IEnumerable<DiscoveredInput> DiscoverInputs(string outputFullPath)
    {
        HashSet<string> yielded = new(_options.PathComparer);

        foreach (string rawInput in _inputs)
        {
            string inputPath = NormalizeAbsolutePath(rawInput);

            if (Directory.Exists(inputPath))
            {
                foreach (DiscoveredInput candidate in EnumerateCandidateFiles(inputPath, outputFullPath))
                {
                    if (yielded.Add(candidate.FilePath))
                    {
                        yield return candidate;
                    }
                }
            }
            else if (File.Exists(inputPath))
            {
                if (!AreSamePath(inputPath, outputFullPath) && yielded.Add(inputPath))
                {
                    yield return new DiscoveredInput(inputPath, ScanRoot: null);
                }
            }
            else
            {
                throw new FileNotFoundException($"Input path does not exist: {rawInput}", rawInput);
            }
        }
    }

    private IEnumerable<DiscoveredInput> EnumerateCandidateFiles(string rootDirectory, string outputFullPath)
    {
        List<DiscoveredInput> solutionFiles = [];
        List<DiscoveredInput> projectFiles = [];
        Stack<string> pendingDirectories = new();
        pendingDirectories.Push(rootDirectory);

        while (pendingDirectories.Count > 0)
        {
            string currentDirectory = pendingDirectories.Pop();

            foreach (string childDirectory in Directory.EnumerateDirectories(currentDirectory).OrderBy(static p => p, StringComparer.OrdinalIgnoreCase))
            {
                if (!IsExcludedDirectory(childDirectory))
                {
                    pendingDirectories.Push(childDirectory);
                }
            }

            foreach (string file in Directory.EnumerateFiles(currentDirectory).OrderBy(static p => p, StringComparer.OrdinalIgnoreCase))
            {
                string fullPath = NormalizeAbsolutePath(file);
                if (AreSamePath(fullPath, outputFullPath))
                {
                    continue;
                }

                string extension = Path.GetExtension(fullPath);
                if (SolutionExtensions.Contains(extension))
                {
                    solutionFiles.Add(new DiscoveredInput(fullPath, rootDirectory));
                }
                else if (_options.IncludeStandaloneProjectsWhenExpandingDirectories && ProjectExtensions.Contains(extension))
                {
                    projectFiles.Add(new DiscoveredInput(fullPath, rootDirectory));
                }
            }
        }

        return solutionFiles
            .OrderBy(static x => x.FilePath, StringComparer.OrdinalIgnoreCase)
            .Concat(projectFiles.OrderBy(static x => x.FilePath, StringComparer.OrdinalIgnoreCase));
    }

    private bool IsExcludedDirectory(string directory)
    {
        string name = Path.GetFileName(directory.TrimEnd(Path.DirectorySeparatorChar, Path.AltDirectorySeparatorChar));
        return _options.ExcludedDirectoryNames.Contains(name);
    }

    private void MergeProjectTypes(SolutionModel target, IReadOnlyList<SourceSolution> sources)
    {
        List<ProjectType> mergedProjectTypes = [];
        HashSet<string> seenSignatures = new(StringComparer.Ordinal);
        Dictionary<string, string> occupiedKeys = new(StringComparer.OrdinalIgnoreCase);

        foreach (SourceSolution source in sources)
        {
            foreach (ProjectType projectType in source.Model.ProjectTypes)
            {
                string signature = ProjectTypeSignature(projectType);
                foreach (string key in ProjectTypeKeys(projectType))
                {
                    if (occupiedKeys.TryGetValue(key, out string? existingSignature) &&
                        !StringComparer.Ordinal.Equals(existingSignature, signature))
                    {
                        throw new InvalidOperationException(
                            $"Conflicting project type definitions while merging '{source.FilePath}'. Conflict key: {key}.");
                    }
                }

                if (seenSignatures.Add(signature))
                {
                    mergedProjectTypes.Add(projectType);
                    foreach (string key in ProjectTypeKeys(projectType))
                    {
                        occupiedKeys[key] = signature;
                    }
                }
            }
        }

        target.ProjectTypes = mergedProjectTypes;
    }

    private static IEnumerable<string> ProjectTypeKeys(ProjectType projectType)
    {
        if (!string.IsNullOrWhiteSpace(projectType.Name))
        {
            yield return "name:" + projectType.Name;
        }

        if (!string.IsNullOrWhiteSpace(projectType.Extension))
        {
            yield return "extension:" + NormalizeExtension(projectType.Extension);
        }

        if (projectType.ProjectTypeId != Guid.Empty)
        {
            yield return "id:" + projectType.ProjectTypeId.ToString("D", CultureInfo.InvariantCulture);
        }
    }

    private static string ProjectTypeSignature(ProjectType projectType)
    {
        string rules = string.Join(";", projectType.ConfigurationRules.Select(RuleSignature));
        return string.Join(
            "\u001f",
            projectType.Name ?? string.Empty,
            NormalizeExtension(projectType.Extension),
            projectType.ProjectTypeId.ToString("D", CultureInfo.InvariantCulture),
            projectType.BasedOn ?? string.Empty,
            rules);
    }

    private static string RuleSignature(ConfigurationRule rule)
    {
        return string.Join(
            "|",
            rule.Dimension,
            rule.SolutionBuildType,
            rule.SolutionPlatform,
            rule.ProjectValue);
    }

    private static string NormalizeExtension(string? extension)
    {
        if (string.IsNullOrWhiteSpace(extension))
        {
            return string.Empty;
        }

        return extension.StartsWith('.') ? extension : "." + extension;
    }

    private static void MergeSolutionBuildDimensions(SolutionModel target, IReadOnlyList<SourceSolution> sources)
    {
        foreach (SourceSolution source in sources)
        {
            foreach (string buildType in source.Model.BuildTypes)
            {
                target.AddBuildType(buildType);
            }

            foreach (string platform in source.Model.Platforms)
            {
                target.AddPlatform(platform);
            }
        }
    }

    private SolutionFolderModel? GetTargetFolder(
        SolutionModel target,
        SolutionFolderModel? sourceFolder,
        string? sourceRootFolderPath)
    {
        string? folderPath = sourceRootFolderPath;

        if (_options.PreserveInputSolutionFolders && sourceFolder is not null)
        {
            folderPath = CombineSolutionFolderPaths(folderPath, sourceFolder.Path);
        }

        return string.IsNullOrWhiteSpace(folderPath) ? null : target.AddFolder(folderPath);
    }

    private SolutionProjectModel? AddOrMergeProject(
        SolutionModel target,
        SolutionProjectModel sourceProject,
        string sourceDirectory,
        string outputDirectory,
        SolutionFolderModel? targetFolder,
        Dictionary<string, SolutionProjectModel> projectsByAbsolutePath,
        List<string> addedProjects,
        List<string> skippedProjects,
        List<string> warnings)
    {
        if (IsNonLocalPath(sourceProject.FilePath))
        {
            string message = $"Non-local project reference skipped: {sourceProject.FilePath}";
            warnings.Add(message);
            skippedProjects.Add(message);
            return null;
        }

        string absoluteProjectPath = ResolveProjectPath(sourceDirectory, sourceProject.FilePath);
        if (!File.Exists(absoluteProjectPath))
        {
            return HandleMissingProject(sourceProject.FilePath, absoluteProjectPath, skippedProjects, warnings);
        }

        string absoluteKey = NormalizeAbsolutePath(absoluteProjectPath);
        if (projectsByAbsolutePath.TryGetValue(absoluteKey, out SolutionProjectModel? existingProject))
        {
            return HandleDuplicateProject(existingProject, sourceProject, absoluteProjectPath, skippedProjects, warnings);
        }

        string relativeProjectPath = ToSolutionPath(Path.GetRelativePath(outputDirectory, absoluteProjectPath));
        string? projectTypeName = string.IsNullOrWhiteSpace(sourceProject.Type) ? null : sourceProject.Type;

        try
        {
            SolutionProjectModel targetProject = target.AddProject(relativeProjectPath, projectTypeName, targetFolder);
            CopyProjectMetadata(sourceProject, targetProject);

            projectsByAbsolutePath.Add(absoluteKey, targetProject);
            addedProjects.Add(relativeProjectPath);
            _options.Log?.Invoke($"Added project: {relativeProjectPath}");
            return targetProject;
        }
        catch (SolutionException ex)
        {
            throw new InvalidOperationException(
                $"Failed to add project '{sourceProject.FilePath}' from '{sourceDirectory}' to the merged solution. " +
                $"Resolved path: '{relativeProjectPath}'. Error: {ex.Message}",
                ex);
        }
    }

    private void AddOrMergeStandaloneProject(
        SolutionModel target,
        StandaloneProjectSource standalone,
        string outputDirectory,
        Dictionary<string, SolutionProjectModel> projectsByAbsolutePath,
        List<string> addedProjects,
        List<string> skippedProjects,
        List<string> warnings)
    {
        if (!File.Exists(standalone.FilePath))
        {
            _ = HandleMissingProject(standalone.FilePath, standalone.FilePath, skippedProjects, warnings);
            return;
        }

        string absoluteKey = NormalizeAbsolutePath(standalone.FilePath);
        if (projectsByAbsolutePath.ContainsKey(absoluteKey))
        {
            string message = $"Skipped duplicate standalone project: {standalone.FilePath}";
            skippedProjects.Add(message);
            warnings.Add(message);
            return;
        }

        string relativeProjectPath = ToSolutionPath(Path.GetRelativePath(outputDirectory, standalone.FilePath));
        SolutionFolderModel? targetFolder = null;

        if (_options.GroupStandaloneProjectsByDirectory)
        {
            string? folderPath = GetStandaloneProjectFolderPath(standalone);
            targetFolder = string.IsNullOrWhiteSpace(folderPath) ? null : target.AddFolder(folderPath);
        }

        try
        {
            SolutionProjectModel targetProject = target.AddProject(relativeProjectPath, projectTypeName: null, folder: targetFolder);
            projectsByAbsolutePath.Add(absoluteKey, targetProject);
            addedProjects.Add(relativeProjectPath);
            _options.Log?.Invoke($"Added standalone project: {relativeProjectPath}");
        }
        catch (SolutionException ex)
        {
            throw new InvalidOperationException(
                $"Failed to add standalone project '{standalone.FilePath}'. Resolved path: '{relativeProjectPath}'. Error: {ex.Message}",
                ex);
        }
    }

    private SolutionProjectModel? HandleMissingProject(
        string originalPath,
        string resolvedPath,
        List<string> skippedProjects,
        List<string> warnings)
    {
        string message = $"Project file not found; skipped '{originalPath}' resolved as '{resolvedPath}'.";
        if (_options.MissingProjectPolicy == MissingProjectPolicy.Error)
        {
            throw new FileNotFoundException(message, resolvedPath);
        }

        skippedProjects.Add(message);
        warnings.Add(message);
        return null;
    }

    private SolutionProjectModel HandleDuplicateProject(
        SolutionProjectModel existingProject,
        SolutionProjectModel sourceProject,
        string absoluteProjectPath,
        List<string> skippedProjects,
        List<string> warnings)
    {
        string message = $"Skipped duplicate project '{absoluteProjectPath}' already present as '{existingProject.FilePath}'.";

        switch (_options.DuplicateProjectPolicy)
        {
            case DuplicateProjectPolicy.Error:
                throw new InvalidOperationException(message);

            case DuplicateProjectPolicy.Skip:
                skippedProjects.Add(message);
                warnings.Add(message);
                return existingProject;

            case DuplicateProjectPolicy.MergeMetadata:
                MergeProjectMetadata(existingProject, sourceProject);
                skippedProjects.Add(message + " Metadata merged.");
                warnings.Add(message + " Metadata merged.");
                return existingProject;

            default:
                throw new ArgumentOutOfRangeException(nameof(_options.DuplicateProjectPolicy));
        }
    }

    private static void CopyProjectMetadata(SolutionProjectModel sourceProject, SolutionProjectModel targetProject)
    {
        targetProject.DisplayName = sourceProject.DisplayName;

        if (sourceProject.ProjectConfigurationRules is not null)
        {
            targetProject.ProjectConfigurationRules = sourceProject.ProjectConfigurationRules.ToArray();
        }
    }

    private static void MergeProjectMetadata(SolutionProjectModel targetProject, SolutionProjectModel sourceProject)
    {
        if (sourceProject.ProjectConfigurationRules is null)
        {
            return;
        }

        List<ConfigurationRule> mergedRules = targetProject.ProjectConfigurationRules?.ToList() ?? [];
        HashSet<string> existing = mergedRules.Select(RuleSignature).ToHashSet(StringComparer.Ordinal);

        foreach (ConfigurationRule rule in sourceProject.ProjectConfigurationRules)
        {
            if (existing.Add(RuleSignature(rule)))
            {
                mergedRules.Add(rule);
            }
        }

        targetProject.ProjectConfigurationRules = mergedRules;
    }

    private async Task SaveAtomicallyAsync(
        SolutionModel model,
        string outputFullPath,
        List<string> warnings,
        CancellationToken cancellationToken)
    {
        string outputDirectory = Path.GetDirectoryName(outputFullPath)
            ?? throw new InvalidOperationException($"Unable to determine output directory for '{outputFullPath}'.");
        string extension = Path.GetExtension(outputFullPath);
        string tempPath = Path.Combine(
            outputDirectory,
            $".{Path.GetFileNameWithoutExtension(outputFullPath)}.{Guid.NewGuid():N}.tmp{extension}");

        var serializer = SolutionSerializers.GetSerializerByMoniker(tempPath)
            ?? throw new NotSupportedException($"Unsupported output solution extension: '{extension}'.");

        try
        {
            _options.Log?.Invoke($"Writing merged solution: {outputFullPath}");
            await serializer.SaveAsync(tempPath, model, cancellationToken).ConfigureAwait(false);

            if (_options.ValidateRoundTrip)
            {
                SolutionModel roundTrip = await serializer.OpenAsync(tempPath, cancellationToken).ConfigureAwait(false);
                if (roundTrip.SolutionProjects.Count != model.SolutionProjects.Count)
                {
                    throw new InvalidOperationException(
                        $"Round-trip validation failed. Expected {model.SolutionProjects.Count} projects; " +
                        $"the saved solution contained {roundTrip.SolutionProjects.Count} projects.");
                }
            }

            File.Move(tempPath, outputFullPath, overwrite: true);
        }
        catch (SolutionException ex)
        {
            throw new InvalidOperationException($"Failed to write solution '{outputFullPath}': {ex.Message}", ex);
        }
        finally
        {
            try
            {
                if (File.Exists(tempPath))
                {
                    File.Delete(tempPath);
                }
            }
            catch (IOException ex)
            {
                warnings.Add($"Temporary file cleanup failed for '{tempPath}': {ex.Message}");
            }
        }
    }

    private string? GetStandaloneProjectFolderPath(StandaloneProjectSource standalone)
    {
        List<string> segments = ["Standalone Projects"];
        string projectDirectory = Path.GetDirectoryName(standalone.FilePath) ?? string.Empty;

        if (!string.IsNullOrWhiteSpace(standalone.ScanRoot))
        {
            string relativeDirectory = Path.GetRelativePath(standalone.ScanRoot, projectDirectory);
            if (relativeDirectory != ".")
            {
                segments.AddRange(SplitPathSegments(relativeDirectory).Select(SafeSolutionFolderSegment));
            }
        }
        else if (!string.IsNullOrWhiteSpace(projectDirectory))
        {
            segments.Add(SafeSolutionFolderSegment(Path.GetFileName(projectDirectory)));
        }

        return ToSolutionFolderPath(segments);
    }

    private static string ResolveProjectPath(string baseDirectory, string projectPath)
    {
        string localPath = ToLocalPath(projectPath);
        return NormalizeAbsolutePath(Path.IsPathRooted(localPath) ? localPath : Path.Combine(baseDirectory, localPath));
    }

    private static bool IsNonLocalPath(string value)
    {
        return Uri.TryCreate(value, UriKind.Absolute, out Uri? uri) && !uri.IsFile;
    }

    private static string ToLocalPath(string path)
    {
        return path.Replace('\\', Path.DirectorySeparatorChar).Replace('/', Path.DirectorySeparatorChar);
    }

    private static string ToSolutionPath(string path)
    {
        return path.Replace('\\', '/').Replace(Path.DirectorySeparatorChar, '/');
    }

    private static string NormalizeAbsolutePath(string path)
    {
        return Path.GetFullPath(path).TrimEnd(Path.DirectorySeparatorChar, Path.AltDirectorySeparatorChar);
    }

    private bool AreSamePath(string left, string right)
    {
        return _options.PathComparer.Equals(NormalizeAbsolutePath(left), NormalizeAbsolutePath(right));
    }

    private static string EnsureSupportedOutputExtension(string outputPath)
    {
        string extension = Path.GetExtension(outputPath);
        if (string.IsNullOrWhiteSpace(extension))
        {
            return outputPath + ".slnx";
        }

        if (!SolutionExtensions.Contains(extension))
        {
            throw new ArgumentException("The output solution path must end with .slnx or .sln.", nameof(outputPath));
        }

        return outputPath;
    }

    private static string CreateUniqueFolderPath(string requestedName, HashSet<string> usedTopLevelFolders)
    {
        string baseName = SafeSolutionFolderSegment(requestedName);
        string candidate = baseName;
        int suffix = 2;

        while (!usedTopLevelFolders.Add(candidate))
        {
            candidate = $"{baseName} ({suffix++})";
        }

        return ToSolutionFolderPath(new[] { candidate });
    }

    private static string CombineSolutionFolderPaths(params string?[] folderPaths)
    {
        List<string> segments = [];
        foreach (string? folderPath in folderPaths)
        {
            if (string.IsNullOrWhiteSpace(folderPath))
            {
                continue;
            }

            segments.AddRange(folderPath.Split('/', StringSplitOptions.RemoveEmptyEntries).Select(SafeSolutionFolderSegment));
        }

        return ToSolutionFolderPath(segments);
    }

    private static string ToSolutionFolderPath(IEnumerable<string> segments)
    {
        string[] safeSegments = segments
            .Where(static segment => !string.IsNullOrWhiteSpace(segment))
            .Select(SafeSolutionFolderSegment)
            .ToArray();

        if (safeSegments.Length == 0)
        {
            throw new ArgumentException("At least one solution-folder segment is required.", nameof(segments));
        }

        return "/" + string.Join('/', safeSegments) + "/";
    }

    private static IEnumerable<string> SplitPathSegments(string path)
    {
        return path.Split(
            [Path.DirectorySeparatorChar, Path.AltDirectorySeparatorChar, '/', '\\'],
            StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);
    }

    private static string SafeSolutionFolderSegment(string value)
    {
        string segment = string.IsNullOrWhiteSpace(value) ? "Folder" : value.Trim();
        Span<char> buffer = segment.Length <= 512 ? stackalloc char[segment.Length] : new char[segment.Length];
        int length = 0;

        foreach (char c in segment)
        {
            buffer[length++] = IsInvalidSolutionFolderChar(c) ? '_' : c;
        }

        string safe = new string(buffer[..length]).Trim();
        safe = string.IsNullOrWhiteSpace(safe) ? "Folder" : safe;

        if (safe is "." or "..")
        {
            safe = "Folder";
        }

        if (IsDosDeviceName(safe))
        {
            safe += "_";
        }

        return safe.Length <= 260 ? safe : safe[..260];
    }

    private static bool IsInvalidSolutionFolderChar(char c)
    {
        return char.IsControl(c) || c is '?' or ':' or '\\' or '/' or '*' or '"' or '<' or '>' or '|';
    }

    private static bool IsDosDeviceName(string value)
    {
        string name = Path.GetFileNameWithoutExtension(value) ?? value;
        if (name.Equals("NUL", StringComparison.OrdinalIgnoreCase) ||
            name.Equals("CON", StringComparison.OrdinalIgnoreCase) ||
            name.Equals("AUX", StringComparison.OrdinalIgnoreCase) ||
            name.Equals("PRN", StringComparison.OrdinalIgnoreCase) ||
            name.Equals("CLOCK$", StringComparison.OrdinalIgnoreCase))
        {
            return true;
        }

        if (name.Length == 4 &&
            (name.StartsWith("COM", StringComparison.OrdinalIgnoreCase) ||
             name.StartsWith("LPT", StringComparison.OrdinalIgnoreCase)) &&
            char.IsDigit(name[3]))
        {
            return name[3] != '0';
        }

        return false;
    }

    private sealed record DiscoveredInput(string FilePath, string? ScanRoot);
    private sealed record SourceSolution(string FilePath, SolutionModel Model);
    private sealed record StandaloneProjectSource(string FilePath, string? ScanRoot);
}
