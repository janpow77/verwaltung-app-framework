# Barrierefreiheit

F-10 beginnt beim Entwurf, nicht erst beim Landing. Rechtsgrundlage,
anwendbare Teile der EN 301 549 und ergänzendes WCAG-2.2-Ziel anhand des
[Quellenregisters](standards.md) festlegen. Diese Stichprobe ist kein
vollständiger Konformitätstest. Alle zusätzlich anwendbaren Kriterien müssen
im Projekt ergänzt werden, einschließlich Dokumentation und Support.

## Prüfablauf

Hauptwege und seltene kritische Zustände auswählen: Anmeldung, Formular,
Inspektor/Detailansicht, Dialog, Validierung, Freigabe, Export, Sitzungsablauf
und Fehlerseite. Komponenten und vollständige Abläufe testen. Je Test
Browser, Betriebssystem, assistive Technik und Version protokollieren.
Automatische Prüfung ergänzen; sie ersetzt keine manuelle Bedienprüfung.

| Fall | Eigener Prüfschritt | Kriterienbezug / Erwartung |
|---|---|---|
| A-01 | Ohne Maus anmelden, Dialog öffnen/schließen und Aufgabe abschließen | WCAG 2.1.1/2.1.2/2.4.3/2.4.7: bedienbar, keine Falle, nachvollziehbarer sichtbarer Fokus |
| A-02 | Formular mit Screenreader ausfüllen und Fehler korrigieren | 1.3.1/3.3.1/3.3.2/4.1.2: Beziehungen, Fehler, Beschriftungen und Bedienelemente verständlich |
| A-03 | Asynchrone Speicherung, Ladezustand und Fehlermeldung auslösen | 4.1.3: Statusänderung ohne erzwungenen Fokuswechsel wahrnehmbar |
| A-04 | Textvergrößerung und schmalen Viewport getrennt prüfen | 1.4.4/1.4.10: 200 % Text; Reflow bei 320 CSS-Pixeln; Ausnahmen dokumentieren |
| A-05 | Alle Interaktionszustände mit Kontrastmessung prüfen | 1.4.1/1.4.3/1.4.11: nicht nur Farbe; Text 4,5:1, großer Text 3:1; relevante Nichttexte 3:1; Ausnahmen beachten |
| A-06 | Lange Seite, feststehende Leisten und kleine Ziele bedienen | 2.4.11/2.5.8 (2.2): Fokus nicht vollständig verdeckt; Zielgröße/Abstand samt Ausnahmen prüfen |
| A-07 | Sortierung per Ziehen und Login mit Passwortmanager testen | 2.5.7/3.3.8 (2.2): Alternative zum Ziehen und zugängliche Authentifizierung |
| A-08 | Erzeugtes PDF/Dokument manuell und mit Dokumentprüfer untersuchen | EN Kapitel 10: Struktur, Lesereihenfolge, Tabellen, Sprache und Alternativtexte |
| A-09 | Zeitablauf und Animationen aktivieren | WCAG 2.2.1/2.2.2/2.3.1; zusätzlich Projektziel reduzierte Bewegung |
| A-10 | Hilfeseite und Rückmeldeweg benutzen | EN Kapitel 12; erforderliche Erklärung, Feedback und weitere gesetzliche Inhalte gesondert prüfen |

## Nachweis und Nachbesserung

[Prüfprotokoll](../vorlagen/barrierefreiheit.md) mit Screenshots und konkreten
Reproduktionsschritten führen; keine echten Falldaten verwenden. Für jeden
Befund Auswirkung auf den Hauptweg, zuständige Person, Korrektur und Nachtest
festhalten. Ein Scoring-Wert oder fehlerfreier Automatenscan ist kein
Barrierefreiheitsnachweis. Bei Änderungen an Designsystem, Formularen oder
Exportvorlagen betroffene Abläufe erneut prüfen.
