# Rollen- und Rechtekonzept

Die Anwendbarkeit bestimmt docs/verbindlichkeit.md. Kontenlebenszyklus, Vertretung und Rechteentzug sind in [Administration](administration.md) konkretisiert. Die Rollenliste ist eine Auswahl für das Projekt, kein Zwang zu identischen Organisationsrollen.

## Mandantenmodell

Bei Mehrmandantenbetrieb wird jedes Projekt, jede Verarbeitungstätigkeit, jedes Dokument und jeder Export eindeutig einem Datenraum zugeordnet (z. B. über eine `tenant_id`). Die API prüft den Datenraum vor der Fachlogik. Ein
Plattformadministrator darf mandantenübergreifend administrieren; ein
Mandantenadministrator bleibt auf seinen Mandanten begrenzt.

## Rollen

| Rolle | Zweck | Freigabe möglich |
| --- | --- | --- |
| Plattformadministrator | technische Plattform, Mandanten und globale Konfiguration | nur nach fachlicher Zuständigkeit |
| Mandantenadministrator | Nutzer, Rollen und Einstellungen eines Mandanten | gemäß Mandantenprozess |
| Fachverantwortung | Fachanforderung, Prüfung und fachliche Entscheidung | nicht allein technisch |
| Entwickler | Fachmodul, Tests und Dokumentation im Template | nein |
| Datenschutz | VVT, Schwellwertanalyse, DSFA und DSB-Beteiligung | Datenschutzfreigabe |
| Sicherheitsprüfung | Schutzbedarf, Baseline und technische Sicherheitsprüfung | Sicherheitsgate |
| Freigabe | Zweitprüfung und produktive Freigabe | ja, als zweite Person |
| Auditor | lesender Nachweiszugriff und Export | nein |
| Lesezugriff | lesende Fachansicht im zugewiesenen Mandanten | nein |

Optionale Referenzrechte stehen im Framework-Repository in `framework/core/permissions.py`; sie sind keine automatisch übernommene Implementierung. Die produktive
Persistenz muss Rollen aus dem Behörden-IdP oder einem verwalteten
Rollenkatalog beziehen und darf Fachmodule nicht mit UI-only-Rechten absichern.
