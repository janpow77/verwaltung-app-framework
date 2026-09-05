"""In-memory-Referenz für VVT-Versionierung und DSFA-Neubewertung."""

from __future__ import annotations

from dataclasses import replace

from .models import ProcessingActivity


class VvtRegistry:
    """Kleine Referenzimplementierung; produktiv durch DB-Service ersetzen."""

    def __init__(self) -> None:
        self._activities: dict[tuple[str, str], ProcessingActivity] = {}

    def register(self, activity: ProcessingActivity) -> ProcessingActivity:
        key = (activity.tenant_id, activity.id)
        if key in self._activities:
            raise ValueError("Tätigkeits-ID ist im Mandanten bereits vorhanden")
        self._activities[key] = replace(activity)
        return replace(activity)

    def get(self, tenant_id: str, activity_id: str) -> ProcessingActivity:
        try:
            return replace(self._activities[(tenant_id, activity_id)])
        except KeyError as exc:
            raise KeyError("Verarbeitungstätigkeit nicht gefunden") from exc

    def update(self, activity: ProcessingActivity) -> ProcessingActivity:
        key = (activity.tenant_id, activity.id)
        if key not in self._activities:
            raise KeyError("Verarbeitungstätigkeit nicht gefunden")
        current = self._activities[key]
        updated = replace(activity, vvt_version=current.vvt_version + 1)
        self._activities[key] = updated
        return replace(updated)

