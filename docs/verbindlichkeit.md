# Verbindlichkeit und Anwendbarkeit

Inhaltsversion: 0.4.0, Stand 2026-09-08. Dieses Modell beschreibt Projektanforderungen, nicht die Freigabe einer konkreten Anwendung.

| Stufe | Bedeutung | Umgang im Projekt |
|---|---|---|
| MUSS | Für jedes Projekt zu bearbeiten | Umsetzung oder begründete Abweichung mit zuständiger Entscheidung dokumentieren |
| BEDINGT | Wird bei einem benannten Auslöser zum MUSS | Auslöser prüfen; Nichtanwendbarkeit mit Begründung festhalten |
| SOLL | Empfohlene Ausgestaltung | Alternative und Folgen kurz dokumentieren |

Immer erforderlich ist die Entscheidung über Datenraum, Zugriffsmodell, Datenschutzrelevanz, fachlichen Lebenszyklus und Betriebsziel. Nicht immer erforderlich ist die gleiche technische Lösung.

## Anwendbarkeitsmatrix

| ID | Immer zu klären | Bedingter Umsetzungsumfang |
|---|---|---|
| F-01 | Datenraum, Organisation und Datenzugriff | Mehrmandantenbetrieb: Trennung in API, Diensten, Datenhaltung und Export; Einzelprojekt: klar begrenzter Datenraum |
| F-02 | Nutzergruppen, erlaubte Aktionen und Verantwortliche | Mehrnutzerbetrieb: Identitäten, Rollen, Vertretung und Rechteentzug; personenbezogene Konten bei zurechenbaren Entscheidungen |
| F-03 | Fachlicher Lebenszyklus und Änderbarkeit | Vorgangsbearbeitung: Zustände, Fristen, Rückgabe und Chronologie; reine Berechnung: Eingabe-, Ergebnis- und Versionsnachweise |
| F-04 | Exportbedarf, Empfänger und Datenumfang | Nur benötigte Formate implementieren; keine Pflicht zu sämtlichen PDF-/DOCX-/XLSX-Adaptern |
| F-05 | Datenarten, Personenbezug und zuständige Prüfung | Personenbezogene Verarbeitung: passende VVT-Unterlagen und DSFA-Vorprüfung; DSFA bei festgestellter Erforderlichkeit |
| F-06 | Welche Ergebnisse verbindlich freigegeben werden | Verbindliche Freigaben: Vier-Augen-Prinzip, Versionsschutz und zurechenbare Entscheidung; einfache Entwurfsspeicherung ist keine Freigabe |
| F-07 | Schutzbedarf und Maßnahmen | Authentifizierung, Uploads, externe Schnittstellen und KI-Nutzung lösen zusätzliche Prüffälle aus |
| F-08 | Erprobung oder vorgesehener Betrieb | Vor Betrieb: benannte Wartung, Sicherung, Wiederherstellung und Übergabe; Prototyp: offene Betriebsfragen sichtbar |
| F-09 | Architektur und Änderungsgrenzen | Eigene Fachmodule: klar definierte Schnittstellen zur Identitäts-, Rechte- und Nachweislogik |
| F-10 | Nutzer und Zugänglichkeit | Oberfläche: Tastatur, Beschriftungen, Fokus, Kontraste, Fehler und assistive Nutzung prüfen |
| F-11 | Art und Intensität der grafischen Nutzung | Regelmäßig genutzte oder kollaborative UI: Designsystem, relevante Mehrfachansichten, Responsive-Verhalten, Bild-/Hintergrund- und Performancekonzept festlegen |
| F-12 | Nutzerkreis und Sprachen/Locales | Mehrsprachiger oder internationaler Nutzerkreis: i18n-Ressourcen, Sprachwahl, Fallback und locale-abhängige Formate technisch vorsehen |
| F-13 | Funktionsumfang und Nutzerrollen | Umfangreiche/modulare Anwendung: Capabilities, Aktivierungsebenen und progressive Freischaltung definieren; Autorisierung bleibt serverseitig |
| F-14 | Nutzung externer/lokaler KI-Provider | Mehrere Provider, BYOK oder persönliche Endpunkte: Gateway-/Providervertrag, Secret Store, Datenklassen und Provider-Protokollierung umsetzen |
| F-15 | Teilbare fachliche Artefakte | Prompts, Agenten, Checklisten, Strategien, Regelwerke oder Templates: Versionen, Forks, Reviews und fachlich lesbare Diffs; Release-Versionen unveränderlich |
| F-16 | Datenimport aus fremden Strukturen | CSV/XLSX/API/Mehrtabellen-Import: versioniertes semantisches Mapping, Transformation, Vorschau, Validierung und Importnachweis |
| F-17 | Analyse, Simulation, ML/KI oder Notebook-Ausführung | Run-Manifest, Seeds/Parameter/Fingerprints, Versionsbezug und – bei interaktiven Workspaces – Isolation, Ressourcenlimits und Kernel-/Session-Lifecycle |
| F-18 | Ableitung von Test-/Austauschdaten aus realen Fällen | Redaction/Pseudonymisierung/Anonymisierung/Synthetic Twin unterscheiden, Zuordnungstabellen trennen, Dokumente technisch prüfen und Human-Review vor Weitergabe vorsehen |

SOLL: organisationsweit unterstützte Technologien, wiederverwendbare Komponenten und automatisierte wiederkehrende Prüfungen nutzen. OIDC/Keycloak, PostgreSQL/RLS und Copier sind technische Optionen; ihre Nennung ist kein automatischer Pflichtumfang.

## Abweichungen und offene Fragen

Nutze vorlagen/anwendbarkeit.md. Eine Abweichung nennt ID, Grund, Folgen, Ersatzmaßnahme und zuständige Entscheidung. Eine KI darf sie vorschlagen, aber nicht genehmigen.

Status je Anforderung: offen, anwendbar, begründet nicht anwendbar, umgesetzt, geprüft oder Abweichung zur Entscheidung. „Nicht anwendbar“ ist kein Ersatz für eine fehlende Antwort. Offene Entscheidungen blockieren nur abhängige Arbeiten, nicht unabhängige Spezifikation oder Arbeit mit Testdaten.

Bei Widersprüchen gelten die aktuelle Inhaltsentscheidung ADR-004 und diese Einstufung für den Umfang. Detaildokumente konkretisieren anwendbare Anforderungen. Historische Softwareentwürfe schaffen keine zusätzlichen Pflichten.
