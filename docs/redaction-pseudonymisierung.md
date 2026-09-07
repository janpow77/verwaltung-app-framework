# Redaction, Pseudonymisierung und Synthetic Twin

Dieses Dokument konkretisiert F-18.

## Grundsatz

Anwendungen, die reale Dokumente oder Vorgänge für Test, Schulung, Community-Austausch oder KI-Erprobung bereinigen, müssen klar zwischen Redaction, Pseudonymisierung, Anonymisierung und synthetischer Neugenerierung unterscheiden.

Eine technische Bearbeitung gilt nicht allein deshalb als datenschutzrechtlich anonymisiert.

## Betriebsarten

Je nach Projekt können mindestens folgende Modi vorgesehen werden:

- **Redaction**: Informationen werden dauerhaft entfernt bzw. unkenntlich gemacht,
- **Pseudonymisierung**: Identitäten werden konsistent ersetzt; eine Zuordnung kann über getrennt gehaltene Zusatzinformationen möglich bleiben,
- **Anonymisierung**: Ziel ist eine Verarbeitung ohne Personenbezug; die Eignung ist nach dem vorgesehenen Nutzungskontext zu bewerten,
- **Synthetic Twin**: Struktur, Beziehungen und fachlich relevante Fehler-/Prozessmuster werden in einen neu erzeugten künstlichen Vorgang überführt.

## Lokale und serverseitige Verarbeitung

Kann eine Anwendung sowohl lokal als auch serverseitig sanitizen, sind die Betriebsarten klar zu kennzeichnen. Vor der Übertragung unbereinigter Daten muss der Nutzer erkennen können, wo die Verarbeitung stattfindet und welche Datenklasse dafür zugelassen ist.

## Erkennung und Ersetzung

Je nach Dokumenttyp können insbesondere verarbeitet werden:

- Namen und Kontaktdaten,
- Unternehmen/Organisationen,
- Adressen,
- Konten/IBAN,
- Aktenzeichen und Referenznummern,
- Steuer-/Identifikationsnummern,
- E-Mail und Telefon,
- Unterschriften/Stempel,
- QR-/Barcodes,
- Dateinamen und Dokumentmetadaten.

Automatische Erkennung darf Vorschläge liefern. Vor einer Weitergabe oder Veröffentlichung eines bereinigten Falls ist ein verbindlicher Human-Review vorzusehen.

## Konsistente Pseudonyme

Bei Pseudonymisierung muss dasselbe Originalobjekt innerhalb des definierten Falls bzw. Datenraums konsistent dasselbe Pseudonym erhalten, soweit dies für die fachliche Prüfung erforderlich ist.

Die Zuordnungstabelle zwischen Original und Pseudonym wird getrennt vom bereinigten Fall gespeichert und erhält strengere Rechte. Sie darf nicht zusammen mit einem Community-/Testfall exportiert werden, sofern dies nicht ausdrücklich und zulässig vorgesehen ist.

## PDF und Dokumente

Bei PDF-Redaction genügt ein sichtbares schwarzes Rechteck nicht. Der verdeckte Text bzw. das zugrunde liegende Objekt muss tatsächlich entfernt oder irreversibel ersetzt sein. Anschließend ist eine Prüfung vorzusehen, die mindestens Textlayer, Formularfelder, eingebettete Objekte und Metadaten berücksichtigt, soweit technisch relevant.

Für DOCX/XLSX und vergleichbare Formate sind je nach Bedarf zusätzlich zu berücksichtigen:

- Kommentare,
- Änderungsverfolgung,
- ausgeblendete Inhalte,
- Dokumenteigenschaften,
- eingebettete Objekte,
- Formeln oder Namen mit Originalbezug.

## Synthetic Twin

Ein Synthetic Twin darf fachlich relevante Strukturen erhalten, ohne Originalidentitäten zu übernehmen. Dazu können gehören:

- zeitliche Abfolgen,
- Betragsrelationen,
- Dokumentbeziehungen,
- Prozessfehler,
- festgelegte Ground Truth.

Die Übernahme identifizierender Originalfreitexte ist zu vermeiden. Ground-Truth-Daten werden getrennt von den der zu prüfenden KI zugänglichen Daten geführt.

## Review und Freigabe

Vor Export, Veröffentlichung oder Übergabe an einen weiteren Dienst zeigt die Anwendung:

- erkannte/ersetzte Fundstellen,
- verbleibende Warnungen,
- gewählten Modus,
- Prüfer/Reviewer,
- Version/Fingerprint des bereinigten Ergebnisses.

Die Freigabe darf nicht automatisch allein durch die Erkennungsengine erfolgen.

## Prüfnachweise

Mindestens zu testen sind:

- geschwärzter PDF-Inhalt ist nicht über Textkopie/Suche wiederherstellbar,
- wiederkehrende Identität wird konsistent pseudonymisiert,
- Zuordnungstabelle wird nicht mit dem Testfall exportiert,
- Metadaten/Dateinamen werden nach festgelegter Regel bereinigt,
- ein Human-Review ist vor als verbindlich definierter Weitergabe erforderlich,
- Synthetic Twin enthält die festgelegte Ground Truth, aber keine absichtlich übernommenen Originalidentitäten.
