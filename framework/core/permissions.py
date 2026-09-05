"""Rollen- und Berechtigungsvertrag; die produktive API muss ihn erzwingen."""

ROLE_PERMISSIONS: dict[str, set[str]] = {
    "plattform_admin": {
        "tenant:admin", "user:admin", "role:admin", "project:read", "project:write",
        "project:release", "audit:read", "privacy:read", "privacy:write", "privacy:release",
        "security:review", "export:all",
    },
    "mandant_admin": {
        "user:admin", "project:read", "project:write", "project:release", "audit:read",
        "privacy:read", "privacy:write", "export:all",
    },
    "fachverantwortung": {"project:read", "project:write", "privacy:read", "export:project"},
    "entwickler": {"project:read", "project:write", "privacy:read", "export:project"},
    "datenschutz": {"project:read", "privacy:read", "privacy:write", "privacy:release", "export:privacy"},
    "sicherheitspruefung": {"project:read", "security:review", "export:project"},
    "freigabe": {"project:read", "project:release", "privacy:read", "privacy:release", "export:all"},
    "auditor": {"project:read", "audit:read", "privacy:read", "export:project"},
    "lesezugriff": {"project:read"},
}


def has_permission(roles: list[str], permission: str) -> bool:
    return any(permission in ROLE_PERMISSIONS.get(role, set()) for role in roles)


def can_access_tenant(user_tenant_ids: list[str], tenant_id: str, roles: list[str]) -> bool:
    return "plattform_admin" in roles or tenant_id in user_tenant_ids

