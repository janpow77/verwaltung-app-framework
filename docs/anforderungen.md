# Verbindliche Anforderungen

Die folgenden Anforderungen gelten für die entstehende Anwendung. Das Repository liefert in dieser Phase Vorgaben und Vorlagen. Technikwahl und Umfang werden im Projekt dokumentiert; Abweichungen brauchen Begründung und zuständige Entscheidung.

## Verbindlichkeit

Maßgeblich für den Umfang ist [Verbindlichkeit und Anwendbarkeit](verbindlichkeit.md). Die folgende Liste ist ein Themenkatalog; bedingte Funktionen werden nur bei entsprechendem Bedarf verbindlich. Jeder Punkt erhält eine begründete Einordnung in vorlagen/anwendbarkeit.md.

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
- Bei erforderlicher DSFA: je Verarbeitungstätigkeit, Risikoszenarien und Maßnahmen
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


## Zuordnung zu prüfbaren Ergebnissen

| ID | Pflichtumfang im Projekt | Prüfkriterium |
|---|---|---|
| F-01 | Datenraum und Mandantenmodell festlegen | Fremde Daten weder über API, Suche, Dokumente noch Exporte erreichbar |
| F-02 | Nutzer, Rollen, Administration und Vertretung festlegen | Rechte serverseitig geprüft; keine eigene Rechteausweitung |
| F-03 | Akte, Prozess, Fristen und Chronologie definieren | Unerlaubte Übergänge abgewiesen; Änderungen nachvollziehbar |
| F-04 | Benötigte Exportformate und Inhalte bestimmen | Vollständigkeit, Berechtigung und sichere Dateiinhalte geprüft |
| F-05 | VVT, DSFA-Vorprüfung und offene Entscheidungen führen | Verarbeitung und Bewertung versioniert; Zuständigkeit benannt |
| F-06 | Freigaben und Schutz freigegebener Fassungen festlegen | Selbstfreigabe abgewiesen; Korrekturen als neue Version |
| F-07 | Schutzbedarf und Sicherheitsmaßnahmen dokumentieren | Maßnahmen mit Verantwortlichen und Nachweisen verknüpft |
| F-08 | Wartung, Sicherung und Übergabe planen | Zuständige Stelle und Wiederherstellungsprüfung dokumentiert |
| F-09 | Fachmodul und technische Basis trennen | Änderungen an Rechten oder Freigaben ausdrücklich geprüft |
| F-10 | Zugängliche, verständliche Oberfläche vorsehen | Tastaturbedienung, Beschriftungen und Fehlerhinweise geprüft |

PDF, DOCX, XLSX und andere Formate werden nach Fachbedarf ausgewählt; nicht benötigte Formate werden begründet ausgeschlossen. Bei einem einzigen Mandanten ist der Datenraum dennoch ausdrücklich zu beschreiben.

Vertiefungen: [Administration](administration.md), [Prüfkatalog](pruefkatalog.md), [KI-Arbeitsablauf](ki-arbeitsablauf.md).
