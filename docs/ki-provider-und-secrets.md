# KI-Provider, Gateways und persönliche Secrets

Dieses Dokument konkretisiert F-14.

## Grundsatz

Anwendungen dürfen einen einzelnen KI-Anbieter nicht voraussetzen, wenn der fachliche Zweck providerunabhängig erfüllt werden kann. Unterstützt die Anwendung mehrere Anbieter oder persönliche Zugänge, erfolgt der Zugriff über eine definierte Provider-/Gateway-Schnittstelle.

## Provider und Endpunkte

Je nach Projekt können unterstützt werden:

- OpenAI-kompatible APIs,
- OpenAI,
- Anthropic,
- lokale oder organisationsinterne Modelle,
- Ollama,
- eigene Gateways/Router,
- sonstige dokumentierte Custom Endpoints.

Der Provider, das Modell und die zulässigen Datenklassen werden getrennt konfiguriert. Ein Nutzer darf nicht allein durch Eintragen eines Endpunkts eine organisationsseitige Datenfreigabe umgehen.

## Persönliche Verbindungen / BYOK

Wenn Nutzer eigene API-Zugänge hinterlegen dürfen, gilt mindestens:

- Secret-Werte werden serverseitig verschlüsselt gespeichert oder durch einen geeigneten Secret Store verwaltet,
- Secrets erscheinen nach dem Speichern nicht erneut im Klartext,
- keine Ablage in Browser-Local-Storage, Notebook-Dateien, Projektdateien, Prompts, Git oder Logs,
- Rotation und Löschen/Widerrufen einer Verbindung sind möglich,
- Verbindungstests geben keine Secrets in Fehlermeldungen aus,
- Nutzer können einen persönlichen Standardprovider wählen, soweit organisatorisch erlaubt.

## AI Gateway

Ein Gateway soll, soweit eingesetzt, mindestens trennen zwischen:

- fachlicher Anfrage,
- Nutzer-/Projektkontext,
- Providerkonfiguration,
- Secret-Auflösung,
- Logging/Audit-Metadaten.

An den Provider werden nur die für den konkreten Aufruf erforderlichen Daten übertragen. Providerwechsel verändern nicht stillschweigend die Datenklasse oder Freigabe.

## Nachvollziehbarkeit

KI-Aufrufe dokumentieren soweit erforderlich:

- Provider,
- Modell und Modellversion/Identifier,
- auslösende Person bzw. technischen Auftrag,
- Zeitpunkt,
- referenzierte Prompt-/Agent-Version,
- zulässige Datenklasse bzw. Verarbeitungsmodus,
- Ergebnisstatus und Fehlerklasse.

Secrets und unnötige Inhaltsdaten gehören nicht in diese Protokolle.

## Prüfnachweise

Das Projekt prüft insbesondere:

- Nutzer A kann Secret oder Verbindung von Nutzer B nicht lesen oder nutzen,
- gelöschte/rotierte Keys sind nicht weiter verwendbar,
- Logs und Fehlermeldungen enthalten keine Keys,
- ein direkt aufgerufener Provider-Endpunkt umgeht keine serverseitigen Rechte,
- Daten werden nur an den ausgewählten und zulässigen Provider übertragen.
