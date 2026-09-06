# ADR-004: Zunächst ein Repository mit Inhalten

Datum: 2026-09-06. Status: angenommen.

Das aktuelle Ergebnis ist ein gepflegter Bestand aus Anforderungen, Anweisungen, Skills, Projektvorlagen und Beispielen. Die Anwendung wird im eigenen Projekt anhand dieser Inhalte entwickelt.

Diese Entscheidung präzisiert ADR-001 und ADR-003: FastAPI, PostgreSQL und OIDC/Keycloak sind technische Referenzoptionen. „Framework-first“ bedeutet zunächst, Vorgaben und Projektunterlagen ab dem ersten Commit zu übernehmen. Eine fertige GUI, ein produktiver Dienst oder Copier ist dafür keine Voraussetzung.

Die vorhandenen Codeentwürfe bleiben als Arbeitsstand erhalten. Ihre Existenz belegt weder erfüllte Sicherheitsanforderungen noch Betriebsbereitschaft.

Strukturelle Umsetzung: frühere Anwendungen, Infrastruktur und Copier liegen unter archiv/softwareentwuerfe/. Aktive Inhaltsprüfungen verlangen diese Dateien nicht. Optionale Referenzlogik unter framework/ bleibt unabhängig prüfbar.
