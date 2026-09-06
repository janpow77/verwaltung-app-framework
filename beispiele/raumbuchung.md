# Musterprojekt: Interne Raumbuchung

Das [vollständige Musterpaket](raumbuchung/README.md) verbindet Spezifikation, Anwendbarkeit, Datenschutz, Testplan und Landing-Bericht.

Fiktives ausgefülltes Beispiel, keine freigegebene Anwendung.
Inhaltsstand: 2026-09-06. Einstieg: Eigeninitiative.

## Zweck und Umfang

Beschäftigte buchen Besprechungsräume. Heute werden Anfragen per E-Mail abgestimmt. Ziel: weniger Rückfragen und keine zeitlich überlappenden bestätigten Buchungen. Keine Leistungsbewertung, externe Vermietung oder Kalenderintegration im ersten Umfang.

## Daten und Rollen

Objekte: Raum (ID, Organisation, Name, Kapazität), Buchung (ID, Organisation, Raum-ID, Beginn, Ende, anfragende Person, Status, Version). Nur synthetische Personen im Prototyp.

Beschäftigte lesen Raumverfügbarkeit, stellen eigene Anfragen und stornieren eigene offene Buchungen. Raumverantwortliche prüfen Anfragen ihrer Organisation. Mandantenadministration verwaltet Räume und Mitgliedschaften; sie erhält nicht automatisch das Recht zur fachlichen Selbstfreigabe.

## Prozess

Entwurf → eingereicht → bestätigt oder zurückgegeben. Zurückgegeben → überarbeitet → eingereicht. Stornierung bleibt als Ereignis nachvollziehbar. Vor Bestätigung werden Rechte und Terminüberschneidungen geprüft. Für diese Musteranwendung bestätigt eine andere zuständige Person.

## Anforderungen und Prüffälle

- F-01: Person aus Organisation A kann Buchungen aus B weder lesen noch exportieren.
- F-02: Beschäftigte können keine Administrationsrechte selbst vergeben.
- F-03: Zwei gleichzeitige Bestätigungen für denselben Raum und Zeitraum führen höchstens zu einer gültigen Buchung.
- F-04: Export enthält nur berechtigte Buchungen und den dokumentierten Auswahlzeitraum.
- F-05: VVT-Arbeitsfassung beschreibt Kontaktdaten und Buchungszweck; Rechtsgrundlage, Löschfrist und DSFA-Vorprüfung bleiben bis zur zuständigen Prüfung offen.
- F-06: Freigebende Person und anfragende Person sind im Muster verschieden.

## Architektur und Landing

Vorgeschlagen: Weboberfläche, serverseitige API und relationale Datenbank. Die konkrete Technik wird im Projekt entschieden. Anmeldung wird an den vorgesehenen Identitätsdienst angebunden.

Zur Vorstellung: Demo, Spezifikation, Rollenmatrix, Nachweise für Parallelbuchungen und Mandantenisolation, Datenschutzentwurf und Wartungsbedarf. Betrieb, Finanzierung und Verantwortliche sind noch nicht entschieden.
