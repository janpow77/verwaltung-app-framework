import copy
import json
import unittest
from pathlib import Path

from checks.validate_content import parse_test_catalog, validate_register


ROOT = Path(__file__).resolve().parents[1]


class ContentChecksTest(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "docs/standards-register.json").read_text())

    def test_real_register_is_consistent(self):
        self.assertEqual(validate_register(ROOT), [])

    def test_missing_requirement_is_rejected(self):
        self.data["mappings"].pop()
        self.assertTrue(validate_register(ROOT, self.data))

    def test_duplicate_requirement_is_rejected(self):
        self.data["mappings"].append(copy.deepcopy(self.data["mappings"][0]))
        self.assertTrue(validate_register(ROOT, self.data))

    def test_unknown_test_is_rejected(self):
        self.data["mappings"][0]["tests"] = ["T-999"]
        self.assertTrue(validate_register(ROOT, self.data))

    def test_existing_test_for_wrong_requirement_is_rejected(self):
        self.data["mappings"][0]["tests"] = ["T-21"]
        self.assertTrue(validate_register(ROOT, self.data))

    def test_duplicate_test_id_is_rejected(self):
        _, errors = parse_test_catalog(
            "| T-21 | F-11, Ansichten | erste Prüfung |\n"
            "| T-21 | F-08, Betrieb | andere Prüfung |\n"
        )
        self.assertTrue(errors)

    def test_test_catalog_preserves_requirement_relations(self):
        cases, errors = parse_test_catalog(
            "| T-36 | F-05/F-07/F-08, Betrieb | Übung |\n"
        )
        self.assertEqual(errors, [])
        self.assertEqual(cases["T-36"], {"F-05", "F-07", "F-08"})

    def test_unknown_source_is_rejected(self):
        self.data["mappings"][0]["sources"] = ["S-999"]
        self.assertTrue(validate_register(ROOT, self.data))

    def test_missing_evidence_is_rejected(self):
        self.data["mappings"][0]["evidence"] = "vorlagen/does-not-exist.md"
        self.assertTrue(validate_register(ROOT, self.data))

    def test_external_evidence_path_is_rejected(self):
        for path in ("../ki-pilotprogramm/README.md", "/etc/passwd"):
            with self.subTest(path=path):
                self.data["mappings"][0]["evidence"] = path
                self.assertTrue(validate_register(ROOT, self.data))

    def test_version_mismatch_is_rejected(self):
        self.data["content_version"] = "0.0.0"
        self.assertTrue(validate_register(ROOT, self.data))

    def test_invalid_review_dates_are_rejected(self):
        for value in ("invalid", "2026-01-01", None):
            with self.subTest(value=value):
                self.data["review_due"] = value
                self.assertTrue(validate_register(ROOT, self.data))

    def test_bad_mapping_types_are_rejected_without_crash(self):
        for value in (None, [], {}, 42):
            with self.subTest(value=value):
                self.data["mappings"][0]["requirement"] = value
                self.assertTrue(validate_register(ROOT, self.data))

    def test_empty_test_list_is_rejected(self):
        self.data["mappings"][0]["tests"] = []
        self.assertTrue(validate_register(ROOT, self.data))

    def test_duplicate_source_is_rejected(self):
        self.data["sources"].append(self.data["sources"][0])
        self.assertTrue(validate_register(ROOT, self.data))

    def test_unknown_schema_is_rejected(self):
        self.data["schema_version"] = 999
        self.assertTrue(validate_register(ROOT, self.data))


if __name__ == "__main__":
    unittest.main()
