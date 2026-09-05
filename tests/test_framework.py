import unittest

from framework.core.dsfa import (
    MINDESTLAENGE_BEGRUENDUNG,
    SCREENING_CRITERIA,
    ScreeningCriterion,
    add_mitigation_measure,
    add_risk_scenario,
    create_dsfa,
    evaluate_screening,
    highest_residual_risk,
    katalog,
    record_authority_consultation,
    release_dsfa,
    requires_reassessment,
    set_dsb_statement,
    set_human_decision,
    set_necessity,
    snapshot_differences,
    start_reassessment,
)
from framework.core.models import ProcessingActivity, ProjectCase
from framework.core.permissions import can_access_tenant, has_permission
from framework.core.process import GateContext, mark_reassessment_required, transition
from framework.core.vvt import VvtRegistry
from framework.export.basic import ExportContext, entschaerfe, export_csv, export_json


def activity(**overrides) -> ProcessingActivity:
    daten = dict(
        id="taet-1", tenant_id="mandant-a", project_id="projekt-1", name="Antragsbearbeitung",
        purpose="Anträge bearbeiten", legal_basis="Art. 6 Abs. 1 lit. e DSGVO",
        affected_persons=["Antragstellende"], data_categories=["Kontaktdaten"],
        recipients=["Fachreferat"], retention="nach Aufbewahrungskonzept",
        security_measures=["Rollen", "Audit"],
    )
    daten.update(overrides)
    return ProcessingActivity(**daten)


def context() -> ExportContext:
    return ExportContext(tenant_id="mandant-a", actor_id="u-1", project_id="projekt-1")


def vollstaendige_dsfa(assessment_id="dsfa-1", created_by="u-1"):
    """DSFA mit allen Pflichtbestandteilen nach Art. 35 Abs. 7 lit. a bis d."""
    assessment = create_dsfa(
        activity(), assessment_id=assessment_id, created_by=created_by,
        answers={"sensible_daten": True, "systematische_beobachtung": True},
    )
    set_necessity(
        assessment,
        necessity="Ohne die Verarbeitung ist der Antrag nicht zu bescheiden.",
        proportionality="Mildere Mittel wurden geprüft und sind nicht geeignet.",
    )
    add_risk_scenario(
        assessment, description="Unbefugte Kenntnisnahme der Antragsdaten",
        severity="mittel", likelihood="gering", residual_risk="gering",
    )
    add_mitigation_measure(
        assessment, description="Rollenbasierter Zugriff mit Protokollierung",
        addresses="Unbefugte Kenntnisnahme", responsible="Fachreferat",
    )
    set_human_decision(assessment, decision="durchfuehren", actor_id="u-3")
    set_dsb_statement(assessment, statement="Der DSB hat die Bewertung geprüft.", vote="zustimmend")
    return assessment


class ProzessTests(unittest.TestCase):
    def test_eigeninitiative_folgt_framework_first(self):
        project = ProjectCase("projekt-1", "mandant-a", "Test", "u-1", "eigeninitiative")
        transition(project, "framework_start", GateContext(actor_id="u-1"))
        transition(project, "in_entwicklung", GateContext(actor_id="u-1"))
        transition(project, "vorstellung", GateContext(actor_id="u-1"))
        self.assertEqual(project.status, "vorstellung")
        self.assertEqual(len(project.chronology), 3)

    def test_release_requires_gates_and_second_person(self):
        project = ProjectCase("p", "t", "Test", "u-1", "hausbedarf", status="sicherheitspruefung")
        ctx = GateContext(actor_id="u-1", has_vvt=True, dsfa_required=True,
                          dsfa_released=True, tests_passed=True, security_passed=True,
                          fachlich_approved=True)
        transition(project, "freigabevorlage", ctx)
        with self.assertRaisesRegex(ValueError, "Vier-Augen"):
            transition(project, "freigegeben", ctx)
        ctx.second_actor_id = "u-2"
        ctx.dsb_involved = True
        transition(project, "freigegeben", ctx)
        self.assertEqual(project.status, "freigegeben")

    def test_unerlaubter_uebergang_wird_abgewiesen(self):
        project = ProjectCase("p", "t", "Test", "u-1", "hausbedarf", status="in_entwicklung")
        with self.assertRaisesRegex(ValueError, "nicht erlaubt"):
            transition(project, "freigegeben", GateContext(actor_id="u-1"))

    def test_unbekannter_zielstatus_wird_abgewiesen(self):
        project = ProjectCase("p", "t", "Test", "u-1", "hausbedarf")
        with self.assertRaisesRegex(ValueError, "Unbekannter Status"):
            transition(project, "erledigt", GateContext(actor_id="u-1"))

    def test_rueckgabe_und_abbruch_ohne_begruendung_scheitern(self):
        for ziel in ("zurueckgegeben", "abgebrochen"):
            project = ProjectCase("p", "t", "Test", "u-1", "hausbedarf", status="in_entwicklung")
            with self.assertRaisesRegex(ValueError, "Begründung"):
                transition(project, ziel, GateContext(actor_id="u-1"))

    def test_change_starts_reassessment(self):
        project = ProjectCase("p", "t", "Test", "u", "hausbedarf", status="betrieb")
        mark_reassessment_required(project, "u-2", "Neue Datenkategorie")
        self.assertEqual(project.status, "neubewertung")


class SchwellwertTests(unittest.TestCase):
    def test_katalog_kennt_harte_ausloeser_mit_fundstelle(self):
        harte = [k for k in katalog() if k.effect == "hart"]
        self.assertEqual(len(harte), 3)
        self.assertTrue(all(k.source.startswith("Art. 35 Abs. 3") for k in harte))
        self.assertEqual(len(SCREENING_CRITERIA), 9)

    def test_harter_ausloeser_ergibt_pflicht_unabhaengig_von_der_punktzahl(self):
        ergebnis = evaluate_screening({"umfangreiche_besondere_kategorien": True})
        self.assertTrue(ergebnis["dsfa_recommended"])
        self.assertEqual(ergebnis["score"], 0)
        self.assertIn("Art. 35 Abs. 3 lit. b DSGVO", ergebnis["reason"])

    def test_screening_weist_nicht_boolesche_antworten_zurueck(self):
        for wert in ("true", 1, None):
            with self.assertRaisesRegex(ValueError, "True oder False"):
                evaluate_screening({"sensible_daten": wert})

    def test_screening_weist_unbekannte_kriterien_zurueck(self):
        with self.assertRaisesRegex(ValueError, "Unbekannte Schwellwertkriterien"):
            evaluate_screening({"sensible_date": True})

    def test_erklaertext_nennt_die_gesamtzahl_der_kriterien(self):
        ergebnis = evaluate_screening(
            {k: True for k in ("sensible_daten", "automatisierte_entscheidung",
                               "schutzbeduerftige_personen")}
        )
        self.assertIn("3 der 9 Kriterien", ergebnis["reason"])
        self.assertNotIn("3 von 2", ergebnis["reason"])

    def test_muss_liste_ist_nachtragbar(self):
        from framework.core import dsfa as modul
        eintrag = ScreeningCriterion(
            key="muss_liste_probe", text="Beispiel", source="Muss-Liste Nr. 1", effect="hart"
        )
        modul.ergaenze_muss_liste([eintrag])
        try:
            self.assertTrue(evaluate_screening({"muss_liste_probe": True})["dsfa_recommended"])
        finally:
            modul._muss_liste.remove(eintrag)


class DsfaTests(unittest.TestCase):
    def test_dsfa_snapshot_and_four_eyes(self):
        assessment = vollstaendige_dsfa()
        self.assertTrue(assessment.system_suggestion["dsfa_recommended"])
        with self.assertRaisesRegex(ValueError, "Vier-Augen"):
            release_dsfa(assessment, releaser_id="u-1")
        release_dsfa(assessment, releaser_id="u-2")
        self.assertTrue(assessment.locked)
        self.assertIsNotNone(assessment.released_at)
        self.assertTrue(requires_reassessment(assessment, activity(vvt_version=2)))

    def test_entscheidung_ist_einer_person_zugeordnet(self):
        assessment = vollstaendige_dsfa()
        self.assertEqual(assessment.decided_by, "u-3")
        self.assertIsNotNone(assessment.decided_at)

    def test_deviation_requires_justification(self):
        assessment = create_dsfa(
            activity(), assessment_id="dsfa-2", created_by="u-1",
            answers={"sensible_daten": True, "automatisierte_entscheidung": True},
        )
        with self.assertRaisesRegex(ValueError, "Begründung"):
            set_human_decision(assessment, decision="nicht_erforderlich", actor_id="u-1",
                               deviation_justification="zu kurz")

    def test_begruendung_auch_bei_abweichung_nach_oben(self):
        assessment = create_dsfa(activity(), assessment_id="d", created_by="u-1", answers={})
        self.assertFalse(assessment.system_suggestion["dsfa_recommended"])
        with self.assertRaisesRegex(ValueError, "Begründung"):
            set_human_decision(assessment, decision="durchfuehren", actor_id="u-1")
        set_human_decision(
            assessment, decision="durchfuehren", actor_id="u-1",
            deviation_justification="x" * MINDESTLAENGE_BEGRUENDUNG,
        )
        self.assertTrue(assessment.deviates_from_suggestion)

    def test_freigabe_ohne_risikoszenarien_scheitert(self):
        assessment = create_dsfa(
            activity(), assessment_id="d", created_by="u-1", answers={"sensible_daten": True,
                                                                     "systematische_beobachtung": True},
        )
        set_necessity(assessment, necessity="erforderlich", proportionality="verhältnismäßig")
        set_human_decision(assessment, decision="durchfuehren", actor_id="u-3")
        set_dsb_statement(assessment, statement="geprüft", vote="zustimmend")
        with self.assertRaisesRegex(ValueError, "lit. c"):
            release_dsfa(assessment, releaser_id="u-2")

    def test_freigabe_ohne_massnahmen_scheitert(self):
        assessment = vollstaendige_dsfa()
        assessment.mitigation_measures.clear()
        with self.assertRaisesRegex(ValueError, "lit. d"):
            release_dsfa(assessment, releaser_id="u-2")

    def test_freigabe_ohne_notwendigkeitspruefung_scheitert(self):
        assessment = vollstaendige_dsfa()
        assessment.necessity = ""
        with self.assertRaisesRegex(ValueError, "lit. b"):
            release_dsfa(assessment, releaser_id="u-2")

    def test_ablehnendes_dsb_votum_blockiert_freigabe(self):
        assessment = vollstaendige_dsfa()
        set_dsb_statement(assessment, statement="Der DSB lehnt ab.", vote="ablehnend")
        with self.assertRaisesRegex(ValueError, "ablehnend"):
            release_dsfa(assessment, releaser_id="u-2")
        release_dsfa(assessment, releaser_id="u-2",
                     dsb_override_justification="Die Leitung trägt das Restrisiko ausdrücklich.")
        self.assertTrue(assessment.locked)

    def test_hohes_restrisiko_verlangt_konsultation(self):
        assessment = vollstaendige_dsfa()
        add_risk_scenario(assessment, description="Offenlegung besonderer Kategorien",
                          severity="hoch", likelihood="mittel", residual_risk="hoch")
        self.assertEqual(highest_residual_risk(assessment), "hoch")
        with self.assertRaisesRegex(ValueError, "Art. 36"):
            release_dsfa(assessment, releaser_id="u-2")
        record_authority_consultation(assessment, authority="HBDI", result="keine Einwände")
        release_dsfa(assessment, releaser_id="u-2")
        self.assertEqual(assessment.status, "freigegeben")

    def test_gesperrte_dsfa_weist_jede_aenderung_ab(self):
        assessment = vollstaendige_dsfa()
        release_dsfa(assessment, releaser_id="u-2")
        with self.assertRaisesRegex(ValueError, "gesperrt"):
            set_human_decision(assessment, decision="nicht_erforderlich", actor_id="u-1")
        with self.assertRaisesRegex(ValueError, "gesperrt"):
            set_dsb_statement(assessment, statement="neu", vote="ablehnend")
        with self.assertRaisesRegex(ValueError, "gesperrt"):
            add_risk_scenario(assessment, description="x", severity="hoch",
                              likelihood="hoch", residual_risk="hoch")

    def test_neubewertung_erzeugt_folgefassung_und_loest_ab(self):
        assessment = vollstaendige_dsfa()
        release_dsfa(assessment, releaser_id="u-2")
        geaendert = activity(vvt_version=2, data_categories=["Kontaktdaten", "Gesundheitsdaten"])
        nachfolger = start_reassessment(assessment, geaendert, new_id="dsfa-1b", actor_id="u-4")
        self.assertEqual(assessment.status, "abgeloest")
        self.assertEqual(nachfolger.predecessor_id, "dsfa-1")
        self.assertEqual(nachfolger.version, 2)
        self.assertFalse(nachfolger.locked)
        unterschiede = nachfolger.system_suggestion["differences_to_predecessor"]
        self.assertEqual([u["field"] for u in unterschiede], ["data_categories"])

    def test_snapshot_bleibt_bei_vvt_aenderung_unveraendert(self):
        assessment = vollstaendige_dsfa()
        geaendert = activity(vvt_version=2, purpose="Anderer Zweck")
        self.assertEqual(assessment.activity_snapshot["purpose"], "Anträge bearbeiten")
        self.assertEqual(len(snapshot_differences(assessment, geaendert)), 1)


class VvtTests(unittest.TestCase):
    def test_vvt_update_increments_version(self):
        registry = VvtRegistry()
        eintrag = registry.register(activity())
        eintrag.purpose = "Geänderter Zweck"
        updated = registry.update(eintrag)
        self.assertEqual(updated.vvt_version, 2)
        self.assertEqual(registry.get("mandant-a", "taet-1").vvt_version, 2)

    def test_registry_trennt_gleiche_taetigkeits_id_in_zwei_mandanten(self):
        registry = VvtRegistry()
        registry.register(activity())
        registry.register(activity(tenant_id="mandant-b", purpose="Anderer Zweck"))
        self.assertEqual(registry.get("mandant-a", "taet-1").purpose, "Anträge bearbeiten")
        self.assertEqual(registry.get("mandant-b", "taet-1").purpose, "Anderer Zweck")

    def test_verzeichnis_deckt_artikel_30_ab(self):
        eintrag = activity()
        for feld in ("legal_basis", "third_country_transfer", "third_country_safeguards",
                     "retention_legal_basis", "controller", "processing_agreement",
                     "joint_controllers"):
            self.assertTrue(hasattr(eintrag, feld), f"Art.-30-Feld fehlt: {feld}")


class RechteUndExportTests(unittest.TestCase):
    def test_permissions(self):
        self.assertTrue(has_permission(["datenschutz"], "privacy:write"))
        self.assertFalse(has_permission(["lesezugriff"], "project:write"))
        self.assertFalse(has_permission(["entwickler"], "project:release"))
        self.assertFalse(can_access_tenant(["a"], "b", ["entwickler"]))

    def test_export_enthaelt_pflichtmetadaten(self):
        ausgabe = export_json(activity(), context=context())
        self.assertIn('"framework_version"', ausgabe)
        self.assertIn('"exported_by": "u-1"', ausgabe)
        self.assertIn('"tenant_id": "mandant-a"', ausgabe)
        self.assertIn('"checksum": "sha256:', ausgabe)

    def test_export_ohne_ausloesende_person_scheitert(self):
        with self.assertRaisesRegex(ValueError, "auslösende Person"):
            ExportContext(tenant_id="mandant-a", actor_id="  ")

    def test_csv_export_enthaelt_alle_spalten_heterogener_zeilen(self):
        ausgabe = export_csv(
            [{"id": "p", "name": "Test"}, {"id": "q", "zusatz": "wichtig"}],
            context=context(), with_metadata=False,
        )
        self.assertIn("id,name,zusatz", ausgabe)
        self.assertIn("wichtig", ausgabe)

    def test_csv_export_entschaerft_fuehrende_formelzeichen(self):
        ausgabe = export_csv([{"bemerkung": "=cmd|'/C calc'!A0"}],
                             context=context(), with_metadata=False)
        self.assertIn("'=cmd", ausgabe)
        self.assertEqual(entschaerfe("+42"), "'+42")
        self.assertEqual(entschaerfe("harmlos"), "harmlos")


if __name__ == "__main__":
    unittest.main()
