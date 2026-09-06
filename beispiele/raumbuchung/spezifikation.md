# RB-01: Spezifikation

Version 0.1. Einstieg: privat begonnene Eigeninitiative einer beschäftigten Person.
Zweck: Besprechungsräume intern buchen. Heute werden Anfragen per E-Mail abgestimmt. Erwarteter Nutzen: weniger Rückfragen und keine doppelten Bestätigungen. Im Pilot sollen Rückfragen pro Buchung und Zahl widersprüchlicher Buchungen vor/nach Erprobung verglichen werden; Ausgangswerte noch nicht erhoben.

Umfang: Raumliste, Buchungsanfrage, Prüfung, Bestätigung, Rückgabe, Stornierung und eigener Buchungsexport. Ausgeschlossen: externe Vermietung, Leistungsbewertung, Dateiupload und automatische Kalenderintegration.

## Datenmodell

| Objekt | Felder | Datenraum / Beziehungen |
|---|---|---|
| Organisation | ID, Name | Oberste Trennungsgrenze |
| Raum | ID, Organisations-ID, Name, Kapazität, aktiv | Gehört zu genau einer Organisation |
| Mitgliedschaft | Nutzer-ID, Organisations-ID, Rolle, Gültigkeit | Rechte gelten nur in dieser Organisation |
| Buchung | ID, Organisations-ID, Raum-ID, Beginn, Ende, anfragende Person, Status, Version | Raum und Person müssen zum zulässigen Datenraum gehören |
| Ereignis | Buchungs-ID, Akteur, Zeitpunkt, Aktion, alte/neue Version | Nachvollziehbarkeit ohne unnötige Inhaltskopien |

Keine sensiblen Besprechungstitel oder Teilnehmerlisten im ersten Umfang.

## Rollenmatrix

| Rolle | Lesen | Ändern | Export | Bestätigung | Administration |
|---|---|---|---|---|---|
| Beschäftigte | Raumverfügbarkeit und eigene Buchungen | Eigene Entwürfe, Anfragen und Stornierung | Eigene Buchungen | Nein | Nein |
| Raumverantwortliche | Anfragen der zugewiesenen Räume | Rückgabe und Prüfung | Zugewiesene Buchungen nach Zweck | Fremde Anfragen | Nein |
| Mandantenadministration | Räume und Mitgliedschaften | Stammdaten und delegierbare Rechte | Keine pauschalen Fallexporte | Nur mit gesonderter Fachrolle; keine Selbstfreigabe | Eigene Organisation |
| Plattformbetrieb | Technischer Zustand | Betriebsparameter | Keine Fachinhalte | Nein | Technischer Betrieb |

Vertretung: zeitlich begrenzte Raumzuständigkeit, höchstens für dokumentierten Vertretungszeitraum. Planungswert für Sperrwirkung: höchstens fünf Minuten, vor Betrieb technisch nachzuweisen. Notfallzugriffe sind im Pilot nicht vorgesehen.

## Übergangsmatrix

| Von | Aktion | Rolle / Voraussetzung | Nach |
|---|---|---|---|
| Entwurf | Einreichen | Eigene Anfrage, Zeitraum gültig | Eingereicht |
| Eingereicht | Zurückgeben | Zuständige Raumverantwortung mit Begründung | Zurückgegeben |
| Zurückgegeben | Überarbeiten | Anfragende Person | Entwurf |
| Eingereicht | Bestätigen | Andere zuständige Person, keine Überschneidung | Bestätigt |
| Eingereicht / Bestätigt | Stornieren | Anfragende oder zuständige Person, Ereignis erfassen | Storniert |

Bestätigte Zeiträume werden nicht direkt überschrieben: stornieren und neu anfragen. Gleichzeitige Bestätigungen müssen konsistent behandelt werden.

## Architekturentscheidung A-01

Vorschlag: Browseroberfläche, serverseitige API, relationale Datenbank; Identität aus dem später zuständigen Organisationsdienst. Jede Anfrage bindet Mitgliedschaft, Rolle und Organisation. Technologieauswahl offen bis zur IT-Abstimmung. Keine lokale Passwortverwaltung für den angestrebten Betrieb. Dies ist ein Vorschlag, keine Infrastrukturzusage.
