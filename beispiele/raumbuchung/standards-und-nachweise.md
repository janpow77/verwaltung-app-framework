# Ergänzung Standards und Nachweise

Synthetisches Beispiel RB-01. Ergänzung für Framework 0.4.0 zum bisherigen
Musterpaket; dessen fachliche Ausgangsfassung bleibt unverändert.
Es gibt keine implementierte Anwendung und keine tatsächlichen Prüfergebnisse.

| Anforderung | Geplante Umsetzung / Prüfung | Geplanter Beleg | Status |
|---|---|---|---|
| F-01/F-02 | Raumbuchungen je Organisation; fremde Buchungs-ID direkt an API senden | T-01/T-02, Rollenmatrix und späterer Testlauf | nicht geprüft |
| F-04/F-10 | Buchungsformular, Konfliktmeldung und Bestätigung mit Tastatur/Screenreader testen | A-01 bis A-05; A-08 bei Dokumentexport | nicht geprüft |
| F-05 | VVT-Entwurf gegen Datenfluss prüfen; DSB-Beratung und menschliche Entscheidung getrennt | T-11/T-12, Datenschutzentwurf | offen |
| F-07/F-08 | Irrtümlichen organisationsfremden Export als Tischübung besprechen | T-36, synthetische Vorfallakte | geplant |
| F-07/F-08 | Bei erster Softwareauslieferung echte Build-SBOM erzeugen | T-37, Generator-/Artefaktnachweis | mangels Build nicht geprüft |
| F-09 | Fachlogik nutzt zentrale Rechteprüfung statt direkten ungeschützten Datenzugriff | T-38, späterer Architekturtest | nicht geprüft |

Das ist ein Ausschnitt, kein Ersatz für die Behandlung aller F-Anforderungen
im [Anwendbarkeitsdokument](anwendbarkeit.md) und im
[Standardsnachweis](../../vorlagen/standardsnachweis.md).
Behördenebene, konkrete Normeinzelstellen und Quellenfassungen sind noch zu
bestätigen. Benannte Betriebsverantwortung, Rechtsgrundlage, Lizenz und
Einsatzfreigabe bleiben menschliche Entscheidungen; siehe
[Entscheidungsregister](../../vorlagen/entscheidungen.md).
