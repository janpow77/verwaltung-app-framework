# Freigabe- und Änderungsprozess

Der Prozess ist zweistufig: KI und Entwickler erarbeiten einen Vorschlag;
fachlich zuständige Personen prüfen und entscheiden. Ein Pull Request ist
kein fachlicher Betriebsbeschluss.

## Verbindliche Gates

- Tests, Struktur-/Vertragsprüfung, Backend-Syntax, Dependency-, Secret- und
  statische Sicherheitsprüfung müssen erfolgreich sein.
- Änderungen an geschützten Bereichen werden von CODEOWNER geprüft.
- Kein Selbst-Review und kein direktes Pushen auf `main`.
- Migrationen brauchen einen Rollback-Plan und einen Test mit PostgreSQL.
- Releases erhalten eine nachvollziehbare Version und ein Änderungsprotokoll.

Branch-Schutz und erforderliche Statuschecks sind im GitHub-Repository als
Pflichtregeln zu konfigurieren; diese Datei dokumentiert die fachliche
Mindestanforderung und ersetzt die Plattformkonfiguration nicht.
