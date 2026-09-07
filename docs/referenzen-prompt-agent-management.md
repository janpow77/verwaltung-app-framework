# Referenzmuster für Prompt- und Agent-Management

Stand der Sichtung: 2026-09-07. Dieses Dokument dokumentiert funktionale Referenzmuster aus öffentlich einsehbaren GitHub-Repositories. Es werden Konzepte beschrieben; fremder Quellcode wird nicht in das Verwaltungs-App-Framework übernommen.

Vor jeder späteren Übernahme konkreter Codebestandteile ist die jeweilige aktuelle Lizenz und Herkunft gesondert zu prüfen.

## 1. Langfuse – Prompt Management

Repository: `langfuse/langfuse`

Beobachtete, für das Framework relevante Muster:

- Prompts besitzen einen stabilen Namen und numerische Versionen.
- Prompt-Typen unterscheiden Text und Chat.
- Versionen führen `createdAt`, `updatedAt`, `createdBy`.
- Prompts führen `labels`, `tags` und eine freie strukturierte `config`.
- Neue Versionen können eine `commitMessage` besitzen.
- Prompt-Metadaten sind nach Name, Version, Label, Tag und Änderungszeit filterbar.
- Labels und Tags sind eigenständige Konzepte; Labels eignen sich als bewegliche Verweise auf bestimmte Versionen.

Übernahme als Framework-Konzept:

- unveränderliche Prompt-Versionen,
- Commit-Message,
- Tags + kontrollierte Kategorien + Keywords,
- bewegliche Labels wie `latest`, `recommended`, `pilot`,
- durchsuchbare Metadaten und Facetten,
- Modell-/Prompt-Konfiguration getrennt vom Prompttext.

Hinweis: GitHub weist für das Repository aktuell keine einfache SPDX-Lizenz (`NOASSERTION`) aus. Deshalb insbesondere keinen Code allein aufgrund des Begriffs „open source“ übernehmen.

## 2. Promptfoo – Tests und Evaluation

Repository: `promptfoo/promptfoo`

Beobachtete Muster:

- Prompts werden gegen deklarative Testfälle ausgeführt.
- Testfälle verwenden Variablen und Assertions.
- Test-Suites können Beschreibung und Tags führen.
- Assertions können deterministisch oder modellgestützt sein.
- Prompt-/Provider-Varianten können auf demselben Testbestand verglichen werden.
- Evaluation wird als wiederholbarer Entwicklungs- und CI/CD-Schritt verstanden.

Übernahme als Framework-Konzept:

- versionierte Testsets / Golden Cases,
- Variablen je Testfall,
- deterministische Assertions,
- Schema-/Formatprüfung,
- Rubrics/Judges als explizit versionierte Bewertungslogik,
- Eval-Ergebnis an Prompt-Version + Testset + Provider/Modell + Run Manifest binden.

GitHub weist das Repository aktuell als MIT-lizenziert aus. Trotzdem wird im Framework kein Code daraus übernommen.

## 3. Agenta – Agent Workspace, Varianten und Revisionen

Repository: `Agenta-AI/agenta`

Beobachtete Muster aus der dokumentierten Agent-Oberfläche:

- eigene Bereiche für `Prompts`, `Agents`, `Evaluation` und `Observability`,
- Agent-Playground mit Build-/Chat-Modus,
- Agent-Konfiguration getrennt nach Modell/Harness, Instructions, Tools, Skills, Triggern und Dateien,
- Arbeitszustand `Draft` vs. gespeicherte Fassung,
- `Commit` als explizite Aktion,
- Agent-Varianten mit jeweils mehreren Versionen/Revisionen,
- Registry-/Playground-Trennung,
- verschlüsselte Provider-Credentials und OpenAI-kompatible Custom Provider als Konzept.

Übernahme als Framework-Konzept:

- Agent → Variante → Revision,
- Draft/Saved/Commit,
- Commit-Message und Agent-Diff,
- Playground zum Testen ohne automatische Veröffentlichung,
- Registry als auffindbare freigegebene Sicht,
- Tools, Skills, Knowledge, Trigger und Provider als getrennte versionierte Agent-Bausteine.

GitHub weist für das Repository aktuell keine einfache SPDX-Lizenz (`NOASSERTION`) aus. Es werden deshalb nur die beschriebenen Produktmuster als Inspiration verwendet.

## 4. A2A Protocol – Agent Card und Discovery

Repository: `a2aproject/A2A`

Das A2A-Protokoll beschreibt eine Agent Card zur maschinenlesbaren Discovery. Für die Registry besonders relevant sind:

- `name`, `description`, `version`,
- unterstützte Interfaces/Protokolle,
- Capabilities,
- Skills,
- je Skill `id`, `name`, `description`, `tags`, `examples`,
- Standard-Input- und Output-MIME-Typen,
- Security Schemes / Security Requirements,
- optionale Extended Agent Cards nach Authentifizierung.

Übernahme als Framework-Konzept:

- Agent-Card-artiges portables Manifest,
- Skills als explizite Such-/Discovery-Einheiten,
- Skill-Tags und Beispiele,
- Input-/Output-Modi,
- Capabilities und Security-Metadaten,
- Möglichkeit einer eingeschränkten öffentlichen und erweiterten berechtigten Registry-Sicht.

GitHub weist das A2A-Repository als Apache-2.0-lizenziert aus. Das Framework übernimmt dennoch keinen Quellcode, sondern nur das Metadaten-/Discovery-Muster.

## 5. Konsolidiertes Framework-Muster

Aus den Referenzen wird für das Verwaltungs-App-Framework folgendes Modell abgeleitet:

```text
Registry Artifact
├─ stable identity
├─ searchable metadata
│  ├─ category
│  ├─ tags
│  ├─ keywords
│  ├─ language
│  ├─ owner / organisation
│  ├─ domain / jurisdiction / audit area
│  └─ status / maturity
├─ immutable versions / revisions
├─ mutable labels → exact version
├─ commit message
├─ diff
├─ tests / evals
├─ relationships
└─ visibility / permissions
```

Für Prompts zusätzlich:

```text
Prompt
├─ text/chat components
├─ variables
├─ output contract
├─ model config
├─ tools
├─ examples
└─ eval sets
```

Für Agenten zusätzlich:

```text
Agent
├─ variants
│  └─ revisions
├─ instructions
├─ skills
├─ capabilities
├─ tools / permissions
├─ knowledge / data sources
├─ provider / model / runtime
├─ input/output modes
├─ triggers / schedules
├─ security metadata
└─ eval sets
```

## 6. Abgrenzung

Diese Referenzen begründen keine technische Abhängigkeit des Frameworks von Langfuse, Promptfoo, Agenta oder A2A. Ein abgeleitetes Verwaltungsprojekt kann vollständig eigene Implementierungen verwenden.

Die verbindlichen Anforderungen stehen in `docs/anforderungen.md`, insbesondere F-14 und F-15. Die hier dokumentierten Projekte dienen ausschließlich als nachvollziehbare Herkunft der übernommenen Designprinzipien.
