# Verwaltungs-App-Framework

Secure-by-Default-Template für kleine, KI-gestützt entwickelte
Verwaltungsanwendungen.

Das Repository ist der gemeinsame Startpunkt für Beschäftigte, Fachreferate,
IT und Entwicklungsagenten. Eine eigene Anwendung wird vom ersten Commit an in
diesem Gerüst entwickelt. Claude, Codex oder ein anderer Agent ergänzt die
Fachlogik; Identität, Mandantentrennung, Rollen, Berechtigungen, Auditierung,
Versionierung, Datenschutz, Tests und Freigaben werden nicht jedes Mal neu
erfunden.

## Zwei Säulen

1. **Datenauswertungen**: optionale Module wie `flowstat` übernehmen
   Datenaufbereitung, Stichprobe, Plausibilität, Statistik, GIS und Exporte.
2. **Fachanwendungen**: Formulare, Vorgänge, Zuständigkeiten, Workflows,
   Dokumente, Fristen und Freigaben werden als fachliches Modul auf dem
   Framework-Kern aufgebaut.

## Prozessmodell

Der Lebenszyklus ist als nachvollziehbarer Verwaltungsprozess aufgebaut: ein
Vorgang mit Akte, Statusmaschine, Übergangsmatrix, Chronologie, Fristen,
Dokumenten, Zweitprüfung und Gesamt-Export. Die generische Statusmaschine liegt in
`framework/core/process.py`; das fachliche Modell ist in
`docs/processmodell.md` und `contracts/process.yaml` beschrieben.

Für Eigenentwicklungen gilt: Das Template wird **vor** der Vorstellung genutzt.
Der Landingprozess prüft ein bereits framework-konform entwickeltes Projekt;
er ersetzt nicht den Framework-Start.

## Datenschutz- und DSFA-Werkzeug

`framework/core/dsfa.py` bildet den aus `regulierung` übernommenen Ablauf ab:

- VVT mit stabiler Tätigkeits-ID und Versionsstand
- Schwellwertanalyse als dokumentierte Systemempfehlung
- DSFA je Verarbeitungstätigkeit mit VVT-Snapshot
- Risikoszenarien und Maßnahmen
- menschliche Entscheidung mit Begründung bei Abweichung
- Beteiligung und Stellungnahme des Datenschutzbeauftragten
- Vier-Augen-Freigabe und unveränderliche freigegebene Fassung
- erneute Prüfung, wenn sich der VVT-Snapshot ändert

Die technische Referenzimplementierung ist bewusst dependency-arm und dient als
Vertrags-/Testkern. Die produktive Webanwendung kann darauf FastAPI,
SQLAlchemy, PostgreSQL, OIDC/Keycloak und eine TypeScript-Oberfläche setzen.

## Schnell prüfen

```bash
python3 -m unittest discover -s tests -v
python3 checks/validate_repo.py
```

## KI-Entwicklung

Vor jeder Änderung lesen Agenten `AGENTS.md`, die passende Skill-Datei und die
relevanten ADRs. Verbindliche Regeln liegen in `AGENTS.md`; `CLAUDE.md` und
`CODEX.md` sind kurze Einstiegspunkte für die jeweiligen Werkzeuge.

## Herkunft der Bausteine

- `audit_designer`: modulare FastAPI-/Datenverarbeitungs- und Agentenstruktur,
  flowstat, Versionierung, Auditierung und Exportmuster
- `flowaudit`: modulare Fachanwendungen, Berichts- und Tabellenexporte,
  Docker-/Health-/Testmuster
- `regulierung`: OIDC/Keycloak, Rollen und Rechte, Mandanten, Audit-/Access-Log,
  VVT/DSFA, DSB-Beteiligung, Vier-Augen-Freigabe und unveränderliche Fassungen

Konkrete Fachdomänen aus den Quell-Repositories werden nicht in den Kern
kopiert.
