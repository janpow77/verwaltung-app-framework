# Start mit dem Inhalts-Framework

Stand: 2026-09-08. Zielgruppe sind Beschäftigte, die eine eigene Fachanwendung mit KI entwickeln möchten, sowie die später prüfenden Stellen.

Das [Quellenregister](standards.md) gehört von Beginn an zur Planung.
[Standardsnachweis](../vorlagen/standardsnachweis.md) und
[Entscheidungsregister](../vorlagen/entscheidungen.md) im eigenen Projekt
führen. Barrierefreiheits-, Vorfall- und SBOM-Unterlagen nach Anwendbarkeit
bearbeiten; eine bloß kopierte Vorlage ist kein erfüllter Nachweis.

1. Lies README.md, AGENTS.md und docs/anforderungen.md.
2. Lege ein eigenes Projekt-Repository an. Übernimm README.md, INHALTSVERSION, AGENTS.md, CLAUDE.md, CODEX.md, GEMINI.md sowie docs/, contracts/, skills/, prompts/, vorlagen/ und beispiele/ in gleicher relativer Struktur. Passe die Projekt-README an und fülle die Vorlagen im Projekt aus. Archiv und Python-Referenzkern werden nicht benötigt. Dokumentiere die verwendete Framework-Version bzw. den Commit.
3. Fülle den Projektsteckbrief aus. Nutze beispiele/raumbuchung/README.md als Orientierung und fülle vorlagen/anwendbarkeit.md mit aus. Prüfe ausdrücklich die Auslöser F-11 bis F-18.
4. Beschreibe Rollen, Daten und Prozess vor dem ersten Implementierungsauftrag. Markiere ungeklärte Punkte ausdrücklich.
5. Bei kollaborativen/visuellen Anwendungen lies `docs/produkt-ux-und-i18n.md` und `docs/capabilities-und-ansichten.md`.
6. Bei Prompts/Agenten/mehreren KI-Providern lies `docs/ki-provider-und-secrets.md`, `docs/kollaborative-artefakte.md` und `docs/prompt-und-agent-registry.md`. Lege Metadaten, Suche, Versionen, Labels, Diffs und Evals vor der Implementierung fest.
7. Bei Datenimport/Analyse/Notebook-Nutzung lies `docs/datenimport-und-mapping.md` und `docs/reproduzierbarkeit-und-workspaces.md`.
8. Bei Redaction/Pseudonymisierung/Synthetic Twin lies `docs/redaction-pseudonymisierung.md`.
9. Verwende prompts/entwicklung.md für kleine, überprüfbare KI-Aufträge. Entwickle gegen synthetische Testdaten.
10. Halte je Anforderung fest, wie sie umgesetzt und geprüft wurde. Verwende prompts/review.md für eine unabhängige Prüfung.
11. Stelle das Projekt mit vorlagen/landing.md vor. Erst eine dokumentierte Betriebsentscheidung erlaubt die Übernahme in den vorgesehenen dienstlichen Betrieb.

Hausbedarf: Bedarf → gemeinsamer Workshop → Vorgaben übernehmen → Entwicklung → Prüfung.
Eigeninitiative, auch privat begonnen: Vorgaben übernehmen → Entwicklung → Vorstellung → Prüfung.
Ein früher Austausch bleibt möglich; das Framework soll vor der Vorstellung bekannt sein.

Das Repository liefert zunächst Inhalte. Frühere Softwareentwürfe liegen in archiv/softwareentwuerfe/ und werden nicht als Projektvorlage übernommen.

Den vollständigen Arbeitsablauf beschreibt docs/ki-arbeitsablauf.md. Vor Nachnutzung außerhalb des eigenen Berechtigtenkreises docs/pflege-und-nachnutzung.md beachten.
