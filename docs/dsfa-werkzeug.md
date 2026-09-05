# DSFA-Werkzeug

## Ziel

Das Werkzeug ist eine geführte Bewertung je Verarbeitungstätigkeit. Es ersetzt
keine fachliche oder datenschutzrechtliche Entscheidung. Es macht aber sichtbar,
welche Verarbeitung bewertet wurde, welche Kriterien ausgelöst haben und wer
welche Entscheidung getroffen hat.

## Ablauf

1. Verarbeitung aus dem VVT auswählen.
2. VVT-Inhalt als unveränderlichen Snapshot in die Bewertung übernehmen
   (Art. 35 Abs. 7 lit. a).
3. Fragenkatalog beantworten und Systemempfehlung erzeugen. Antworten sind
   `True` oder `False`; ein unbekannter Schlüssel oder ein anderer Typ ist ein
   Fehler und keine stille Null.
4. Notwendigkeit und Verhältnismäßigkeit bewerten (Art. 35 Abs. 7 lit. b).
5. Risikoszenarien mit Schwere, Eintrittswahrscheinlichkeit und Restrisiko
   erfassen (lit. c) sowie Abhilfemaßnahmen (lit. d).
6. Menschliche Entscheidung treffen; die Abweichung von der Empfehlung wird
   berechnet, nicht behauptet, und ist in **beide** Richtungen zu begründen.
7. Datenschutzbeauftragten beteiligen und Stellungnahme, Votum und Datum
   speichern (Art. 35 Abs. 2).
8. Bei verbleibendem hohem Restrisiko vor der Verarbeitung die Aufsichtsbehörde
   konsultieren und das Ergebnis festhalten (Art. 36 Abs. 1).
9. Durch eine zweite Person freigeben; Fassung danach sperren.
10. Bei VVT-Änderung Neubewertung anstoßen: `start_reassessment` legt die
    Folgefassung mit Vorgängerbezug und Feld-Diff an, die bisherige Fassung
    wird `abgeloest` und bleibt unverändert erhalten (Art. 35 Abs. 11).

## Fragenkatalog

Der Katalog steht als Daten in `framework/core/dsfa.py`, jede Frage mit ihrer
Fundstelle:

| Block | Inhalt | Wirkung |
| --- | --- | --- |
| A | Art. 35 Abs. 3 lit. a bis c DSGVO | harter Auslöser — ein „ja“ genügt |
| B | Muss-Liste der zuständigen Aufsichtsbehörde nach Art. 35 Abs. 4 DSGVO | harter Auslöser |
| C | die neun Kriterien des EDSA nach WP 248 rev.01 | je ein Punkt, Schwelle 2 |

Block B ist im Kern **bewusst leer**. Die Muss-Liste ist je Aufsichtsbehörde
verschieden; die zuständige Datenschutzorganisation trägt sie über
`ergaenze_muss_liste()` nach, ohne die Auswertung anzufassen.

## Mindestinhalt nach Art. 35 Abs. 7 DSGVO

Die Freigabe prüft den Mindestinhalt und verweigert sich, solange er fehlt:

| Norm | Bestandteil | Feld |
| --- | --- | --- |
| lit. a | Beschreibung der Verarbeitung und der Zwecke | `activity_snapshot` |
| lit. b | Bewertung von Notwendigkeit und Verhältnismäßigkeit | `necessity`, `proportionality` |
| lit. c | Bewertung der Risiken für die Rechte und Freiheiten | `risk_scenarios` |
| lit. d | Abhilfemaßnahmen, Garantien und Verfahren | `mitigation_measures` |
| Abs. 9 | Standpunkt der betroffenen Personen | `data_subject_view` |

## Übernommene Muster aus `regulierung`

- Statusfolge `entwurf → dsb_beteiligung → freigegeben → abgeloest`
- VVT-Version und Tätigkeits-Snapshot
- Systemvorschlag mit Kriterientext und Fundstelle statt Black-Box-Ampel
- berechnete Abweichung mit Mindestlänge der Begründung
- Pflicht zur menschlichen Entscheidung, zurechenbar mit Person und Zeitpunkt
- DSB-Stellungnahme und Votum; ein ablehnendes Votum blockiert die Freigabe,
  bis eine dokumentierte, substanzielle Begründung vorliegt
- Vier-Augen-Freigabe
- Feld-Diff der Tätigkeit als Grundlage der Neubewertung
- DB-seitig zu schützende Unveränderlichkeit nach Freigabe
- PDF-/Excel-Übersichten als spätere Produktionsadapter

## Abgrenzung

Schwellwerte, Kriteriengewichtung und rechtliche Bewertung werden
konfigurierbar gehalten. Der Frameworkkern liefert Struktur, Nachweis und
Freigabelogik; die zuständige Datenschutzorganisation legt die fachlich
gültigen Kriterien und Anwendungsgrenzen fest.

Die Unveränderlichkeit einer freigegebenen Fassung ist im Vertragskern eine
Funktionskonvention (`locked`). Produktiv ist sie **in der Datenbank**
durchzusetzen; ein In-Memory-Objekt schützt sich nicht gegen direkten
Attributzugriff.
