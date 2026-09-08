# Verwaltungs-App-Framework – Inhalte für Säule 2

Dieses Repository bündelt Anforderungen, Agentenanweisungen, Skills und Projektvorlagen für KI-gestützte Fachanwendungen aus der Verwaltung.

Beschäftigte nutzen diese Inhalte bereits beim Start einer eigenen Entwicklung. Claude, Codex oder Gemini setzen die Anwendung anhand der Spezifikation und Vorgaben um. Anschließend wird das Projekt im Landingprozess vorgestellt und geprüft.

## Hier beginnen

1. [Startanleitung](docs/start.md)
2. [Anforderungen und Prüfkriterien](docs/anforderungen.md)
3. [Projektsteckbrief, Rollenmatrix und Prozessmodell](vorlagen/projekt.md)
4. [VVT und DSFA-Vorprüfung](vorlagen/datenschutz.md)
5. [Entwicklungsauftrag](prompts/entwicklung.md) und [unabhängiges Review](prompts/review.md)
6. [Vorstellung und Betriebsbedarf](vorlagen/landing.md)
7. [Zusammenhängendes Musterpaket: Raumbuchung](beispiele/raumbuchung/README.md)
8. [Pflege und Nachnutzung](docs/pflege-und-nachnutzung.md)

## Erweiterte Anwendungsbausteine (0.3.0)

Für moderne kollaborative, internationale und daten-/KI-intensive Fachanwendungen ergänzt Version 0.3.0 die bedingten Anforderungen F-11 bis F-18:

- [Produkt-UX, Mehrfachansichten und Internationalisierung](docs/produkt-ux-und-i18n.md)
- [Capabilities und progressive Freischaltung](docs/capabilities-und-ansichten.md)
- [KI-Provider, Gateways und persönliche Secrets](docs/ki-provider-und-secrets.md)
- [Kollaborative Artefakte: Versionen, Forks, Reviews und Diffs](docs/kollaborative-artefakte.md)
- [Prompt- und Agent-Registry mit Metadaten, Suche und Evaluation](docs/prompt-und-agent-registry.md)
- [Datenimport und semantisches Mapping](docs/datenimport-und-mapping.md)
- [Analytische Reproduzierbarkeit und Workspaces](docs/reproduzierbarkeit-und-workspaces.md)
- [Redaction, Pseudonymisierung und Synthetic Twin](docs/redaction-pseudonymisierung.md)

Besonders für Prompt-/Agent-Registries gilt: Prompts sind versionierte Artefakte mit Metadaten, Commit-Message, Tags/Kategorien/Keywords/Labels, Test-/Eval-Bezug und fachlich lesbarem Diff. Agenten werden über versionierte Manifeste mit Skills, Capabilities, Tools, Datenquellen und Security-Metadaten beschrieben.

## Verbindliche Inhalte im Überblick

- [MUSS, bedingte Anforderungen und SOLL](docs/verbindlichkeit.md)
- [Administrative Rollen und Kontenlebenszyklus](docs/administration.md)
- [Prüfkatalog](docs/pruefkatalog.md) und [Testplan](vorlagen/testplan.md)
- [Durchgängiger KI-Arbeitsablauf](docs/ki-arbeitsablauf.md)
- [Anwendbarkeit und offene Entscheidungen](vorlagen/anwendbarkeit.md)
- [Inhaltsrelease und Zuständigkeiten](vorlagen/release.md)
- [Standards, Quellen und Nachweise](docs/standards.md)
- [Barrierefreiheit](docs/barrierefreiheit.md), [Sicherheitsvorfälle](docs/security/sicherheitsvorfaelle.md) und [SBOM](docs/security/lieferkette.md)
- [Nutzungsrechte](vorlagen/nutzungsrechte.md) und [Entscheidungsregister](vorlagen/entscheidungen.md)

## Umfang und Stand

Inhaltsversion: 0.4.0 · Stand: 2026-09-08. Das Ergebnis dieser Phase ist das Inhalts-Repository; die Versionsnummer ist keine organisatorische Freigabe.
Mandanten, Nutzerrechte, Akten, Exporte, Datenschutz, Produkt-UX, Registry-Funktionen und Analyse-Workspaces sind Anforderungen an die entstehende Anwendung, soweit nach Anwendbarkeitsmatrix einschlägig. Eine fertige GUI oder produktive Dienste werden in dieser Phase nicht zugesagt.

Unvollständige Softwareentwürfe liegen ausschließlich im [Archiv](archiv/README.md). Der Python-Kern unter framework/ bleibt separat als getestete Referenzlogik erhalten. Beides gehört nicht zum zu übernehmenden Projektpaket. Details: [ADR-004](docs/adr/ADR-004-inhalts-framework.md).

## Zwei Säulen im Pilotprogramm

Datenauswertungen werden im Workshop fachlich aufgesetzt. Dieses Inhalts-Framework unterstützt insbesondere Säule 2: eigene Fachanwendungen mit Formularen, Vorgängen und Berechtigungen. Hausbedarf und Eigeninitiative sind beide mögliche Einstiege.

AGENTS.md ist die gemeinsame Arbeitsgrundlage. CLAUDE.md, CODEX.md und GEMINI.md verweisen darauf. Skills konkretisieren Aufgaben; die Umsetzung und ihre Nachweise werden im jeweiligen Projekt geprüft.

## Prüfen

```bash
python3 -m unittest discover -s tests -v
python3 checks/validate_repo.py
```

Diese Prüfungen betreffen Referenzkern und Inhaltsstruktur, nicht die Betriebsfähigkeit einer erzeugten Anwendung.
