# RB-01: Testplan und Prüfbericht

Version 0.1. Prüfobjekt: bislang Spezifikation; noch keine Anwendung vorhanden.
Geplante Umgebung: isolierter Prototyp mit Organisationen A/B und synthetischen Konten A1 (Anfrage), A2 (Prüfung), B1 (Anfrage). Alle Ausführungsergebnisse: nicht ausgeführt.

| Fall | Aufbau / Schritte | Erwartung | Ergebnis |
|---|---|---|---|
| T-01 | B1 fragt ID einer Buchung von A1 über API und Export ab | Keine fremden Inhalte | Nicht ausgeführt |
| T-02 | A1 sendet direkte Rollenänderung auf Administration | Abgewiesen | Nicht ausgeführt |
| T-03 | A1 angemeldet, Mitgliedschaft gesperrt, erneuter Zugriff | Innerhalb fünf Minuten kein Zugriff | Nicht ausgeführt |
| T-04 | Vertretungszeit von A2 endet; A2 bestätigt außerhalb des Zeitraums | Abgewiesen | Nicht ausgeführt |
| T-05 | Entwurf direkt bestätigen; zurückgegebene Anfrage überarbeiten | Sprung abgewiesen, Überarbeitung möglich | Nicht ausgeführt |
| T-06 | A1 erhält zusätzlich Prüfrolle und bestätigt eigene Anfrage | Selbstfreigabe abgewiesen | Nicht ausgeführt |
| T-09 | Drei eigene Buchungen eines Zeitraums exportieren | Genau drei zulässige Datensätze mit Auswahlbezug | Nicht ausgeführt |
| T-10 | Raumname beginnt mit Formelzeichen und enthält Sonderzeichen | Keine aktive Tabellenformel, lesbare Ausgabe | Nicht ausgeführt |
| T-11 | Felder der Anwendung gegen VVT-RB-01 vergleichen | Keine undokumentierten Daten/Empfänger | Nicht ausgeführt |
| T-12 | Geplante Teilnehmerliste ergänzen | Neubewertung sichtbar, keine automatische Freigabe | Nicht ausgeführt |
| T-13 | Fehlendes/abgelaufenes/fremdes Token nutzen | Geschützte Aktionen abgewiesen | Nicht ausgeführt |
| T-14 | Loginfehler und CSV-Export erzeugen, Logs lesen | Keine Tokens oder unnötigen Buchungsinhalte | Nicht ausgeführt |
| T-15 | Sicherung in isolierter Umgebung wiederherstellen | Konsistente Räume, Buchungen, Mitgliedschaften | Nicht ausgeführt |
| T-16–18 | Tastatur, Beschriftung, Fehler, Zoom, Kontrast prüfen | Hauptablauf ohne Barrieren im vereinbarten Prüfumfang | Nicht ausgeführt |
| T-20 | A2 und zweite zuständige Person bestätigen überlappende Anfragen gleichzeitig | Höchstens eine bestätigte Buchung | Nicht ausgeführt |

T-07/T-08 nicht anwendbar: kein Dokumentenupload/-speicher im Umfang.
T-19 nicht anwendbar: kein KI-Dokumentendienst im Betrieb; KI dient nur der Entwicklung.

## Offene Befunde

B-01: Umsetzung fehlt; deshalb keine technischen Tests bestanden.
B-02: Entscheidungen E-01 bis E-04 offen.
Empfehlung: Spezifikation vorstellen und Prototyp mit Testdaten erarbeiten. Kein Betriebsnachweis.
