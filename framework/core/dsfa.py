"""VVT-/Schwellwert-/DSFA-Vertragskern nach dem Muster aus regulierung.

Der Fragenkatalog steht als Daten in diesem Modul, nicht verstreut in der
Auswertung. Jede Frage trägt ihre Fundstelle, damit die Systemempfehlung
zitierfähig ist und bei einer Änderung der Rechtslage nachgeführt werden
kann, ohne die Logik anzufassen.

Aufbau des Katalogs:

* Block A  Muss-Kriterien nach Art. 35 Abs. 3 DSGVO. Ein „ja“ genügt, die
           DSFA ist dann Pflicht (harter Auslöser).
* Block B  Muss-Liste der Aufsichtsbehörde nach Art. 35 Abs. 4 DSGVO. Der
           Kern liefert die Struktur; die fachlich gültigen Einträge legt
           die zuständige Datenschutzorganisation über
           ``ergaenze_muss_liste`` fest (siehe docs/dsfa-werkzeug.md).
* Block C  Die neun Kriterien des Europäischen Datenschutzausschusses
           (WP 248 rev.01). Jedes „ja“ zählt einen Punkt; ab zwei Punkten
           ist die DSFA durchzuführen.

Die Entscheidung trifft ein Mensch. Weicht sie vom Vorschlag ab, verlangt
der Kern eine Begründung — in beide Richtungen.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Any

from .models import DsfaAssessment, ProcessingActivity


WIRKUNG_HART = "hart"
WIRKUNG_PUNKT = "punkt"

#: Mindestlänge einer Begründung, die eine Systemempfehlung überstimmt.
MINDESTLAENGE_BEGRUENDUNG = 30

#: Ab diesem Restrisiko ist die Aufsichtsbehörde vorher zu konsultieren.
RESTRISIKO_KONSULTATION = "hoch"

RESTRISIKOSTUFEN = ("gering", "mittel", "hoch")

DSB_VOTEN = ("zustimmend", "mit_auflagen", "ablehnend")

ENTSCHEIDUNGEN = ("durchfuehren", "nicht_erforderlich")


@dataclass(frozen=True)
class ScreeningCriterion:
    """Eine Frage der Schwellwertanalyse samt Fundstelle."""

    key: str
    text: str
    source: str
    effect: str


# Block A: harte Auslöser unmittelbar aus der Verordnung.
_BLOCK_A: tuple[ScreeningCriterion, ...] = (
    ScreeningCriterion(
        key="umfassende_bewertung_mit_rechtswirkung",
        text=(
            "Systematische und umfassende Bewertung persönlicher Aspekte, die sich "
            "auf automatisierte Verarbeitung einschließlich Profiling gründet und "
            "die ihrerseits Grundlage von Entscheidungen mit Rechtswirkung ist"
        ),
        source="Art. 35 Abs. 3 lit. a DSGVO",
        effect=WIRKUNG_HART,
    ),
    ScreeningCriterion(
        key="umfangreiche_besondere_kategorien",
        text=(
            "Umfangreiche Verarbeitung besonderer Kategorien personenbezogener "
            "Daten oder von Daten über strafrechtliche Verurteilungen und Straftaten"
        ),
        source="Art. 35 Abs. 3 lit. b DSGVO in Verbindung mit Art. 9 Abs. 1, Art. 10 DSGVO",
        effect=WIRKUNG_HART,
    ),
    ScreeningCriterion(
        key="systematische_ueberwachung_oeffentlicher_bereiche",
        text="Systematische umfangreiche Überwachung öffentlich zugänglicher Bereiche",
        source="Art. 35 Abs. 3 lit. c DSGVO",
        effect=WIRKUNG_HART,
    ),
)

# Block C: die neun Kriterien des EDSA. Die Schlüssel sind bewusst stabil.
_BLOCK_C: tuple[ScreeningCriterion, ...] = (
    ScreeningCriterion(
        key="bewertung_oder_scoring",
        text="Bewerten oder Einstufen einschließlich Profiling und Vorhersagen",
        source="WP 248 rev.01, Kriterium 1",
        effect=WIRKUNG_PUNKT,
    ),
    ScreeningCriterion(
        key="automatisierte_entscheidung",
        text=(
            "Automatisierte Entscheidungsfindung mit Rechtswirkung oder ähnlich "
            "erheblicher Beeinträchtigung"
        ),
        source="WP 248 rev.01, Kriterium 2",
        effect=WIRKUNG_PUNKT,
    ),
    ScreeningCriterion(
        key="systematische_beobachtung",
        text="Systematische Überwachung betroffener Personen",
        source="WP 248 rev.01, Kriterium 3",
        effect=WIRKUNG_PUNKT,
    ),
    ScreeningCriterion(
        key="sensible_daten",
        text="Vertrauliche Daten oder höchstpersönliche Daten",
        source="WP 248 rev.01, Kriterium 4",
        effect=WIRKUNG_PUNKT,
    ),
    ScreeningCriterion(
        key="daten_hoher_personenzahl",
        text="Verarbeitung in großem Umfang",
        source="WP 248 rev.01, Kriterium 5",
        effect=WIRKUNG_PUNKT,
    ),
    ScreeningCriterion(
        key="zusammenfuehrung_von_daten",
        text="Abgleichen oder Zusammenführen von Datensätzen",
        source="WP 248 rev.01, Kriterium 6",
        effect=WIRKUNG_PUNKT,
    ),
    ScreeningCriterion(
        key="schutzbeduerftige_personen",
        text="Daten schutzbedürftiger betroffener Personen",
        source="WP 248 rev.01, Kriterium 7",
        effect=WIRKUNG_PUNKT,
    ),
    ScreeningCriterion(
        key="innovative_technologie",
        text="Innovative Nutzung neuer technologischer oder organisatorischer Lösungen",
        source="WP 248 rev.01, Kriterium 8",
        effect=WIRKUNG_PUNKT,
    ),
    ScreeningCriterion(
        key="verhinderung_von_rechten_oder_diensten",
        text=(
            "Die Verarbeitung hindert betroffene Personen daran, ein Recht auszuüben "
            "oder eine Dienstleistung oder einen Vertrag in Anspruch zu nehmen"
        ),
        source="WP 248 rev.01, Kriterium 9",
        effect=WIRKUNG_PUNKT,
    ),
)

# Block B ist bewusst leer: die Muss-Liste nach Art. 35 Abs. 4 DSGVO wird von
# der zuständigen Aufsichtsbehörde veröffentlicht und ist je Land verschieden.
_muss_liste: list[ScreeningCriterion] = []


def ergaenze_muss_liste(kriterien: list[ScreeningCriterion]) -> None:
    """Trägt die Muss-Liste der zuständigen Aufsichtsbehörde nach.

    Die Einträge wirken als harte Auslöser. Zweck ist die Nachführbarkeit:
    ändert die Aufsichtsbehörde ihre Liste, wird hier nachgetragen und nicht
    die Auswertung angefasst.
    """
    for kriterium in kriterien:
        if kriterium.effect != WIRKUNG_HART:
            raise ValueError("Einträge der Muss-Liste sind harte Auslöser")
        if kriterium.key in _katalog_schluessel():
            raise ValueError(f"Kriterium ist bereits vergeben: {kriterium.key}")
        _muss_liste.append(kriterium)


def katalog() -> tuple[ScreeningCriterion, ...]:
    """Vollständiger Fragenkatalog in Auswertungsreihenfolge."""
    return _BLOCK_A + tuple(_muss_liste) + _BLOCK_C


def _katalog_schluessel() -> set[str]:
    return {kriterium.key for kriterium in katalog()}


#: Die neun Punktkriterien; die Schwelle bezieht sich allein auf sie.
SCREENING_CRITERIA = tuple(kriterium.key for kriterium in _BLOCK_C)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def activity_snapshot(activity: ProcessingActivity) -> dict[str, Any]:
    return asdict(activity)


def _pruefe_antworten(answers: dict[str, Any]) -> None:
    """Weist unbekannte Schlüssel und nicht-boolesche Werte zurück.

    Eine Schwellwertanalyse darf bei fehlerhafter Eingabe nicht die
    nachsichtigere Antwort geben. Über eine JSON-Schnittstelle kommt ein
    „ja“ leicht als Zeichenkette an; ohne diese Prüfung zählte es als Nein.
    """
    bekannt = _katalog_schluessel()
    unbekannt = sorted(set(answers) - bekannt)
    if unbekannt:
        raise ValueError(f"Unbekannte Schwellwertkriterien: {', '.join(unbekannt)}")
    falsch_typisiert = sorted(k for k, v in answers.items() if not isinstance(v, bool))
    if falsch_typisiert:
        raise ValueError(
            "Antworten müssen True oder False sein: " + ", ".join(falsch_typisiert)
        )


def evaluate_screening(answers: dict[str, Any], *, threshold: int = 2) -> dict[str, Any]:
    """Prüft harte Auslöser, zählt die EDSA-Kriterien und begründet das Ergebnis."""
    _pruefe_antworten(answers)
    hart = [k.key for k in katalog() if k.effect == WIRKUNG_HART and answers.get(k.key) is True]
    punkte = [k for k in SCREENING_CRITERIA if answers.get(k) is True]
    score = len(punkte)
    required = bool(hart) or score >= threshold
    fundstellen = [_kriterium(k).source for k in hart]

    if hart:
        reason = (
            "Die Folgenabschätzung ist durchzuführen, weil "
            f"{len(hart)} Muss-Kriterium bejaht wurde: {fundstellen[0]}."
            if len(hart) == 1
            else (
                "Die Folgenabschätzung ist durchzuführen, weil "
                f"{len(hart)} Muss-Kriterien bejaht wurden: {'; '.join(fundstellen)}."
            )
        )
    elif required:
        reason = (
            f"Es sind {score} der {len(SCREENING_CRITERIA)} Kriterien des Europäischen "
            f"Datenschutzausschusses erfüllt. Ab {threshold} Kriterien ist regelmäßig von "
            "einem voraussichtlich hohen Risiko auszugehen (WP 248 rev.01); die "
            "Folgenabschätzung ist durchzuführen."
        )
    else:
        reason = (
            "Kein Muss-Kriterium ist erfüllt und es sind "
            f"{score} der {len(SCREENING_CRITERIA)} Kriterien des Europäischen "
            f"Datenschutzausschusses bejaht, also weniger als {threshold}. Eine "
            "Folgenabschätzung ist damit nicht erforderlich; das Ergebnis ist "
            "gleichwohl zu dokumentieren (Art. 5 Abs. 2 DSGVO)."
        )

    return {
        "criteria": punkte,
        "hard_triggers": hart,
        "sources": fundstellen,
        "score": score,
        "threshold": threshold,
        "total_criteria": len(SCREENING_CRITERIA),
        "dsfa_recommended": required,
        "reason": reason,
    }


def _kriterium(key: str) -> ScreeningCriterion:
    for kriterium in katalog():
        if kriterium.key == key:
            return kriterium
    raise KeyError(f"Unbekanntes Kriterium: {key}")


def create_dsfa(
    activity: ProcessingActivity,
    *,
    assessment_id: str,
    created_by: str,
    answers: dict[str, Any],
) -> DsfaAssessment:
    suggestion = evaluate_screening(answers)
    return DsfaAssessment(
        id=assessment_id,
        tenant_id=activity.tenant_id,
        activity_id=activity.id,
        vvt_version=activity.vvt_version,
        activity_snapshot=activity_snapshot(activity),
        screening_answers=dict(answers),
        system_suggestion=suggestion,
        created_by=created_by,
        created_at=_now(),
    )


def _pruefe_offen(assessment: DsfaAssessment) -> None:
    if assessment.locked:
        raise ValueError(
            f"Fassung {assessment.version} ist freigegeben und gesperrt. Für eine "
            "Änderung ist eine neue Fassung anzulegen; die freigegebene Fassung "
            "bleibt als Nachweis erhalten."
        )


def set_necessity(
    assessment: DsfaAssessment, *, necessity: str, proportionality: str
) -> None:
    """Bewertung nach Art. 35 Abs. 7 lit. b DSGVO."""
    _pruefe_offen(assessment)
    if not necessity.strip() or not proportionality.strip():
        raise ValueError(
            "Notwendigkeit und Verhältnismäßigkeit sind zu bewerten "
            "(Art. 35 Abs. 7 lit. b DSGVO)"
        )
    assessment.necessity = necessity
    assessment.proportionality = proportionality


def add_risk_scenario(
    assessment: DsfaAssessment,
    *,
    description: str,
    severity: str,
    likelihood: str,
    residual_risk: str,
) -> None:
    """Risikoszenario nach Art. 35 Abs. 7 lit. c DSGVO."""
    _pruefe_offen(assessment)
    if not description.strip():
        raise ValueError("Ein Risikoszenario braucht eine Beschreibung")
    if residual_risk not in RESTRISIKOSTUFEN:
        raise ValueError(f"Restrisiko muss eine der Stufen {RESTRISIKOSTUFEN} sein")
    assessment.risk_scenarios.append({
        "description": description,
        "severity": severity,
        "likelihood": likelihood,
        "residual_risk": residual_risk,
    })


def add_mitigation_measure(
    assessment: DsfaAssessment, *, description: str, addresses: str, responsible: str
) -> None:
    """Abhilfemaßnahme nach Art. 35 Abs. 7 lit. d DSGVO."""
    _pruefe_offen(assessment)
    if not description.strip():
        raise ValueError("Eine Abhilfemaßnahme braucht eine Beschreibung")
    assessment.mitigation_measures.append({
        "description": description,
        "addresses": addresses,
        "responsible": responsible,
    })


def highest_residual_risk(assessment: DsfaAssessment) -> str | None:
    """Höchstes Restrisiko über alle Szenarien."""
    stufen = [
        s.get("residual_risk")
        for s in assessment.risk_scenarios
        if s.get("residual_risk") in RESTRISIKOSTUFEN
    ]
    if not stufen:
        return None
    return max(stufen, key=RESTRISIKOSTUFEN.index)


def set_human_decision(
    assessment: DsfaAssessment,
    *,
    decision: str,
    actor_id: str,
    deviation_justification: str | None = None,
) -> None:
    """Menschliche Entscheidung über den Systemvorschlag.

    Die Abweichung wird berechnet, nicht behauptet, und gilt in beide
    Richtungen: Wer eine empfohlene DSFA unterlässt, begründet das ebenso
    wie wer eine nicht empfohlene DSFA anordnet.
    """
    _pruefe_offen(assessment)
    if decision not in ENTSCHEIDUNGEN:
        raise ValueError(f"Ungültige menschliche Entscheidung: {decision}")
    if not actor_id.strip():
        raise ValueError("Die Entscheidung ist einer Person zuzuordnen")
    if assessment.system_suggestion is None:
        raise ValueError(
            "Zu dieser Fassung liegt kein Vorschlag vor. Zuerst die "
            "Schwellwertanalyse ausfüllen."
        )
    empfohlen = bool(assessment.system_suggestion.get("dsfa_recommended"))
    abweichung = (decision == "durchfuehren") != empfohlen
    if abweichung and len((deviation_justification or "").strip()) < MINDESTLAENGE_BEGRUENDUNG:
        raise ValueError(
            "Abweichung von der Systemempfehlung benötigt eine substanzielle "
            f"Begründung von mindestens {MINDESTLAENGE_BEGRUENDUNG} Zeichen"
        )
    assessment.human_decision = decision
    assessment.deviates_from_suggestion = abweichung
    assessment.deviation_justification = deviation_justification
    assessment.decided_by = actor_id
    assessment.decided_at = _now()
    assessment.status = "dsb_beteiligung"


def set_dsb_statement(assessment: DsfaAssessment, *, statement: str, vote: str) -> None:
    """Stellungnahme und Votum der oder des Datenschutzbeauftragten."""
    _pruefe_offen(assessment)
    if vote not in DSB_VOTEN:
        raise ValueError(f"Ungültiges DSB-Votum: {vote}")
    if not statement.strip():
        raise ValueError("DSB-Stellungnahme darf nicht leer sein")
    assessment.dsb_statement = statement
    assessment.dsb_vote = vote
    assessment.dsb_involved_at = _now()


def set_data_subject_view(assessment: DsfaAssessment, *, view: str) -> None:
    """Standpunkt der betroffenen Personen nach Art. 35 Abs. 9 DSGVO."""
    _pruefe_offen(assessment)
    assessment.data_subject_view = view


def record_authority_consultation(
    assessment: DsfaAssessment, *, authority: str, result: str, decided_at: str | None = None
) -> None:
    """Ergebnis der vorherigen Konsultation nach Art. 36 Abs. 1 DSGVO."""
    _pruefe_offen(assessment)
    if not authority.strip() or not result.strip():
        raise ValueError("Konsultation braucht Aufsichtsbehörde und Ergebnis")
    assessment.authority_consultation = {
        "authority": authority,
        "result": result,
        "decided_at": decided_at or _now(),
    }


def release_dsfa(
    assessment: DsfaAssessment,
    *,
    releaser_id: str,
    dsb_override_justification: str | None = None,
) -> None:
    """Vier-Augen-Freigabe; die Fassung wird danach gesperrt."""
    _pruefe_offen(assessment)
    if not assessment.human_decision:
        raise ValueError("Menschliche Entscheidung fehlt")
    if not assessment.dsb_statement or not assessment.dsb_vote:
        raise ValueError("DSB-Beteiligung fehlt (Art. 35 Abs. 2 DSGVO)")

    if assessment.human_decision == "durchfuehren":
        if not assessment.necessity.strip() or not assessment.proportionality.strip():
            raise ValueError(
                "Bewertung von Notwendigkeit und Verhältnismäßigkeit fehlt "
                "(Art. 35 Abs. 7 lit. b DSGVO)"
            )
        if not assessment.risk_scenarios:
            raise ValueError(
                "Mindestens ein Risikoszenario ist zu dokumentieren "
                "(Art. 35 Abs. 7 lit. c DSGVO)"
            )
        if not assessment.mitigation_measures:
            raise ValueError(
                "Mindestens eine Abhilfemaßnahme ist zu dokumentieren "
                "(Art. 35 Abs. 7 lit. d DSGVO)"
            )
        if (
            highest_residual_risk(assessment) == RESTRISIKO_KONSULTATION
            and assessment.authority_consultation is None
        ):
            raise ValueError(
                "Bei verbleibendem hohem Risiko ist vor der Verarbeitung die "
                "Aufsichtsbehörde zu konsultieren (Art. 36 Abs. 1 DSGVO)"
            )

    if assessment.dsb_vote == "ablehnend" and (
        len((dsb_override_justification or "").strip()) < MINDESTLAENGE_BEGRUENDUNG
    ):
        raise ValueError(
            "Das Votum der oder des Datenschutzbeauftragten ist ablehnend. Eine "
            "Freigabe setzt eine dokumentierte, substanzielle Begründung der "
            "abweichenden Entscheidung voraus."
        )

    if assessment.created_by == releaser_id:
        raise ValueError("Vier-Augen-Prinzip: Ersteller darf nicht selbst freigeben")

    if dsb_override_justification:
        assessment.dsb_statement = (
            f"{assessment.dsb_statement}\n\nAbweichende Freigabeentscheidung: "
            f"{dsb_override_justification}"
        )
    assessment.released_by = releaser_id
    assessment.released_at = _now()
    assessment.status = "freigegeben"
    assessment.locked = True


def requires_reassessment(assessment: DsfaAssessment, activity: ProcessingActivity) -> bool:
    return assessment.vvt_version != activity.vvt_version


def snapshot_differences(
    assessment: DsfaAssessment, activity: ProcessingActivity
) -> list[dict[str, Any]]:
    """Wesentliche Unterschiede zwischen Snapshot und aktuellem VVT-Stand."""
    aktuell = activity_snapshot(activity)
    vorher = assessment.activity_snapshot or {}
    unbeachtlich = {"vvt_version", "updated_at"}
    unterschiede = []
    for feld in sorted(set(vorher) | set(aktuell)):
        if feld in unbeachtlich:
            continue
        if vorher.get(feld) != aktuell.get(feld):
            unterschiede.append({
                "field": feld,
                "before": vorher.get(feld),
                "after": aktuell.get(feld),
            })
    return unterschiede


def start_reassessment(
    assessment: DsfaAssessment,
    activity: ProcessingActivity,
    *,
    new_id: str,
    actor_id: str,
) -> DsfaAssessment:
    """Legt die Folgefassung an; die bisherige wird abgelöst, nicht geändert.

    Antworten und Bewertungen werden übernommen, damit nicht alles neu zu
    erfassen ist. Die Unterschiede zur Vorfassung stehen im Vorschlag, damit
    sichtbar ist, was zu prüfen ist (Art. 35 Abs. 11 DSGVO).
    """
    if assessment.status == "abgeloest":
        raise ValueError("Diese Fassung ist bereits abgelöst")
    unterschiede = snapshot_differences(assessment, activity)
    nachfolger = DsfaAssessment(
        id=new_id,
        tenant_id=activity.tenant_id,
        activity_id=activity.id,
        vvt_version=activity.vvt_version,
        activity_snapshot=activity_snapshot(activity),
        screening_answers=dict(assessment.screening_answers),
        necessity=assessment.necessity,
        proportionality=assessment.proportionality,
        risk_scenarios=[dict(s) for s in assessment.risk_scenarios],
        mitigation_measures=[dict(m) for m in assessment.mitigation_measures],
        data_subject_view=assessment.data_subject_view,
        version=assessment.version + 1,
        created_by=actor_id,
        created_at=_now(),
        predecessor_id=assessment.id,
    )
    nachfolger.system_suggestion = {
        **evaluate_screening(nachfolger.screening_answers),
        "differences_to_predecessor": unterschiede,
    }
    assessment.status = "abgeloest"
    return nachfolger


def as_export_record(assessment: DsfaAssessment) -> dict[str, Any]:
    """Nachweisfassung der Abschätzung als einfaches Wörterbuch."""
    return asdict(assessment)
