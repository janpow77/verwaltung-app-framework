"""Prüft Nachweisverknüpfungen, nicht die Erfüllung externer Standards."""

from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path


def parse_test_catalog(text: str) -> tuple[dict[str, set[str]], list[str]]:
    """Eindeutige Fall-IDs samt ausdrücklich genannten F-Bezügen lesen."""
    cases: dict[str, set[str]] = {}
    errors: list[str] = []
    for case, body in re.findall(r"^\| ([TA]-\d{2}) \|([^\n]+)", text, re.M):
        if case in cases:
            errors.append(f"Doppelte Prüffall-ID: {case}")
        cases[case] = set(re.findall(r"\bF-\d{2}\b", body))
    return cases, errors


def validate_register(root: Path, register: dict | None = None) -> list[str]:
    """Optionaler Registerparameter erlaubt isolierte negative Tests."""
    errors: list[str] = []
    try:
        data = register if register is not None else json.loads(
            (root / "docs/standards-register.json").read_text(encoding="utf-8")
        )
        if not isinstance(data, dict):
            return ["Standardsregister muss ein Objekt sein"]
        if data.get("schema_version") != 1:
            errors.append("Unbekannte Register-Schemafassung")
        if data.get("content_version") != (root / "INHALTSVERSION").read_text().strip():
            errors.append("Register und Inhaltsversion weichen ab")
        try:
            reviewed = date.fromisoformat(data["reviewed_at"])
            due = date.fromisoformat(data["review_due"])
            if due <= reviewed:
                errors.append("Wiedervorlage muss nach der Quellenprüfung liegen")
        except (KeyError, TypeError, ValueError):
            errors.append("Ungültige Prüfdaten im Standardsregister")

        def local_file(value: object) -> Path | None:
            if not isinstance(value, str) or not value or Path(value).is_absolute():
                errors.append(f"Ungültiger lokaler Nachweispfad: {value!r}")
                return None
            path = (root / value).resolve()
            if not path.is_relative_to(root.resolve()) or not path.is_file():
                errors.append(f"Fehlender oder repo-fremder Nachweispfad: {value}")
                return None
            return path

        source_file = local_file(data.get("sources_document"))
        source_text = source_file.read_text(encoding="utf-8") if source_file else ""
        sources = data.get("sources")
        if (not isinstance(sources, list) or not sources
                or any(not isinstance(s, str) for s in sources)):
            return errors + ["Quellenliste fehlt oder ist ungültig"]
        source_ids = set(re.findall(r"^\| (S-\d+) \|", source_text, re.M))
        if len(set(sources)) != len(sources) or set(sources) != source_ids:
            errors.append("Quellen-IDs doppelt oder nicht deckungsgleich mit Quellenregister")

        requirements_text = (root / "docs/anforderungen.md").read_text(encoding="utf-8")
        requirements = set(re.findall(r"\bF-\d{2}\b", requirements_text))
        tests_text = (root / "docs/pruefkatalog.md").read_text(encoding="utf-8")
        tests_text += (root / "docs/barrierefreiheit.md").read_text(encoding="utf-8")
        cases, catalog_errors = parse_test_catalog(tests_text)
        errors.extend(catalog_errors)
        test_ids = set(cases)
        mappings = data.get("mappings")
        if not isinstance(mappings, list):
            return errors + ["Anforderungszuordnungen fehlen"]
        seen: set[str] = set()
        for row in mappings:
            if not isinstance(row, dict):
                errors.append("Ungültige Zuordnungszeile")
                continue
            req = row.get("requirement")
            if not isinstance(req, str) or req not in requirements or req in seen:
                errors.append(f"Unbekannte oder doppelte Anforderung: {req!r}")
            if isinstance(req, str):
                seen.add(req)
            for key, allowed in (("sources", source_ids), ("tests", test_ids)):
                refs = row.get(key)
                if (not isinstance(refs, list) or not refs
                        or any(not isinstance(ref, str) or ref not in allowed for ref in refs)):
                    errors.append(f"{req}: ungültige oder fehlende {key}-Referenz")
                elif key == "tests" and isinstance(req, str):
                    for ref in refs:
                        if cases[ref] and req not in cases[ref]:
                            errors.append(f"{req}: Prüffall {ref} gehört zu einer anderen Anforderung")
            local_file(row.get("evidence"))
        if seen != requirements:
            errors.append("Nicht alle F-Anforderungen sind eindeutig zugeordnet")
    except (OSError, ValueError) as exc:
        errors.append(f"Standardsregister nicht lesbar: {exc}")
    return errors
