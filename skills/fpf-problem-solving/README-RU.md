# fpf-problem-solving-skill

[English version (README.md)](README.md)

Skill для AI coding agent по [First Principles Framework (FPF)](https://github.com/ailev/FPF) от [Анатолия Левенчука](https://github.com/ailev).

FPF — трансдисциплинарная архитектура рассуждения для системной инженерии, координации знаний и смешанных human/AI-команд.

FPF работает как **усилитель мышления**: помогает глубже планировать и принимать более качественные решения через систематическое исследование релевантных альтернатив, а не фиксацию на первом варианте.

## Как это работает

Skill работает как **agentic RAG**: retrieval-augmented generation, где поиск выполняет сам агент без внешней векторной базы и embedding pipeline. Спецификация FPF примерно на 82 000 строк разделена на двухуровневую иерархию: 20 директорий и 269 файлов. `SKILL.md` содержит router по thinking verbs, который сопоставляет намерение пользователя с нужной секцией: решения, причинность, временные рассуждения, описание архитектуры, стабильность публикаций, обновление SoTA-паков, provenance и другие задачи. Затем агент читает `_index.md`, выбирает самый узкий подраздел и загружает только его в контекст. Агент одновременно является retriever, router и reasoner.

## Установка

```bash
npx skills add CodeAlive-AI/fpf-problem-solving-skill -g
```

## Структура

```text
sections/
  04-part-a-kernel-architecture-cluster/
    _index.md                          # TOC с описаниями всех подразделов
    01-a-0---onboarding-glossary.md    # 248 строк
    02-a-1---holonic-foundation.md     # 185 строк
    ...                                # 19 подразделов
  08-part-c-kernel-extensions-specifications/
    _index.md
    ...                                # 49 подразделов
  ...                                  # 20 директорий
```

Агент сначала читает `_index.md`, затем выбирает нужный файл подраздела и загружает только его.

## Секции

| # | Section | Sub-sections |
|---|---------|:---:|
| 01 | Title page | 0 |
| 02 | Table of Content | 1 |
| 03 | Preface | 17 |
| 04 | Part A — Kernel Architecture | 19 |
| 05 | A.IV.A — Signature Stack & Boundary | 22 |
| 06 | A.V — Constitutional Principles | 33 |
| 07 | Part B — Trans-disciplinary Reasoning | 25 |
| 08 | Part C — Kernel Extensions | 49 |
| 09 | Part D — Ethics & Conflict | 1 |
| 10 | Part E — Constitution & Authoring | 0 |
| 11 | E-I — FPF Constitution | 42 |
| 12 | Part F — Unification Suite | 0 |
| 13 | F.I — Context of Meaning and Lexical Inputs | 19 |
| 14 | UTS Layout A | 0 |
| 15 | UTS Layout B | 1 |
| 16 | Part G — SoTA Patterns Kit | 15 |
| 17 | Part H — Glossary | 0 |
| 18 | Part I — Annexes | 1 |
| 19 | Part J — Indexes | 1 |
| 20 | Part K — Lexical Debt | 3 |

## Обновление после изменений в FPF

Когда upstream-спецификация FPF меняется, нужно обновить два слоя.

### 1. Перегенерировать section files

Обновите submodule и снова запустите splitter:

```bash
git submodule update --remote
python3 scripts/split_spec.py
```

### 2. Обновить навигацию в SKILL.md

Section files — это сырой контент. `SKILL.md` является навигационным слоем поверх него. После регенерации проверьте, нужно ли обновить thinking-verb router, use cases или Section INDEX, чтобы отразить новые, изменённые или удалённые паттерны.

См. **[FPF-SKILL-UPDATE-GUIDE.md](FPF-SKILL-UPDATE-GUIDE.md)**: там описано, что проверять, как валидировать router entries и как проводить FPF self-audit для самого skill-файла.

> **Примечание:** submodule `FPF` временно отслеживает fork ([rodion-m/FPF](https://github.com/rodion-m/FPF), branch `fix/restore-orphaned-part-headings`), который восстанавливает заголовки Part D/E/F/G, случайно удалённые upstream. См. [ailev/FPF#42](https://github.com/ailev/FPF/issues/42) и [PR #43](https://github.com/ailev/FPF/pull/43). После merge PR submodule будет снова привязан к upstream `ailev/FPF`.

## Credits

- **FPF specification**: [Анатолий Левенчук](https://github.com/ailev) — [github.com/ailev/FPF](https://github.com/ailev/FPF)
- **Skill packaging**: [CodeAlive-AI](https://github.com/CodeAlive-AI)

## License

MIT
