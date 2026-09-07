# Prompt- und Agent-Registry: Metadaten, Suche, Versionen und Evaluation

Dieses Dokument konkretisiert F-15 und F-14 für Anwendungen, die Prompts und Agenten als auffindbare, wiederverwendbare Fachartefakte verwalten.

Die Struktur orientiert sich an bewährten Mustern aus Open-Source-Systemen: getrennte unveränderliche Prompt-Versionen mit Labels/Tags und Konfiguration, testbare Prompt-Suites, Agent-Varianten/-Revisionen sowie beschreibende Agent-Cards mit Skills, Capabilities und Security-Informationen. Es wird kein fremder Quellcode übernommen.

## 1. Registry statt Dateiablage

Prompts und Agenten werden nicht als ungeordnete Textdateien verwaltet. Sie bilden eine durchsuchbare Registry mit stabilen Identitäten, Versionen, Metadaten, Beziehungen und Qualitätsnachweisen.

Die Registry muss mindestens unterstützen:

- Volltextsuche über freigegebene Suchfelder,
- Filter/Facetten,
- Tags und Kategorien,
- Versionen und Labels,
- Fork/Herkunft,
- Review-/Reifegrad,
- Test-/Evaluationsergebnisse,
- Beziehungen zu Projekten, Themen und anderen Artefakten,
- persönliche Favoriten bzw. gespeicherte Suchen, soweit fachlich vorgesehen.

## 2. Gemeinsame Kernmetadaten

Jedes Registry-Artefakt besitzt mindestens:

```yaml
id: stable-uuid
slug: fnlc-evidence-review
name: FNLC Evidence Review
artifact_type: prompt # prompt | agent | checklist | strategy | template
short_description: Prüft Nachweise zu Bedingungen und Meilensteinen.
description: ...
version: 1.4.0
status: reviewed
visibility: community
language: [de, en]
category: [fnlc, evidence]
tags: [audit, cohesion, verification]
keywords: [milestone, condition, evidence]
owner:
  user_id: ...
  organisation_id: ...
created_at: ...
updated_at: ...
created_by: ...
commit_message: Improve missing-evidence handling
content_hash: sha256:...
```

Zusätzlich sollen, soweit relevant, unterstützt werden:

- `jurisdiction` / Rechtsraum,
- `fund` / Fonds oder Programmbereich,
- `programming_period`,
- `audit_area`,
- `target_audience`,
- `license` / Nutzungsstatus,
- `documentation_url`,
- `source_repository`,
- `related_topics`,
- `related_projects`,
- `related_checklists`,
- `maturity`,
- `last_reviewed_at`,
- `last_tested_at`.

Metadatenfelder werden kontrolliert erweitert. Wichtige Filterfelder sollen als definierte Enums/Taxonomien oder referenzierte Katalogwerte geführt werden, nicht ausschließlich als Freitext.

## 3. Tags, Kategorien, Keywords und Labels unterscheiden

Die Registry unterscheidet bewusst:

- **Kategorie**: fachliche Einordnung aus kontrolliertem Katalog, z. B. `FNLC`, `Reporting`, `System Audit`.
- **Tags**: flexible Mehrfachkennzeichnung zur Suche und Gruppierung.
- **Keywords**: Suchbegriffe/Synonyme, die nicht zwingend in der UI als Tag erscheinen.
- **Labels**: bewegliche Verweise auf konkrete Versionen, z. B. `latest`, `recommended`, `pilot`, `production`, `training`.

Ein Label verweist innerhalb eines Artefakts immer eindeutig auf eine konkrete Version. Das Umsetzen eines Labels verändert die zugrunde liegende Version nicht und wird protokolliert.

## 4. Auffindbarkeit und Suche

Mindestens filterbar/suchbar sind, soweit vorhanden:

- Name und Kurzbeschreibung,
- Kategorie,
- Tags/Keywords,
- Artefakttyp,
- Sprache,
- Institution/Owner,
- Status/Reifegrad,
- Version/Label,
- Rechtsraum/Fonds/Programmbereich,
- unterstützte Modelle/Provider,
- benötigte Tools/Skills,
- Zeitpunkt der letzten Änderung bzw. Prüfung.

Für größere Registries sind Facetten mit Trefferzahlen vorzusehen.

Beispiel:

```text
Prompts
Search: "FNLC evidence"

Category      FNLC (12)  Reporting (4)
Language      EN (10)    DE (8)
Status        Reviewed (6)  Experimental (5)
Provider      Any (9)    OpenAI-compatible (4)
Organisation  Austria (3) Hessen (4) ...
```

Die Suche über eigentliche Prompt-/Agent-Inhalte ist gesondert konfigurierbar, weil Inhalte schutzbedürftiger sein können als Metadaten. Mandanten- und Sichtbarkeitsrechte gelten bereits bei Indexierung und Suche.

## 5. Prompt-Metadaten

Zusätzlich zu den Kernmetadaten besitzt ein Prompt mindestens:

```yaml
prompt_type: chat # text | chat | system | multi_message
purpose: evidence_review
variables:
  - name: condition
    type: string
    required: true
    description: Zu prüfende Bedingung
  - name: evidence
    type: document_set
    required: true
output:
  format: json
  schema_ref: evidence-review-v1
model_compatibility:
  provider_independent: true
  tested:
    - provider: openai-compatible
      model: ...
model_config:
  temperature: 0.1
  max_tokens: 4000
tools: [legal_search, document_search]
```

Optional:

- system/user/message components separately,
- examples,
- negative examples,
- expected citations/source behavior,
- data classification allowed,
- token/cost observations,
- deprecation/replacement reference.

## 6. Prompt-Versionen und Commit-Messages

Jede fachlich relevante Änderung erzeugt eine neue unveränderliche Prompt-Version. Zu jeder Version gehört eine kurze Commit-Message bzw. Änderungsbegründung.

Eine Version speichert den vollständigen Snapshot. Eine Version darf nach Veröffentlichung nicht in-place überschrieben werden.

Neben numerischen/semantischen Versionen können Labels auf Versionen zeigen. Beispiel:

```text
v1.2.0   reviewed
v1.3.0   pilot
v1.4.0   latest, recommended
```

## 7. Prompt-Diff

Der Versionsvergleich ist eine Kernfunktion der Registry.

Der Diff umfasst mindestens:

- System-Prompt,
- User-/Task-Prompt bzw. Chat-Messages,
- Variablen,
- Output-Schema,
- Modellkonfiguration,
- Tools/Berechtigungen,
- Metadaten,
- Tags/Kategorien/Labels,
- Testfälle/Evals.

Die UI bietet mindestens:

- Side-by-Side Diff,
- Unified Diff,
- Filter `nur fachliche Änderungen`,
- einklappbare unveränderte Bereiche.

Besonders hervorzuheben sind Änderungen an:

- Tool-Rechten,
- erlaubten Datenquellen,
- Output-Verträgen,
- sicherheitsrelevanten Instruktionen,
- Grounding-/Quellenanforderungen.

## 8. Prompt-Tests und Evaluation

Prompts können ein oder mehrere versionierte Testsets referenzieren.

Ein Testfall enthält mindestens:

```yaml
id: case-017
name: missing milestone evidence
variables: {...}
expected:
  properties:
    - identifies_missing_evidence
    - no_final_legal_decision
assertions:
  - type: schema
  - type: contains
  - type: rubric
```

Unterstützt werden können:

- deterministische Assertions,
- Schema-/Formatprüfungen,
- Referenz-/Golden-Outputs,
- regelbasierte Qualitätsmetriken,
- modellgestützte Rubrics/Judges mit eigener dokumentierter Version,
- menschliche Bewertung.

Eval-Ergebnisse werden der Prompt-Version, dem Testset, Modell/Provider und Run-Manifest zugeordnet. Ein `recommended`- oder vergleichbares Qualitätslabel kann projektbezogen an Mindestkriterien gebunden werden.

## 9. Agent Registry / Agent Card

Ein Agent wird durch ein portables Manifest beschrieben. Die Registry soll sich konzeptionell an einer Agent-Card orientieren: Identität, Version, Beschreibung, Fähigkeiten/Skills, Ein-/Ausgabeformen, Schnittstellen und Security-Informationen werden explizit beschrieben.

Mindestens:

```yaml
id: ...
name: FNLC Evidence Agent
version: 2.1.0
description: ...
provider_organisation: ...
icon: ...
documentation_url: ...
status: reviewed

skills:
  - id: evidence-review
    name: Evidence Review
    description: Prüft Nachweise gegen definierte Bedingungen.
    tags: [fnlc, evidence]
    examples:
      - "Check whether milestone M3 is sufficiently evidenced"

capabilities:
  streaming: false
  file_input: true
  structured_output: true
  human_review: required

input_modes:
  - text/plain
  - application/pdf
  - application/vnd.openxmlformats-officedocument.wordprocessingml.document
output_modes:
  - application/json
  - text/markdown
```

## 10. Agent-Konfiguration

Zusätzlich werden, soweit relevant, versioniert:

- Runtime/Harness,
- Provider und Modellanforderungen,
- Instructions/System Prompt,
- Tools,
- Skills,
- Datenquellen/Knowledge,
- Guardrails,
- Handoffs/aufgerufene Workflows,
- Trigger/Schedules,
- Dateien/Knowledge Packs,
- Output-Verträge,
- Security-/Authentifizierungsbedarf.

Eine Änderung an Tool- oder Datenrechten wird als sicherheitsrelevanter Diff markiert.

## 11. Agent-Varianten und Revisionen

Ein Agent kann mehrere **Varianten** besitzen, z. B. unterschiedliche fachliche Konfigurationen. Jede Variante besitzt eine lineare oder nachvollziehbar verzweigte Folge unveränderlicher **Revisionen**.

Beispiel:

```text
Agent: Finding Assistant
├─ Variant: default
│  ├─ v1
│  ├─ v2
│  └─ v3  [recommended]
└─ Variant: concise-report
   ├─ v1
   └─ v2
```

Eine Arbeitskopie kann `Draft` sein. `Commit` erzeugt eine neue Revision mit Commit-Message. `Revert` verwirft nur ungespeicherte Änderungen; veröffentlichte Revisionen werden nicht verändert.

## 12. Agent-Diff

Zwischen Revisionen bzw. Varianten werden mindestens verglichen:

- Instructions,
- Modell/Provider/Parameter,
- Tools und Tool-Rechte,
- Skills,
- Knowledge/Datenquellen,
- Trigger/Schedules,
- Output-Vertrag,
- Guardrails,
- Metadaten,
- Test-/Eval-Zuordnung.

## 13. Playground und Registry

Wenn Agenten interaktiv testbar sind, soll ein Playground Entwürfe ausführen können, ohne diese automatisch zu veröffentlichen.

Die Registry ist dagegen die freigegebene bzw. auffindbare Sicht auf vorhandene Versionen/Revisionen.

Der Playground zeigt mindestens:

- verwendete Variante/Revision,
- Draft/Saved-Zustand,
- Provider/Modell,
- aktivierte Tools/Skills,
- Session/Testkontext.

## 14. Security-Metadaten für Agenten

Agenten können deklarieren:

- Authentifizierungsart,
- erforderliche Scopes/Rollen,
- zulässige Datenklassen,
- externe Datenübertragungen,
- benötigte Netzwerkziele,
- schreibende vs. lesende Tools.

Diese Angaben sind Teil der Registry-Metadaten und werden bei sicherheitsrelevanten Änderungen erneut geprüft.

## 15. Beziehungen und Graph

Registry-Artefakte dürfen miteinander verknüpft werden:

```text
Topic
  ↓
Project
  ├─ Prompt
  ├─ Agent
  ├─ Checklist
  ├─ Dataset/Testset
  └─ Tool/Framework
```

Diese Beziehungen verbessern Suche, Nachnutzung und Impact-Analyse. Vor dem Deprecaten einer Version kann angezeigt werden, welche Agenten, Projekte oder Tests sie verwenden.

## 16. Prüfnachweise

Mindestens zu prüfen sind:

- Suche findet Artefakte über Name, Kategorie, Tags und Keywords,
- Facetten berücksichtigen Sichtbarkeits-/Mandantenrechte,
- Label verweist eindeutig auf die erwartete Version,
- Umsetzen eines Labels ändert keine Version,
- Prompt-Diff zeigt Inhalts-, Variablen-, Konfigurations- und Teständerungen,
- Eval-Lauf verweist auf exakte Prompt-Version + Testset + Modell,
- Agent-Diff hebt Tool-/Berechtigungsänderungen hervor,
- Draft-Ausführung veröffentlicht keinen Agenten,
- Agent-Skills/Capabilities sind über Metadaten auffindbar,
- Deprecation benennt optional eine Ersatzversion/einen Ersatzagenten,
- Secrets werden weder indexiert noch als Registry-Metadaten gespeichert.
