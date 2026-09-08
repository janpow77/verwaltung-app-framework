# Skill: Prompt- und Agent-Registry spezifizieren und prüfen

Anwendbar bei F-15 und regelmäßig zusammen mit F-14/F-17.

Vor der Umsetzung festlegen:

- Artefakttypen und stabile IDs,
- Metadatenschema, Kategorien, Tags, Keywords und Labels,
- Such-/Facettenfelder und Sichtbarkeit,
- Versionsschema und Commit-Message,
- Draft/Review/Release/Deprecated-Status,
- Fork-/Contribution-/Merge-Modell,
- Prompt-Diff für Text, Metadaten, Variablen, Modellkonfiguration, Tools und Tests,
- Agent-Diff für Instructions, Modell, Tools/Rechte, Skills, Knowledge, Guardrails und Tests,
- Testsets/Evals und Mindestkriterien für Qualitätslabels,
- Beziehungen zu Projekten, Topics, Checklisten und Datensätzen.

Bei Prompts muss jeder Lauf auf exakte Version + Hash zeigen. Bewegliche Labels wie `latest` oder `recommended` zeigen auf Versionen und dürfen Versionen nicht verändern.

Bei Agenten ein Agent-Card-artiges Manifest vorsehen: Name, Beschreibung, Version, Skills mit Tags/Beispielen, Capabilities, Input-/Output-Modi, Security-/Datenanforderungen sowie optionale Schnittstellen.

Keine Registry ohne Suche: mindestens Name, Beschreibung, Kategorie, Tags/Keywords, Sprache, Owner/Institution, Status und Version/Label prüfen. Facetten dürfen keine fremden Mandanteninhalte verraten.

Vor Abschluss T-26 bis T-29 aus docs/pruefkatalog.md ausführen und Befunde dokumentieren.
