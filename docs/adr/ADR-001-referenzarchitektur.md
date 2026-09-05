# ADR-001: Eine verbindliche Referenzarchitektur

## Entscheidung

Der Frameworkkern verwendet als Referenz FastAPI, SQLAlchemy, Alembic,
PostgreSQL, OIDC/Keycloak und eine TypeScript-Oberfläche. Fachmodule werden
über definierte Schnittstellen ergänzt. Docker Compose dient der lokalen
Entwicklung; Produktionsprofile werden getrennt dokumentiert.

## Begründung

`audit_designer` liefert die passende FastAPI-/Datenverarbeitungsbasis,
`regulierung` die Identitäts-, Rollen- und Datenschutzmuster. `flowaudit` liefert
Export- und Fachanwendungserfahrung, hat aber konkurrierende Flask/React- und
doppelte Backend-Strukturen. Diese Historie wird nicht in den Kern übernommen.

