"""Strukturelle Guardrails für das Framework-Repository.

Der Prüfer bestätigt nicht nur die Existenz von Dateien, sondern gleicht die
Verträge unter ``contracts/`` gegen den Code ab. Ohne diesen Abgleich driften
Vertrag und Modell auseinander, ohne dass eine Prüfung anschlägt.

Bewusst ohne YAML-Abhängigkeit: der Kern bleibt dependency-arm, deshalb liest
``_read_list_block`` nur die hier benötigte, flache Listenstruktur.
"""

from __future__ import annotations

import re
from pathlib import Path

if __package__:
    from .validate_content import validate_register
else:
    from validate_content import validate_register

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = (
    "docs/start.md", "docs/adr/ADR-004-inhalts-framework.md",
    "vorlagen/projekt.md", "vorlagen/datenschutz.md", "vorlagen/landing.md",
    "prompts/entwicklung.md", "prompts/review.md", "beispiele/raumbuchung.md",
    "docs/pflege-und-nachnutzung.md",
    "AGENTS.md", "CLAUDE.md", "CODEX.md", "GEMINI.md", "docs/anforderungen.md",
    "docs/processmodell.md", "docs/dsfa-werkzeug.md", "docs/security/bsi-baseline.md",
    "docs/rollen-und-rechte.md", "docs/akte-und-exporte.md",
    "contracts/process.yaml", "contracts/privacy.yaml", "skills/fachanwendung/SKILL.md",
"INHALTSVERSION", "docs/verbindlichkeit.md", "docs/administration.md",
    "docs/pruefkatalog.md", "docs/ki-arbeitsablauf.md",
    "vorlagen/anwendbarkeit.md", "vorlagen/testplan.md", "vorlagen/release.md",
    "beispiele/raumbuchung/README.md", "beispiele/raumbuchung/spezifikation.md",
    "beispiele/raumbuchung/anwendbarkeit.md", "beispiele/raumbuchung/datenschutz.md",
    "beispiele/raumbuchung/testplan.md", "beispiele/raumbuchung/landing.md",
    "archiv/README.md", ".github/CODEOWNERS",
    "docs/standards.md", "docs/standards-register.json", "docs/barrierefreiheit.md",
    "docs/security/sicherheitsvorfaelle.md", "docs/security/lieferkette.md",
    "vorlagen/standardsnachweis.md", "vorlagen/barrierefreiheit.md",
    "vorlagen/sicherheitsvorfall.md", "vorlagen/sbom.md",
    "vorlagen/nutzungsrechte.md", "vorlagen/entscheidungen.md",
    "skills/standards-pruefung/SKILL.md",
    "beispiele/raumbuchung/standards-und-nachweise.md",
)

AGENTS_TERMS = ("Mandantentrennung", "serverseitig", "Vier-Augen-Prinzip", "VVT", "DSFA")

#: Einstiegsdateien der Agenten. Sie dürfen keine eigenen Regeln aufstellen,
#: sondern nur auf AGENTS.md verweisen (Regel aus AGENTS.md selbst).
AGENT_ENTRYPOINTS = ("CLAUDE.md", "CODEX.md", "GEMINI.md")


def _read_list_block(text: str, parent: str, child: str) -> list[str]:
    """Liest die Einträge einer verschachtelten YAML-Liste ``parent: child: -``."""
    zeilen = text.splitlines()
    in_parent = False
    in_child = False
    eintraege: list[str] = []
    for zeile in zeilen:
        if re.match(rf"^{re.escape(parent)}:\s*$", zeile):
            in_parent = True
            continue
        if in_parent and re.match(r"^\S", zeile):
            break
        if in_parent and re.match(rf"^\s{{2}}{re.escape(child)}:\s*$", zeile):
            in_child = True
            continue
        if in_child:
            treffer = re.match(r"^\s{4}-\s*(\S+)", zeile)
            if treffer:
                eintraege.append(treffer.group(1))
            elif zeile.strip() and not zeile.strip().startswith("#"):
                break
    return eintraege


def _dataclass_fields(source: str, klasse: str) -> set[str]:
    """Feldnamen einer Dataclass aus dem Quelltext, ohne Import."""
    muster = re.compile(rf"^@dataclass\s*\nclass {re.escape(klasse)}[^\n]*:\n", re.M)
    treffer = muster.search(source)
    if not treffer:
        return set()
    rest = source[treffer.end():]
    ende = re.search(r"^@dataclass", rest, re.M)
    block = rest[: ende.start()] if ende else rest
    return set(re.findall(r"^    ([a-z_][a-z0-9_]*)\s*:", block, re.M))


def _fehlt(pfade: tuple[str, ...]) -> list[str]:
    return [p for p in pfade if not (ROOT / p).is_file()]


def main() -> int:
    fehler: list[str] = validate_register(ROOT)

    missing = _fehlt(REQUIRED)
    if missing:
        fehler.append("Fehlende Framework-Bausteine:\n" + "\n".join(f"  - {p}" for p in missing))

    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    fehlende_begriffe = [t for t in AGENTS_TERMS if t not in agents]
    if fehlende_begriffe:
        fehler.append(f"AGENTS.md fehlt: {', '.join(fehlende_begriffe)}")

    # Die Einstiege dürfen keine abweichenden Regeln enthalten.
    for name in AGENT_ENTRYPOINTS:
        pfad = ROOT / name
        if not pfad.is_file():
            continue
        text = pfad.read_text(encoding="utf-8")
        if "AGENTS.md" not in text:
            fehler.append(f"{name} verweist nicht auf AGENTS.md")
        if len(text.splitlines()) > 20:
            fehler.append(
                f"{name} ist zu umfangreich für einen Einstieg — Regeln gehören in AGENTS.md"
            )

    # Vertrag gegen Modell: jedes Pflichtfeld muss es im Code geben.
    modelle = (ROOT / "framework/core/models.py").read_text(encoding="utf-8")
    privacy = (ROOT / "contracts/privacy.yaml").read_text(encoding="utf-8")
    abgleich = (
        ("verarbeitungsverzeichnis", "ProcessingActivity"),
        ("dsfa", "DsfaAssessment"),
    )
    for dokument, klasse in abgleich:
        gefordert = _read_list_block(privacy, "required_fields", dokument)
        if not gefordert:
            fehler.append(f"contracts/privacy.yaml: keine Pflichtfelder für {dokument}")
            continue
        vorhanden = _dataclass_fields(modelle, klasse)
        fehlend = [f for f in gefordert if f not in vorhanden]
        if fehlend:
            fehler.append(
                f"{klasse} fehlen vertraglich zugesagte Felder: {', '.join(fehlend)}"
            )

    # Prozessvertrag gegen Statusmaschine.
    prozess_quelle = (ROOT / "framework/core/process.py").read_text(encoding="utf-8")
    codestatus = set(re.findall(r'^    "([a-z_]+)": "', prozess_quelle, re.M))
    prozess_vertrag = (ROOT / "contracts/process.yaml").read_text(encoding="utf-8")
    statusblock = re.search(r"^statuses:\s*$(.*?)^\S", prozess_vertrag, re.M | re.S)
    vertragstatus = set(
        re.findall(r"^  - id:\s*(\S+)", statusblock.group(1), re.M) if statusblock else []
    )
    if codestatus and vertragstatus and codestatus != vertragstatus:
        nur_code = sorted(codestatus - vertragstatus)
        nur_vertrag = sorted(vertragstatus - codestatus)
        fehler.append(
            "Status weichen ab — nur im Code: "
            f"{nur_code or '—'}; nur im Vertrag: {nur_vertrag or '—'}"
        )

    # Framework-Version: pyproject und Code müssen übereinstimmen.
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    init = (ROOT / "framework/__init__.py").read_text(encoding="utf-8")
    v_pyproject = re.search(r'^version\s*=\s*"([^"]+)"', pyproject, re.M)
    v_code = re.search(r'^__version__\s*=\s*"([^"]+)"', init, re.M)
    if not v_pyproject or not v_code:
        fehler.append("Framework-Version ist nicht in pyproject.toml und framework/__init__.py gesetzt")
    elif v_pyproject.group(1) != v_code.group(1):
        fehler.append(
            f"Framework-Version weicht ab: pyproject {v_pyproject.group(1)} "
            f"gegen Code {v_code.group(1)}"
        )

    # Fachdomänen bleiben außerhalb des generischen Frameworks.
    verboten = ("kpang", "kraftstoff", "tankstelle", "bussgeld", "bußgeld")
    for pfad in ROOT.rglob("*"):
        if (not pfad.is_file() or ".git" in pfad.parts or "graphify-out" in pfad.parts
                or any(part in pfad.parts for part in ("archiv", "node_modules", ".venv", "__pycache__"))
                or pfad == ROOT / "checks/validate_repo.py"):
            continue
        try:
            text = pfad.read_text(encoding="utf-8").lower()
        except UnicodeDecodeError:
            continue
        if any(term in text for term in verboten):
            fehler.append(f"Fachdomänenbezug in generischem Framework: {pfad.relative_to(ROOT)}")

    if fehler:
        print("Prüfung fehlgeschlagen:")
        for eintrag in fehler:
            print(f"- {eintrag}")
        return 1

    print(
        f"Framework-Struktur vollständig: {len(REQUIRED)} Pflichtdateien, "
        "Verträge stimmen mit Modell und Statusmaschine überein; "
        "Standardszuordnungen konsistent (kein Konformitätsnachweis)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
