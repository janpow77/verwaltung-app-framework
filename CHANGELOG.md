# Änderungsprotokoll

## Inhaltsversion 0.4.0 – 2026-09-08

- Quellenregister und maschinenprüfbare Themenzuordnung für F-01 bis F-18 ergänzt.
- Zehn vertiefende Barrierefreiheitsfälle sowie Vorfall-, SBOM- und Architekturprüfungen ergänzt.
- Nachweisvorlagen für Standards, Barrierefreiheit, Vorfälle, Lieferkette, Nutzungsrechte und menschliche Entscheidungen hinzugefügt.
- KI-Skill zur Standardsprüfung und Sicherheitsanweisungen mit den Nachweisen verbunden.
- BSI-Themenübersicht von einem vollständigen Grundschutz-Check abgegrenzt; Datenschutzberatung und verantwortliche Entscheidung getrennt.
- Für Bestandsprojekte: neue Vorlagen anhand der Anwendbarkeit übernehmen, Quellenstände bestätigen, T-36 bis T-38 und A-01 bis A-10 einplanen. Keine bestehenden Freigaben automatisch ändern.
- Technischer Inhaltsstand; Verantwortlichkeiten, Lizenz und organisatorische Freigabe bleiben offen.
- Zusammengeführt mit dem veröffentlichten Stand 0.3.0; dessen F-11 bis F-18 und T-21 bis T-35 bleiben erhalten. Im lokalen Zwischenstand 090f8ee bezeichneten T-21/T-22/T-23 noch Vorfall/SBOM/Architektur; diese Referenzen auf T-36/T-37/T-38 umstellen.

## Inhaltsversion 0.3.0 – 2026-09-07

- Bedingte Anforderungen F-11 bis F-18 ergänzt: Produkt-UX/Mehrfachansichten, Internationalisierung, progressive Capabilities, KI-Provider/BYOK, kollaborative Artefakte, Datenmapping, analytische Reproduzierbarkeit/Workspaces sowie Redaction/Pseudonymisierung/Synthetic Twin.
- Prompt- und Agent-Registry als eigener Anforderungsbaustein ergänzt. Metadaten unterscheiden Kategorien, Tags, Keywords und bewegliche Labels; Suche/Facetten berücksichtigen Sichtbarkeit und Mandantenrechte.
- Prompt-Versionen erhalten Commit-Message, unveränderliche Snapshots, Hash und verbindlichen Diff für Text, Variablen, Konfiguration, Tools/Berechtigungen, Metadaten und Test-/Eval-Änderungen.
- Agenten erhalten Agent-Card-artige Metadaten mit Skills, Tags, Beispielen, Capabilities, Input-/Output-Modi und Security-Informationen sowie Varianten/Revisionen, Draft/Commit und Agent-Diff.
- Prompt-/Agent-Evaluation mit versionierten Testsets, Assertions/Rubrics und exakter Zuordnung von Prompt-Version, Modell/Provider und Run-Manifest ergänzt.
- Neue Skills für Produkt-UX/i18n, Prompt-/Agent-Registry, Datenmapping/Reproduzierbarkeit und Redaction/Testdatenableitung ergänzt.
- Prüfkatalog um T-21 bis T-35 erweitert und Projekt-/Anwendbarkeitsvorlagen an F-11 bis F-18 angepasst.
- Konzepte aus Langfuse, Promptfoo, Agenta und dem A2A-Protokoll als fachliche Referenz ausgewertet; kein fremder Quellcode übernommen.

## Inhaltsversion 0.2.0 – 2026-09-06

- MUSS/BEDINGT/SOLL, administrative Regeln und zwanzig konkrete Prüffälle ergänzt.
- Durchgängigen KI-Arbeitsablauf und zusammenhängendes Musterpaket hinzugefügt.
- Anwendbarkeits-, Test- und Releasevorlagen ergänzt; organisatorische Besetzung und Nutzungsrechte ausdrücklich offen.
- Unvollständige Softwareentwürfe unter archiv/softwareentwuerfe/ eingeordnet.
- Für Bestandsprojekte: Anwendbarkeit neu dokumentieren, Prüffälle abgleichen und historische Softwarepfade nicht mehr als Projektgenerator verwenden.


## 2026-09-06 – Inhalts-Framework

- Umfang präzisiert: Anforderungen, Anweisungen, Skills und Vorlagen für Säule 2.
- Startanleitung, Projekt- und Datenschutzvorlagen, Landing-Unterlagen, Musterprojekt und Pflegeprozess ergänzt.
- Frühere Softwareentwürfe sind unvollständig und nicht als produktive Dienste freigegeben.

## Frühere technische Entwürfe (unvollständig)

- Erzeugbare FastAPI-/React-Referenz mit PostgreSQL, Alembic, OIDC/Keycloak,
  PostgreSQL-RLS, Dokumenten-, Akten-, Audit- und Exportdiensten.
- Copier-Vorlage und verpflichtende CI-/CODEOWNER-Gates.
