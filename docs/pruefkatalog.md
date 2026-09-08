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
| T-21 | F-11, Mehrfachansichten | Dasselbe Objekt in Tabelle, Board/Galerie und weiterer aktiver View ändern | Alle Ansichten zeigen denselben Fachstand; View-Layout erzeugt keinen Parallelbestand |
| T-22 | F-11, Bilder/Hintergründe | Große/ungültige Bilddatei und erlaubtes Cover/Hintergrundbild verwenden | Regeln zu Typ/Größe/Thumbnail greifen; visuelle Einstellung verändert keine Fachdaten |
| T-23 | F-12, Internationalisierung | Sprache/Locale wechseln und Datum, Zahl, Prozent, Währung prüfen | UI wechselt vollständig; Fachwerte bleiben identisch; Formate folgen Locale |
| T-24 | F-13, Capability | Modul deaktivieren, direkten API-Aufruf versuchen, wieder aktivieren | UI blendet aus; API bleibt nach Rechten geschützt; Daten bleiben erhalten |
| T-25 | F-14, persönliche KI-Verbindung | Nutzer A legt Key an; Nutzer B versucht Lesen/Nutzen; Fehler/Logs prüfen | Kein Zugriff auf fremdes Secret; Key nie im Klartext in Antwort, Log oder Client-Speicher |
| T-26 | F-15, Prompt-Version/Diff | Prompt ändern: Text, Variable, Config, Tool und Testfall; Version vergleichen | Alte Version unverändert; Diff zeigt alle Änderungsklassen und Commit-Message |
| T-27 | F-15, Prompt-Suche/Metadaten | Über Kategorie, Tags, Keywords, Sprache, Label und Institution suchen | Erwartete Versionen auffindbar; nicht berechtigte Artefakte erscheinen weder Treffer noch Facette |
| T-28 | F-15, Labels/Fork/Agent | Label auf neue Version setzen; Prompt/Agent forken; Toolrecht in Agent-Revision ändern | Label eindeutig und historisiert; Fork-Herkunft vorhanden; Agent-Diff markiert Toolrecht deutlich |
| T-29 | F-15/F-17, Evaluation | Zwei Prompt-Versionen mit demselben Testset/Modell evaluieren | Ergebnisse referenzieren exakte Prompt-Version, Testset, Modell und Run-Manifest; Vergleich nachvollziehbar |
| T-30 | F-16, Mapping | Quellspalten umbenennen/fehlen lassen, Zahlen-/Datumsformat ändern und Mapping-Version wechseln | Vorschau zeigt Transformation/Fehler; Historie bleibt alter Mapping-Version zugeordnet |
| T-31 | F-17, Reproduzierbarkeit | Analyse mit identischer Daten-/Tool-Version und Seed wiederholen | Soweit methodisch deterministisch gleiches Ergebnis; Manifest enthält Versionen, Parameter und Fingerprints |
| T-32 | F-17, Workspace | Fremde Notebook-/Workspace-ID direkt aufrufen und Ressourcenlimit provozieren | Kein Zugriff auf fremden Workspace; Ressourcenlimit und Session-Regeln greifen |
| T-33 | F-18, PDF-Redaction | Text im PDF schwärzen und danach kopieren/suchen/extrahieren | Der entfernte Inhalt ist über die vorgesehenen Zugriffspfade nicht wiederherstellbar; Review zeigt Status |
| T-34 | F-18, Pseudonymisierung | Dieselbe Identität in mehreren Dokumenten bereinigen und Testfall exportieren | Konsistentes Pseudonym; Zuordnungstabelle getrennt und nicht im Testexport |
| T-35 | F-18, Synthetic Twin | Fall mit definierter Ground Truth synthetisieren und Originalidentitäten suchen | Ground Truth/Fachrelationen erhalten; absichtlich zu ersetzende Originalidentitäten nicht enthalten |
| T-36 | F-05/F-07/F-08, Betrieb | Synthetische Vorfall-Tischübung nach Sicherheitsvorfall-Leitfaden durchführen | Zuständigkeiten, Fristbewertung, sichere Belege und Wiederanlaufentscheidung nachvollziehbar |
| T-37 | F-07/F-08, auslieferbare Software | SBOM gegen Schema und Artefakt prüfen; falschen Digest, Versionswechsel und Testbefund einspielen | Abweichungen erkannt; Bewertung, Korrektur und Nachtest dokumentiert |
| T-38 | F-09, Architektur | Fachmodulabhängigkeiten und direkte Zugriffe auf geschützte Persistenz im Code und Architekturtest untersuchen | Kein Umgehen zentraler Rechte-, Mandanten- und Freigaberegeln; zulässige Schnittstellen belegt |

Vertiefung: [A-01 bis A-10](barrierefreiheit.md),
[Vorfallübung](security/sicherheitsvorfaelle.md),
[Lieferkettenprüfung](security/lieferkette.md).

Uploads zusätzlich festlegen: erlaubte Inhalte, Größen, Quarantäne/Scan falls vorgesehen, Speicherort, Zugriff und Fehlerbereinigung. Exporte zusätzlich festlegen: Empfänger, Auswahlzeitraum, Pflichtmetadaten, fehlende Dokumente und Größenlimits.

Bei Prompt-/Agent-Registries zusätzlich festlegen: indexierte Metadaten, Taxonomie, Sichtbarkeit, Versions-/Labelregeln, Diff-Umfang, Eval-Kriterien und Deprecation. Prompt-Diffs dürfen keine Secrets oder unzulässigen Inhalte offenlegen.

BSI-orientierte Maßnahmen werden mit konkreter Ausgestaltung und Nachweisen im Projekt verknüpft. Dieser Katalog ist weder eine Zertifizierung noch eine vollständige rechtliche oder Barrierefreiheitsprüfung.
