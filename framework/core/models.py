"""Generische, fachdomänenneutrale Modelle für den Framework-Vertrag."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Tenant:
    id: str
    name: str
    active: bool = True


@dataclass
class User:
    id: str
    tenant_ids: list[str]
    roles: list[str]
    active: bool = True


@dataclass
class ProjectCase:
    id: str
    tenant_id: str
    name: str
    owner_id: str
    initiative: str  # "hausbedarf" oder "eigeninitiative"
    status: str = "idee_eingegangen"
    version: int = 1
    created_at: str | None = None
    processing_activity_ids: list[str] = field(default_factory=list)
    evidence: list[dict[str, Any]] = field(default_factory=list)
    chronology: list[dict[str, Any]] = field(default_factory=list)
    deadlines: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class ProcessingActivity:
    """Verarbeitungstätigkeit nach Art. 30 Abs. 1 DSGVO.

    Die Feldnamen folgen der Reihenfolge der Norm. ``legal_basis`` ist dort
    nicht ausdrücklich gefordert, gehört aber in jedes behördliche
    VVT-Muster und ist deshalb Pflichtangabe.
    """

    id: str
    tenant_id: str
    project_id: str
    name: str
    # lit. b Zwecke der Verarbeitung
    purpose: str
    # Rechts- bzw. Ermächtigungsgrundlage (Art. 6, ggf. Art. 9 DSGVO)
    legal_basis: str
    # lit. c Kategorien betroffener Personen und personenbezogener Daten
    affected_persons: list[str]
    data_categories: list[str]
    # lit. d Kategorien von Empfängern
    recipients: list[str]
    # lit. f Fristen für die Löschung
    retention: str
    # lit. g allgemeine Beschreibung der TOM nach Art. 32 Abs. 1 DSGVO
    security_measures: list[str]

    # lit. a Verantwortlicher und Datenschutzbeauftragter
    controller: str = ""
    data_protection_officer: str = ""
    # lit. e Übermittlung an Drittländer und Garantien nach Art. 46/49 DSGVO
    third_country_transfer: bool = False
    third_country_recipients: list[str] = field(default_factory=list)
    third_country_safeguards: str = ""
    # Rechtsgrundlage der Aufbewahrungs- bzw. Löschfrist
    retention_legal_basis: str = ""
    # Auftragsverarbeitung (Art. 28 Abs. 3) und gemeinsame Verantwortlichkeit (Art. 26)
    processors: list[str] = field(default_factory=list)
    processing_agreement: bool = False
    joint_controllers: list[str] = field(default_factory=list)

    vvt_version: int = 1
    contains_personal_data: bool = True
    updated_at: str | None = None


@dataclass
class DsfaAssessment:
    """Datenschutz-Folgenabschätzung zu genau einer Verarbeitungstätigkeit.

    Die Felder ``necessity``, ``proportionality``, ``risk_scenarios`` und
    ``mitigation_measures`` bilden den Mindestinhalt nach Art. 35 Abs. 7
    lit. a bis d DSGVO ab; ``data_subject_view`` den Standpunkt nach
    Art. 35 Abs. 9 und ``authority_consultation`` die vorherige Konsultation
    nach Art. 36 Abs. 1.
    """

    id: str
    tenant_id: str
    activity_id: str
    vvt_version: int
    # lit. a Beschreibung der Verarbeitung: unveränderlicher VVT-Stand
    activity_snapshot: dict[str, Any]
    screening_answers: dict[str, Any] = field(default_factory=dict)
    # lit. b Bewertung von Notwendigkeit und Verhältnismäßigkeit
    necessity: str = ""
    proportionality: str = ""
    # lit. c Risiken für die Rechte und Freiheiten der betroffenen Personen
    risk_scenarios: list[dict[str, Any]] = field(default_factory=list)
    # lit. d Abhilfemaßnahmen, Garantien, Sicherheitsvorkehrungen, Verfahren
    mitigation_measures: list[dict[str, Any]] = field(default_factory=list)
    # Art. 35 Abs. 9: Standpunkt der Betroffenen oder ihrer Vertreter
    data_subject_view: str = ""
    system_suggestion: dict[str, Any] | None = None
    human_decision: str | None = None
    deviates_from_suggestion: bool = False
    deviation_justification: str | None = None
    decided_by: str | None = None
    decided_at: str | None = None
    dsb_statement: str | None = None
    dsb_vote: str | None = None
    dsb_involved_at: str | None = None
    # Art. 36 Abs. 1: Ergebnis der vorherigen Konsultation der Aufsichtsbehörde
    authority_consultation: dict[str, Any] | None = None
    status: str = "entwurf"
    version: int = 1
    created_by: str = ""
    created_at: str | None = None
    released_by: str | None = None
    released_at: str | None = None
    predecessor_id: str | None = None
    locked: bool = False
