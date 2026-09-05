# Projektakte und Exporte

## Projektakte

Die Akte ist die zentrale Nachweisfläche des Landingprozesses. Sie führt
Steckbrief, Mandant, Verantwortliche, Repository-/Release-Referenz, Rollen,
Workflow, VVT-/DSFA-Nachweise, Sicherheitsprüfungen, Tests, Fristen, Dokumente
und die Chronologie zusammen.

Fristen werden erledigt, nicht gelöscht. Dokumente und Freigaben bleiben mit
Version, Prüfsumme, Ersteller und Freigeber nachvollziehbar. Änderungen
erzeugen neue Fassungen.

## Exportarten

- **Projektpaket**: JSON-Metadaten, Rollenmatrix, Prozess, Nachweise,
  Prüfergebnis und Dokumentenverzeichnis
- **VVT/DSFA**: strukturierter JSON-Export und Tabellenexport
- **Arbeitslisten**: CSV für Vorgänge, Fristen, Status und Prüfaufgaben
- **Berichte**: PDF/DOCX/XLSX als versionierte Produktionsadapter
- **Gesamtakte**: Deckblatt, Statuschronologie, Dokumente, Prüfsummen und
  Nachweisindex

Jeder Export erhält mindestens Projekt-/Mandantenkennung, Erstellungszeitpunkt,
Framework-Version und auslösende Person. Exportberechtigungen sind eigene
Rechte; ein Datenbankzugriff darf nicht automatisch einen Voll-Export erlauben.
