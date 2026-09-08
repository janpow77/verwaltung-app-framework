# Skill: Datenmapping und analytische Reproduzierbarkeit

Anwendbar bei F-16 und F-17.

Vor der Umsetzung festlegen:

- Quellformate und semantisches Zielmodell,
- Mapping- und Transformationsregeln,
- Pflichtfelder, Schlüssel und Beziehungen,
- Mapping-Versionen und Mapping-Diff,
- Vorschau, Warnungen und blockierende Fehler,
- Import-Fingerprint und Ergebnisversion,
- welche Analyseläufe ein Run Manifest benötigen,
- Tool-/Code-/Daten-/Prompt-/Agent-Versionen,
- Parameter und Random Seeds,
- Input-/Output-Fingerprints,
- Grenzen der Reproduzierbarkeit bei externen KI-Modellen.

Bei Notebook-/Jupyter-Funktionen zusätzlich Workspace-Isolation, Ressourcenlimits, Netzwerkzugriffe, paketierte Laufzeitumgebung, Kernel-/Session-Lifecycle und Secret-Zugriff dokumentieren.

GUI und Notebook dürfen keine getrennten Berechtigungswege zur selben Datenquelle bilden.

Vor Abschluss T-30 bis T-32 aus docs/pruefkatalog.md ausführen und Befunde dokumentieren.
