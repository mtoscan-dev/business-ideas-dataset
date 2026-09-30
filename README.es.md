<p align="center">
  <img src="assets/banner.webp" alt="Business Ideas Database, a public dataset of validated business ideas" width="100%">
</p>

<h1 align="center">Business Ideas Dataset</h1>

<p align="center">
  <strong>Un dataset público, licenciado bajo MIT, de ideas de negocio validadas, obtenidas de dolores reales expresados en Reddit y de reseñas de App Store, puntuadas por IA en oportunidad, severidad del problema, factibilidad y timing. Incluye un CLI, agent skills listos para usar, y recetas de integración para Claude Code, Codex CLI, Cursor y cualquier sistema que entienda markdown.</strong>
</p>

<p align="center">
  <a href="https://businessideasdb.com?utm_source=github&utm_medium=dataset&utm_campaign=business-ideas-dataset"><img alt="Live site" src="https://img.shields.io/badge/live-businessideasdb.com-00856A?style=flat-square"></a>
  <a href="data/ideas.json"><img alt="Ideas" src="https://img.shields.io/badge/dynamic/json?label=ideas&query=%24.total_ideas&url=https%3A%2F%2Fraw.githubusercontent.com%2Ftheomarsoliman%2Fbusiness-ideas-dataset%2Fmain%2Fdata%2Fsummary.json&color=4B7BF5&style=flat-square"></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-22A86A?style=flat-square"></a>
  <a href="data/ideas.json"><img alt="JSON" src="https://img.shields.io/badge/format-JSON%20%2B%20CSV-555?style=flat-square"></a>
  <a href="cli/"><img alt="CLI" src="https://img.shields.io/badge/cli-Python-FFD43B?style=flat-square"></a>
  <a href="skills/"><img alt="Skills" src="https://img.shields.io/badge/agent%20skills-6-7C3AED?style=flat-square"></a>
</p>

<p align="center">
  <a href="data/ideas.json"><strong>ideas.json</strong></a> &nbsp;·&nbsp;
  <a href="data/ideas.csv"><strong>ideas.csv</strong></a> &nbsp;·&nbsp;
  <a href="cli/"><strong>CLI</strong></a> &nbsp;·&nbsp;
  <a href="skills/"><strong>Skills</strong></a> &nbsp;·&nbsp;
  <a href="INTEGRATIONS.md"><strong>Integraciones</strong></a> &nbsp;·&nbsp;
  <a href="METHODOLOGY.md"><strong>Metodología</strong></a> &nbsp;·&nbsp;
  <a href="https://businessideasdb.com/state-of-indie-business-ideas-2026?utm_source=github&utm_medium=dataset&utm_campaign=business-ideas-dataset"><strong>Reporte 2026</strong></a>
</p>

> Este documento es una traducción del [README.md](README.md) en inglés, que es la fuente de verdad. Ante cualquier discrepancia, prevalece la versión en inglés.

---

## Qué es esto

Un dataset público, legible por máquina, de ideas de negocio que ya pasaron un filtro de validación. Cada idea en `data/ideas.json` empezó como una queja real en Reddit (alguien pidiendo una herramienta que todavía no existe, o describiendo un flujo de trabajo que odia) o como un patrón de reseñas negativas en una app popular del App Store. Cada idea está enriquecida con:

1. La palabra clave subyacente y su volumen de búsqueda mensual en EE. UU.
2. Crecimiento interanual de esa búsqueda
3. Cuatro scores de IA de 0 a 10 (oportunidad, severidad del problema, factibilidad, timing)
4. Nivel de competencia, dificultad, rango de revenue estimado
5. Un link directo al análisis editorial completo en [businessideasdb.com](https://businessideasdb.com?utm_source=github&utm_medium=dataset&utm_campaign=business-ideas-dataset)

Si construís, invertís en, o escribís sobre indie SaaS, micro SaaS, apps móviles o pequeños negocios, esta es una fuente citable de evidencia de demanda. El análisis editorial completo (perfil de cliente, feature list del MVP, URLs de threads de Reddit, research de competidores) vive en el sitio.

## Tres formas de usarlo

### 1. Datos crudos

```bash
# JSON
curl -sL https://raw.githubusercontent.com/theomarsoliman/business-ideas-dataset/main/data/ideas.json

# CSV
curl -sL https://raw.githubusercontent.com/theomarsoliman/business-ideas-dataset/main/data/ideas.csv
```

### 2. Herramienta CLI

```bash
# Instalar (una línea, sin dependencias)
curl -sL https://raw.githubusercontent.com/theomarsoliman/business-ideas-dataset/main/cli/bid.py \
  -o ~/.local/bin/bid && chmod +x ~/.local/bin/bid

# Usar
bid stats
bid list --category SaaS --min-feas 8 --limit 5
bid get trade-invoice-autopilot
bid search "invoice"
bid top-growth
```

Ver [`cli/README.md`](cli/README.md) para todas las opciones.

### 3. Agent skills de IA

Seis archivos de skill portables para Claude Code, Codex CLI, Cursor, o cualquier agente que entienda markdown. Colocalos en el directorio de skills de tu agente y lo va a usar automáticamente cuando el usuario pregunte sobre ideas de negocio.

| Skill | Qué hace |
|---|---|
| [validate-idea](skills/validate-idea.md) | Puntúa una idea del usuario contra el rubric de BID |
| [find-saas-wedge](skills/find-saas-wedge.md) | Muestra oportunidades validadas en un nicho |
| [mvp-build-plan](skills/mvp-build-plan.md) | Produce un plan de build día a día de 2 a 4 semanas |
| [reddit-pain-finder](skills/reddit-pain-finder.md) | Recorre el patrón de 170 queries de BID sobre Reddit |
| [competitor-mapping](skills/competitor-mapping.md) | Mapea competidores directos, adyacentes e indirectos |
| [keyword-demand-check](skills/keyword-demand-check.md) | Valida intención de compra vía volumen de búsqueda |

Ver [`INTEGRATIONS.md`](INTEGRATIONS.md) para la receta de instalación de tu agente específico (Claude Code, Codex CLI, Cursor, Cline, Continue, Aider, MCP, genérico).

## Qué hay en los datos

<p align="center">
  <img src="assets/category-distribution.svg" alt="Business ideas grouped by category" width="100%">
</p>

42 ideas en 6 categorías al último export. Las categorías incluyen SaaS (B2B y B2C), App y Mobile App (consumer y prosumer), Tool (utilidades de un solo propósito), Platform (multi sided), y un pequeño grupo SaaS + Hardware.

<p align="center">
  <img src="assets/score-distribution.svg" alt="AI score distribution across opportunity, problem severity, feasibility, and timing" width="100%">
</p>

Los scores se inclinan hacia 7 o más en al menos una dimensión porque el dataset está filtrado por eso en la entrada. La feasibility mediana está en el rango de 7 a 9, lo que significa que la mayoría de las ideas se pueden lanzar como MVP en 2 a 4 semanas para un founder solo usando el stack moderno asistido por IA.

## Ejemplos rápidos

```bash
# Ideas SaaS con mayor opportunity score
curl -sL https://raw.githubusercontent.com/theomarsoliman/business-ideas-dataset/main/data/ideas.json \
  | jq '.ideas | map(select(.category == "SaaS")) | sort_by(-.opportunity_score) | .[0:5] | .[] | {title, opportunity_score, url}'
```

```python
import json, urllib.request
data = json.load(urllib.request.urlopen("https://raw.githubusercontent.com/theomarsoliman/business-ideas-dataset/main/data/ideas.json"))
top_growth = sorted(
    [i for i in data["ideas"] if i["growth_percent"]],
    key=lambda i: -i["growth_percent"],
)[:10]
for i in top_growth:
    print(f"{i['growth_percent']:+}% {i['title']} ({i['category']})")
    print(f"   {i['url']}")
```

## Schema

Cada entrada en `data/ideas.json`, dentro del array `ideas`, tiene estos campos:

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | number | ID interno, estable entre exports |
| `slug` | string | Slug de URL, coincide con la URL de BID |
| `title` | string | Título corto y descriptivo de la idea |
| `pitch` | string | Resumen de una oración, incluye números concretos cuando se conocen |
| `category` | string | Una de: SaaS, App, Mobile App, Tool, Platform, SaaS + Hardware |
| `tags` | string[] | Tags de tema, en minúscula |
| `keyword` | string | Palabra clave principal usada para validar demanda |
| `search_volume` | number | Volumen de búsqueda mensual en EE. UU. (DataForSEO) |
| `growth_percent` | number | Cambio interanual en el volumen de búsqueda |
| `competition` | string | Low, Medium, o High |
| `difficulty` | string | Easy, Medium, o Hard - complejidad de build |
| `revenue_range` | string | Rango de revenue estimado, ej. "$10K a $50K" |
| `opportunity_score` | 0 a 10 | Potencial de mercado y brecha competitiva |
| `problem_score` | 0 a 10 | Severidad del dolor del usuario |
| `feasibility_score` | 0 a 10 | Qué tan fácil es el MVP para un equipo chico |
| `timing_score` | 0 a 10 | Si la ventana de mercado está abierta ahora |
| `signal_count` | number | Cantidad de threads de Reddit que respaldan la idea (URLs y cuerpos viven en el sitio) |
| `competitor_names` | string[] | Nombres de competidores existentes (sin URLs) |
| `created_at` | string | Cuándo entró la idea al dataset |
| `updated_at` | string | Timestamp de la última edición |
| `url` | string | URL canónica del análisis editorial completo (limpia, sin UTMs) |
| `tracked_url` | string | Misma URL con parámetros UTM para atribución |

Ver [data/README.md](data/README.md) para queries de ejemplo y semántica de los campos.

## Metodología

Ver [METHODOLOGY.md](METHODOLOGY.md) para el rubric completo de scoring, el pipeline de fuentes, y los criterios de validación. Versión corta:

1. Un scanner extrae posts de 5 o más subreddits (r/SaaS, r/SmallBusiness, r/Entrepreneur, r/IndieHackers, r/SideProject, más subs específicos de categoría) contra 170 patrones de query
2. La API del App Store de iTunes muestra apps con muchas instalaciones y reseñas negativas agrupadas
3. Cada señal candidata es puntuada por un rubric de IA (Grok 3 mini) en las cuatro dimensiones
4. Las señales que puntúan 7 o más en al menos una dimensión pasan a la cola de revisión editorial
5. La revisión editorial enriquece con datos de keywords de DataForSEO, mapeo de competidores, y el análisis extendido publicado en businessideasdb.com

## Ejemplos

* [Top 10 ideas por opportunity score](examples/top-by-opportunity.md)
* [Keywords con mayor crecimiento (interanual)](examples/top-by-growth.md)
* [Subset solo SaaS](examples/saas-ideas.md)
* [Subset App y Mobile App](examples/app-ideas.md)
* [Mayor feasibility para founders solos](examples/high-feasibility.md)
* [Todas las ideas](examples/all-ideas.md), las 42 ideas ordenadas por score compuesto, una fila por idea

## Casos de uso

| Quién | Qué te da esto |
|---|---|
| Founders indie buscando una cuña | Una lista pre filtrada de ideas validadas con la demanda de búsqueda adjunta |
| Inversores y angels | Una capa de señal de demanda para sourcing de oportunidades en etapa temprana |
| Builders de agentes de IA | Un dataset estructurado más 6 skills para meter en Claude Code, Codex, Cursor |
| Investigadores y escritores | Un dataset público, citable y fechado para posts sobre tendencias indie |
| Productos de LLM y búsqueda con IA | Datos estructurados con URLs estables para citar en respuestas |

## Atribución

Este dataset estampa parámetros UTM en los links de vuelta a businessideasdb.com para que el sitio en vivo pueda trackear qué superficie (README, CLI, skill específico) generó qué click. El campo `url` se mantiene canónico para fines de citación. El campo `tracked_url` tiene el UTM agregado.

Si forkeás el CLI o los skills, por favor mantené intacta la plantilla de UTM (cambiá `utm_medium` para que coincida con tu contexto). Quitar la atribución no rompe nada pero corta el loop de señal que le permite al dataset mejorar.

## Cita

Si usás este dataset en un post, paper, o producto, por favor citá la fuente en vivo:

```
Business Ideas Database (2026). Validated Business Ideas Dataset.
Retrieved from https://businessideasdb.com/state-of-indie-business-ideas-2026
```

Cada idea individual se puede citar por su campo `url`, que apunta al análisis editorial canónico en businessideasdb.com.

## Licencia

[MIT](LICENSE). Usar, modificar, redistribuir, construir sobre esto. La atribución de vuelta a [businessideasdb.com](https://businessideasdb.com?utm_source=github&utm_medium=dataset&utm_campaign=business-ideas-dataset) se aprecia pero no es obligatoria.

## Relacionado

* **[App Ideas From Reddit](https://github.com/theomarsoliman/app-ideas-from-reddit)**, dataset compañero: 614 ideas de app tomadas de pedidos reales en Reddit, cada una linkeando al thread original
* **[State of Indie Business Ideas 2026](https://businessideasdb.com/state-of-indie-business-ideas-2026?utm_source=github&utm_medium=dataset&utm_campaign=business-ideas-dataset)**, reporte anual de datos con agregados completos
* **[SaaS Ideas](https://businessideasdb.com/saas-ideas?utm_source=github&utm_medium=dataset&utm_campaign=business-ideas-dataset)**, subset SaaS filtrado con comentario editorial
* **[Micro SaaS Ideas](https://businessideasdb.com/micro-saas-ideas?utm_source=github&utm_medium=dataset&utm_campaign=business-ideas-dataset)**, subset filtrado para founder solo (feasibility 7 o más)
* **[App Ideas](https://businessideasdb.com/app-ideas?utm_source=github&utm_medium=dataset&utm_campaign=business-ideas-dataset)**, subset de apps móviles con análisis de brechas del App Store
* **[Home Business Ideas](https://businessideasdb.com/home-business-ideas?utm_source=github&utm_medium=dataset&utm_campaign=business-ideas-dataset)**, subset de negocios digitales para operadores solo con laptop
* **[Low Cost Business Ideas](https://businessideasdb.com/low-cost-business-ideas?utm_source=github&utm_medium=dataset&utm_campaign=business-ideas-dataset)**, ideas de negocio que se pueden arrancar con menos de $1,000
* **[Full database](https://businessideasdb.com/ideas?utm_source=github&utm_medium=dataset&utm_campaign=business-ideas-dataset)**, todas las ideas con el análisis extendido
