# Verbindliche Anforderungen

## Fachanwendungskern

- Mandantentrennung auf API-, Service- und Persistenzebene
- OIDC/SSO-Adapter, Nutzer, Rollen und fein granulierte Berechtigungen
- serverseitige Autorisierung für jede schreibende und lesende Aktion
- Vorgangs-/Aktenmodell mit Statusmaschine, Fristen, Dokumenten und Chronologie
- Versionen, Entwürfe, Zweitprüfung, Freigabe und unveränderliche Nachweise
- JSON-, CSV-, XLSX-, PDF- und DOCX-Export über definierte Adapter
- Health-Checks, strukturierte Fehler, Monitoring und Backup-/Restore-Nachweis

## Datenschutz

- VVT je Mandant bzw. Organisation und stabile Tätigkeits-IDs
- VVT-Version als Snapshot in jeder DSFA
- Schwellwertanalyse mit erklärbarer Systemempfehlung
- DSFA je Verarbeitungstätigkeit, Risikoszenarien und Maßnahmen
- menschliche Entscheidung und Begründung jeder Abweichung
- DSB-Beteiligung, Votum und Freigabehistorie
- erneute Prüfung bei relevanter VVT- oder Systemänderung

## BSI-orientierte Baseline

Die konkrete Schutzbedarfsfeststellung entscheidet über den Umfang. Die
Baseline ist an BSI-Grundschutz-Prinzipien ausgerichtet, aber kein Zertifikat.
Mindestens sind Identitäts-/Berechtigungsmanagement, Protokollierung,
Sicherheitsanforderungen, sichere Softwareentwicklung, Schwachstellenbehandlung,
Backup/Wiederherstellung und Notfallvorsorge nachzuweisen.

## KI-Entwicklung

Jede KI-Aufgabe muss auf eine Fachanforderung, einen betroffenen Modulbereich
und konkrete Akzeptanztests verweisen. Der Agent darf den Plattformkern nur über
definierte Schnittstellen erweitern. Die fachliche, datenschutzrechtliche und
produktive Verantwortung bleibt bei benannten Menschen.

