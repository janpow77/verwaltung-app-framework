# Rollen- und Rechtekonzept

## Mandantenmodell

Jedes Projekt, jede Verarbeitungstätigkeit, jedes Dokument und jeder Export
trägt einen `tenant_id`. Die API prüft den Datenraum vor der Fachlogik. Ein
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

Die Referenzrechte stehen in `framework/core/permissions.py`. Die produktive
Persistenz muss Rollen aus dem Behörden-IdP oder einem verwalteten
Rollenkatalog beziehen und darf Fachmodule nicht mit UI-only-Rechten absichern.

