# RB-01: Datenschutzentwurf

Arbeitsfassung VVT-RB-01, Version 0.1. Keine rechtliche Freigabe.

- Verantwortliche Organisation: noch nicht benannt; E-01.
- Datenschutzkontakt: noch zu benennen; E-01.
- Zweck: interne Raumbelegung und Bearbeitung von Buchungsanfragen.
- Betroffene: beschäftigte anfragende und prüfende Personen.
- Daten: Organisationskennung, Nutzerkennung, Buchungszeitraum, Zuständigkeit und Bearbeitungsereignisse. Keine Teilnehmerlisten oder sensiblen Besprechungstitel vorgesehen.
- Herkunft: Nutzerangaben und späterer Identitätsdienst.
- Empfänger: eigene anfragende Person sowie zuständige Raumverantwortung; Administration nur entsprechend Rollenmatrix.
- Speicherung: noch zu bestimmende Organisationsinfrastruktur; keine reale Verarbeitung im Prototyp.
- Dienstleister und Drittlandbezug: nicht entschieden; vor Anschluss externer Dienste klären.
- Rechtsgrundlage: offen, E-01.
- Löschfristen und Aufbewahrung von Ereignissen/Sicherungen: offen, E-01.
- Maßnahmenentwurf: Datenraumtrennung, rollenbezogener Zugriff, Rechteentzug, nachvollziehbare Änderungen, eingeschränkter Export und Sicherungskonzept.

## Datenfluss

Synthetische Person → Webformular → API mit Rechteprüfung → Buchungsspeicher → zuständige Prüferansicht → berechtigter CSV-Export.
Ein externer Entwicklungsagent erhält ausschließlich synthetische Beispiele und Code, keine echten Buchungsdaten.

## DSFA-Vorprüfung

Katalog, zuständige Prüfstelle und verbindliche Bewertung sind vor realer Verarbeitung zu bestimmen. Ausgangspunkte: Datenumfang begrenzt, keine Leistungsbewertung geplant, keine automatisierte Entscheidung über Beschäftigte vorgesehen. Diese Planungsannahmen ersetzen keine Kriterienprüfung.

Status: nicht abgeschlossen. Systemempfehlung: nicht erstellt. Menschliche Entscheidung: offen. Keine DSFA-Freigabe behauptet.

Falls erforderlich: DSFA mit Referenz auf VVT-RB-01 v0.1, Snapshot, Risiken, Maßnahmen und dokumentierter Beteiligung führen. Neue Kalenderintegration, Auswertung individueller Nutzung oder zusätzliche Empfänger lösen erneute Bewertung aus.
