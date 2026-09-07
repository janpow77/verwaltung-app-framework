# Kollaborative Artefakte: Versionen, Forks, Reviews und Diffs

Dieses Dokument konkretisiert F-15. Es gilt für fachlich teilbare Artefakte wie Prompts, Agenten, Checklisten, Regelwerke, Strategien, Notebook-Templates oder vergleichbare Konfigurationen.

## Grundsatz

Ein gemeinsam genutztes Artefakt ist kein überschreibbarer Textblock. Jede fachlich relevante Änderung erzeugt eine neue Version oder einen nachvollziehbaren Entwurf. Freigegebene bzw. veröffentlichte Versionen bleiben unverändert.

Mindestens zu speichern sind:

- stabile Artefakt-ID,
- Typ und Titel,
- Eigentümer/Autor und Organisation,
- Version,
- Status,
- Erstellungs- und Änderungszeit,
- Vorgängerversion,
- Herkunft/Fork-Bezug,
- Änderungsbegründung,
- Inhaltshash,
- Reviewer/Freigabe, soweit vorgesehen.

## Prompt-Versionierung

Prompts erhalten eine eigenständige Versionierung. Eine Prompt-Version umfasst mindestens:

- System Prompt, falls vorhanden,
- User-/Task-Prompt bzw. Template,
- Variablen und deren Typen/Pflichtstatus,
- erwartetes Ausgabeformat,
- Tool-/Datenquellenbezug,
- empfohlene Modellparameter,
- unterstützte Sprache(n),
- Testfälle und erwartete Eigenschaften,
- Status und Herkunft.

Ein gespeicherter KI-Lauf verweist auf die **exakte Prompt-Version und deren Hash**, nicht nur auf den Prompt-Namen.

## Prompt-Diff als Pflichtfunktion

Zwischen zwei Prompt-Versionen muss ein fachlich lesbarer Diff erzeugt und angezeigt werden können. Mindestens erforderlich sind:

1. **Text-Diff** für System- und User-Prompt mit Hinzufügungen, Löschungen und Änderungen,
2. **Metadaten-Diff** für Modellparameter, Sprache, Status und Beschreibung,
3. **Variablen-Diff** für hinzugefügte, entfernte oder geänderte Eingabevariablen,
4. **Tool-/Berechtigungs-Diff** bei Agenten oder toolfähigen Prompts,
5. **Test-Diff** für hinzugefügte, entfernte oder geänderte Testfälle.

Die Anwendung soll mindestens eine Side-by-Side- oder Unified-Diff-Ansicht anbieten. Bei langen Prompts müssen unveränderte Bereiche einklappbar sein.

Der Diff ist aus den gespeicherten Versionen reproduzierbar zu erzeugen; er wird nicht als alleinige Wahrheit separat gepflegt. Geheimnisse, Tokens oder unzulässige personenbezogene Inhalte dürfen in Diffs nicht offengelegt werden.

## Änderungen mit Wirkung

Ändert eine Prompt-Version Tool-Rechte, Datenquellen, Ausgabeformat oder sicherheitsrelevante Instruktionen, ist dies im Diff besonders zu kennzeichnen. Eine solche Änderung kann einen erneuten Review auslösen.

Für veröffentlichte Prompts gilt:

- keine In-place-Änderung,
- neue Version bei fachlicher Änderung,
- vorherige Version bleibt abrufbar,
- Rollback bedeutet Auswahl einer älteren Version bzw. Erzeugung einer neuen Folgeversion, kein Umschreiben der Historie.

## Agenten

Ein Agent wird ebenfalls versioniert. Eine Version umfasst mindestens:

- Zweck,
- System Prompt und zusätzliche Prompt-Bausteine,
- Eingabe-/Ausgabevertrag,
- Tools und Tool-Rechte,
- Datenquellen,
- Provider-/Modellanforderungen,
- Guardrails,
- Testfälle,
- Status.

Der Agent-Diff zeigt zusätzlich Änderungen an Tool-Rechten und Datenquellen prominent an.

## Fork und Merge

Ein Artefakt kann, soweit fachlich vorgesehen, geforkt werden. Der Fork speichert:

- Parent-Artefakt,
- Parent-Version,
- Zeitpunkt,
- Ersteller/Organisation.

Eine Rückführung in den Hauptzweig erfolgt als Contribution/Merge-Vorschlag. Vor einem Merge ist der Diff zwischen Zielversion und Contribution sichtbar. Konflikte werden ausdrücklich entschieden; ein automatisches Überschreiben ist unzulässig.

## Statusmodell

Empfohlen:

- Draft,
- Experimental,
- In Review,
- Reviewed,
- Released/Recommended,
- Deprecated,
- Archived.

Welche Status eine formelle Freigabe darstellen, legt das Projekt fest. Wo eine verbindliche Freigabe vorgesehen ist, gelten F-06 und das Vier-Augen-Prinzip.

## Prüfnachweise

Mindestens zu testen sind:

- frühere Version bleibt nach Änderung unverändert abrufbar,
- Prompt-Lauf verweist auf die tatsächlich genutzte Version,
- Diff zeigt Text-, Variablen- und Metadatenänderungen korrekt,
- Fork kennt seine Herkunft,
- Merge kann ohne Review keine als geschützt definierte Release-Version überschreiben,
- Tool-Rechteänderungen eines Agenten sind im Diff sichtbar,
- Secrets erscheinen weder in Versionstext noch Diff oder Audit-Log.
