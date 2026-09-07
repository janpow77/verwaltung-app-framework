# Produkt-UX, Ansichten und Internationalisierung

Dieses Dokument konkretisiert F-11 und F-12. Es ergänzt die bestehende Anforderung F-10 nicht um neue Barrierefreiheitsregeln; F-10 bleibt unverändert maßgeblich.

## F-11 Produkt-UX und visuelle Qualität

Anwendungen mit regelmäßig genutzter grafischer Oberfläche legen vor der Umsetzung ein konsistentes Designsystem fest. Es beschreibt mindestens Farben, Typografie, Abstände, Radien, Schatten, Icons, Oberflächen, Dialoge, Statusdarstellungen und Interaktionszustände.

Die Oberfläche soll der fachlichen Aufgabe angemessen hochwertig und ruhig wirken. Eine technisch funktionierende CRUD-Oberfläche allein genügt nicht, wenn das Projekt einen kollaborativen, visuellen oder publikumsnahen Einsatz vorsieht.

Je nach Fachbedarf sind insbesondere zu entscheiden und zu dokumentieren:

- Light-, Dark- und Systemdarstellung,
- responsive Layouts für die vorgesehenen Gerätegrößen,
- Karten mit Coverbildern, Farben oder Hintergrundbildern,
- Projekt-, Board- oder Bereichshintergründe,
- Empty-, Loading-, Error- und Success-States,
- konsistente Motion-/Transition-Regeln,
- Bildoptimierung, Thumbnails und Dateigrenzen,
- Performance bei großen Listen, Boards und Tabellen durch Pagination, Lazy Loading oder Virtualisierung.

## Mehrfachansichten

Wenn dieselben Fachobjekte in unterschiedlichen Arbeitsweisen genutzt werden, soll die Anwendung **ein Datenmodell mit mehreren Ansichten** verwenden statt paralleler Datenbestände.

Je nach Bedarf kommen insbesondere in Betracht:

- Tabelle,
- Liste,
- Kanban/Board,
- Galerie/Karten,
- Kalender,
- Timeline,
- Dashboard/Diagrammansicht.

Eine View speichert ihre Darstellungsparameter getrennt von den Fachdaten, insbesondere Typ, Filter, Sortierung, Gruppierung, sichtbare Felder und Layout. Projekte mit gemeinsamer Zusammenarbeit unterscheiden zwischen einer offiziellen bzw. geteilten View und persönlichen Views eines Nutzers.

Bild- und Hintergrundfunktionen dürfen die fachlichen Daten nicht verändern. Dateien werden über den normalen Datei-/Berechtigungsdienst eingebunden; externe Bild-URLs oder eingebettete Daten-URLs sind nur nach dokumentierter Sicherheitsentscheidung zulässig.

## F-12 Internationalisierung und Locale

Sobald mehr als eine Sprache oder mehr als ein regionales Zahlen-/Datumsformat vorgesehen ist, wird Internationalisierung vor dem ersten UI-Ausbau als Architekturentscheidung festgelegt.

Dann gilt mindestens:

- UI-Texte liegen in versionierten Sprachressourcen und nicht verteilt als hart codierte Fachtexte im Quellcode,
- der Nutzer kann eine unterstützte Sprache bzw. Locale wählen,
- Datum, Uhrzeit, Zahlen, Prozentwerte und Währungen werden locale-abhängig formatiert,
- Sprachumschaltung verändert keine fachlichen Werte,
- fehlende Übersetzungen besitzen eine definierte Fallback-Regel,
- mehrsprachige Fachinhalte speichern Originalsprache und verfügbare Sprachfassungen getrennt.

Für deutsch-englische Anwendungen sind mindestens `de` und `en` als eigenständige Ressourcen zu führen. Übersetzungen durch KI dürfen vorgeschlagen werden, gelten aber nicht automatisch als freigegebene Fachfassung.

## Prüfnachweise

Das Projekt dokumentiert mindestens:

- Designsystem bzw. Design-Tokens,
- unterstützte View-Typen und deren gemeinsame Datenquelle,
- gespeicherte persönliche/geteilte View-Konfigurationen,
- unterstützte Sprachen/Locales,
- Screenshot- oder UI-Testnachweise für die wesentlichen Darstellungen,
- Performancegrenzen für besonders große Ansichten, soweit relevant.
