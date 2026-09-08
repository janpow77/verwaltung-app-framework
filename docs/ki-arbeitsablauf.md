# Mit KI vom Bedarf zu prüfbaren Projektunterlagen

Gemeinsame Grundlage für Claude, Codex und Gemini: AGENTS.md. Die Agenteneinstiege verweisen darauf; der Auftrag benennt zusätzlich explizit die zu lesenden Dateien und Skills. Automatisches Laden ist nicht vorausgesetzt.

| Schritt | Eingaben | Ergebnis | Passender Skill | Übergangskriterium |
|---|---|---|---|---|
| 1 Spezifizieren | Projektidee, Framework-Stand | Projektsteckbrief, Anwendbarkeit, Rollen und Prozess | skills/fachanwendung/SKILL.md | Fachlicher Umfang verständlich; offene Fragen benannt |
| 2 Produkt-UX / Internationalisierung | Zielgruppen, Arbeitsweisen, Sprachen | Design-/View-/Locale-Entscheidungen | skills/produkt-ux-i18n/SKILL.md | F-11/F-12 bewertet; Views und Sprachkonzept festgelegt, soweit anwendbar |
| 3 Architektur | Spezifikation, Datenfluss | Komponenten, Schnittstellen, Architekturentscheidungen | skills/secure-coding/SKILL.md | Rechte, Datenraum und Freigaben keinem Zufall überlassen |
| 4 Datenschutz und Rechte | Datenmodell, Rollenmatrix | Datenschutzentwurf und administrative Regeln | skills/datenschutz-vvt-dsfa/SKILL.md; skills/rollen-und-rechte/SKILL.md | Zuständige Prüfung und abhängige Entscheidungen sichtbar |
| 5 KI-/Artefakt-Registry | Prompts, Agenten, Provider, Kollaboration | Metadatenschema, Versionen, Diffs, Evals, Provider-/Secret-Modell | skills/prompt-agent-registry/SKILL.md | F-14/F-15 bewertet; exakte Versionierung und Such-/Reviewmodell festgelegt |
| 6 Datenintegration / Analyse | Quellen, Mapping, Analyseanforderung | Importprofile, Run-Manifest, Workspace-Regeln | skills/daten-mapping-reproduzierbarkeit/SKILL.md | F-16/F-17 bewertet; Reproduzierbarkeit und Workspace-Grenzen definiert |
| 7 Testdatenableitung | reale Fälle/Testbedarf | Redaction-/Pseudonym-/Synthetic-Twin-Konzept | skills/redaction-testdaten/SKILL.md | F-18 bewertet; Betriebsart, Review und Ground-Truth-Trennung definiert |
| 8 Umsetzen | Abgegrenzte Anforderungs-IDs, Akzeptanzfälle | Kleiner nachvollziehbarer Änderungssatz | skills/secure-coding/SKILL.md plus anwendbarer Fachskill | Vereinbarte Funktion mit synthetischen Daten prüfbar |
| 9 Unabhängig prüfen | Umsetzung, Prüfkatalog | Befunde mit Belegen und Grenzen | skills/tests-und-export/SKILL.md | Fehler und nicht geprüfte Bereiche transparent |
| 10 Dokumentieren und vorstellen | Spezifikation, Ergebnisse, Betriebsskizze | Landing-Paket und offene Entscheidungsliste | skills/release-und-landing/SKILL.md | Vorstellung möglich; Betriebsfreigabe bleibt menschlich |

Nicht jeder Schritt ist in jedem Projekt inhaltlich groß. Die Anwendbarkeitsmatrix entscheidet, ob F-11 bis F-18 nur begründet ausgeschlossen oder vollständig spezifiziert und umgesetzt werden müssen.

Für jeden Auftrag: Ziel, Anforderungs-IDs, erlaubter Änderungsbereich, zu lesende Unterlagen, Prüffälle und gewünschtes Ergebnisformat nennen. prompts/entwicklung.md und prompts/review.md sind wiederverwendbare Einstiege.

Bei Standards- und Nachweisprüfung zusätzlich
[standards-pruefung](../skills/standards-pruefung/SKILL.md) explizit laden.
Das [Quellenregister](standards.md) verbindet die F-IDs mit Prüffällen;
[Standardsnachweis](../vorlagen/standardsnachweis.md) und
[Entscheidungsregister](../vorlagen/entscheidungen.md) halten tatsächliche
Ergebnisse und offene menschliche Entscheidungen getrennt fest.

## Ungeklärte Fragen

KI dokumentiert die Frage, Alternativen und betroffene Folgearbeiten im Entscheidungsregister. Sie darf technische, reversible Details begründet wählen; fachliche Befugnisse, Datenschutzentscheidungen und Betriebszusagen nicht erfinden. Unabhängige Arbeit kann weitergehen. Keine Umsetzung auf Basis einer ungeklärten kritischen Berechtigung.

## Änderungen und Abweichungen

Vor Änderung an Rollen, Datenraum, Freigaben, Verarbeitung, Provider-/Secret-Modell, veröffentlichten Artefakten oder Mapping-/Run-Verträgen betroffene Spezifikation und Prüffälle aktualisieren. Abweichungen nach docs/verbindlichkeit.md dokumentieren. Ein anderer Agent kann den Review unterstützen; er ersetzt keine zuständige menschliche Entscheidung.

## Übergabe zwischen Agenten

Aktuellen Inhaltsstand, bearbeitete Anforderungen, geänderte Dateien, verwendete Prompt-/Agent-Versionen soweit relevant, Prüfergebnisse, offene Fragen und nächste Aufgabe zusammenfassen. Gesprächsverlauf allein ist keine Projektdokumentation.
