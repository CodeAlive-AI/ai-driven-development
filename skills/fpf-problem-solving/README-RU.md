# fpf-problem-solving-skill

[English version (README.md)](README.md)

Skill для AI coding agent по FPF Library [Анатолия Левенчука](https://github.com/ailev):
ядро [First Principles Framework (FPF)](https://github.com/ailev/FPF) и 36 доменных фреймворков (DPF),
всё хранится локально.

FPF — трансдисциплинарная архитектура рассуждения для системной инженерии, координации знаний и
смешанных human/AI-команд. FPF работает как **усилитель мышления**: помогает глубже планировать и
принимать более качественные решения через систематическое исследование релевантных альтернатив, а не
фиксацию на первом варианте. Доменные фреймворки применяют его к конкретным областям: стратегии, целям и
OKR, операционному управлению, исследованиям, проектированию решений, системной инженерии, объяснению,
математике, развитию человеческих способностей и другим.

## Как это работает

Skill работает как **agentic RAG** без векторной базы: агент одновременно retriever, router и reasoner.

1. **Вход.** Step 0 в `SKILL.md` выясняет, как появился FPF: назван паттерн (`F.19`, `C.11.DUA`,
   `GOALS.7`), узнаваемая проблема, вопрос внутри области или общая мыслительная задача.
2. **Три карты.** Map A (`references/core-router.md`, обзор — в `SKILL.md`) ведёт от мыслительной
   задачи к паттернам ядра, в пяти группах. Map B ведёт от
   вопроса области к её доменному фреймворку. Map C сопоставляет частые проблемы в работе с агентом —
   оговорки вместо суждения, потерянный исходный вопрос, продолжение после передачи задачи, одинаковые
   «варианты» — с паттерном, который их решает; она следует шпаргалке Анатолия Левенчука по самым
   ходовым паттернам.
3. **Разрешение ссылок.** `scripts/find_pattern.py <ID>` по PatternID или ссылке на раздел
   (`HCD.12:4.1`) печатает карточку: когда применять паттерн и когда нет, его семейство, файл и карту
   разделов; для нескольких ID — по карточке на каждый, чтобы выбрать. По DocID выводятся входы
   фреймворка («ситуация → с чего начать») и его паттерны; `--search <слова>` ранжирует входы,
   названия и ключевые слова.
4. **Чтение.** Агент открывает самый узкий файл: сначала Problem frame и Solution, затем Conformance
   Checklist для проверки своего результата, и останавливается на первом полезном результате.

Публикации upstream разрезаны на файлы по разделам, а все ссылки между ними — якоря внутри документа,
относительные пути, ссылки на GitHub и fpf.tools — переписаны на локальные файлы, поэтому по ним можно
ходить без сети.

## Установка

```bash
npx skills add CodeAlive-AI/fpf-problem-solving-skill -g
```

## Пример запроса

> Используй скилл FPF. Помоги структурировать мой проект / проблему / программу.
> Объясняй простым языком для инженера-менеджера.
> Предложи: (1) ограниченные контексты и специализации, (2) критерии решения, (3) ключевые
> альтернативы, (4) передачи работы между участниками и (5) недостающие свидетельства или проверки
> до принятия обязательств.
> Внутренние термины FPF вводи только там, где они добавляют нужную точность.

## Структура

```text
SKILL.md            вход, Step 0, карты B и C, обзор карты A, правила чтения
references/         core-router.md — Map A: мыслительная задача → паттерны ядра
PATTERN-INDEX.md    каждый DocID и PatternID → локальный файл (генерируется)
sections/           ядро FPF: папка на часть, файл на паттерн; _index.md перечисляет файлы
dpfs/               доменные фреймворки: dpfs/<suite>/<docid>/ или dpfs/<docid>/
  management-dpf-suite/goals/_index.md   practical entries, оглавление с ключевыми словами, список файлов
library/            Readme библиотеки, USING-FPF.md, LICENSING.md, Library Architectural Reference
scripts/            split_spec.py (регенерация), find_pattern.py (поиск), check_skill.py (проверка)
```

## Секции ядра

| # | Section | Sub-sections |
|---|---------|:---:|
| 01 | Title page | 0 |
| 02 | Table of Contents | 0 |
| 03 | FPF Readme | 12 |
| 04 | Architectural Reference | 22 |
| 05 | Part A — Kernel Architecture | 38 |
| 06 | A.IV.A — Signature Stack & Boundary | 29 |
| 07 | A.V — Constitutional Principles | 50 |
| 08 | Part B — Trans-disciplinary Reasoning | 43 |
| 09 | Part C — Kernel Extensions | 130 |
| 10 | Part D — Ethics & Conflict | 5 |
| 11 | Part E — Constitution & Authoring | 69 |
| 12 | Part F — Unification Suite | 24 |
| 13 | Part G — SoTA Patterns Kit | 15 |
| 14 | Part H — Reserved | 0 |

Числа соответствуют H2-заголовкам upstream. Architectural Reference содержит 21 содержательный раздел и
маркер границы `FPF.Reference:End` без содержимого.

## Доменные фреймворки

| Suite или группа | Фреймворки (DocID) |
|---|---|
| Management | STR, GOALS, OPS, ADM, CGOV, MA, FIN, MKT, CUST, EAM, LDR, CB, OCE, HRM |
| Engineering | SYSE, KCAE, SIE, CAD, MNT |
| Foundational Thinking | MATH, MMP, PHY, CMP, NOT |
| Human Capability Engineering | HCD, SOM |
| Отдельные | PSDA, RMP, EXD, NSTD, IS, ECO, FDM, DTM, RHY, MDPE |

`dpfs/_index.md` — каталог upstream с описанием, над чем работает каждый фреймворк.

## Обновление после изменений upstream

```bash
git clone --depth 1 https://github.com/ailev/FPF.git /tmp/fpf-upstream
python3 scripts/split_spec.py --source /tmp/fpf-upstream
python3 scripts/check_skill.py
```

Splitter заменяет `sections/`, `dpfs/`, `library/` и `PATTERN-INDEX.md` только после того, как все
публикации разрезаны и проверены. Checker перечисляет, что нужно поправить в `SKILL.md` и README:
неразрешённые ID, фреймворки без места на карте, счётчики, коммит upstream. Полный метод описан в
**[FPF-SKILL-UPDATE-GUIDE.md](FPF-SKILL-UPDATE-GUIDE.md)**.

## Credits

- **FPF Library**: [Анатолий Левенчук](https://github.com/ailev) — [github.com/ailev/FPF](https://github.com/ailev/FPF)
- **Skill packaging**: [CodeAlive-AI](https://github.com/CodeAlive-AI)

## License

Упаковка скилла и скрипты: MIT. Адаптировано из *FPF Library* Анатолия Левенчука — ядра *First
Principles Framework (FPF)*, доменных фреймворков и документов библиотеки —
[ailev/FPF](https://github.com/ailev/FPF), коммит источника `e317958532699b762dd9e7baf460f97bad7a4c9c`.
Текст библиотеки распространяется под [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); см.
[область действия лицензии источника](https://github.com/ailev/FPF/blob/main/LICENSING.md). Изменения:
публикации разделены на файлы секций с генерируемыми навигационными индексами, их ссылки переписаны на
локальные файлы, а `SKILL.md` добавляет маршрутизацию и инструкции для агента. Автор FPF не подтверждал
и не одобрял эту адаптацию.
