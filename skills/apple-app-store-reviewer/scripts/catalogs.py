#!/usr/bin/env python3
"""Pinned deterministic catalogs for the Apple App Store Reviewer skill.

Keep this file synchronized with references/source-catalog.json. Values are
conservative: a match can prove that an artifact is structurally acceptable,
but a non-match should not be treated as an Apple policy decision without
checking the current official source.
"""

from __future__ import annotations

from collections.abc import Iterable

APPLE_GUIDELINES_URL = "https://developer.apple.com/app-store/review/guidelines/"
APPLE_UPCOMING_REQUIREMENTS_URL = "https://developer.apple.com/news/upcoming-requirements/"
APPLE_SCREENSHOT_SPEC_URL = (
    "https://developer.apple.com/help/app-store-connect/reference/app-information/"
    "screenshot-specifications"
)
APPLE_METADATA_REFERENCE_URL = (
    "https://developer.apple.com/help/app-store-connect/reference/app-information/app-information"
)
APPLE_REQUIRED_PROPERTIES_URL = (
    "https://developer.apple.com/help/app-store-connect/reference/app-information/"
    "required-localizable-and-editable-properties"
)
APPLE_AGE_RATING_URL = (
    "https://developer.apple.com/help/app-store-connect/manage-app-information/set-an-app-age-rating"
)
APPLE_AGE_RATING_DEFINITIONS_URL = (
    "https://developer.apple.com/help/app-store-connect/reference/app-information/"
    "age-ratings-values-and-definitions"
)
APPLE_ACCOUNT_DELETION_URL = (
    "https://developer.apple.com/support/offering-account-deletion-in-your-app/"
)
APPLE_PRIVACY_MANIFEST_URL = (
    "https://developer.apple.com/documentation/bundleresources/privacy_manifest_files"
)
APPLE_THIRD_PARTY_SDK_URL = (
    "https://developer.apple.com/support/third-party-SDK-requirements/"
)
APPLE_REQUIRED_REASON_API_URL = (
    "https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/"
    "describing_use_of_required_reason_api"
)
APPLE_SUBSCRIPTION_URL = "https://developer.apple.com/app-store/subscriptions/"
APPLE_HIG_GENERATIVE_AI_URL = "https://developer.apple.com/design/human-interface-guidelines/generative-ai"
APPLE_FOUNDATION_MODELS_AUP_URL = (
    "https://developer.apple.com/apple-intelligence/acceptable-use-requirements-for-the-foundation-models-framework/"
)

# Accepted screenshot dimensions, pinned 2026-08-25. Both orientations are
# included explicitly so callers can use a simple tuple lookup.
SCREENSHOT_DIMENSIONS: dict[str, set[tuple[int, int]]] = {
    "iphone-6.9": {
        (1260, 2736), (2736, 1260),
        (1290, 2796), (2796, 1290),
        (1320, 2868), (2868, 1320),
    },
    "iphone-6.5": {
        (1284, 2778), (2778, 1284),
        (1242, 2688), (2688, 1242),
    },
    "iphone-6.3": {
        (1179, 2556), (2556, 1179),
        (1206, 2622), (2622, 1206),
    },
    "iphone-6.1": {
        (1170, 2532), (2532, 1170),
        (1125, 2436), (2436, 1125),
        (1080, 2340), (2340, 1080),
    },
    "iphone-5.5": {(1242, 2208), (2208, 1242)},
    "iphone-4.7": {(750, 1334), (1334, 750)},
    "iphone-4": {
        (640, 1096), (640, 1136), (1136, 600), (1136, 640),
    },
    "iphone-3.5": {
        (640, 920), (640, 960), (960, 600), (960, 640),
    },
    "ipad-13": {
        (2064, 2752), (2752, 2064),
        (2048, 2732), (2732, 2048),
    },
    "ipad-12.9": {(2048, 2732), (2732, 2048)},
    "ipad-11": {
        (1488, 2266), (2266, 1488),
        (1668, 2420), (2420, 1668),
        (1668, 2388), (2388, 1668),
        (1640, 2360), (2360, 1640),
    },
    "ipad-10.5": {(1668, 2224), (2224, 1668)},
    "ipad-9.7": {
        (1536, 2008), (1536, 2048), (2048, 1496), (2048, 1536),
        (768, 1004), (768, 1024), (1024, 748), (1024, 768),
    },
    "mac": {(1280, 800), (1440, 900), (2560, 1600), (2880, 1800)},
    "apple-tv": {(1920, 1080), (3840, 2160)},
    "vision-pro": {(3840, 2160)},
    "apple-watch": {
        (422, 514), (410, 502), (416, 496),
        (396, 484), (368, 448), (312, 390),
    },
}

DEVICE_FAMILY_GROUPS: dict[str, set[str]] = {
    "iphone": {key for key in SCREENSHOT_DIMENSIONS if key.startswith("iphone-")},
    "ipad": {key for key in SCREENSHOT_DIMENSIONS if key.startswith("ipad-")},
    "mac": {"mac"},
    "apple-tv": {"apple-tv"},
    "vision-pro": {"vision-pro"},
    "apple-watch": {"apple-watch"},
}

# Apple currently requires the newest iPhone display set, with 6.5 accepted as
# the fallback when 6.9 is absent; iPad uses 13-inch. Other platforms have one
# generic required family.
REQUIRED_SCREENSHOT_COVERAGE: dict[str, tuple[set[str], ...]] = {
    "iphone": ({"iphone-6.9"}, {"iphone-6.5"}),
    "ipad": ({"ipad-13"},),
    "mac": ({"mac"},),
    "apple-tv": ({"apple-tv"},),
    "vision-pro": ({"vision-pro"},),
    "apple-watch": ({"apple-watch"},),
}

METADATA_LIMITS = {
    "name_min_chars": 2,
    "name_max_chars": 30,
    "subtitle_max_chars": 30,
    "promotional_text_max_chars": 170,
    "description_max_chars": 4000,
    "whats_new_max_chars": 4000,
    "keywords_max_utf8_bytes": 100,
    "review_notes_max_utf8_bytes": 4000,
}

# Privacy-sensitive APIs commonly inferred from source. This is intentionally
# broader than one language/framework. Keys are Info.plist purpose strings.
PERMISSION_USAGE_KEYS: dict[str, tuple[str, ...]] = {
    "camera": ("NSCameraUsageDescription",),
    "microphone": ("NSMicrophoneUsageDescription",),
    "photo-library": ("NSPhotoLibraryUsageDescription",),
    "photo-library-add": ("NSPhotoLibraryAddUsageDescription",),
    "contacts": ("NSContactsUsageDescription",),
    "calendars": ("NSCalendarsUsageDescription", "NSCalendarsFullAccessUsageDescription", "NSCalendarsWriteOnlyAccessUsageDescription"),
    "reminders": ("NSRemindersUsageDescription", "NSRemindersFullAccessUsageDescription"),
    "location": ("NSLocationWhenInUseUsageDescription", "NSLocationAlwaysAndWhenInUseUsageDescription"),
    "location-always": ("NSLocationAlwaysAndWhenInUseUsageDescription",),
    "bluetooth": ("NSBluetoothAlwaysUsageDescription", "NSBluetoothPeripheralUsageDescription"),
    "motion": ("NSMotionUsageDescription",),
    "health": ("NSHealthShareUsageDescription", "NSHealthUpdateUsageDescription"),
    "homekit": ("NSHomeKitUsageDescription",),
    "local-network": ("NSLocalNetworkUsageDescription",),
    "face-id": ("NSFaceIDUsageDescription",),
    "speech-recognition": ("NSSpeechRecognitionUsageDescription",),
    "media-library": ("NSAppleMusicUsageDescription",),
    "tracking": ("NSUserTrackingUsageDescription",),
    "nearby-interaction": ("NSNearbyInteractionUsageDescription",),
    "sensitive-content-analysis": ("NSSensitiveContentAnalysisUsageDescription",),
}

PERMISSION_SOURCE_PATTERNS: dict[str, tuple[str, ...]] = {
    "camera": ("AVCaptureDevice", "UIImagePickerController.SourceType.camera", "PHPickerConfiguration"),
    "microphone": ("requestRecordPermission", "AVAudioSession", "SFSpeechAudioBufferRecognitionRequest"),
    "photo-library": ("PHPhotoLibrary", "PHPickerViewController", "PhotosPicker"),
    "contacts": ("CNContactStore", "ContactsUI"),
    "calendars": ("EKEventStore", "EventKit"),
    "reminders": ("EKEntityType.reminder", "EKEntityTypeReminder"),
    "location": ("CLLocationManager", "requestWhenInUseAuthorization", "requestAlwaysAuthorization"),
    "bluetooth": ("CBCentralManager", "CBPeripheralManager", "CoreBluetooth"),
    "motion": ("CMMotionManager", "CMPedometer", "CoreMotion"),
    "health": ("HKHealthStore", "HealthKit"),
    "homekit": ("HMHomeManager", "HomeKit"),
    "local-network": ("NWBrowser", "NetServiceBrowser", "bonjour"),
    "face-id": ("LABiometryType.faceID", "biometryType == .faceID"),
    "speech-recognition": ("SFSpeechRecognizer", "SpeechRecognizer"),
    "media-library": ("MPMediaLibrary", "MusicKit"),
    "tracking": ("ATTrackingManager", "requestTrackingAuthorization"),
    "nearby-interaction": ("NISession", "NearbyInteraction"),
    "sensitive-content-analysis": ("SCSensitivityAnalyzer", "SensitiveContentAnalysis"),
}

# Approved-reason identifiers pinned from Apple's required-reason API catalog.
# The script validates syntax and known categories; it does not decide that a
# stated reason truthfully matches behavior, which still requires manual review.
REQUIRED_REASON_API_CATEGORIES: dict[str, set[str]] = {
    "NSPrivacyAccessedAPICategoryFileTimestamp": {"C617.1", "3B52.1", "0A2A.1", "DDA9.1"},
    "NSPrivacyAccessedAPICategorySystemBootTime": {"35F9.1", "8FFB.1"},
    "NSPrivacyAccessedAPICategoryDiskSpace": {"E174.1", "85F4.1", "7D9E.1", "B728.1"},
    "NSPrivacyAccessedAPICategoryActiveKeyboards": {"3EC4.1", "54BD.1"},
    "NSPrivacyAccessedAPICategoryUserDefaults": {"CA92.1", "1C8F.1", "C56D.1", "AC6B.1"},
}

REQUIRED_REASON_SOURCE_PATTERNS: dict[str, tuple[str, ...]] = {
    "NSPrivacyAccessedAPICategoryFileTimestamp": (
        "creationDate", "contentModificationDate", "fileModificationDate", "stat(", "lstat(", "fstat(",
    ),
    "NSPrivacyAccessedAPICategorySystemBootTime": (
        "systemUptime", "mach_absolute_time", "kern.boottime", "ProcessInfo.processInfo.systemUptime",
    ),
    "NSPrivacyAccessedAPICategoryDiskSpace": (
        "volumeAvailableCapacity", "systemFreeSize", "systemSize", "fileSystemAttributes", "statfs(",
    ),
    "NSPrivacyAccessedAPICategoryActiveKeyboards": (
        "activeInputModes", "UITextInputMode.activeInputModes",
    ),
    "NSPrivacyAccessedAPICategoryUserDefaults": (
        "UserDefaults", "NSUserDefaults", "CFPreferences",
    ),
}

# SDKs on Apple's signature/privacy-manifest list. Names are normalized for
# broad path matching; false positives are reported as review signals rather
# than automatic blockers unless an embedded framework is directly observed.
LISTED_THIRD_PARTY_SDKS: tuple[str, ...] = tuple(sorted({
    "Abseil", "AFNetworking", "Alamofire", "AppAuth", "BoringSSL", "openssl_grpc",
    "Capacitor", "Charts", "connectivity_plus", "Cordova", "device_info_plus",
    "DKImagePickerController", "DKPhotoGallery", "FBAEMKit", "FBLPromises",
    "FBSDKCoreKit", "FBSDKCoreKit_Basics", "FBSDKLoginKit", "FBSDKShareKit",
    "file_picker", "FirebaseABTesting", "FirebaseAuth", "FirebaseCore",
    "FirebaseCoreDiagnostics", "FirebaseCoreExtension", "FirebaseCoreInternal",
    "FirebaseCrashlytics", "FirebaseDynamicLinks", "FirebaseFirestore",
    "FirebaseInstallations", "FirebaseMessaging", "FirebaseRemoteConfig", "Flutter",
    "flutter_inappwebview", "flutter_local_notifications", "fluttertoast", "FMDB",
    "geolocator_apple", "GoogleDataTransport", "GoogleSignIn", "GoogleToolboxForMac",
    "GoogleUtilities", "grpcpp", "GTMAppAuth", "GTMSessionFetcher", "hermes",
    "image_picker_ios", "IQKeyboardManager", "IQKeyboardManagerSwift", "Kingfisher",
    "leveldb", "Lottie", "MBProgressHUD", "nanopb", "OneSignal", "OneSignalCore",
    "OneSignalExtension", "OneSignalOutcomes", "OpenSSL", "OrderedSet", "package_info",
    "package_info_plus", "path_provider", "path_provider_ios", "Promises", "Protobuf",
    "Reachability", "RealmSwift", "RxCocoa", "RxRelay", "RxSwift", "SDWebImage",
    "share_plus", "shared_preferences_ios", "SnapKit", "sqflite", "Starscream",
    "SVProgressHUD", "SwiftyGif", "SwiftyJSON", "Toast", "UnityFramework",
    "url_launcher", "url_launcher_ios", "video_player_avfoundation", "wakelock",
    "webview_flutter_wkwebview",
}))

AI_PROVIDER_PATTERNS: dict[str, tuple[str, ...]] = {
    "OpenAI": ("api.openai.com", "OpenAI", "ChatGPT", "Responses API"),
    "Anthropic": ("api.anthropic.com", "Anthropic", "Claude"),
    "Google Gemini": ("generativelanguage.googleapis.com", "VertexAI", "GoogleGenerativeAI", "Gemini"),
    "Azure OpenAI": ("openai.azure.com", "AzureOpenAI"),
    "AWS Bedrock": ("bedrock-runtime", "BedrockRuntime"),
    "Mistral": ("api.mistral.ai", "MistralAI"),
    "Cohere": ("api.cohere.com", "Cohere"),
    "Perplexity": ("api.perplexity.ai", "Perplexity"),
    "Replicate": ("api.replicate.com", "Replicate"),
    "Hugging Face": ("api-inference.huggingface.co", "HuggingFace"),
    "Together AI": ("api.together.xyz", "TogetherAI"),
    "xAI": ("api.x.ai", "xAI", "Grok"),
    "Stability AI": ("api.stability.ai", "StabilityAI"),
    "ElevenLabs": ("api.elevenlabs.io", "ElevenLabs"),
}

FOUNDATION_MODELS_PATTERNS = (
    "import FoundationModels", "LanguageModelSession", "SystemLanguageModel", "@Generable",
)

PAYMENT_PATTERNS: dict[str, tuple[str, ...]] = {
    "storekit": ("import StoreKit", "Product.products", "SKPaymentQueue", "Transaction.currentEntitlements"),
    "revenuecat": ("Purchases.configure", "RevenueCat", "Purchases.shared"),
    "stripe": ("StripeSDK", "StripePaymentSheet", "buy.stripe.com", "stripe.com"),
    "paddle": ("Paddle", "paddle.com", "PaddleCheckout"),
    "paypal": ("PayPal", "paypal.com"),
    "external_checkout": ("checkout_url", "checkoutURL", "purchase externally", "buy on the web"),
}

PRIVATE_OR_DEPRECATED_PATTERNS = (
    "UIWebView", "LSApplicationWorkspace", "_statusBar", "dlopen(", "dlsym(", "class-dump",
)

DYNAMIC_CODE_PATTERNS = (
    "NSClassFromString", "dlopen(", "dlsym(", "JavaScriptCore", "WKUserScript", "eval(", "Function(",
)

PLACEHOLDER_PATTERNS = (
    "lorem ipsum", "todo:", "fixme:", "example.com", "localhost", "127.0.0.1",
    "staging.", "dev.", "test account", "sample text", "coming soon", "under construction",
)

SECRET_PATTERNS: tuple[tuple[str, str], ...] = (
    ("OpenAI/API key", r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b"),
    ("Google API key", r"\bAIza[0-9A-Za-z_-]{30,}\b"),
    ("AWS access key", r"\bAKIA[0-9A-Z]{16}\b"),
    ("GitHub token", r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    ("Stripe secret", r"\bsk_(?:live|test)_[A-Za-z0-9]{16,}\b"),
    ("Private key", r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
)

TEXT_EXTENSIONS = {
    ".swift", ".m", ".mm", ".h", ".hpp", ".c", ".cc", ".cpp",
    ".plist", ".xcprivacy", ".entitlements", ".strings", ".stringsdict",
    ".json", ".yaml", ".yml", ".toml", ".xml", ".md", ".txt",
    ".js", ".jsx", ".ts", ".tsx", ".dart", ".kt", ".kts", ".java",
    ".rb", ".py", ".sh", ".html", ".htm", ".css", ".xcconfig",
    ".pbxproj", ".lock", ".podspec", ".gradle", ".properties",
}

IGNORED_DIRECTORY_NAMES = {
    ".git", ".hg", ".svn", ".idea", ".vscode", "DerivedData", "build", ".build",
    "node_modules", "Pods", "Carthage", ".swiftpm", "vendor", "coverage", ".pytest_cache",
    "__pycache__", "dist", ".dart_tool", ".gradle", "xcuserdata",
}

INFO_PLIST_NAMES = {"Info.plist", "info.plist"}
PRIVACY_MANIFEST_NAME = "PrivacyInfo.xcprivacy"


def groups_for_dimensions(width: int, height: int) -> list[str]:
    """Return every accepted screenshot group matching an exact dimension."""
    size = (int(width), int(height))
    return sorted(group for group, values in SCREENSHOT_DIMENSIONS.items() if size in values)


def contains_any(text: str, needles: Iterable[str]) -> bool:
    lowered = text.casefold()
    return any(needle.casefold() in lowered for needle in needles)
