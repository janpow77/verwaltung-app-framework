# Standards und Nachweise

Das Framework gibt eine projektbezogene Arbeitsmethode vor, keine pauschale
Rechtskonformität oder Zertifizierung. Maßgeblich für MUSS/BEDINGT/SOLL bleibt
[Verbindlichkeit](verbindlichkeit.md). Die folgenden Referenzen ergänzen die
Anforderungen F-01 bis F-18; sie ersetzen weder Fachrecht noch Behördenvorgaben.

## Quellenregister

Recherche: 2026-09-08. Die angegebenen Fassungen sind bewusst gewählte
Referenzstände, keine Zusage, jeweils die neueste Ausgabe abzubilden.

| ID | Quelle / Referenzstand | Verwendung und Grenze |
|---|---|---|
| S-01 | [BSI-Standard 200-2](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/BSI_Standards/standard_200_2.pdf?__blob=publicationFile&v=2), Ausgabe 2017 | Methodik und Modellierung; konkrete Fassung vor Projektfreigabe bestätigen |
| S-02 | [BSI-Standard 200-3](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/BSI_Standards/standard_200_3.pdf?__blob=publicationFile&v=2), Ausgabe 2017 | Risikoanalyse; konkrete Fassung vor Projektfreigabe bestätigen |
| S-03 | [IT-Grundschutz-Kompendium, Edition 2023](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium/XML_Kompendium_2023.html) und [Errata](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium/errata_2023.pdf?__blob=publicationFile&v=8) | Ausgangspunkt der Sicherheitsbaseline; Modellierung und Einzelanforderungen im Projekt nachtragen |
| S-04 | [OWASP ASVS 5.0.0](https://owasp.org/www-project-application-security-verification-standard/) | Technischer Prüfkatalog für Webanwendungen; Prüfniveau und versionierte Einzel-IDs auswählen, keine gesetzliche Pauschalpflicht |
| S-05 | [EN 301 549 V3.2.1 (2021-03)](https://www.etsi.org/deliver/etsi_en/301500_301599/301549/03.02.01_60/en_301549v030201p.pdf) | Kapitel 9 Web, 10 Dokumente, 11 Software, 12 Dokumentation/Support; anwendbare Abschnitte ermitteln |
| S-06 | [WCAG 2.2, Recommendation 2024-12-12](https://www.w3.org/TR/2024/REC-WCAG22-20241212/) | A/AA als ergänzendes Projektziel; nicht mit dem WCAG-2.1-Bezug der EN-Ausgabe gleichsetzen |
| S-07 | [DSGVO, VO (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=de) | Insbesondere Art. 5, 25, 28, 30, 32–36, 39; zusätzlich anwendbares Bundes-/Landes- und Fachrecht bestimmen |
| S-08 | [BITV 2.0, konsolidierter Abruf](https://www.gesetze-im-internet.de/bitv_2_0/BJNR184300011.html), 2026-09-08 | Bundesregelung; Landesrecht und konkrete Reichweite gesondert prüfen |
| S-09 | [CycloneDX JSON 1.6](https://cyclonedx.org/docs/1.6/json/) | Beispiel für ein festzulegendes SBOM-Austauschformat; Alternativen mit festgelegter Schemafassung möglich |

BSI-Downloads und der EUR-Lex-Volltext waren beim direkten Abruf teilweise
technisch gesperrt. Ihre Einträge sind deshalb Quellenverweise, keine Behauptung
eines vollständigen aktuellen Volltextabgleichs. Vor einer normativen Freigabe
Originalfassung, Berichtigungen und gegebenenfalls Nachfolgemethodik durch die
zuständige Stelle prüfen. Die Informationssicherheitsrolle legt auch die für
Kryptografie anzuwendenden Ausgaben der TR-02102-Reihe fest.

## Vom Standard zum Nachweis

[standards-register.json](standards-register.json) ordnet jeder F-Anforderung
Quellen, vorhandene Akzeptanzfälle und eine Nachweisvorlage zu. Das ist eine
thematische Zuordnung eigener Anforderungen, keine vollständige Abbildung aller
BSI-/ASVS-/EN-Einzelanforderungen. Insbesondere F-03 und F-09 enthalten eigene
Architekturentscheidungen, die nicht unmittelbar aus einer Norm folgen.
Das gilt ebenfalls für die Produkt-, Kollaborations- und Analyseentscheidungen
F-11 bis F-18: Die Quellen markieren berührte Sicherheits-, Datenschutz- oder
Zugänglichkeitsaspekte, keine Normpflicht zu Mehrfachansichten, bestimmten
Sprachen, KI-Providern, Registries oder Notebooks. Die bedingte Anwendbarkeit
bleibt erhalten.

Im Projekt [Standardsnachweis](../vorlagen/standardsnachweis.md) anlegen:
Quelle mit Fassung und genauer Fundstelle → anwendbare Einzelanforderung →
Umsetzung am Commit → Testlauf/Review → Befund → zuständige Entscheidung.
Für BSI die ausgewählten Bausteine bis zur Anforderungs-ID modellieren;
für ASVS IDs einschließlich Version verwenden. Fehlende Zuordnungen bleiben
offen, eine bloße Themenähnlichkeit wird nicht als Erfüllung gewertet.

## Pflege

Projektverantwortung und prüfende Stelle festlegen. Vor jedem Landing sowie
bei Rechts-, Norm-, Datenfluss- oder Architekturänderungen Quellen und
Anwendbarkeit neu bewerten. Zusätzlich spätestens nach sechs Monaten eine
Wiedervorlage einplanen; das ist eine Framework-Pflegeregel, keine gesetzliche
Frist. Änderungen mit Auswirkungen auf bestehende Projekte dokumentieren.
Öffentlich verlinken statt geschützte Normtexte vollständig ins Repo kopieren.

## Ergänzende Arbeitspakete

- [Barrierefreiheit](barrierefreiheit.md)
- [Sicherheitsvorfälle](security/sicherheitsvorfaelle.md)
- [Lieferkette und SBOM](security/lieferkette.md)
- [Nutzungsrechte](../vorlagen/nutzungsrechte.md) und [menschliche Entscheidungen](../vorlagen/entscheidungen.md)

Die Inhaltsprüfung kontrolliert Referenzen und Zuordnungen, nicht Rechtmäßigkeit,
Vollständigkeit der Originalnormen oder Umsetzung einer Fachanwendung.
