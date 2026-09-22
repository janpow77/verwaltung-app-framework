# Lastenheft AuditCore-Plattform

## Repository-Inventur, gemeinsame Bibliotheken, Anwendungs-Refactoring, IT-Sicherheit und APT-Deployment

**Version:** 1.4  
**Stand:** 22.09.2026  
**Status:** verbindliche Implementierungs- und Abnahmespezifikation  
**Primärsysteme:** GitHub, KIRA RAG, Graphify  
**Verbindliche Security-/Compliance-Baseline:** dieses Repository verwaltung-app-framework

---

# 1. Zweck

Dieses Lastenheft beschreibt die Entwicklung einer gemeinsamen Plattform, mit der die bestehende Softwarelandschaft systematisch inventarisiert, konsolidiert, technisch verbessert und anschließend reproduzierbar deployt werden soll.

Das Ziel ist ausdrücklich nicht nur die Erstellung einer neuen Bibliothek.

Der vollständige Zielprozess lautet:

~~~text
Bestehende GitHub-Repositories
        ↓
Gesamtinventur
        ↓
Wiederverwendbare Logik erkennen
        ↓
Gemeinsame Bibliotheken erstellen
        ↓
Fachanwendungen von Duplikaten entlasten
        ↓
Fachanwendungen auf Shared Libraries migrieren
        ↓
Fachanwendungen technisch optimieren
        ↓
IT-Sicherheits- und Qualitätsprüfung
        ↓
Debian-Paket erzeugen
        ↓
Installation / Upgrade testen
        ↓
Deployment über apt
~~~

---

# 2. Verbindlichkeit für Codex und andere Agenten

Dieses Dokument ist ein Arbeitsauftrag und eine Definition of Done.

Ein Agent, der dieses Lastenheft umsetzt, muss:

1. vorhandenen Code zuerst analysieren,
2. bestehende Funktionen wiederverwenden,
3. keine parallelen Ersatzimplementierungen ohne Grund erzeugen,
4. tatsächlich ausführbaren Code erstellen,
5. Tests ausführen,
6. Fehler selbstständig beheben,
7. Prüfergebnisse nicht erfinden,
8. Sicherheits- und Compliance-Anforderungen dieses Repositories beachten,
9. fachliche oder rechtliche Konflikte nicht selbst auflösen,
10. erst nach den vorgesehenen Quality Gates abschließen.

Nicht ausreichend sind:

- reine Gerüste,
- TODO-Dateien,
- Platzhalter,
- ungetestete Beispielimplementierungen,
- nur dokumentierte APIs ohne reale Funktion,
- behauptete, aber nicht ausgeführte Tests.

Wenn eine Prüfung technisch nicht ausgeführt werden kann, lautet der Status:

- NOT_EXECUTED oder
- NOT_CONFIGURED.

---

# 3. Verbindliche vorhandene Vorgaben dieses Repositories

Vor Implementierung oder Änderung sind mindestens zu lesen und zu beachten:

- AGENTS.md
- docs/anforderungen.md
- docs/verbindlichkeit.md
- docs/standards.md
- docs/pruefkatalog.md
- docs/ki-arbeitsablauf.md
- docs/security/bsi-baseline.md
- docs/security/lieferkette.md
- docs/security/sicherheitsvorfaelle.md
- SECURITY.md
- alle für die konkrete Änderung einschlägigen ADRs
- passende Skills unter skills/

Dieses Lastenheft ersetzt diese Vorgaben nicht.

Bei Widersprüchen gilt:

1. ausdrücklich dokumentierte menschliche Entscheidung,
2. verbindliche MUSS-Anforderung des Frameworks,
3. dieses Lastenheft,
4. technische Default-Annahme.

Abweichungen von MUSS-Anforderungen sind nicht stillschweigend zulässig.

---

# 4. Security- und Compliance-Grundsatz

Dieses Repository ist die führende Quelle der Sicherheits- und Verwaltungsanforderungen.

Es gilt:

~~~text
verwaltung-app-framework
    = SOURCE OF SECURITY / COMPLIANCE POLICY TRUTH

GitHub-Repositories
    = SOURCE OF CODE TRUTH

KIRA
    = KNOWLEDGE SOURCE

Graphify
    = STRUCTURAL CODE ANALYSIS
~~~

AuditCore darf keine zweite, widersprüchliche Sicherheitswelt erzeugen.

Die vorhandenen Anforderungen werden als maschinenlesbare beziehungsweise ausführbare Policies in die AuditCore-Werkzeuge eingebunden.

---

# 5. Kernkomponenten

Die Plattform besteht aus sechs klar getrennten Komponenten.

## 5.1 auditcore

Zentrale frameworkunabhängige Fachbibliothek.

Sie enthält ausschließlich gemeinsam nutzbare Fachlogik.

Beispiele möglicher Domains:

- risk
- sampling
- procurement
- grants
- findings
- documents
- reporting
- validation
- anonymization
- accounting

auditcore enthält grundsätzlich keine:

- FastAPI-Router,
- Vue- oder React-Logik,
- konkreten Datenbank-Sessions,
- konkreten HTTP-Endpunkte,
- anwendungsspezifische Authentifizierung,
- UI-Logik.

## 5.2 auditcore_bibquality

Ausführbares Quality Gate für Python-Bibliotheken.

Aufgaben:

- Syntax,
- Typisierung,
- Architekturgrenzen,
- verbotene Imports,
- Dokumentation,
- Secrets,
- Datenschutz-/Open-Source-Prüfung,
- Dependency-Prüfung,
- Komplexität,
- API-Stabilität,
- Regression,
- Security-Gate-Integration.

## 5.3 auditcore_consolidator

Analyse- und Planungsinstanz.

Aufgaben:

- GitHub-Gesamtinventur,
- Symbolinventur,
- KIRA-Synchronisierung,
- Graphify-Auswertung,
- semantische Duplikaterkennung,
- Bibliothekskandidaten,
- Provenienz,
- Konfliktanalyse,
- Characterization-Planung,
- ConsolidationPlan.

Der Consolidator soll möglichst wenig konkreten Anwendungscode ändern.

## 5.4 auditcore_apprefactor

Werkzeug für die konkrete Fachanwendung.

Aufgaben:

- Migration auf auditcore,
- Migration auf weitere Shared Libraries,
- Compatibility Wrapper,
- Entfernung von Legacy-Code nach erfolgreicher Migration,
- Framework-Entkopplung,
- Datenbank-Entkopplung,
- Modulbereinigung,
- Dependency Reduction,
- Type-Hint-Verbesserung,
- Fehlerbehandlung,
- Testbarkeit,
- Performance- und Speicheroptimierung,
- Regression und Integration.

## 5.5 auditcore_security

Ausführbare Security-Policy-Engine.

Sie liest die Anforderungen dieses Repositories und stellt sie den anderen AuditCore-Komponenten als prüfbare Regeln zur Verfügung.

Die Bibliothek ersetzt nicht die menschlich lesbaren Vorgaben.

Sie operationalisiert sie.

## 5.6 auditcore_deployer

Release- und Deployment-Werkzeug.

Aufgaben:

- fertige Fachanwendung analysieren,
- DeploymentPlan erzeugen,
- Frontend vorbauen,
- Backend paketieren,
- Build-Manifest,
- Debian-Paket,
- systemd-Integration,
- Installationsprüfung,
- Upgradeprüfung,
- Health Check,
- APT-Repository.

---

# 6. Gesamtarchitektur

~~~text
                    GitHub-Repositories
                           │
                           ▼
                auditcore_consolidator
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
             auditcore        Shared Libraries
                 │                   │
                 └─────────┬─────────┘
                           ▼
                auditcore_apprefactor
                           │
                           ▼
                    Fachanwendung
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
   auditcore_bibquality          auditcore_security
             │                           │
             └─────────────┬─────────────┘
                           ▼
                 READY_FOR_DEPLOYMENT
                           │
                           ▼
                  auditcore_deployer
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
               .deb             APT Repository
                 │                   │
                 └─────────┬─────────┘
                           ▼
                       Zielserver
~~~

---

# 7. Leitprinzipien

Verbindlich:

~~~text
GITHUB BEFORE KIRA
INVENTORY BEFORE CONSOLIDATION
REUSE BEFORE REWRITE
CHARACTERIZE BEFORE REFACTOR
EVIDENCE BEFORE ASSUMPTION
NO SILENT SEMANTIC CHANGES
NO SILENT API BREAKS
NO SILENT SECURITY EXCEPTIONS
TEST LIBRARY AND CONSUMERS
AUDITABILITY OVER CLEVERNESS
CONSOLIDATE FIRST
REFACTOR SECOND
TEST THIRD
PACKAGE FOURTH
DEPLOY LAST
HUMAN DECIDES DOMAIN, LEGAL, SECURITY WAIVERS AND POLICY
~~~

---

# 8. Betriebsmodi

## GLOBAL

Gesamte relevante Repositorylandschaft des authentifizierten GitHub-Benutzers.

Verwendung:

- Erstinventur,
- periodische Gesamtinventur,
- repositoryübergreifende Duplikate,
- neue Bibliothekskandidaten,
- Architekturübersicht.

## REPO

Nur ein konkretes Repository.

Verwendung:

- lokaler Bug,
- reine UI-Änderung,
- lokale API-Anpassung,
- anwendungsspezifischer Code ohne Shared-Core-Bezug.

## REPO_AUDITCORE

Aktuelles Repository plus:

- auditcore,
- bekannte Shared Libraries,
- relevantes Inventar,
- KIRA,
- Graphify.

Standardmodus für:

- Fachlogik,
- Berechnungen,
- Datenmodelle,
- Parser,
- Validatoren,
- Rule Engines,
- wiederverwendbare technische Komponenten.

---

# 9. GLOBAL INITIAL INVENTORY

Wenn noch kein gültiges Inventar existiert, muss zuerst eine Gesamtinventur durchgeführt werden.

Zu erfassen sind mindestens:

- alle relevanten zugänglichen Repositories,
- Owner,
- Visibility,
- Default Branch,
- Commit SHA,
- aktiv / archiviert / Fork,
- primäre Sprache,
- Frameworks,
- Package Manager,
- Python-Version,
- Tests,
- CI,
- Lizenz,
- interne Packages,
- externe Dependencies.

Danach strukturelle Tiefenanalyse relevanter Code-Repositories.

---

# 10. Symbolinventar

Mindestens erfassen:

- Repository,
- Pfad,
- Modul,
- Symbol,
- Symboltyp,
- Signatur,
- Docstring-Zusammenfassung,
- Imports,
- Caller,
- Callees,
- Framework-Dependencies,
- Datenbank-Dependencies,
- Domain-Kategorie,
- Commit SHA.

Symboltypen mindestens:

- FUNCTION
- CLASS
- METHOD
- DATACLASS
- ENUM
- PROTOCOL
- PYDANTIC_MODEL
- RULE
- PARSER
- VALIDATOR
- EXPORTER.

---

# 11. Persistentes Inventar

Das Inventar darf nicht nur in einer Chatantwort existieren.

Lokale Ablage mindestens:

~~~text
.auditcore/
    inventory/
        repositories.json
        symbols.json
        dependencies.json
        libraries.json
        consumers.json
        migrations.json
        inventory_metadata.json
~~~

Zu dokumentieren:

- inventory_version,
- generated_at,
- scanner_version,
- scan_scope,
- Repository-Revisionen.

Spätere Inventuren inkrementell anhand von Branch und Commit SHA.

---

# 12. KIRA RAG

KIRA ist das dauerhafte Wissensgedächtnis über die Softwarelandschaft.

KIRA speichert mindestens folgende Wissensarten:

- REPOSITORY
- SOURCE_FILE
- SYMBOL
- DEPENDENCY
- DOMAIN_CONCEPT
- LIBRARY_CANDIDATE
- PROVENANCE
- QUALITY_REPORT
- SECURITY_POLICY
- SECURITY_CHECK_REPORT
- CONSOLIDATION_REPORT
- APPLICATION_REFACTOR
- MIGRATION
- APPLICATION_RELEASE
- PACKAGE_BUILD
- ARCHITECTURE_DECISION
- PROMPT
- POLICY.

Jeder repositorybezogene Datensatz erhält:

- Repository,
- Branch,
- Commit SHA,
- Pfad,
- Symbol,
- indexed_at.

Abweichender Commit:

STALE.

Kein Treffer in KIRA bedeutet nur:

NOT_FOUND_IN_CURRENT_INDEX.

Es bedeutet nicht, dass der Code nicht existiert.

---

# 13. Schutz vor Geheimnissen in KIRA

Vor Indexierung prüfen:

- Passwörter,
- API Keys,
- Access Tokens,
- Bearer Tokens,
- Private Keys,
- personenbezogene Echtdaten,
- Produktionskonfiguration,
- interne Zugangsdaten.

Verbindlich:

~~~text
NO SECRETS IN GIT
NO SECRETS IN KIRA
NO SECRETS IN LOGS
NO SECRETS IN DEB
NO SECRETS IN BUILD MANIFESTS
~~~

---

# 14. Graphify

Graphify analysiert für relevante Fundstellen:

- Imports,
- Caller,
- Callees,
- Dependency Chains,
- zentrale Module,
- Frameworkkopplungen,
- Datenbankkopplungen,
- gemeinsame Helper.

Neue relevante Symbole werden wieder mit GitHub und KIRA abgeglichen.

---

# 15. Bibliothekskandidaten

Repositoryübergreifend suchen nach:

- identischen Funktionen,
- semantisch ähnlichen Funktionen,
- kopierten Helfern,
- gemeinsamen Datenmodellen,
- Parsern,
- Dokumentenlogik,
- Risikologik,
- Stichprobenlogik,
- Reporting,
- Validierung,
- Anonymisierung,
- Office-Funktionen.

Jeder Kandidat dokumentiert:

- Quellen,
- betroffene Repositories,
- Symbole,
- Gemeinsamkeiten,
- Unterschiede,
- Frameworkkopplung,
- DB-Kopplung,
- Tests,
- Consumer,
- Konflikte,
- vorgeschlagenes Ziel.

Es gilt:

SO FEW SHARED LIBRARIES AS POSSIBLE, AS MANY AS NECESSARY.

---

# 16. Konfliktanalyse

Status mindestens:

- IDENTICAL
- TECHNICALLY_DIFFERENT
- SEMANTICALLY_EQUIVALENT
- SEMANTICALLY_DIFFERENT
- POLICY_DIFFERENCE
- LEGAL_INTERPRETATION_DIFFERENCE
- SECURITY_DIFFERENCE
- UNKNOWN.

Bei fachlicher, rechtlicher oder sicherheitsbezogener Konfliktlage:

HUMAN_DECISION_REQUIRED.

Keine eigenständige Harmonisierung durch das LLM.

---

# 17. Characterization und Golden Master

Vor Refactoring bestehender Fachlogik muss das tatsächliche Verhalten dokumentiert werden.

~~~text
Legacy Code
    ↓
Known Input
    ↓
Known Output
    ↓
Characterization Test
    ↓
Shared Library
    ↓
Regression Comparison
~~~

Unerklärbare Abweichung:

MIGRATION_BLOCKED.

---

# 18. auditcore

Gemeinsame Funktion erst erstellen, wenn:

1. Quellen bekannt sind,
2. Provenienz dokumentiert ist,
3. relevante Abhängigkeiten verstanden sind,
4. Konflikte klassifiziert sind,
5. Characterization Tests vorhanden sind,
6. fachliche Entscheidung nicht offen ist.

Framework- und Infrastrukturcode bleibt außerhalb des Fachkerns.

Veränderliche Rechts- und Regelparameter sollen soweit sinnvoll über versionierte RuleSets eingebunden werden.

Keine Rechtsregel erfinden.

---

# 19. auditcore_bibquality

CLI mindestens:

~~~text
auditcore-bibquality PATH
auditcore-bibquality PATH --format json
auditcore-bibquality PATH --strict
auditcore-bibquality PATH --output report.json
~~~

Status:

- PASS
- FAIL
- WARNING
- REVIEW_REQUIRED
- NOT_EXECUTED
- NOT_CONFIGURED.

Prüfbereiche mindestens:

- AC-SYN: Syntax,
- AC-ARCH: Architektur,
- AC-TYPE: Typisierung,
- AC-DOC: Dokumentation,
- AC-SEC: Security,
- AC-OSS: Datenschutz/Open Source,
- AC-DEP: Dependencies,
- AC-COMP: Komplexität,
- AC-API: API-Stabilität,
- AC-TEST: Tests.

Optionale Integrationen:

- Ruff,
- mypy oder pyright,
- Bandit,
- pip-audit,
- radon,
- vulture,
- pytest-cov.

Nicht installierte Tools sind NOT_EXECUTED, niemals PASS.

---

# 20. auditcore_security

## 20.1 Policy Source

Die Security Policy wird aus diesem Repository geladen.

Mindestens einzubeziehen:

- AGENTS.md,
- docs/anforderungen.md,
- docs/verbindlichkeit.md,
- docs/standards.md,
- docs/pruefkatalog.md,
- docs/security/bsi-baseline.md,
- docs/security/lieferkette.md,
- docs/security/sicherheitsvorfaelle.md,
- SECURITY.md,
- relevante ADRs.

## 20.2 Verbindliche Grundanforderungen

Die vorhandenen Vorgaben umfassen unter anderem:

- Mandantentrennung,
- serverseitige Autorisierung,
- Rollen und Rechte,
- kein UI-only Security Model,
- Vier-Augen-Prinzip für verbindliche Freigaben,
- keine Selbstfreigabe,
- unveränderliche freigegebene Versionen,
- sichere Secret-Verwaltung,
- keine echten Personen-/Falldaten in Git, Tests, Logs oder Prompts,
- keine persönlichen KI-Secrets im Browser-Local-Storage,
- Versionierung von Prompts und Agenten,
- Sichtbarkeits- und Mandantengrenzen bei Registry und Suche,
- reproduzierbare Analyseläufe,
- kontrollierte Redaction/Pseudonymisierung,
- sichere Uploads,
- Auditierung und Chronologie,
- Backup-/Restore-Nachweis,
- Schwachstellenbehandlung,
- Lieferketten- und SBOM-Anforderungen.

## 20.3 SecurityPolicyProvider

Bereitstellen:

~~~text
load_policy_set()
get_requirement()
policy_version()
source_revision()
~~~

Jede maschinenlesbare Sicherheitsregel referenziert ihre Quelle.

## 20.4 Keine stillen Security-Ausnahmen

Status bei nicht erfüllbarer Anforderung:

WAIVER_REQUIRED.

Ein Waiver benötigt mindestens:

- Requirement-ID,
- Grund,
- Risiko,
- Geltungsbereich,
- genehmigende Person/Stelle,
- Datum,
- Ablaufdatum, soweit anwendbar.

Codex oder ein LLM dürfen einen Waiver nicht selbst freigeben.

---

# 21. Anwendbarkeitsmatrix

Nicht jede Fachanwendung benötigt dieselben technischen Funktionen.

Daher muss pro Anwendung die vorhandene Anwendbarkeitsmatrix dieses Frameworks berücksichtigt werden.

Insbesondere F-01 bis F-18 sind zu bewerten.

MUSS-Anforderungen sind umzusetzen oder mit zuständiger Entscheidung als Abweichung zu dokumentieren.

BEDINGT-Anforderungen werden bei Eintritt des jeweiligen Auslösers zu MUSS.

SOLL-Abweichungen sind zu begründen.

---

# 22. Standards und Nachweise

Die in docs/standards.md hinterlegten Referenzen sind projektbezogen zu verwenden.

Insbesondere sind die dort dokumentierten Bezüge zu:

- BSI-Standard 200-2,
- BSI-Standard 200-3,
- IT-Grundschutz-Kompendium,
- OWASP ASVS,
- DSGVO,
- EN 301 549,
- WCAG,
- SBOM-Standards

nicht pauschal als automatisch erfüllt zu behaupten.

Erfüllung benötigt:

Quelle / Fassung → Anforderung → Umsetzung → Commit → Test / Review → Befund.

---

# 23. auditcore_apprefactor

Primäre Eingabe:

ConsolidationPlan.

Vor Änderungen erzeugen:

ApplicationRefactoringPlan.

Dieser enthält mindestens:

- Anwendung,
- Source Commit,
- Zielbibliotheken,
- zu ändernde Dateien,
- zu ersetzende Symbole,
- Importänderungen,
- Compatibility Wrapper,
- Tests,
- Dependencies,
- Optimierungsschritte,
- Security Impacts,
- Rollback-Strategie.

Dry Run verpflichtend verfügbar.

CLI mindestens:

~~~text
auditcore-refactor inspect REPOSITORY
auditcore-refactor plan REPOSITORY
auditcore-refactor apply PLAN --dry-run
auditcore-refactor apply PLAN
auditcore-refactor optimize REPOSITORY
auditcore-refactor verify REPOSITORY
~~~

---

# 24. Regeln für Anwendungs-Refactoring

Refactoring darf nicht:

- Authentifizierung abschwächen,
- Autorisierung umgehen,
- Mandantengrenzen aufheben,
- Logging/Audit Trail entfernen,
- Vier-Augen-Prinzip umgehen,
- Secrets in Code verschieben,
- freigegebene Versionen überschreibbar machen,
- Datenzugriff aus Notebook/Demo-Code direkt auf Produktion ermöglichen.

Legacy-Code erst entfernen, wenn:

- neue Shared-Library-Funktion getestet,
- Anwendung migriert,
- Regression bestanden,
- Integration bestanden,
- Consumer geprüft,
- Security Gate bestanden.

---

# 25. Optimierung

Nach gesicherter fachlicher Gleichheit prüfen:

- Modulstruktur,
- API-Design,
- Type Hints,
- Fehlerbehandlung,
- Komplexität,
- Duplikate,
- Dependencies,
- Frameworkkopplung,
- DB-Kopplung,
- Testbarkeit,
- Laufzeit,
- Speicherverbrauch.

Keine Micro-Optimierung ohne erkennbaren Nutzen.

Performanceänderungen bei kritischen Funktionen mit Vorher-/Nachher-Vergleich.

---

# 26. Application Quality Gate

Nach Refactoring mindestens:

- Application Unit Tests,
- Characterization Tests,
- Regression Tests,
- Integration Tests,
- Ruff,
- Type Checking,
- Security Checks,
- Dependency Scan,
- auditcore_bibquality,
- projektspezifische Prüffälle aus docs/pruefkatalog.md.

Die Akzeptanzfälle dieses Frameworks sind keine behaupteten bestandenen Tests. Sie müssen in der konkreten Anwendung tatsächlich ausgeführt werden, soweit anwendbar.

---

# 27. auditcore_deployer

Deployment erst bei:

READY_FOR_DEPLOYMENT.

Ziel:

~~~text
auditcore-deploy inspect APPLICATION
auditcore-deploy plan APPLICATION
auditcore-deploy build APPLICATION
auditcore-deploy test-package PACKAGE.deb
auditcore-deploy test-upgrade OLD.deb NEW.deb
~~~

Ergebnis mindestens:

~~~text
dist/
    application_VERSION_ARCH.deb
    application_VERSION_build-manifest.json
    application_VERSION_checksums.txt
~~~

---

# 28. Zielserver

Mindestens Debian-/Ubuntu-Server unterstützen.

Voraussetzungen dürfen sich auf einen weitgehend standardmäßig installierten Server beschränken.

Der Zielserver kann:

- über SSH administriert werden,
- einen Proxy verwenden,
- Pakete über apt installieren und aktualisieren.

Der Zielserver soll keine Entwicklungsumgebung benötigen.

Kein Source-Build auf dem Zielserver.

---

# 29. Linux-Dateisystem

Serveranwendung grundsätzlich:

~~~text
/opt/APPLICATION/
    application/
    frontend/
    runtime/

/etc/APPLICATION/
    configuration

/var/lib/APPLICATION/
    persistent-data

/usr/lib/systemd/system/
    APPLICATION.service
~~~

Code, Konfiguration und persistente Daten getrennt halten.

---

# 30. Python- und Frontend-Build

Kein ungeprüftes systemweites pip install.

PEP-668 berücksichtigen.

Zulässige Strategien:

- Debian-native Python-Pakete,
- isolierte Runtime,
- versionierter Wheelhouse.

Frontend bereits im CI-/Buildprozess erzeugen.

Kein npm build auf dem Zielserver.

---

# 31. systemd und Least Privilege

Serverdienste nicht unnötig als root betreiben.

Dedizierter Service-User.

Dateirechte minimal.

Soweit kompatibel und nach Policy vorgesehen, systemd-Hardening prüfen, beispielsweise:

- NoNewPrivileges,
- PrivateTmp,
- ProtectSystem,
- ProtectHome,
- RestrictSUIDSGID,
- CapabilityBoundingSet,
- ReadWritePaths.

Hardening nicht blind setzen; Funktionsfähigkeit testen.

---

# 32. Proxy und Netzwerk

Build und Laufzeit müssen gegebenenfalls respektieren:

- HTTP_PROXY,
- HTTPS_PROXY,
- NO_PROXY.

DeploymentPlan dokumentiert:

- Listen-Port,
- Health Endpoint,
- eingehende Verbindungen,
- ausgehende Verbindungen,
- externe Dienste.

Keine unnötigen Listener oder Internetabhängigkeiten.

---

# 33. Datenbankmigration

Versioniert und nachvollziehbar.

Upgrade darf Daten nicht unkontrolliert verlieren.

Migrationen müssen fehlschlagen können, ohne stillen Erfolg zu melden.

Automatische Migration in postinst nur, wenn sie sicher und reproduzierbar ist.

---

# 34. Debian- und APT-Paketierung

Ziel:

~~~text
sudo apt update
sudo apt install regulierung
~~~

Späteres Update:

~~~text
sudo apt update
sudo apt upgrade
~~~

Unterstützen:

- .deb,
- signiertes APT Repository,
- Checksums,
- Paketversionierung,
- Build Manifest.

Keine Secrets in Paketen.

---

# 35. Build Manifest

Mindestens:

- application,
- version,
- git_commit,
- auditcore_version,
- weitere Shared-Library-Versionen,
- security_policy_commit,
- built_at,
- quality_status,
- test_status.

---

# 36. SBOM und Lieferkette

Für freigabefähige Releases SBOM unterstützen.

Bevorzugt:

- CycloneDX oder
- SPDX.

Erfassen:

- Anwendung,
- Shared Libraries,
- Python Dependencies,
- Frontend Dependencies,
- Systemabhängigkeiten,
- Versionen.

Die Anforderungen aus docs/security/lieferkette.md sind verbindlich einzubeziehen.

---

# 37. Debian Deployment Quality Gate

Mindestens:

- Paketstruktur,
- Dependencies,
- Konfigurationstrennung,
- persistente Daten,
- systemd,
- Service User,
- Rechte,
- Secrets,
- reproduzierbarer Build,
- Installationsprüfung,
- Upgradeprüfung,
- Remove-Prüfung,
- Health Check,
- SBOM,
- Checksums,
- APT-Metadaten,
- Signierung soweit gefordert.

---

# 38. Saubere Testumgebung

.deb automatisiert in isolierter Debian-/Ubuntu-Umgebung prüfen.

Mindestens:

~~~text
apt install ./application.deb
systemctl status APPLICATION
Health Check
apt remove APPLICATION
~~~

Upgradepfad soweit relevant ebenfalls testen.

Kein echter Behördenserver als erste Testumgebung.

---

# 39. KIRA nach Migration und Release

Nach erfolgreicher Konsolidierung speichern:

- neue Shared-Library-Symbole,
- Provenienz,
- Consumer,
- Refactoringstatus,
- Security Status,
- Quality Status,
- API Snapshot,
- Migration,
- Architekturentscheidungen.

Nach Release zusätzlich:

- APPLICATION_RELEASE,
- PACKAGE_BUILD,
- DEPLOYMENT_PLAN,
- verwendete Policy-Version.

Keine Serverpasswörter oder vertraulichen Zugangsdaten in KIRA.

---

# 40. Consumer Registry und Impact Analysis

Für gemeinsame APIs speichern:

- bekannte Consumer,
- Versionen,
- betroffene Symbole.

Vor API-Änderung prüfen:

- welche Anwendungen betroffen,
- welche Tests erforderlich,
- ob Breaking Change.

Breaking Change niemals still einführen.

---

# 41. Workflow-Zustände

## Consolidator

- CREATED
- INVENTORY_REQUIRED
- INVENTORY_RUNNING
- INVENTORY_COMPLETE
- KIRA_SYNCHRONIZED
- CANDIDATES_DETECTED
- DEPENDENCIES_ANALYZED
- CONFLICTS_ANALYZED
- WAITING_FOR_HUMAN_DECISION
- READY_FOR_CONSOLIDATION
- CHARACTERIZED
- COMPLETE
- FAILED

## AppRefactor

- CREATED
- APPLICATION_ANALYZED
- REFACTOR_PLAN_CREATED
- DRY_RUN_COMPLETE
- LEGACY_CHARACTERIZED
- MIGRATION_APPLIED
- APPLICATION_TESTED
- OPTIMIZATION_APPLIED
- REGRESSION_VERIFIED
- INTEGRATION_VERIFIED
- SECURITY_VERIFIED
- QUALITY_VERIFIED
- READY_FOR_DEPLOYMENT
- FAILED

## Deployer

- CREATED
- APPLICATION_INSPECTED
- DEPLOYMENT_PLAN_CREATED
- SECURITY_VERIFIED
- QUALITY_VERIFIED
- BACKEND_BUILT
- FRONTEND_BUILT
- PACKAGE_STAGED
- DEB_BUILT
- PACKAGE_VALIDATED
- INSTALL_TESTED
- UPGRADE_TESTED
- HEALTH_CHECKED
- APT_READY
- PUBLISHED
- COMPLETE
- FAILED

---

# 42. Prompt- und Policy-Bibliothek

Prompts versioniert speichern.

Mindestens:

- system,
- global_inventory,
- repo_analysis,
- repo_auditcore,
- library_detection,
- conflict_analysis,
- consolidation,
- app_refactor,
- optimization,
- deployment.

Policies maschinenlesbar speichern:

- consolidation,
- architecture,
- human_decisions,
- quality,
- security,
- deployment.

Prompts beschreiben, wie das LLM analysiert.

Policies definieren, was erlaubt oder verboten ist.

Python erzwingt die Reihenfolge.

---

# 43. Tests der Plattform selbst

Fake-/Mock-Provider für:

- GitHub,
- KIRA,
- Graphify,
- LLM.

Tests mindestens für:

- Global Inventory,
- inkrementelle Inventur,
- Stale Detection,
- Symbolanalyse,
- KIRA Sync,
- Graphify Adapter,
- Bibliothekskandidaten,
- Conflict Detection,
- Human Decision Gate,
- Security Policy Loading,
- Security Policy Versioning,
- Provenienz,
- Characterization,
- ConsolidationPlan,
- RefactoringPlan,
- Dry Run,
- Import Migration,
- Compatibility Wrapper,
- Legacy Cleanup,
- Regression,
- Integration,
- Debian Build,
- Install Test,
- Upgrade Test,
- Health Check,
- CLI,
- JSON Reports,
- State Machines.

---

# 44. Repository-eigene Prüfungen

Nach Änderungen an diesem Framework-Repository müssen die bereits vorhandenen Prüfungen ausgeführt werden:

~~~text
python -m unittest discover -s tests -v
python checks/validate_repo.py
~~~

Weitere vorhandene Checks dürfen nicht durch AuditCore ersetzt werden.

AuditCore ergänzt sie.

---

# 45. CI

Mindestens Python 3.11 und 3.12; weitere unterstützte Versionen nach Projektlage.

Ausführen:

- pytest beziehungsweise vorhandene unittest-Suite,
- Ruff,
- mypy/pyright,
- Framework-Checks,
- auditcore_bibquality,
- auditcore_security,
- komponentenspezifische Tests.

Kein erfolgreicher Build bei blockierendem FAIL.

---

# 46. Definition of Done – Plattform

Erst abgeschlossen, wenn:

- auditcore installierbar,
- auditcore_bibquality installierbar,
- auditcore_consolidator installierbar,
- auditcore_apprefactor installierbar,
- auditcore_security installierbar,
- auditcore_deployer installierbar,
- alle CLIs funktionieren,
- Prompt Library vorhanden,
- Policy Library vorhanden,
- Security Policy dieses Repositories eingebunden,
- State Machines funktionieren,
- Inventar persistent gespeichert werden kann,
- KIRA Sync implementiert,
- Graphify-Adapter vorhanden,
- Bibliothekskandidaten erkannt,
- Provenienz dokumentiert,
- Conflict Detection vorhanden,
- Human Decision Gate vorhanden,
- Characterization-Infrastruktur vorhanden,
- App-Refactoring funktioniert,
- Security Gates funktionieren,
- Debian-Paketierung funktioniert,
- Tests bestanden,
- CI vorhanden,
- Dokumentation vorhanden.

---

# 47. Definition of Done – eine reale Konsolidierung

Eine reale Konsolidierung ist erst abgeschlossen, wenn:

1. Quellen identifiziert,
2. Commitstände dokumentiert,
3. Provenienz gespeichert,
4. Konflikte geprüft,
5. Characterization Tests vorhanden,
6. Shared-Library-Code implementiert,
7. Shared-Library-Tests bestanden,
8. BibQuality bestanden,
9. Security Gate bestanden,
10. betroffene Anwendung migriert,
11. Application Tests bestanden,
12. Integration bestanden,
13. Legacy-Code kontrolliert entfernt oder deprecated,
14. Inventar aktualisiert,
15. KIRA aktualisiert.

---

# 48. Definition of Done – deploybare Fachanwendung

Eine Anwendung gilt erst als READY_FOR_DEPLOYMENT, wenn:

- konsolidierte Architektur,
- Shared Libraries integriert,
- Refactoring abgeschlossen,
- Unit Tests bestanden,
- Regression bestanden,
- Integration bestanden,
- projektspezifische Prüffälle berücksichtigt,
- Security Policy erfüllt oder genehmigter Waiver,
- Dependencies geprüft,
- Build reproduzierbar,
- Frontend vorgebaut,
- Backend-Laufzeit reproduzierbar.

Sie gilt erst als vollständig paketiert, wenn zusätzlich:

- .deb erfolgreich gebaut,
- Installationsprüfung bestanden,
- systemd-Dienst funktionsfähig,
- Health Check bestanden,
- Upgradepfad geprüft,
- persistente Daten geschützt,
- Build Manifest vorhanden,
- SBOM vorhanden, soweit gefordert,
- Checksums vorhanden,
- verwendete Security-Policy-Version dokumentiert.

---

# 49. Initiale Reihenfolge für Codex

Codex arbeitet in folgender Reihenfolge:

## Phase A – vorhandene Vorgaben verstehen

1. AGENTS.md lesen.
2. Anforderungen und Verbindlichkeit lesen.
3. Standards und Security-Dokumente lesen.
4. Prüfkatalog und relevante ADRs lesen.
5. vorhandene Code- und Check-Struktur analysieren.

## Phase B – AuditCore-Plattform

6. auditcore implementieren beziehungsweise vorhandenen Stand erweitern.
7. auditcore_bibquality.
8. auditcore_security.
9. auditcore_consolidator.
10. auditcore_apprefactor.
11. auditcore_deployer.
12. Tests und CI.

## Phase C – Selbstprüfung

13. Plattform installieren.
14. Tests ausführen.
15. Framework-eigene Checks ausführen.
16. Quality und Security Gates ausführen.
17. Fehler beheben und erneut prüfen.

## Phase D – Softwareinventur

18. GLOBAL INITIAL INVENTORY des authentifizierten GitHub-Accounts.
19. persistentes Inventar.
20. KIRA Sync.
21. Graphify.
22. Bibliothekskandidaten und Consumer.

## Phase E – echte Konsolidierung

23. geeigneten Kandidaten auswählen.
24. Characterization.
25. Shared Library erstellen.
26. testen.
27. Fachanwendung mit auditcore_apprefactor migrieren.
28. optimieren.
29. Regression / Integration / Security.

## Phase F – Deployment

30. READY_FOR_DEPLOYMENT feststellen.
31. DeploymentPlan.
32. .deb bauen.
33. isoliert installieren.
34. Health Check.
35. Upgrade prüfen.
36. Releasewissen in KIRA aktualisieren.

---

# 50. Verbindlicher Abschlussbericht

Am Ende mindestens:

~~~text
AUDITCORE PLATFORM BUILD REPORT

Framework policy version:
Framework commit:
Security policy status:

auditcore:
auditcore_bibquality:
auditcore_security:
auditcore_consolidator:
auditcore_apprefactor:
auditcore_deployer:

Tests:
Framework checks:
Ruff:
Type checking:
Security checks:
Dependency checks:

GitHub inventory:
Repositories found:
Repositories analyzed:

KIRA:
Graphify:

Library candidates:
Libraries created:
Applications migrated:
Applications optimized:

Regression:
Integration:

Debian packaging:
Installation test:
Upgrade test:
Health check:

Human decisions required:
Security waivers required:
Blockers:
~~~

Keine erfundenen Ergebnisse.

---

# 51. Endgültiges Zielbild

Eine spätere Anforderung wie:

„Ich brauche im Audit-Designer eine neue Dokumentenprüfung.“

soll nicht unmittelbar zu neuem isolierten Code führen.

Stattdessen:

~~~text
Aufgabe
  ↓
aktuelles Repository
  ↓
Inventar
  ↓
auditcore / Shared Libraries
  ↓
KIRA
  ↓
GitHub-Verifikation
  ↓
Graphify
  ↓
Security-/Framework-Anforderungen
  ↓
Reuse / Extend / Consolidate / Local Implementation
  ↓
Tests
  ↓
App Refactor
  ↓
Security + Quality Gate
  ↓
Deployment
~~~

Das Endziel ist eine Softwarelandschaft mit weniger Duplikaten, klaren gemeinsam genutzten Bibliotheken, schlankeren Fachanwendungen, nachvollziehbaren Sicherheitsanforderungen und reproduzierbarem Deployment über Debian-/APT-Pakete.
