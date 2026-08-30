# fpf-problem-solving-skill

[English version (README.md)](README.md)

Skill для AI coding agent по [First Principles Framework (FPF)](https://github.com/ailev/FPF) от [Анатолия Левенчука](https://github.com/ailev).

FPF — трансдисциплинарная архитектура рассуждения для системной инженерии, координации знаний и смешанных human/AI-команд.

FPF работает как **усилитель мышления**: помогает глубже планировать и принимать более качественные решения через систематическое исследование релевантных альтернатив, а не фиксацию на первом варианте.

## Как это работает

Skill работает как **agentic RAG**: retrieval-augmented generation, где поиск выполняет сам агент без внешней векторной базы и embedding pipeline. Upstream-спецификация FPF разделена на двухуровневую иерархию: 15 директорий и 355 файл. `SKILL.md` содержит router по thinking verbs, который сопоставляет намерение пользователя с нужной секцией: выбор практической точки входа, поиск систем, которые могут нести значимые последствия, восстановление кандидата метода из свидетельств о работе, выбор следующего действия в ходе работы, проверка конфигурации исполнителей и средств поддержки при прерываниях, передачах, задержках и реконфигурациях, сравнение конечных изменений конфигурации, уточнение утверждений о learning, применение паттерна до первого полезного результата, навигация по DPF Suite Reference, перепроверка затронутых решений после изменения источника, запрос ограниченного результата другой практики, подбор представлений для одного использования, построение сопоставимых способов получить один результат, сборка формы публикации framework, синтез архитектуры из несовпадающих структур практики, развитие capability для именованного Work, синтез исходных онтологий без утраты их локальных смыслов, восстановление предметов и ролей, трассировка зависимостей от внешнего использования, различение отношений и их реализаций, преобразование эпистем, рассуждения о решениях, причинности, фактической временной структуре, времени, архитектуре и структурной адекватности, публикация стабильных multi-view артефактов, управление ontic admission, обновление SoTA-паков и provenance. Затем агент читает `_index.md`, выбирает самый узкий подраздел и загружает только его в контекст. Агент одновременно является retriever, router и reasoner.

## Установка

```bash
npx skills add CodeAlive-AI/fpf-problem-solving-skill -g
```

## Структура

```text
sections/
  05-part-a---kernel-architecture-cluster/
    _index.md                          # TOC с описаниями всех подразделов
    01-a-0---onboarding-glossary.md    # 248 строк
    02-a-1---holon-ontic-foundation.md # 356 строк
    ...                                # 26 подразделов
  09-part-c---kernel-extension-specifications/
    _index.md
    ...                                # 79 подразделов
  ...                                  # 15 директорий
```

Агент сначала читает `_index.md`, затем выбирает нужный файл подраздела и загружает только его.

## Секции

| # | Section | Sub-sections |
|---|---------|:---:|
| 01 | Title page | 0 |
| 02 | Table of Contents | 0 |
| 03 | FPF Readme | 9 |
| 04 | Preface | 21 |
| 05 | Part A — Kernel Architecture | 26 |
| 06 | A.IV.A — Signature Stack & Boundary | 27 |
| 07 | A.V — Constitutional Principles | 46 |
| 08 | Part B — Trans-disciplinary Reasoning | 25 |
| 09 | Part C — Kernel Extensions | 79 |
| 10 | Part D — Ethics & Conflict | 5 |
| 11 | Part E — Constitution & Authoring | 64 |
| 12 | Part F — Unification Suite | 22 |
| 13 | Part G — SoTA Patterns Kit | 15 |
| 14 | Part H — Reserved | 0 |
| 15 | Part I — Annexes | 1 |

## Обновление после изменений в FPF

Когда upstream-спецификация FPF меняется, нужно обновить два слоя.

### 1. Перегенерировать section files

Склонируйте официальный upstream `ailev/FPF` во временный skill layout вне этого репозитория, запустите там splitter и замените отслеживаемое дерево `sections/` сгенерированным:

```bash
tmpdir="$(mktemp -d)"
mkdir -p "$tmpdir/skill/scripts"
git clone https://github.com/ailev/FPF.git "$tmpdir/skill/FPF"
cp scripts/split_spec.py "$tmpdir/skill/scripts/split_spec.py"
python3 "$tmpdir/skill/scripts/split_spec.py"
rsync -a --delete "$tmpdir/skill/sections/" sections/
rm -rf "$tmpdir"
```

### 2. Обновить навигацию в SKILL.md

Section files — это сырой контент. `SKILL.md` является навигационным слоем поверх него. После регенерации проверьте, нужно ли обновить thinking-verb router, use cases или Section INDEX, чтобы отразить новые, изменённые или удалённые паттерны.

См. **[FPF-SKILL-UPDATE-GUIDE.md](FPF-SKILL-UPDATE-GUIDE.md)**: там описано, что проверять, как валидировать router entries и как проводить FPF self-audit для самого skill-файла.

## Credits

- **FPF specification**: [Анатолий Левенчук](https://github.com/ailev) — [github.com/ailev/FPF](https://github.com/ailev/FPF)
- **Skill packaging**: [CodeAlive-AI](https://github.com/CodeAlive-AI)

## License

MIT
