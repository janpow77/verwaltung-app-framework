# Arbeitsregeln für KI-Agenten

Diese Datei ist für alle Entwicklungsagenten verbindlich. `CLAUDE.md` und
`CODEX.md` verweisen auf sie und dürfen keine abweichenden Regeln enthalten.

## Vor dem Arbeiten

1. Lies diese Datei, `docs/anforderungen.md`, die passende Skill-Datei und alle
   betroffenen ADRs.
2. Ordne die Änderung ein: Plattformkern, Fachmodul, Datenschutz, Sicherheit,
   Export oder Betrieb.
3. Prüfe, ob die Änderung tenantbezogene Daten, Rollen, Freigaben oder
   Nachweise berührt.

## Verbindliche Regeln

- Plattformkern und Fachmodul sind getrennt. Fachlogik darf keine
  Mandantentrennung, serverseitige Rechteprüfung, Auditierung oder Freigabe
  umgehen.
- Das Vier-Augen-Prinzip ist für verbindliche Freigaben technisch zu erzwingen;
  Selbstfreigabe ist nicht zulässig.
- Jede neue Fachfunktion beschreibt Datenmodell, Nutzergruppen, Rollenmatrix,
  Statusübergänge, Exportbedarf und VVT-/DSFA-Bezug.
- Eine Berechtigung wird immer serverseitig geprüft. UI-Ausblenden ist keine
  Zugriffskontrolle.
- Freigegebene Fassungen und Chronologie werden nicht überschrieben oder
  gelöscht. Korrekturen erzeugen eine neue Version.
- Ersteller und Freigeber müssen bei verbindlichen Ergebnissen verschieden sein.
- KI darf Vorschläge erzeugen, aber keine menschliche Fach-, Datenschutz- oder
  Betriebsfreigabe simulieren.
- Secrets, echte Personen- oder Falldaten und Produktionskonfigurationen
  gehören nicht in Git, Tests oder Logs.
- Migrationen, Exporte und Statusübergänge werden mit Tests abgesichert.
- Nach jeder Änderung: `python -m unittest discover -s tests -v`,
  `python checks/validate_repo.py` und gegebenenfalls Frontend-/Container-Checks.

## Nicht erlaubt

- direkter produktiver Datenzugriff aus Entwicklungs- oder Demo-Code
- globale Admin-Umgehungen und pauschale `is_admin`-Abkürzungen in Fachmodulen
- physisches Löschen von Nachweisen ohne dokumentierte Aufbewahrungs- und
  Löschregel
- automatische Freigabe, wenn ein menschlicher Entscheidungs- oder
  Datenschutzschritt gefordert ist
- Kopieren einer kompletten Fachdomäne aus `audit_designer`, `flowaudit` oder
  `regulierung` in den Frameworkkern
