# Arbeitsregeln für KI-Agenten

Diese Datei ist für alle Entwicklungsagenten verbindlich. `CLAUDE.md` und
`CODEX.md` verweisen auf sie und dürfen keine abweichenden Regeln enthalten.

## Aktueller Umfang

Maßgeblich ist docs/adr/ADR-004-inhalts-framework.md. In dieser Phase werden Inhalte gepflegt: Anforderungen, Arbeitsaufträge, Skills und Projektvorlagen. Bestehende Softwareentwürfe sind nicht als fertige Dienste darzustellen. Für neue Projekte zuerst docs/start.md und vorlagen/ lesen.

Die Einstufung in docs/verbindlichkeit.md legt den Projektumfang fest. Lies außerdem docs/ki-arbeitsablauf.md. Archivdateien sind historische Entwürfe und werden nicht automatisch übernommen. framework/ enthält optionale Referenzlogik.

## Vor dem Arbeiten

1. Lies diese Datei, `docs/anforderungen.md`, die passende Skill-Datei und alle
   betroffenen ADRs.
2. Ordne die Änderung ein: Plattformkern, Fachmodul, Datenschutz, Sicherheit,
   Export, Produkt-UX, Registry/KI-Artefakte, Datenimport/Analyse oder Betrieb.
3. Prüfe, ob die Änderung tenantbezogene Daten, Rollen, Freigaben, Secrets,
   versionierte Artefakte, Mappingprofile oder Nachweise berührt.
4. Bei Standards- oder Nachweisarbeit lies `docs/standards.md` und
   `skills/standards-pruefung/SKILL.md`. Ordne Aussagen einer Quellenfassung,
   Anforderung und einem tatsächlichen Beleg zu. Fehlende Belege bleiben offen.

## Verbindliche Regeln

- Plattformkern und Fachmodul sind getrennt. Fachlogik darf keine
  Mandantentrennung, serverseitige Rechteprüfung, Auditierung oder Freigabe
  umgehen.
- Welche Vorgänge verbindlich freigegeben werden, wird im Projekt festgelegt. Für diese Freigaben ist das Vier-Augen-Prinzip technisch zu erzwingen;
  Selbstfreigabe ist nicht zulässig.
- Jede neue Fachfunktion beschreibt Datenmodell, Nutzergruppen, Rollenmatrix,
  Statusübergänge, Exportbedarf und VVT-/DSFA-Bezug.
- Eine Berechtigung wird immer serverseitig geprüft. UI-Ausblenden oder das
  Deaktivieren einer Capability ist keine Zugriffskontrolle.
- Freigegebene Fassungen und Chronologie werden nicht überschrieben oder
  gelöscht. Korrekturen erzeugen eine neue Version.
- Ersteller und Freigeber müssen bei verbindlichen Ergebnissen verschieden sein.
- KI darf Vorschläge erzeugen, aber keine menschliche Fach-, Datenschutz- oder
  Betriebsfreigabe simulieren.
- Secrets, echte Personen- oder Falldaten und Produktionskonfigurationen
  gehören nicht in Git, Tests oder Logs.
- Persönliche KI-Secrets gehören nicht in Browser-Local-Storage, Notebook,
  Prompt, Agentenmanifest oder Projektdatei; sie werden über die vorgesehene
  serverseitige Secret-/Gateway-Schnittstelle genutzt.
- Versionierte Prompts, Agenten, Checklisten, Strategien und vergleichbare
  Artefakte werden nach Veröffentlichung nicht in-place überschrieben.
- Prompt-Versionen benötigen eine Änderungsbegründung und einen reproduzierbaren
  Diff; Runs referenzieren die tatsächlich verwendete Prompt-Version und deren
  Hash. Tool-/Berechtigungsänderungen eines Agenten müssen im Versionsvergleich
  sichtbar sein.
- Registry-Metadaten, Suche und Facetten beachten Sichtbarkeits- und
  Mandantengrenzen bereits bei Indexierung und Abfrage.
- Import- und Mappingprofile werden versioniert; historische Importe bleiben
  ihrer damaligen Mapping-Version zugeordnet.
- Analytische Läufe dokumentieren die für ihre Reproduzierbarkeit erforderlichen
  Versionen, Parameter, Seeds und Fingerprints. Jupyter/Notebook ist kein
  alternativer direkter Datenbankzugang.
- Redaction, Pseudonymisierung, Anonymisierung und Synthetic Twin werden nicht
  gleichgesetzt. Vor definierter Weitergabe bereinigter realer Fälle bleibt der
  vorgesehene menschliche Review erforderlich.
- Migrationen, Exporte, Statusübergänge und die für das Projekt anwendbaren
  F-11-bis-F-18-Funktionen werden mit den zugeordneten Prüffällen abgesichert.
- In diesem Framework-Repository nach Änderungen: `python -m unittest discover -s tests -v` und `python checks/validate_repo.py`. In abgeleiteten Projekten die vereinbarten Prüfungen aus dem projektspezifischen Testplan ausführen; fehlende Framework-Skripte nicht als vorhanden voraussetzen.

## Nicht erlaubt

- direkter produktiver Datenzugriff aus Entwicklungs- oder Demo-Code
- globale Admin-Umgehungen und pauschale `is_admin`-Abkürzungen in Fachmodulen
- physisches Löschen von Nachweisen ohne dokumentierte Aufbewahrungs- und
  Löschregel
- automatische Freigabe, wenn ein menschlicher Entscheidungs- oder
  Datenschutzschritt gefordert ist
- Kopieren einer kompletten Fachdomäne aus `audit_designer`, `flowaudit` oder
  `regulierung` in den Frameworkkern
- Übernahme fremden Open-Source-Codes nur aufgrund einer funktionalen Ähnlichkeit;
  Konzepte dürfen als Inspiration dienen, Code nur nach dokumentierter Lizenz- und
  Herkunftsprüfung
