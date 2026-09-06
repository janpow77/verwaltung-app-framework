# Historischer Entwurf einer Referenzimplementierung

Status: archiviert und unvollständig. Die nachstehenden Pfade beschreiben den damaligen Entwurf unter archiv/softwareentwuerfe/. Aussagen zur Startbarkeit sind nicht nachgewiesen. Für den aktuellen Inhalt gelten README.md und ADR-004; dieses Dokument ist keine Leistungszusage.

`apps/backend` und `apps/frontend` sind ein tatsächlich startbarer vertikaler
Referenzschnitt für neue Fachanwendungen. Sie ersetzen nicht die fachliche
Analyse und keine Organisationsfreigabe.

## Schutzschichten

1. OIDC/Keycloak identifiziert die Person und liefert Rollen/Mandanten-Claims.
2. FastAPI prüft serverseitig Berechtigungen und den Mandanten.
3. SQLAlchemy setzt pro Transaktion `app.tenant_id`.
4. PostgreSQL erzwingt mit `FORCE ROW LEVEL SECURITY` die Trennung auch bei
   vergessenen Query-Filtern.
5. Audit-Ereignisse sind append-only; freigegebene DSFA-Fassungen sind nicht
   überschreibbar.

## Dienste

Akten werden im Beispiel als `project_case` geführt. Dokumente erhalten einen
geprüften Storage-Key, SHA-256-Nachweis, Größenlimit, Downloadkontrolle und Audit-Ereignis. JSON,
CSV und ZIP enthalten Metadaten; CSV-Werte werden gegen Tabellenformel-
Injektion geschützt. Für Produktion sind Virenscan, verschlüsselter
Objekt-Storage, Backup/Restore-Tests, Aufbewahrung und Löschung als
Organisationskonfiguration zu ergänzen.
