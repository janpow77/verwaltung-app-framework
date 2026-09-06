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

## Verbindliche Inhalte im Überblick

- [MUSS, bedingte Anforderungen und SOLL](docs/verbindlichkeit.md)
- [Administrative Rollen und Kontenlebenszyklus](docs/administration.md)
- [Prüfkatalog](docs/pruefkatalog.md) und [Testplan](vorlagen/testplan.md)
- [Durchgängiger KI-Arbeitsablauf](docs/ki-arbeitsablauf.md)
- [Anwendbarkeit und offene Entscheidungen](vorlagen/anwendbarkeit.md)
- [Inhaltsrelease und Zuständigkeiten](vorlagen/release.md)

## Umfang und Stand

Inhaltsversion: 0.2.0 · Stand: 2026-09-06. Das Ergebnis dieser Phase ist das Inhalts-Repository.
Mandanten, Nutzerrechte, Akten, Exporte und Datenschutz sind Anforderungen an die entstehende Anwendung. Eine fertige GUI oder produktive Dienste werden in dieser Phase nicht zugesagt.

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
