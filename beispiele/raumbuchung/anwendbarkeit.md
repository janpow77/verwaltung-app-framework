# RB-01: Anwendbarkeit und Entscheidungen

Version 0.1; Basis Inhaltsversion 0.2.0. Bewertung als Muster, nicht als Organisationsentscheidung.

| ID | Anwendung | Status / Begründung | Nachweisplan |
|---|---|---|---|
| F-01 | Zwei synthetische Organisationen A und B | Anwendbar, nicht implementiert | T-01 |
| F-02 | Beschäftigte, Raumverantwortung und getrennte Administration | Anwendbar, Rollen spezifiziert | T-02 bis T-04 |
| F-03 | Anfrage bis Stornierung | Anwendbar, Übergänge spezifiziert | T-05, T-20 |
| F-04 | CSV eigener bzw. zugewiesener Buchungen | Anwendbar; PDF/DOCX/XLSX und ZIP begründet nicht benötigt | T-09, T-10 |
| F-05 | Kontaktdaten und Buchungsbezug im Zielbetrieb | Anwendbar; Datenschutzentscheidung offen | T-11, T-12 |
| F-06 | Verbindliche Bestätigung durch andere Person | Anwendbar | T-06 |
| F-07 | Anmeldung und Datenzugriff; kein Upload | Anwendbar; Uploadfälle nicht anwendbar im definierten Umfang | T-13, T-14 |
| F-08 | Prototyp, Betrieb noch nicht zugesagt | Planung anwendbar; Betriebsnachweise offen | T-15 |
| F-09 | API, Fachlogik und Rechteprüfung getrennt | Anwendbar | Architekturreview |
| F-10 | Weboberfläche für Beschäftigte | Anwendbar | T-16 bis T-18 |

## Offene Entscheidungen

| ID | Frage | Zuständige Rolle, noch zu besetzen | Betroffene Arbeiten |
|---|---|---|---|
| E-01 | Rechtsgrundlage, Aufbewahrung, DSFA-Vorprüfung | Verantwortliche Organisation mit Datenschutzbeteiligung | Verwendung realer personenbezogener Daten |
| E-02 | Hosting, Identitätsdienst, Wartung, Finanzierung | IT und fachliche Verantwortung | Dienstlicher Betrieb |
| E-03 | Wer übernimmt fachliche Verantwortung und Raumzuständigkeiten? | Organisatorische Leitung | Verbindliche reale Bestätigungen |
| E-04 | Nachnutzung über die eigene Organisation hinaus | Rechteinhaber / veröffentlichende Stelle | Veröffentlichung |

Unabhängig möglich: Spezifikation und Prototyp gegen synthetische Daten. Keine Abweichung genehmigt; alle vier Entscheidungen offen.
