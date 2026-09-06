# Beiträge und Änderungen

Fachmodule werden in einem eigenen Projekt anhand der Inhalte aus docs/start.md entwickelt. Unvollständige Copier- und Softwareentwürfe im Archiv sind keine Startvoraussetzung.
Der Framework-Kern bleibt generisch und wird nur mit ADR, Tests und Review
erweitert.

Vor einem Pull Request:

- Fachanforderung, Rollen-/Rechtematrix und Prozessmodell ergänzen;
- Datenschutz/VVT/DSFA und Informationssicherheit bewerten;
- Migrationen, Mandantentrennung, Exporte und Statusübergänge testen;
- `python -m unittest discover -s tests -v` und `python checks/validate_repo.py` ausführen.

Für Inhaltsreleases sind die organisatorischen Rollen aus vorlagen/release.md zu besetzen. Ein CODEOWNER-Eintrag ist nur technische Review-Zuordnung, keine bereits erteilte Freigabe. Für Änderungen an
Authentifizierung, RLS, Freigaben, Audit oder Exporten gilt zusätzlich das
Vier-Augen-Prinzip; der Autor darf die eigene Änderung nicht freigeben.
