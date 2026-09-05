"""Dependency-arme Exportfunktionen; PDF/DOCX können später Adapter werden.

Jeder Export trägt Mandant, Projekt, Zeitpunkt, Framework-Version, auslösende
Person und eine Prüfsumme über die Nutzdaten (docs/akte-und-exporte.md). Ein
Export ohne diese Angaben ist als Nachweis nicht verwendbar und wird daher
nicht angeboten.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
from dataclasses import asdict, dataclass, is_dataclass
from datetime import datetime, timezone
from typing import Any

from .. import __version__


#: Zeichen, mit denen eine Tabellenkalkulation den Zellinhalt als Formel liest.
FORMELZEICHEN = ("=", "+", "-", "@", "\t", "\r")


@dataclass(frozen=True)
class ExportContext:
    """Pflichtangaben zu jedem Export."""

    tenant_id: str
    actor_id: str
    project_id: str | None = None
    purpose: str = ""

    def __post_init__(self) -> None:
        if not self.tenant_id.strip():
            raise ValueError("Export benötigt eine Mandantenkennung")
        if not self.actor_id.strip():
            raise ValueError("Export benötigt die auslösende Person")


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _payload(value: Any) -> Any:
    return asdict(value) if is_dataclass(value) and not isinstance(value, type) else value


def _pruefsumme(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def _metadaten(context: ExportContext, pruefsumme: str) -> dict[str, Any]:
    return {
        "tenant_id": context.tenant_id,
        "project_id": context.project_id,
        "exported_by": context.actor_id,
        "exported_at": _now(),
        "framework_version": __version__,
        "purpose": context.purpose,
        "checksum": pruefsumme,
    }


def entschaerfe(wert: Any) -> Any:
    """Verhindert, dass eine Tabellenkalkulation den Zellinhalt als Formel liest.

    Freitext aus Anträgen landet ungefiltert in Arbeitslisten. Ohne diese
    Entschärfung ist ein Zellwert wie ``=cmd|'/C calc'!A0`` ein Ausführungsweg
    auf dem Arbeitsplatz der sachbearbeitenden Person.
    """
    if isinstance(wert, str) and wert.startswith(FORMELZEICHEN):
        return "'" + wert
    return wert


def export_json(value: Any, *, context: ExportContext) -> str:
    """Nachweisfähiger JSON-Export mit Metadatenkopf und Prüfsumme."""
    daten = _payload(value)
    rumpf = json.dumps(daten, ensure_ascii=False, indent=2, sort_keys=True)
    envelope = {"meta": _metadaten(context, _pruefsumme(rumpf)), "data": daten}
    return json.dumps(envelope, ensure_ascii=False, indent=2, sort_keys=True)


def _spalten(rows: list[dict[str, Any]], fields: list[str] | None) -> list[str]:
    """Vereinigung aller Schlüssel; die erste Zeile bestimmt die Reihenfolge.

    ``rows[0].keys()`` allein würde Spalten späterer Zeilen stillschweigend
    verwerfen — in einer Nachweisliste ist das Datenverlust.
    """
    if fields:
        return list(fields)
    spalten: list[str] = []
    for row in rows:
        for schluessel in row:
            if schluessel not in spalten:
                spalten.append(schluessel)
    return spalten


def export_csv(
    rows: list[dict[str, Any]],
    *,
    context: ExportContext,
    fields: list[str] | None = None,
    with_metadata: bool = True,
) -> str:
    """CSV-Export mit Spaltenvereinigung, Formelschutz und Metadatenblock."""
    spalten = _spalten(rows, fields)
    daten = io.StringIO(newline="")
    schreiber = csv.DictWriter(daten, fieldnames=spalten, extrasaction="ignore")
    schreiber.writeheader()
    for row in rows:
        schreiber.writerow({k: entschaerfe(row.get(k, "")) for k in spalten})
    rumpf = daten.getvalue()

    if not with_metadata:
        return rumpf

    kopf = io.StringIO(newline="")
    kopfschreiber = csv.writer(kopf)
    for schluessel, wert in _metadaten(context, _pruefsumme(rumpf)).items():
        kopfschreiber.writerow([f"# {schluessel}", entschaerfe(wert)])
    kopfschreiber.writerow([])
    return kopf.getvalue() + rumpf
