# Nutzer, Rollen und Administration

Anwendungsumfang nach docs/verbindlichkeit.md festlegen. Dieses Dokument konkretisiert F-01, F-02 und F-06.

## Grundregeln

Rechte werden pro Aktion, Mandant und gegebenenfalls Vorgang vergeben. Die Oberfläche darf Rechte anzeigen; maßgeblich ist die Prüfung im Server. Neue Rollen erhalten standardmäßig keine Rechte.

| Aufgabe | Vorgesehene Zuständigkeit | Prüfkriterium |
|---|---|---|
| Nutzer einladen | Benannte Mandantenadministration | Einladung nur für eigenen Mandanten, befristet und nicht wiederverwendbar |
| Mitgliedschaft bestätigen | Zuständige Administration nach Identitätsprüfung | Keine bloße E-Mail-Domain als Rechtebeleg |
| Rollen vergeben | Berechtigte Administration | Nur delegierbare Rollen; keine Selbsteskalation; Vergabe nachvollziehbar |
| Höhere Administrationsrechte | Andere zuständige Person | Zurechenbare Zweitentscheidung und dokumentierter Umfang |
| Nutzer sperren / ausscheiden | Zuständige Administration | Neue Zugriffe gesperrt; bestehende Sitzungen und Hintergrundaufträge berücksichtigt |
| Vertretung | Fachverantwortung veranlasst, Administration setzt um | Zweck, Zeitraum, Umfang und automatisches Ende dokumentiert |
| Mandant wechseln | Nutzer wählt aus bestätigten Mitgliedschaften | Rechte für Zielmandant neu geprüft; keine Übernahme aus anderem Mandanten |
| Plattformbetrieb | Benannte technische Administration | Kein automatisches fachliches Lese- oder Freigaberecht |
| Notfallzugriff | Benannte Notfallverantwortung | Befristet, begründet, protokolliert und nachträglich unabhängig geprüft |

## Kontenlebenszyklus

Einladung → Identität bestätigt → Mitgliedschaft aktiv → Änderung/Vertretung → Sperre/Austritt. Für jede Änderung Akteur, Zeitpunkt, Mandant und Umfang festhalten; keine Tokens oder Geheimnisse protokollieren.

Im Projekt festlegen: maximale Frist bis zum wirksamen Rechteentzug, Wiederprüfung bestehender Rechte, Umgang mit ungültigen Identitätsdaten, gesperrten Nutzern und gelöschten Mitgliedschaften. Beim Austritt Vorgänge geordnet übergeben; Nachweise nicht allein wegen Kontosperrung löschen.

## Fachliche Freigaben

Administration und Fachprüfung sind unterschiedliche Aufgaben. Wer Rechte verwaltet, darf damit keine vorgeschriebene Zweitprüfung umgehen. Bei mehreren Rollen bleiben Selbstfreigabe und Zuständigkeitsgrenzen wirksam.

## Konkrete Negativfälle

- Sachbearbeitung versucht direkt per API eine Adminrolle zu vergeben.
- Admin aus A lädt jemanden zu B ein.
- Rolle für A wird bei einer Anfrage für B wiederverwendet.
- Gesperrter Nutzer verwendet ein noch vorhandenes Token.
- Abgelaufene Vertretung bestätigt einen Vorgang.
- Ersteller versucht mit zusätzlicher Prüferrolle die eigene verbindliche Freigabe.
- Plattformadmin greift ohne fachliche Berechtigung auf Dokumente zu.

Erwartung: verweigern und angemessen nachvollziehbar machen. Abweichungen benötigen eine ausdrückliche Projektentscheidung.
