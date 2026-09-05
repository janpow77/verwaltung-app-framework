# Architektur — verwaltung-app-framework

_Automatisch generiert von graphify-kira aus dem Code-Graphen. Nicht von Hand editieren — wird beim nächsten Lauf überschrieben._

**Umfang:** 61 Knoten, 132 Kanten, 6 größere Module, 0 zirkuläre Abhängigkeiten.

## Modulkarte

- **Community 0** (13): `models.py`, `vvt.py`
- **Community 1** (12): `dsfa.py`, `Any`, `models.py`, `test_framework.py`
- **Community 2** (11): `models.py`, `process.py`, `test_framework.py`
- **Community 3** (11): `permissions.py`, `basic.py`, `Any`, `test_framework.py`
- **Community 4** (4): `test_framework.py`
- **Community 5** (3): `validate_repo.py`

## Zentrale Bausteine (God Nodes)

_Hohe Zentralität ist nicht automatisch ein Defekt (zentrale Stores/Modelle sind oft legitim). Konkrete Refactoring-Prioritäten siehe Optimierungs-Report._

- `ProcessingActivity (framework/core/models.py)` — Grad 13 (ein 13/aus 0)
- `ProjectCase (framework/core/models.py)` — Grad 11 (ein 11/aus 0)
- `test_framework.py (tests/test_framework.py)` — Grad 22 (ein 0/aus 22)
- `DsfaAssessment (framework/core/models.py)` — Grad 7 (ein 7/aus 0)
- `VvtRegistry (framework/core/vvt.py)` — Grad 10 (ein 5/aus 5)
- `models.py (framework/core/models.py)` — Grad 10 (ein 5/aus 5)
- `dsfa.py (framework/core/dsfa.py)` — Grad 12 (ein 2/aus 10)
- `FrameworkContractTests (tests/test_framework.py)` — Grad 13 (ein 1/aus 12)
- `GateContext (framework/core/process.py)` — Grad 8 (ein 7/aus 1)
- `process.py (framework/core/process.py)` — Grad 9 (ein 2/aus 7)

## Schnittstellen / Brücken (Betweenness)

- `models.py (framework/core/models.py)` — Betweenness 0.008
- `VvtRegistry (framework/core/vvt.py)` — Betweenness 0.007
- `dsfa.py (framework/core/dsfa.py)` — Betweenness 0.004
- `create_dsfa() (framework/core/dsfa.py)` — Betweenness 0.004
- `process.py (framework/core/process.py)` — Betweenness 0.003
- `vvt.py (framework/core/vvt.py)` — Betweenness 0.003
- `FrameworkContractTests (tests/test_framework.py)` — Betweenness 0.002
- `transition() (framework/core/process.py)` — Betweenness 0.002
- `.test_dsfa_snapshot_and_four_eyes() (tests/test_framework.py)` — Betweenness 0.002
- `.test_permissions_and_exports() (tests/test_framework.py)` — Betweenness 0.001

## Empfohlene Spezialisten

Passend zu Stack/Domäne dieses Projekts (Claude-Code-Agents/Skills):

`/deutsche-formulierung`, `@git-workflow`.

## Hinweis für Änderungen

Vor dem Ändern eines zentralen Bausteins die Abhängigen prüfen — am schnellsten über den **graphify-MCP** (globaler Graph): „Was hängt an `<datei>`?". Brücken-Knoten stabil halten.

