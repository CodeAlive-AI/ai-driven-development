---
name: openrouter-provider-ranking
description: "Use this skill when a user asks to rank, compare, benchmark, prioritize, or generate routing for OpenRouter provider endpoints (provider.order, provider.only, :exacto) by TPS/throughput, TTFT/latency, effective price, uptime, cache hit rate, tool-call/Exacto quality, quantization, context, privacy, or fallback diversity; also for requests about «сортировка/приоритет провайдеров OpenRouter». Do not use for broad model-family selection unless endpoint-level provider routing is required."
compatibility: "Requires Python 3.10+; live endpoint discovery requires outbound HTTPS and a management-capable OpenRouter key in OPENROUTER_API_KEY. Offline endpoint JSON is supported. The bundled ranker uses only the Python standard library."
metadata:
  version: "1.0.0"
  domain: "openrouter-routing"
---

# OpenRouter Provider Ranking

Ранжируй **endpoint-провайдеров одного OpenRouter model slug** под конкретный workload. Не называй порядок «глобально оптимальным»: он оптимален только относительно входных ограничений, весов, профиля токенов и доступной телеметрии.

## Обязательные правила

1. Сначала применяй hard constraints, затем считай score. Никогда не компенсируй несовместимость высоким TPS или низкой ценой.
2. Для tool-calling по умолчанию используй `native-exacto`: модель с суффиксом `:exacto`, без `provider.sort` и без `provider.order`. Собственный score в этом режиме — диагностический, а не замена закрытой телеметрии OpenRouter.
3. Используй `manual` только когда пользователь требует детерминированный порядок, собственная production-телеметрия важнее Exacto, либо нужен явно зафиксированный failover chain.
4. Не сочетай `:exacto` с `provider.sort`: явный sort имеет приоритет. Не добавляй `provider.order` в режиме `native-exacto`.
5. Учитывай цену **на реальном профиле токенов**, а не только headline input/output price. Включай cache read/write, per-request fee, conditional pricing overrides и наблюдаемый cache hit rate.
6. Не выдумывай отсутствующие Exacto/benchmark/cache/tool-success метрики. Применяй conservative prior и uncertainty penalty; явно отмечай пробелы.
7. Для multi-turn workload передавай стабильный `session_id`. Помни: ручной `provider.order` отключает OpenRouter sticky provider routing; `session_id` не отменяет это ограничение.
8. Не сохраняй API key в skill, конфиг, лог или итоговый JSON. Читай его только из `OPENROUTER_API_KEY` либо указанной environment variable.

## Входные данные

Собери или оцени:

- model slug, например `deepseek/deepseek-v4-flash-0731`;
- `uses_tools`, streaming, требуемые параметры, context и output limits;
- ожидаемые prompt/completion tokens и requests per session;
- cacheable prompt fraction, token-level cache read/write rate, response-cache hit rate;
- hard caps: цена, latency, TPS, uptime, quantization, moderation, ZDR/data policy;
- цель: quality, balanced, interactive latency, cost или batch throughput;
- собственную telemetry по provider tag, если она есть.

Когда вход неполный, используй профиль `agentic-balanced`. Для tool-calling включай `uses_tools=true`. Не задавай ненулевой cache hit rate без наблюдений или обоснованной workload-модели.

## Процедура

### 1. Классифицируй workload

Выбери один профиль:

- `agentic-balanced` — default для агентов и B2B SaaS;
- `agentic-quality` — tool correctness и reliability важнее цены;
- `interactive` — минимизация TTFT и end-to-end latency;
- `cost` — минимизация ожидаемой стоимости при SLO;
- `batch` — throughput/cost для длинных completion.

Для нестандартной цели переопредели `weights`, но сумма после нормализации должна быть положительной. Подробная формула: [references/scoring.md](references/scoring.md).

### 2. Получи свежие endpoint-метрики

Предпочтительный путь — OpenRouter Endpoints API через bundled script:

```bash
python3 scripts/rank_providers.py \
  --model deepseek/deepseek-v4-flash-0731 \
  --config assets/config.example.json \
  --format markdown \
  --output recommendation.md
```

Для воспроизводимого/offline анализа:

```bash
python3 scripts/rank_providers.py \
  --endpoints-file endpoints.json \
  --config config.json \
  --observations telemetry.jsonl \
  --previous-ranking previous-result.json \
  --output result.json
```

Endpoint API дает provider tag, pricing, quantization, context/output limits, supported parameters, uptime, latency и throughput percentiles. Если анализируется performance page, перенеси видимые provider-specific Auto Exacto/benchmark значения в observations по точному `tag`; не пытайся угадывать соответствие по display name при наличии tag.

Форматы входа: [references/input-formats.md](references/input-formats.md).

### 3. Добавь production-телеметрию

Приоритет сигналов качества:

1. собственный tool-call/schema success по тому же model, prompt class и provider tag;
2. provider-specific Exacto/benchmark значения с performance page;
3. endpoint performance/uptime API;
4. conservative prior при отсутствии данных.

Собирай минимум: `provider_name` или `provider_tag`, success, tool success, prompt/completion/cached/cache-write tokens, TTFT, generation time/TPS и total cost. Для долей с малой выборкой используй Wilson lower bound, а не raw percentage.

### 4. Запусти ranking и проверь результат

Скрипт должен:

- исключить неактивные/несовместимые endpoints;
- разрешить pricing overrides на момент запроса;
- посчитать expected cost для workload;
- смешать OpenRouter percentiles с собственными наблюдениями по sample confidence;
- нормализовать cost/TPS/TTFT/E2E относительно текущего eligible pool;
- применить quality, reliability, cache, fidelity и uncertainty components;
- стабилизировать порядок предыдущим результатом;
- выбрать fallback chain с provider-family diversity, если разрыв score приемлем.

Проверь exit code. При `4` не ослабляй ограничения молча: покажи, какие constraints исключили все endpoints, и предложи минимальное ослабление.

### 5. Выбери routing mode

| Условие | Режим | Что отправлять |
|---|---|---|
| Tool calls, нет требования фиксированного порядка | `native-exacto` | `model: <slug>:exacto`, filters/preferences, без `sort/order` |
| Фиксированный failover chain или сильная собственная telemetry | `manual` | `provider.order` из ranking |
| Только одна простая цель без custom score | native OpenRouter | `provider.sort: price/throughput/latency`; bundled ranker не обязателен |

OpenRouter-specific взаимодействия и ограничения: [references/openrouter-routing.md](references/openrouter-routing.md).

## Формат ответа пользователю

Всегда возвращай:

1. выбранный mode и краткое обоснование;
2. таблицу eligible ranking: provider tag, score, expected cost/request, TPS percentile, TTFT, E2E, uptime, quality confidence и cache hit rate;
3. готовый JSON request fragment;
4. excluded providers с причинами;
5. coverage/warnings и список отсутствующих сигналов;
6. правило обновления ranking: пересчитывать после заметного drift, изменения цен/endpoints или достаточного прироста telemetry; не фиксировать бессрочно.

В `native-exacto` четко разделяй **diagnostic ranking** и **authoritative runtime ordering by Exacto**.

## Validation checklist

Перед выдачей результата проверь:

- provider tags взяты из свежего API/файла, а не из памяти;
- hard constraints применены до score;
- цены переведены из USD/token в понятные USD/M и workload cost без двойного пересчета;
- p90 throughput трактуется как нижняя граница, достигаемая примерно 90% запросов, а p90 latency — как верхняя граница примерно для 90% запросов;
- `provider.max_price` передан в USD per million tokens, тогда как endpoint pricing хранится в USD per token;
- `provider.order` отсутствует в `native-exacto`;
- service-tier tags (`/fast`, `/flex`) не включены случайно;
- при cache-heavy сессиях указан stable `session_id`, а последствия manual order отмечены;
- низкая выборка не переоценивается;
- итоговый request JSON синтаксически валиден.

## Bundled resources

- `scripts/rank_providers.py` — автономный ranker и генератор routing fragment.
- `scripts/validate_skill.py` — self-check frontmatter, resources, syntax и unit tests.
- `assets/config.example.json` — конфиг для tool-using agent workload.
- `assets/observations.example.json` — агрегированные provider observations.
- `assets/telemetry.example.jsonl` — сырые request-level observations.
- `tests/trigger-evals.json` — positive/negative activation queries для description.
- `references/scoring.md` — формула, нормализация и профили.
- `references/input-formats.md` — схема config/telemetry.
- `references/openrouter-routing.md` — semantics OpenRouter routing/caching.

Для проверки пакета запусти:

```bash
python3 scripts/validate_skill.py
```
