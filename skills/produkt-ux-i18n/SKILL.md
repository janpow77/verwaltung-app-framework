# Skill: Produkt-UX, Mehrfachansichten und Internationalisierung

Anwendbar bei F-11 und F-12. Bestehende Barrierefreiheitsanforderungen aus F-10 werden durch diesen Skill nicht erweitert oder ersetzt.

Vor der Umsetzung festlegen:

- Designsystem/Design-Tokens,
- relevante View-Typen auf demselben Datenmodell,
- persönliche vs. geteilte Views,
- Bild-/Cover-/Hintergrundfunktionen,
- Empty-/Loading-/Error-/Success-Zustände,
- Light/Dark/System soweit vorgesehen,
- responsive Zielgrößen,
- Performancegrenzen für Listen/Boards/Tabellen,
- Sprachen, Fallback-Locale und locale-abhängige Formate.

Keine parallelen Fachbestände nur für unterschiedliche Ansichten anlegen. Eine View speichert Filter, Sortierung, Gruppierung, sichtbare Felder und Layout getrennt von den Fachdaten.

UI-Texte mehrsprachiger Anwendungen gehören in versionierte Sprachressourcen. Datums-, Zahlen- und Währungsdarstellung folgt der gewählten Locale, ohne den fachlichen Wert zu verändern.

Vor Abschluss T-21 bis T-23 aus docs/pruefkatalog.md ausführen und Befunde dokumentieren.
