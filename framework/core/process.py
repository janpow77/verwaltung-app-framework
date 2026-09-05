"""KPAnG-inspirierte Statusmaschine für eine generische Projektakte."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone

from .models import ProjectCase


STATUS_LABELS = {
    "idee_eingegangen": "Idee eingegangen",
    "workshop": "Im Workshop eingeordnet",
    "framework_start": "Im Framework angelegt",
    "in_entwicklung": "In Entwicklung",
    "vorstellung": "Projekt vorgestellt",
    "fachpruefung": "Fachprüfung",
    "datenschutzpruefung": "Datenschutzprüfung",
    "sicherheitspruefung": "Sicherheitsprüfung",
    "freigabevorlage": "Zur Freigabe vorgelegt",
    "freigegeben": "Freigegeben",
    "betrieb": "Im Betrieb",
    "neubewertung": "Neubewertung erforderlich",
    "zurueckgegeben": "Zur Korrektur zurückgegeben",
    "abgebrochen": "Abgebrochen",
}

# Lücken im Nummernraum erlauben spätere Zwischenstände, ohne bestehende
# Statuskennungen zu ändern. Die fachliche Anzeige nutzt die Klartextlabels.
STATUS_CODES = {
    "idee_eingegangen": 10,
    "workshop": 20,
    "framework_start": 30,
    "in_entwicklung": 40,
    "vorstellung": 50,
    "fachpruefung": 60,
    "datenschutzpruefung": 70,
    "sicherheitspruefung": 80,
    "freigabevorlage": 90,
    "freigegeben": 100,
    "betrieb": 110,
    "neubewertung": 120,
    "zurueckgegeben": 190,
    "abgebrochen": 199,
}

TRANSITIONS: dict[str, set[str]] = {
    "idee_eingegangen": {"workshop", "framework_start", "abgebrochen"},
    "workshop": {"framework_start", "abgebrochen"},
    "framework_start": {"in_entwicklung", "abgebrochen"},
    "in_entwicklung": {"vorstellung", "zurueckgegeben", "abgebrochen"},
    "vorstellung": {"fachpruefung", "zurueckgegeben", "abgebrochen"},
    "fachpruefung": {"datenschutzpruefung", "sicherheitspruefung", "zurueckgegeben", "abgebrochen"},
    "datenschutzpruefung": {"sicherheitspruefung", "zurueckgegeben", "abgebrochen"},
    "sicherheitspruefung": {"freigabevorlage", "zurueckgegeben", "abgebrochen"},
    "freigabevorlage": {"freigegeben", "zurueckgegeben", "abgebrochen"},
    "freigegeben": {"betrieb", "abgebrochen"},
    "betrieb": {"neubewertung", "abgebrochen"},
    "neubewertung": {"in_entwicklung", "datenschutzpruefung", "sicherheitspruefung", "abgebrochen"},
    "zurueckgegeben": {"in_entwicklung", "vorstellung", "abgebrochen"},
    "abgebrochen": set(),
}


@dataclass
class GateContext:
    actor_id: str
    second_actor_id: str | None = None
    has_vvt: bool = False
    dsfa_required: bool = False
    dsfa_released: bool = False
    dsb_involved: bool = False
    tests_passed: bool = False
    security_passed: bool = False
    fachlich_approved: bool = False
    justification: str | None = None


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def validate_transition(project: ProjectCase, target: str, context: GateContext) -> None:
    if target not in STATUS_LABELS:
        raise ValueError(f"Unbekannter Status: {target}")
    if target not in TRANSITIONS.get(project.status, set()):
        raise ValueError(f"Übergang {project.status} → {target} ist nicht erlaubt")
    if target == "freigabevorlage":
        if not context.tests_passed or not context.security_passed or not context.fachlich_approved:
            raise ValueError("Freigabevorlage benötigt Tests, Sicherheits- und Fachprüfung")
        if not context.has_vvt:
            raise ValueError("Freigabevorlage benötigt einen VVT-Nachweis")
        if context.dsfa_required and not context.dsfa_released:
            raise ValueError("Erforderliche DSFA ist noch nicht freigegeben")
    if target == "freigegeben":
        if not context.second_actor_id or context.second_actor_id == context.actor_id:
            raise ValueError("Vier-Augen-Prinzip: eine zweite Person muss freigeben")
        if context.dsfa_required and not context.dsb_involved:
            raise ValueError("DSB-Beteiligung fehlt")
    if target in {"zurueckgegeben", "abgebrochen"} and not context.justification:
        raise ValueError(f"{STATUS_LABELS[target]} benötigt eine Begründung")


def transition(project: ProjectCase, target: str, context: GateContext) -> ProjectCase:
    validate_transition(project, target, context)
    previous = project.status
    project.status = target
    project.version += 1
    project.chronology.append({
        "at": _now(),
        "actor_id": context.actor_id,
        "action": "statuswechsel",
        "from": previous,
        "to": target,
        "justification": context.justification,
    })
    return project


def mark_reassessment_required(project: ProjectCase, actor_id: str, reason: str) -> ProjectCase:
    if project.status == "abgebrochen":
        raise ValueError("Abgebrochene Vorgänge werden nicht automatisch reaktiviert")
    previous = project.status
    project.status = "neubewertung"
    project.version += 1
    project.chronology.append({
        "at": _now(), "actor_id": actor_id, "action": "neubewertung_ausgeloest",
        "from": previous, "to": "neubewertung", "justification": reason,
    })
    return project
