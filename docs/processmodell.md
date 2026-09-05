# Prozessmodell für Projektakte und Landingprozess

## Grundidee

Das Framework verbindet Statusmaschine, Akte, Chronologie, Fristen, Dokumente
und Freigabegates. Jeder Statuswechsel ist eine fachliche Handlung mit Person,
Zeit, Begründung sowie Vorher/Nachher. Ein Übergang außerhalb der Matrix ist
nicht zulässig.

## Zwei zulässige Einstiege

### Hausbedarf

```text
Idee eingegangen → Workshop → Framework angelegt → Entwicklung
```

### Eigeninitiative

```text
Eigene Idee → Framework angelegt → Entwicklung → Projekt vorstellen
```

Die zweite Route verhindert Schatten-IT, weil die Entwicklung nicht erst nach
einer Genehmigung in das Framework wechseln muss. Das Framework ist von Anfang
an verfügbar. Die spätere Vorstellung ist der geregelte Landingprozess.

## Prozessgrafik

```mermaid
flowchart TD
  A[Idee oder Eigeninitiative] --> B{Einstieg}
  B -->|Hausbedarf| C[Bottom-up-Workshop]
  B -->|Eigeninitiative| D[Framework sofort nutzen]
  C --> E[Projektakte und Repository anlegen]
  D --> E
  E --> F[Entwicklung mit Claude/Codex]
  F --> G[Projekt vorstellen]
  G --> H[Fachprüfung]
  H --> I[Datenschutz: VVT und Schwellwertanalyse]
  I --> J{DSFA erforderlich?}
  J -->|ja| K[DSFA je Verarbeitung · DSB-Beteiligung]
  J -->|nein| L[Datenschutzprüfung dokumentiert]
  K --> M[Sicherheitsprüfung und Tests]
  L --> M
  M --> N[Freigabevorlage]
  N --> O{Vier-Augen-Freigabe}
  O -->|zurück| P[Korrektur mit Begründung]
  P --> F
  O -->|freigegeben| Q[Versionierter Betrieb]
  Q --> R{Änderung der Verarbeitung?}
  R -->|ja| S[Neubewertung]
  S --> I
  R -->|nein| Q
  G --> T[Abbruch möglich]
```

## Akte und Nachweise

Die Projektakte enthält mindestens:

- Projektsteckbrief, verantwortliche Personen und Mandant
- Repository-/Release-Referenz und verwendete Framework-Version
- Rollenmatrix und Workflowbeschreibung
- Datenquellen, Datenkategorien und VVT-Tätigkeit
- Schwellwertanalyse und gegebenenfalls DSFA-Snapshot
- Sicherheitsbaseline, Tests, Abhängigkeiten und offene Risiken
- Präsentations-/Landingprotokoll und Freigabeentscheidung
- Dokumente, Exporte, Fristen und unveränderliche Chronologie
