# Prüf-Prompt für Claude oder Gemini

Diesen Prompt zusammen mit dem Repository an Claude Code, Gemini Code Assist
oder einen anderen Entwicklungsagenten geben.

```text
Du prüfst das Repository verwaltung-app-framework als unabhängiger Senior
Softwarearchitekt für eine öffentliche Verwaltung. Lies zuerst vollständig:

- AGENTS.md
- README.md
- docs/anforderungen.md
- docs/processmodell.md
- docs/dsfa-werkzeug.md
- docs/akte-und-exporte.md
- docs/rollen-und-rechte.md
- docs/security/bsi-baseline.md
- alle ADRs unter docs/adr/
- alle Skills unter skills/
- den Python-Kern unter framework/ und die Tests unter tests/

Wenn die Schwester-Repositories lokal vorhanden sind, vergleiche zusätzlich:

- /home/janpow/Projekte/audit_designer
- /home/janpow/Projekte/flowaudit
- /home/janpow/Projekte/regulierung

## Zielbild

Das Repository soll als Secure-by-Default-Template für zwei Säulen dienen:

1. wiederkehrende Datenauswertungen, perspektivisch mit flowstat;
2. kleine interne Fachanwendungen, die Beschäftigte mit Claude, Codex oder
   Gemini ab dem ersten Commit entwickeln können.

Es soll Innovation aus den Fachreferaten ermöglichen, aber Schatten-IT in einen
transparenten Landing- und Betriebsprozess überführen. Das Framework muss
Mandanten, Nutzer, Adminrollen, fein granulierte Rechte, OIDC/SSO,
Statusmaschinen, Akten, Fristen, Dokumente, Audit-Logging, Versionierung,
Vier-Augen-Freigaben und Exporte vorsehen.

Der Datenschutzbaustein muss das Muster aus regulierung abbilden:

- Verzeichnis von Verarbeitungstätigkeiten je Mandant;
- stabile Tätigkeits-ID und VVT-Version;
- DSFA je Verarbeitungstätigkeit mit VVT-Snapshot;
- erklärbare Schwellwertanalyse;
- Risikoszenarien und Maßnahmen;
- menschliche Entscheidung;
- Begründungspflicht bei Abweichung von der Systemempfehlung;
- Beteiligung und Votum des Datenschutzbeauftragten;
- Vier-Augen-Freigabe und Sperre der freigegebenen Fassung;
- Neubewertung bei Änderung des VVT oder der Verarbeitung.

Das Prozessmodell soll wie beim KPAnG nicht nur eine Liste sein, sondern eine
erzwungene Status- und Übergangsmatrix mit Vorgangsakte, Chronologie, Fristen,
Dokumenten, Rückgabe/Korrektur, Freigabe, Betrieb und Neubewertung. Es muss zwei
Einstiege zulassen:

- Hausbedarf: Bedarf → Bottom-up-Workshop → Framework → Entwicklung;
- Eigeninitiative: Framework → Entwicklung → Vorstellung/Landing.

## Prüfe besonders

1. Ist die Trennung zwischen Plattformkern und Fachmodul sauber?
2. Sind Mandantentrennung und Berechtigungen serverseitig erzwingbar?
3. Kann ein Entwickler die eigene Arbeit oder DSFA selbst freigeben?
4. Werden VVT-Snapshots, Versionen und Neubewertungen korrekt behandelt?
5. Sind Prozessübergänge, Abbruch und Rückgabe vollständig und testbar?
6. Sind Exporte beweis- bzw. nachweisgeeignet beschrieben?
7. Ist die BSI-orientierte Baseline konkret genug, ohne fälschlich eine
   Zertifizierung zu behaupten?
8. Sind AGENTS.md, CLAUDE.md, CODEX.md und Skills für verschiedene Agenten
   konsistent und ausreichend verbindlich?
9. Welche Best-of-Bausteine aus den drei Schwester-Repositories fehlen noch?
10. Welche Teile sind nur Dokumentation und welche bereits ausführbar?
11. Welche Risiken entstehen durch KI-generierten Code, Abhängigkeiten,
    Geheimnisse, Uploads, Exporte und Prompt-Injection?
12. Welche Minimalversion kann mit vertretbarem Aufwand produktionsnah werden?

## Arbeitsweise

- Führe die vorhandenen Tests und `python3 checks/validate_repo.py` aus.
- Lies den Code, nicht nur die README.
- Verändere keine Dateien ohne ausdrückliche Bitte.
- Erfinde keine angebliche Zertifizierung oder rechtliche Freigabe.
- Kennzeichne jede Aussage als „belegt“, „Risiko“ oder „Empfehlung“.

## Ergebnisformat

Liefere einen Bericht mit genau diesen Abschnitten:

1. Kurzurteil mit Reifegrad 0–5
2. Was bereits funktioniert
3. Kritische Lücken vor produktiver Nutzung
4. Best-of-Abgleich je Schwester-Repository
5. DSFA/VVT-Prüfung
6. KPAnG-artige Prozessprüfung
7. Rollen-, Mandanten- und Exportprüfung
8. BSI-/Secure-by-Design-Prüfung
9. Claude-/Codex-/Gemini-Tauglichkeit
10. priorisierte nächste zehn Maßnahmen
11. konkrete Testfälle, die noch fehlen

Schließe mit einer klaren Entscheidung:

- „als Template für Entwicklung geeignet“,
- „nur als Konzept geeignet“ oder
- „für produktionsnahe Nutzung bereit“.
``` 

