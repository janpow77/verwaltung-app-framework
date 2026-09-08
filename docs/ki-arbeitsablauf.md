# Mit KI vom Bedarf zu prüfbaren Projektunterlagen

Gemeinsame Grundlage für Claude, Codex und Gemini: AGENTS.md. Die Agenteneinstiege verweisen darauf; der Auftrag benennt zusätzlich explizit die zu lesenden Dateien und Skills. Automatisches Laden ist nicht vorausgesetzt.

| Schritt | Eingaben | Ergebnis | Passender Skill | Übergangskriterium |
|---|---|---|---|---|
| 1 Spezifizieren | Projektidee, Framework-Stand | Projektsteckbrief, Anwendbarkeit, Rollen und Prozess | skills/fachanwendung/SKILL.md | Fachlicher Umfang verständlich; offene Fragen benannt |
| 2 Architektur | Spezifikation, Datenfluss | Komponenten, Schnittstellen, Architekturentscheidungen | skills/secure-coding/SKILL.md | Rechte, Datenraum und Freigaben keinem Zufall überlassen |
| 3 Datenschutz und Rechte | Datenmodell, Rollenmatrix | Datenschutzentwurf und administrative Regeln | skills/datenschutz-vvt-dsfa/SKILL.md; skills/rollen-und-rechte/SKILL.md | Zuständige Prüfung und abhängige Entscheidungen sichtbar |
| 4 Umsetzen | Abgegrenzte Anforderungs-IDs, Akzeptanzfälle | Kleiner nachvollziehbarer Änderungssatz | skills/secure-coding/SKILL.md | Vereinbarte Funktion mit synthetischen Daten prüfbar |
| 5 Unabhängig prüfen | Umsetzung, Prüfkatalog | Befunde mit Belegen und Grenzen | skills/tests-und-export/SKILL.md | Fehler und nicht geprüfte Bereiche transparent |
| 6 Dokumentieren und vorstellen | Spezifikation, Ergebnisse, Betriebsskizze | Landing-Paket und offene Entscheidungsliste | skills/release-und-landing/SKILL.md | Vorstellung möglich; Betriebsfreigabe bleibt menschlich |

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

Vor Änderung an Rollen, Datenraum, Freigaben oder Verarbeitung betroffene Spezifikation und Prüffälle aktualisieren. Abweichungen nach docs/verbindlichkeit.md dokumentieren. Ein anderer Agent kann den Review unterstützen; er ersetzt keine zuständige menschliche Entscheidung.

## Übergabe zwischen Agenten

Aktuellen Inhaltsstand, bearbeitete Anforderungen, geänderte Dateien, Prüfergebnisse, offene Fragen und nächste Aufgabe zusammenfassen. Gesprächsverlauf allein ist keine Projektdokumentation.
