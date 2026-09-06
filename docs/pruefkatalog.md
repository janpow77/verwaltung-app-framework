# Prüfkatalog für das eigene Projekt

Die folgenden Fälle sind Akzeptanzkriterien, keine Behauptung bereits bestandener Tests. Anwendbarkeit nach docs/verbindlichkeit.md; Ergebnisse in vorlagen/testplan.md.

| Fall | Bezug / Auslöser | Durchführung | Erwartung |
|---|---|---|---|
| T-01 | F-01, getrennte Datenräume | IDs von A in Lesen, Suche, Änderung und Export unter B einsetzen | Keine fremden Inhalte oder Änderungen |
| T-02 | F-02, Rollen | Direkten API-Aufruf ohne erforderliches Recht senden | Zugriff verweigert, auch bei sichtbarer UI |
| T-03 | F-02, Rechteentzug | Sitzung öffnen, Nutzer sperren, erneut zugreifen | Entzug innerhalb der festgelegten Frist wirksam |
| T-04 | F-02, Vertretung | Vor, während und nach Vertretungszeit handeln | Nur im zulässigen Zeit- und Aufgabenbereich erlaubt |
| T-05 | F-03, Prozess | Unzulässigen Sprung, Rückgabe und erneute Bearbeitung versuchen | Übergangsmatrix durchgesetzt; Historie bleibt erhalten |
| T-06 | F-06, verbindliche Freigabe | Ersteller versucht Selbstfreigabe und spätere Änderung | Selbstfreigabe abgewiesen; Korrektur erzeugt Folgefassung |
| T-07 | F-07, Upload | Übergröße, falschen Typ, manipulierten Pfad und fremde Vorgangs-ID verwenden | Nach festgelegter Regel abweisen; keine fremden Dateien überschreiben |
| T-08 | F-03/F-07, Dokumente | Fehlenden bzw. veränderten gespeicherten Inhalt abrufen | Verständlicher Fehler oder Integritätsbefund; kein stiller Erfolg |
| T-09 | F-04, Export | Auswahl mit bekannter Zahl, Filter und Berechtigung exportieren | Umfang, Datensätze, Metadaten und Version stimmen |
| T-10 | F-04, Tabellen/Archive | Formeleingaben, Sonderzeichen, gleiche Namen und Pfadsegmente exportieren | Sichere, eindeutige Ausgabe; keine unbeabsichtigte Formel oder Archivpfade |
| T-11 | F-05, personenbezogene Verarbeitung | Datenmodell und Datenfluss gegen VVT-Arbeitsfassung vergleichen | Zwecke, Kategorien, Empfänger und offene Entscheidungen nachvollziehbar |
| T-12 | F-05, DSFA | Verarbeitung ändern und Vorprüfung unvollständig lassen | Neubewertungsbedarf sichtbar; keine simulierte Freigabe |
| T-13 | F-07, Anmeldung | Fehlendes, abgelaufenes und für andere Anwendung bestimmtes Token senden | Geschützte Aktion abgewiesen |
| T-14 | F-07, Protokolle | Fehler, Login und Export auslösen, Logs prüfen | Erforderliche Nachweise, keine Tokens oder unnötigen Inhaltsdaten |
| T-15 | F-08, Betrieb | Sicherung in isolierter Umgebung wiederherstellen | Daten und benötigte Konfiguration nutzbar; Dauer dokumentiert |
| T-16 | F-10, Oberfläche | Hauptablauf ausschließlich mit Tastatur bedienen | Sichtbarer Fokus, sinnvolle Reihenfolge, keine Tastaturfalle |
| T-17 | F-10, Formulare | Felder mit assistiver Technik prüfen, Fehler auslösen | Verständliche Beschriftungen, Zuordnung und Statusmeldungen |
| T-18 | F-10, Darstellung | Zoom, schmale Ansicht, Kontrast und reduzierte Bewegung prüfen | Inhalte und Aktionen nutzbar; Bedeutung nicht nur über Farbe |
| T-19 | F-07, KI verarbeitet Dokumente | Dokument enthält Anweisung zum Datenabfluss | Dokument als Daten behandelt; keine unberechtigte Aktion |
| T-20 | F-03, parallele Bearbeitung | Widersprechende Änderungen gleichzeitig ausführen | Kein stilles Überschreiben; fachliche Konsistenz erhalten |

Uploads zusätzlich festlegen: erlaubte Inhalte, Größen, Quarantäne/Scan falls vorgesehen, Speicherort, Zugriff und Fehlerbereinigung. Exporte zusätzlich festlegen: Empfänger, Auswahlzeitraum, Pflichtmetadaten, fehlende Dokumente und Größenlimits.

BSI-orientierte Maßnahmen werden mit konkreter Ausgestaltung und Nachweisen im Projekt verknüpft. Dieser Katalog ist weder eine Zertifizierung noch eine vollständige rechtliche oder Barrierefreiheitsprüfung.
