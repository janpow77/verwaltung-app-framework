# Unabhängiger Prüfauftrag

Prüfe das Projekt anhand AGENTS.md, docs/anforderungen.md und der ausgefüllten Projektunterlagen. Ändere keine Dateien.

- Verfolge jede anwendbare Anforderung von der Spezifikation zur Umsetzung und zum Prüfnachweis.
- Unterscheide fehlende Spezifikation, fehlende Umsetzung und fehlenden Nachweis.
- Prüfe unberechtigten Zugriff, fremde Mandanten, unzulässige Statuswechsel, Selbstfreigabe und unvollständige Exporte.
- Prüfe Datenschutzunterlagen, dokumentierte Entscheidungen und offene Betriebsfragen.
- Bei F-11/F-12: prüfe gemeinsame Datenbasis der Views, UI-Zustände, Sprachressourcen und locale-abhängige Darstellung.
- Bei F-13/F-14: prüfe Capability-Ausblendung gegen direkte API-Aufrufe sowie persönliche Provider/Secrets gegen fremden Zugriff und Leakage in Client/Logs.
- Bei F-15: prüfe Metadatensuche/Facetten, unveränderliche Versionen, Labels, Fork-Herkunft, Commit-Messages, Prompt- und Agent-Diffs sowie Eval-Zuordnung. Ein Prompt-Diff muss mindestens Text, Variablen, Modellkonfiguration, Tools/Berechtigungen und Tests erfassen.
- Bei F-16/F-17: prüfe Mapping-Versionen, Importnachweise, Run-Manifeste, Seeds/Fingerprints und Workspace-Isolation.
- Bei F-18: prüfe technische Wirksamkeit von Redaction, Trennung von Pseudonym-Zuordnungen und den vorgesehenen Human-Review.
- Belege Befunde durch Datei und Stelle; benenne nicht ausgeführte Prüfungen.
- Liefere priorisierte Befunde und die nächsten konkreten Schritte. Stelle keine menschliche Freigabe aus.
