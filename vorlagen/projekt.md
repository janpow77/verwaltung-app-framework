# Projektsteckbrief und Spezifikation

Status: Entwurf. Alle Platzhalter ausfüllen oder begründet als offen kennzeichnen.

- Projekt / Version / Datum: […]
- Framework-Stand (Commit oder Inhaltsversion): […]
- Entwickler / fachlich verantwortliche Stelle: […]
- Einstieg (Hausbedarf / Eigeninitiative): […]
- Problem, heutiger Ablauf und messbarer Nutzen: […]
- Zielgruppen und Aufgaben: […]
- Umfang und ausdrücklich ausgeschlossene Funktionen: […]
- Workshop-Ergebnis bzw. Stand der Eigenentwicklung: […]

## Datenmodell

| Objekt | Felder / Pflichtfelder | Mandant | Beziehungen | Aufbewahrung / Löschung |
|---|---|---|---|---|
| […] | […] | […] | […] | […] |

## Rollenmatrix

Rechte gelten pro Mandant und gegebenenfalls pro Vorgang. Administration ist nicht automatisch eine fachliche Freigabeberechtigung.

| Rolle | Lesen | Anlegen / Ändern | Exportieren | Freigeben | Nutzer verwalten |
|---|---|---|---|---|---|
| Sachbearbeitung | […] | […] | […] | […] | […] |
| Prüfung | […] | […] | […] | […] | […] |
| Mandantenadministration | […] | […] | […] | […] | […] |
| Plattformadministration | […] | […] | […] | […] | […] |

## Prozessmodell

| Ausgangsstatus | Aktion | Rolle | Voraussetzung / Nachweis | Zielstatus |
|---|---|---|---|---|
| […] | […] | […] | […] | […] |

Ergänzen: Rückgabe, Korrektur, Abbruch, Fristen, Vertretung und Umgang mit Änderungen freigegebener Ergebnisse.

## Produkt-UX und Ansichten (F-11)

- Designsystem / Design-Tokens: […]
- Light / Dark / System: […]
- Zielgeräte / Responsive-Grenzen: […]
- benötigte Ansichten (Tabelle, Kanban, Galerie, Kalender, Timeline, Dashboard …): […]
- gemeinsame vs. persönliche Views: […]
- Karten-/Cover-/Hintergrundbilder und Bildspeicherung: […]
- Empty-/Loading-/Error-States: […]
- Performancegrenzen / Virtualisierung / Pagination: […]

## Sprachen und Locale (F-12)

- unterstützte Sprachen: […]
- Standardsprache / Fallback: […]
- Sprachressourcen / Übersetzungsprozess: […]
- Datum/Zahlen/Währung/Zeitzone: […]
- mehrsprachige Fachinhalte: […]

## Capabilities und progressive Freischaltung (F-13)

| Capability | Standard aktiv | Aktivierung durch | Ebene (Organisation/Projekt/Nutzer) | Abhängigkeiten | Verhalten bei Deaktivierung |
|---|---|---|---|---|---|
| […] | […] | […] | […] | […] | […] |

Beschreiben: Welche Kernfunktionen sieht ein neuer Nutzer zuerst? Welche erweiterten Funktionen werden erst bei Bedarf sichtbar?

## KI-Provider und persönliche Verbindungen (F-14)

- unterstützte Provider / OpenAI-kompatible Endpunkte: […]
- zentraler Gateway/Router: […]
- BYOK/persönliche API-Verbindungen: […]
- Secret Store / Verschlüsselung / Rotation: […]
- zulässige Datenklassen je Provider: […]
- Standardprovider / Modellrouting: […]

## Prompt-/Agent-/Artefakt-Registry (F-15)

### Taxonomie und Suche

- Artefakttypen: […]
- Kategorien: […]
- Tags / Keywords: […]
- versionierte Labels (z. B. latest/recommended/pilot): […]
- weitere Facetten (Sprache, Institution, Rechtsraum, Fonds, Audit Area …): […]
- Volltextsuche über welche Felder: […]

### Versionierung und Diff

- Versionsschema: […]
- Commit-Message/Änderungsbegründung: […]
- Fork-/Contribution-/Merge-Modell: […]
- Prompt-Diff: Text / Metadaten / Variablen / Konfiguration / Tools / Tests: […]
- Agent-Diff: Instructions / Modell / Tools / Skills / Knowledge / Guardrails / Tests: […]
- Review-/Release-Status: […]

### Evaluation

- Testsets / Golden Cases: […]
- Assertions / Rubrics / Human Review: […]
- Mindestkriterien für Labels wie `recommended`: […]

## Datenimport und Mapping (F-16)

- Quellformate / Systeme: […]
- internes semantisches Zielmodell: […]
- Mappingprofile / Versionierung: […]
- Transformationsregeln: […]
- Auto-/KI-Mapping und notwendige Bestätigung: […]
- Vorschau/Validierung/Fehlerklassen: […]
- Beziehungen zwischen mehreren Dateien/Tabellen: […]

## Reproduzierbarkeit und Workspaces (F-17)

- welche Läufe benötigen ein Run Manifest: […]
- Tool-/Code-Version: […]
- Input-/Output-Fingerprints: […]
- Parameter / Random Seed: […]
- Modell-/Prompt-/Agent-Version: […]
- Laufzeitumgebung: […]
- Jupyter/Notebook/persönliche/projektbezogene Workspaces: […]
- Ressourcenlimits / Netzwerkzugriff / Session-Lifecycle: […]

## Redaction / Pseudonymisierung / Synthetic Twin (F-18)

- benötigte Modi: […]
- lokale vs. serverseitige Verarbeitung: […]
- Datenklassen / Zulässigkeit: […]
- Erkennungs- und Ersetzungsregeln: […]
- getrennte Pseudonym-Zuordnung: […]
- PDF/DOCX/XLSX/Metadaten-Bereinigung: […]
- verbindlicher Human-Review vor welcher Weitergabe: […]
- Synthetic-Twin-/Ground-Truth-Anforderungen: […]

## Umsetzung und Nachweise

| Anforderungs-ID | Umsetzung / geplante Lösung | Prüffall | Ergebnis / Beleg | Offene Entscheidung |
|---|---|---|---|---|
| F-01 | […] | […] | […] | […] |
| F-11 | […] | […] | […] | […] |
| F-12 | […] | […] | […] | […] |
| F-13 | […] | […] | […] | […] |
| F-14 | […] | […] | […] | […] |
| F-15 | […] | […] | […] | […] |
| F-16 | […] | […] | […] | […] |
| F-17 | […] | […] | […] | […] |
| F-18 | […] | […] | […] | […] |

## Architekturentscheidung

- Entscheidung und Alternativen: […]
- Betroffene Anforderungen / begründete Abweichung: […]
- Auswirkungen und ausgleichende Maßnahmen: […]
- Zuständige prüfende Person / Entscheidung / Datum: […]
