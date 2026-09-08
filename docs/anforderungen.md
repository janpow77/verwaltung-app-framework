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

## Erweiterte Produkt-, Kollaborations- und Analyseanforderungen

Die folgenden Anforderungen werden bei entsprechendem fachlichem Auslöser verbindlich:

- **F-11 Produkt-UX und Mehrfachansichten:** Designsystem, hochwertige konsistente Zustände, responsive Darstellung und – soweit fachlich sinnvoll – mehrere Views auf demselben Datenmodell, z. B. Tabelle, Kanban, Galerie, Kalender, Timeline oder Dashboard. Details: [Produkt-UX und Internationalisierung](produkt-ux-und-i18n.md).
- **F-12 Internationalisierung:** Mehrsprachige Anwendungen trennen UI-Texte vom Code, speichern unterstützte Locales und formatieren Datum, Zahlen und Währungen locale-gerecht. Details: [Produkt-UX und Internationalisierung](produkt-ux-und-i18n.md).
- **F-13 Capabilities / progressive Freischaltung:** Große Anwendungen dürfen Funktionen nutzer-, organisations- oder projektbezogen aktivieren und ausblenden; serverseitige Rechte bleiben davon unabhängig. Details: [Capabilities und Ansichten](capabilities-und-ansichten.md).
- **F-14 KI-Provider und persönliche Secrets:** Mehrere Provider, OpenAI-kompatible Endpunkte oder BYOK werden über definierte Schnittstellen und serverseitig geschützte Secrets angebunden. Details: [KI-Provider und Secrets](ki-provider-und-secrets.md).
- **F-15 Kollaborative, versionierte Artefakte:** Prompts, Agenten, Checklisten, Regelwerke, Strategien oder Templates werden mit Version, Herkunft, Review und unveränderlicher Historie geführt. **Prompts benötigen einen fachlich lesbaren Diff zwischen Versionen**, einschließlich Text-, Metadaten-, Variablen-, Tool-/Berechtigungs- und Teständerungen. Details: [Kollaborative Artefakte](kollaborative-artefakte.md).
- **F-16 Datenimport und semantisches Mapping:** Fremde Tabellen-/Datenstrukturen erhalten versionierte Import- und Mappingprofile mit Transformation, Vorschau, Validierung und Importnachweis. Details: [Datenimport und Mapping](datenimport-und-mapping.md).
- **F-17 Analytische Reproduzierbarkeit und Workspaces:** Datenanalysen, Stichproben, Simulationen, ML/KI-Läufe und optionale Notebook-Workspaces dokumentieren Versionen, Parameter, Seeds, Eingabe-/Ausgabe-Fingerprints und isolierte Laufzeitumgebungen. Details: [Reproduzierbarkeit und Workspaces](reproduzierbarkeit-und-workspaces.md).
- **F-18 Redaction, Pseudonymisierung und Synthetic Twin:** Anwendungen zur Bereinigung oder Ableitung von Testfällen unterscheiden die Verarbeitungsmodi, trennen Zuordnungstabellen, prüfen Dokumentinhalte technisch und verlangen vor definierter Weitergabe einen Human-Review. Details: [Redaction und Pseudonymisierung](redaction-pseudonymisierung.md).

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
| F-11 | Designsystem, relevante Views und UI-Zustände festlegen | Views nutzen dieselben Fachdaten; visuelle Konfiguration verändert keine Berechtigungen oder Fachwerte |
| F-12 | Sprachen und Locales festlegen | UI-Ressourcen getrennt; Umschaltung und Formatierung ohne Änderung fachlicher Werte |
| F-13 | Capabilities und Aktivierungsebenen definieren | Ausblenden/Deaktivieren umgeht keine serverseitige Autorisierung und löscht keine Daten |
| F-14 | KI-Provider, Gateway und Secret-Verwaltung festlegen | Keine Secrets in Client, Notebook, Prompt, Git oder Logs; fremde Verbindungen nicht nutzbar |
| F-15 | Kollaborative Artefakte versionieren und reviewen | Historie unverändert; Prompt-/Agent-Diffs vollständig; Runs referenzieren exakte Version/Hash |
| F-16 | Import- und Mappingmodell definieren | Mapping/Transformation versioniert; fehlerhafte Daten sichtbar; historischer Import reproduzierbar |
| F-17 | Run-Manifest und Workspace-Grenzen definieren | Versionen/Parameter/Seed/Fingerprints nachvollziehbar; Notebook umgeht keine Rechte |
| F-18 | Sanitizing-Modi, Review und Trennung festlegen | Redaction technisch wirksam; Pseudonymtabelle getrennt; Weitergabe erst nach vorgesehenem Review |

PDF, DOCX, XLSX und andere Formate werden nach Fachbedarf ausgewählt; nicht benötigte Formate werden begründet ausgeschlossen. Bei einem einzigen Mandanten ist der Datenraum dennoch ausdrücklich zu beschreiben.

Vertiefungen: [Administration](administration.md), [Prüfkatalog](pruefkatalog.md), [KI-Arbeitsablauf](ki-arbeitsablauf.md) sowie die F-11-bis-F-18-Detaildokumente.
