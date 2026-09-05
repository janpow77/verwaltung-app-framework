# BSI-orientierte Sicherheitsbaseline

Diese Baseline ist eine technische und organisatorische Startanforderung. Sie
ist **keine Aussage über eine BSI-Zertifizierung**, kein abgeschlossener
IT-Grundschutz-Check und keine Schutzbedarfsfeststellung. Sie beschreibt, was
eine Anwendung auf diesem Framework mitbringen muss, damit die zuständige
Stelle den Grundschutz-Check überhaupt durchführen kann.

Grundlage sind BSI-Standard 200-2 (IT-Grundschutz-Methodik), BSI-Standard
200-3 (Risikoanalyse) und das IT-Grundschutz-Kompendium.

## 1. Geltungsbereich und Abgrenzung

Ein Repositoriums-Template kann nur die anwendungsseitigen Bausteine
abdecken. Alles andere liegt beim Betreiber und ist hier ausdrücklich
**nicht** Gegenstand.

| Ebene | Zuständig | In dieser Baseline |
| --- | --- | --- |
| Anwendung, Datenhaltung, Container-Definition | Projektteam | ja |
| Entwicklungsprozess, Abhängigkeiten, Auslieferungsartefakte | Projektteam | ja |
| Netz, Rechenzentrum, Gebäude, Clients (NET, INF, SYS.2) | Betreiber bzw. zentrale IT | nein, nur zu benennen |
| Identitätsanbieter, PKI, zentrale Protokollierung | Betreiber bzw. zentrale IT | Schnittstelle ja, Betrieb nein |
| ISMS, Notfallkonzept der Behörde, Sensibilisierung | Informationssicherheitsbeauftragte(r) | nein, nur zu verweisen |

Jedes Projekt trägt in seiner Akte ein, welche Zeilen der Tabelle in
Abschnitt 3 offen sind und wer sie verantwortet. Eine offene Zeile ohne
benannte Person gilt als nicht erfüllt.

## 2. Schutzbedarfsfeststellung

Vor der Umsetzung ist der Schutzbedarf je Grundwert festzustellen. Ohne
diesen Schritt lässt sich das Anforderungsniveau in Abschnitt 3 nicht
bestimmen.

| Grundwert | Schutzbedarf | Begründung (Schadensszenario) |
| --- | --- | --- |
| Vertraulichkeit | normal / hoch / sehr hoch | |
| Integrität | normal / hoch / sehr hoch | |
| Verfügbarkeit | normal / hoch / sehr hoch | |

Regeln der Ableitung: Der Schutzbedarf eines Zielobjekts ergibt sich aus dem
höchsten Schutzbedarf der darauf verarbeiteten Daten (**Maximumprinzip**).
Mehrere für sich unkritische Verfahren können zusammen einen höheren Bedarf
ergeben (**Kumulationseffekt**); verteilt sich eine Aufgabe auf mehrere
Systeme, kann der Bedarf des Einzelsystems geringer sein
(**Verteilungseffekt**).

Bei **hohem oder sehr hohem** Schutzbedarf ist zusätzlich eine Risikoanalyse
nach BSI-Standard 200-3 durchzuführen. Deren Ergebnis, alle akzeptierten
Restrisiken und die zeichnende Person gehören in die Projektakte.

Für den Datenschutzteil gilt die eigenständige Bewertung nach
[`docs/dsfa-werkzeug.md`](../dsfa-werkzeug.md); Schutzbedarf und
Schwellwertanalyse ersetzen einander nicht.

## 3. Bausteine, Umsetzung und offene Punkte

Spalte „Anforderung" nennt das Niveau nach IT-Grundschutz (B = Basis,
S = Standard). Spalte „offen" ist bei Abgabe an die Sicherheitsprüfung
auszufüllen — leer bedeutet nicht erfüllt, sondern nicht bearbeitet.

| Baustein | Anf. | Was die Anwendung mitbringen muss | Offen / bei der Behörde |
| --- | --- | --- | --- |
| **APP.3.1** Webanwendungen | B+S | Serverseitige Autorisierung je Aktion, Eingabevalidierung, Ausgabekodierung, Schutz gegen SQL-Injection über ORM oder Parameterbindung, CSRF-Schutz, sichere Sitzungsverwaltung, Ratenbegrenzung an Anmeldung und teuren Endpunkten, Fehlerausgaben ohne interne Details, keine offene API-Dokumentation im Wirkbetrieb | |
| **APP.3.2** Webserver | B | TLS am Proxy, Content-Security-Policy, HSTS, `X-Frame-Options: DENY`, Referrer-Policy, Versionskennung abgeschaltet | Zertifikate und Cipher-Vorgaben der Landes-PKI |
| **APP.4.3** Relationale Datenbanken | B | Eigener Datenbankbenutzer je Anwendung, nur im internen Netz erreichbar, Migrationen mit Review, Append-only-Schutz für Nachweise und Chronologie | |
| **SYS.1.6** Containerisierung | B | Festgelegte Basis-Images, Prozess ohne Root, Ressourcengrenzen, Healthcheck, keine Host-Ports außer dem Proxy | Image-Scanning im Prozess der Behörde |
| **ORP.4** Identitäts- und Berechtigungsmanagement | B+S | OIDC/SSO-Anbindung, Rollenmatrix, serverseitige Rechteprüfung, Mandantentrennung, Vier-Augen-Prinzip identitätsbasiert, Konten deaktivieren statt löschen | Anbindung an den Identitätsanbieter der Behörde |
| **OPS.1.1.2** Ordnungsgemäße IT-Administration | B | Getrennte Administrationskonten, dokumentierte administrative Eingriffe | Betriebskonzept der Behörde |
| **OPS.1.1.3** Patch- und Änderungsmanagement | B | Festgeschriebene Abhängigkeiten mit Lockfile, dokumentierter Aktualisierungsrhythmus, Update mit Sicherung und Migration | Freigabeprozess der Behörde |
| **OPS.1.1.4** Schutz vor Schadprogrammen | B | Prüfung hochgeladener Dateien vor der Verarbeitung, Ablage außerhalb des Webroots, Dateinamensbereinigung, Typ- und Größengrenzen | Schadsoftwareprüfung der Behörde |
| **OPS.1.1.5** Protokollierung | B+S | Audit-Log mit Person, Zeit, Aktion, Objekt sowie Vorher und Nachher; Zugriffsprotokoll; Export- und Freigabeaktionen protokolliert; Protokolle unveränderbar | Weiterleitung an ein zentrales Protokollsystem |
| **OPS.1.1.6** Software-Tests und Freigaben | B | Testnachweis vor der Freigabe, Freigabe durch eine zweite benannte Person, Freigabeentscheidung dokumentiert — entspricht dem Landingprozess in [`docs/processmodell.md`](../processmodell.md) | |
| **CON.1** Kryptokonzept | B | Verfahren und Schlüssellängen nach **BSI TR-02102-1/-2**, keine eigenen Verfahren, Schlüsselwechsel dokumentiert | Schlüsselverwaltung der Behörde |
| **CON.2** Datenschutz | B | VVT, Schwellwertanalyse, DSFA, Löschkonzept, Betroffenenrechte | Freigabe durch die oder den DSB |
| **CON.3** Datensicherung | B | Verschlüsselte Sicherung, dokumentierte und **geprobte** Wiederherstellung, Nachweise append-only | Zweiter Ablageort, Aufbewahrungsregel |
| **CON.6** Löschen und Vernichten | B | Aufbewahrungsfristen je Datenart, automatische Löschung mit Nachweis, ausdrückliche Begründung für Daten ohne Frist | Aktenordnung der Behörde |
| **CON.8** Software-Entwicklung | B+S | Anforderungen, Reviews, Tests, Linter, Typprüfung, Abhängigkeits-, Geheimnis- und statische Sicherheitsprüfung in der CI, ADRs | Externer Penetrationstest |
| **DER.1** Detektion | B | Auswertbare Protokolle, erkennbare Fehlversuche | Zentrale Auswertung |
| **DER.4** Notfallmanagement | B | Wiederherstellung dokumentiert und geprobt, Ansprechpartner benannt | Notfallkonzept der Behörde |
| **ISMS.1**, **ORP.1–ORP.3** | — | Benennung der zuständigen ISB-Rolle im Projekt | Sicherheitsmanagement der Behörde |

## 4. KI-spezifische Anforderungen

Das Framework richtet sich ausdrücklich an KI-gestützt entwickelte und
teilweise KI-gestützt betriebene Anwendungen. Dafür gilt zusätzlich:

- Inhalte aus Uploads, Bürgereingaben, E-Mails und importierten Tabellen sind
  **nicht vertrauenswürdig**. Sie werden als Daten übergeben, nie als
  Anweisung, und nie ungefiltert in einen Prompt eingesetzt.
- Ein Agent erhält nur die Werkzeugrechte, die seine Aufgabe braucht; ein
  schreibender Zugriff auf Nachweise, Freigaben oder Rechte ist ausgeschlossen.
- KI-Aktionen werden wie Nutzeraktionen protokolliert, mit Modell, Zeitpunkt
  und auslösender Person.
- Eine KI darf keine fachliche, datenschutzrechtliche oder betriebliche
  Freigabe auslösen oder simulieren (siehe [`AGENTS.md`](../../AGENTS.md)).
- Handelt es sich um ein Hochrisiko-KI-System, ist zusätzlich die
  Grundrechte-Folgenabschätzung nach Art. 27 VO (EU) 2024/1689 zu prüfen; sie
  darf mit der DSFA verbunden werden (Art. 27 Abs. 4).

## 5. Grundschutz-Check je Anforderung

Für die Abgabe an die Sicherheitsprüfung ist Abschnitt 3 je Zeile mit einem
Umsetzungsstatus zu versehen:

| Status | Bedeutung |
| --- | --- |
| entbehrlich | Anforderung trifft auf das Zielobjekt nicht zu — mit Begründung |
| ja | vollständig umgesetzt, Nachweis benannt |
| teilweise | begonnen, mit Restaufgabe, Verantwortlichem und Termin |
| nein | nicht umgesetzt — erfordert eine gezeichnete Risikoakzeptanz |

Eine Abweichung wird nicht stillschweigend hingenommen. Sie braucht die
betroffene Anforderung, das verbleibende Risiko, die Begründung, die
zeichnende Person und ein Datum der Wiedervorlage. Der Eintrag gehört in die
Projektakte und ist Teil des Freigabepakets.

**Eine grüne CI-Prüfung ersetzt keine dieser Entscheidungen.**
