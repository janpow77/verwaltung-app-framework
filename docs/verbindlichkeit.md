# Verbindlichkeit und Anwendbarkeit

Inhaltsversion: 0.2.0, Stand 2026-09-06. Dieses Modell beschreibt Projektanforderungen, nicht die Freigabe einer konkreten Anwendung.

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

SOLL: organisationsweit unterstützte Technologien, wiederverwendbare Komponenten und automatisierte wiederkehrende Prüfungen nutzen. OIDC/Keycloak, PostgreSQL/RLS und Copier sind technische Optionen; ihre Nennung ist kein automatischer Pflichtumfang.

## Abweichungen und offene Fragen

Nutze vorlagen/anwendbarkeit.md. Eine Abweichung nennt ID, Grund, Folgen, Ersatzmaßnahme und zuständige Entscheidung. Eine KI darf sie vorschlagen, aber nicht genehmigen.

Status je Anforderung: offen, anwendbar, begründet nicht anwendbar, umgesetzt, geprüft oder Abweichung zur Entscheidung. „Nicht anwendbar“ ist kein Ersatz für eine fehlende Antwort. Offene Entscheidungen blockieren nur abhängige Arbeiten, nicht unabhängige Spezifikation oder Arbeit mit Testdaten.

Bei Widersprüchen gelten die aktuelle Inhaltsentscheidung ADR-004 und diese Einstufung für den Umfang. Detaildokumente konkretisieren anwendbare Anforderungen. Historische Softwareentwürfe schaffen keine zusätzlichen Pflichten.
