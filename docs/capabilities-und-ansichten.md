# Capabilities, progressive Freischaltung und Ansichten

Dieses Dokument konkretisiert F-13.

## Grundsatz

Anwendungen mit großem Funktionsumfang sollen neue Nutzer nicht mit allen Modulen gleichzeitig konfrontieren. Funktionen können als **Capabilities** modelliert werden, die je Nutzer, Organisation oder Projekt aktiviert werden.

Die Aktivierung einer Capability ist eine Darstellungs- und Nutzungsentscheidung. Sie ersetzt niemals die serverseitige Berechtigungsprüfung.

## Aktivierungsebenen

Ein Projekt legt fest, welche Ebenen benötigt werden:

- **Plattform**: technisch grundsätzlich verfügbar,
- **Organisation/Mandant**: für eine Organisation freigeschaltet,
- **Projekt/Vorgang**: in einem konkreten Arbeitsbereich aktiviert,
- **Nutzer**: persönlich eingeblendet oder als Standard gewählt.

Die wirksame Berechtigung ergibt sich weiterhin aus dem Rollen- und Rechtemodell. Ein ausgeblendetes Modul kann nicht allein deshalb als geschützt gelten.

## Progressive Disclosure

Bei einem umfangreichen System soll der Einstieg auf die fachlich erforderlichen Kernfunktionen reduziert werden. Erweiterte Funktionen werden erst angezeigt, wenn sie aktiviert oder im aktuellen Kontext benötigt werden.

Zu dokumentieren sind:

- welche Capabilities standardmäßig aktiv sind,
- wer zusätzliche Capabilities aktivieren darf,
- ob die Aktivierung lediglich die Navigation verändert oder auch technische Ressourcen startet,
- welche Abhängigkeiten zwischen Capabilities bestehen,
- wie eine Deaktivierung mit vorhandenen Daten umgeht.

Eine Deaktivierung löscht Daten nicht automatisch. Löschung folgt ausschließlich der festgelegten Aufbewahrungs- und Löschregel.

## View-Konfiguration

Capabilities dürfen eigene Ansichten anbieten. View-Konfigurationen sollen als eigenständige, versionierbare oder zumindest nachvollziehbar änderbare Einstellungen gespeichert werden.

Mindestens zu unterscheiden sind:

- geteilte/amtliche Ansicht,
- persönliche Ansicht,
- projektbezogene Ansicht.

Filter, Sortierung und sichtbare Felder dürfen keine unzulässigen Datenzugriffe ermöglichen. Serverantworten werden nach Berechtigung begrenzt; ein Client-Filter ist keine Zugriffskontrolle.

## Prüfnachweise

Das Projekt weist nach:

- neue Nutzer sehen nur die vorgesehenen Startfunktionen,
- aktivierte Capabilities erscheinen kontextgerecht,
- direkte API-Aufrufe bleiben unabhängig von der UI serverseitig geschützt,
- Deaktivierung führt nicht zu unbeabsichtigtem Datenverlust,
- persönliche Views verändern keine geteilten Fachdaten.
