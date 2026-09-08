# Sicherheitsvorfälle

Bezug: F-05, F-07 und F-08. Vor Betriebsübergabe Meldeweg, Erreichbarkeit,
Vertretung, Entscheidungsbefugnisse und sichere Kommunikationsalternative
festlegen. Die Anwendung liefert Signale und Belege; sie entscheidet keine
gesetzliche Meldung. [Vorfallakte](../../vorlagen/sicherheitsvorfall.md).

## Ablauf

1. Erkennen: Verdacht, Beobachtungszeit und Bekanntwerden getrennt erfassen;
   Umfang und Unsicherheiten nennen. Informationssicherheit/Betrieb alarmieren.
2. Bewerten: Betroffene Systeme, Datenräume, Datenarten und mögliche Folgen
   feststellen. Bei Personenbezug Datenschutzverantwortliche einbeziehen.
3. Eindämmen: Befugte Betriebsrolle entscheidet über Sperren, Tokenwiderruf,
   Isolation oder Abschaltung. Auswirkungen und Beweiserhalt berücksichtigen;
   keine eigenmächtigen Löschungen oder produktiven Eingriffe durch KI.
4. Sichern: Belege mit Herkunft, Zeit, Hash, Zugriffsrechten und Übergaben
   dokumentieren. Originale geschützt erhalten; keine Geheimnisse oder
   personenbezogenen Rohdaten in Issues, Prompts oder öffentliche Repos laden.
5. Melden: Zuständige menschliche Stelle entscheidet und dokumentiert
   Meldepflicht, Empfänger, Frist, Inhalt und Versandnachweis.
6. Wiederanlaufen: Ursache beheben, saubere Sicherung isoliert testen,
   Datenkonsistenz und Rechte kontrollieren; zuständige Betriebsfreigabe einholen.
7. Nachbereiten: Ursache, Wirksamkeit, Restaufgaben und Wiedervorlage festhalten;
   Schutzmaßnahmen, VVT/DSFA und Tests bei Bedarf aktualisieren.

## Datenschutzmeldung

Unter der DSGVO meldet der Verantwortliche eine Datenschutzverletzung
unverzüglich und möglichst binnen 72 Stunden nach Bekanntwerden, außer wenn
voraussichtlich kein Risiko für Rechte und Freiheiten entsteht. Die Uhr beginnt
nicht erst mit einem abgeschlossenen Untersuchungsbericht. Bei Verspätung
Gründe dokumentieren; Informationen nötigenfalls schrittweise nachreichen.
Auftragsverarbeiter unterrichten den Verantwortlichen unverzüglich.
Dokumentation ist auch bei begründeter Nichtmeldung erforderlich.
Bei voraussichtlich hohem Risiko ist die unverzügliche Benachrichtigung
Betroffener einschließlich der gesetzlichen Ausnahmen gesondert zu prüfen.
Quellen: [Art. 33/34 DSGVO, amtliche Wiedergabe](https://ao.bundesfinanzministerium.de/ao/2022/Datenschutz-Grundverordnung/inhalt.html).

DSB beraten und überwachen; die Verantwortung bleibt bei der verantwortlichen
Stelle. Zusätzlich anwendbare sektorale oder behördliche Meldewege und Fristen
festlegen; die DSGVO-Frist ersetzt diese nicht. Keine echte Meldung als Test
versenden.

## Übung T-21

Mit synthetischem Szenario „Export an falschen Datenraum“ eine Tischübung
durchführen: Meldung aufnehmen, Kontaktvertretung erreichen, Fristbeginn
diskutieren, Sperrentscheidung simulieren, Belegliste und Wiederanlaufplan
erstellen. Abweichungen mit Verantwortlichkeit und Termin dokumentieren.
RTO (zulässige Wiederanlaufdauer) und RPO (zulässiger Datenverlust in Zeit)
müssen fachlich festgelegt sein; Übung und Restoretest sind getrennte Nachweise.
