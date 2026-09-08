# Analytische Reproduzierbarkeit und interaktive Workspaces

Dieses Dokument konkretisiert F-17.

## Grundsatz

Anwendungen mit Datenanalyse, Stichproben, Simulationen, ML/KI-Auswertungen oder interaktiven Notebook-Umgebungen müssen Ergebnisse so dokumentieren, dass ein fachkundiger Dritter den Lauf und seine Eingaben nachvollziehen kann.

## Run Manifest

Für relevante Läufe werden mindestens soweit fachlich erforderlich gespeichert:

- Tool/Funktion und Version,
- Code-/Release-Referenz,
- Eingabe-Fingerprint,
- verwendete Mapping-/Datenversion,
- Parameter,
- Random Seed,
- Modell/Provider und Modell-Identifier,
- Prompt-/Agent-Version und Hash,
- Laufzeitumgebung bzw. Environment-Version,
- auslösende Person oder technischer Auftrag,
- Start-/Endzeit,
- Ergebnis-Fingerprint,
- Status und Warnungen.

Nicht relevante Felder dürfen entfallen; das Projekt begründet dies. Secrets und unnötige Inhaltsdaten gehören nicht in das Manifest.

## Deterministische Wiederholung

Wo eine Methode deterministisch sein kann, müssen identische Eingaben, Versionen und Parameter ein reproduzierbares Ergebnis liefern. Bei zufallsbehafteten Verfahren ist ein Seed oder ein gleichwertiger Mechanismus zu speichern, sofern die Methode dies zulässt.

Bei nicht vollständig reproduzierbaren externen KI-Modellen muss die Grenze sichtbar dokumentiert werden. Gespeicherte Provider-/Modell- und Prompt-Versionen ersetzen keine Garantie, dass ein externer Dienst später identisch antwortet.

## Interaktive Workspaces / Notebooks

Wenn Jupyter, Code-Notebooks oder vergleichbare interaktive Ausführungsumgebungen angeboten werden, sind mindestens zu regeln:

- persönliche und projektbezogene Workspace-Isolation,
- serverseitige Rechte auf Dateien und Datenquellen,
- Kernel-/Session-Lifecycle,
- Ressourcenlimits für CPU, RAM, Laufzeit und Speicher,
- erlaubte Netzwerkzugriffe,
- paketierte bzw. versionierte Laufzeitumgebungen,
- Umgang mit temporären Dateien und Outputs,
- Beendigung verwaister Sessions,
- Übergang zwischen GUI-Ergebnis und Notebook ohne Berechtigungsumgehung.

Ein Notebook darf keine Secrets im Klartext persistieren. Providerzugänge werden über die nach F-14 vorgesehenen Schnittstellen bereitgestellt.

## GUI und Notebook

Bietet eine Anwendung sowohl GUI- als auch Notebook-Zugriff, sollen beide auf denselben fachlichen Daten- und Berechtigungsdiensten aufsetzen. Ein Notebook ist kein alternativer Direktzugang zur Datenbank.

## Versionierung von Analyseartefakten

Wiederverwendbare Notebook-Templates, Analysekonfigurationen, Strategien oder Modelle erhalten Versionen. Läufe verweisen auf die tatsächlich verwendete Version.

Bei fachlich relevanten Änderungen soll ein Diff bzw. ein strukturierter Vergleich der Konfigurationen verfügbar sein.

## Prüfnachweise

Mindestens zu testen sind:

- identischer Lauf mit identischem Seed/Version erzeugt erwartbar gleiches Ergebnis, soweit methodisch möglich,
- Run Manifest verweist auf die tatsächlich verwendeten Versionen,
- Nutzer können fremde Workspaces/Kernels nicht öffnen,
- Ressourcenlimits greifen,
- Notebook kann keine Rechte der GUI/API umgehen,
- Secret-Werte werden nicht in Notebook oder Output persistiert,
- historische Runs bleiben auch nach einer neuen Tool-/Prompt-Version ihrer alten Version zugeordnet.
