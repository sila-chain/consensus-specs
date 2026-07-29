"""Narrow identity helpers for Sila consensus-specs generation.

External preset/config identity remains hyphenated where that is the
canonical network/path name. Python module/import tokens must be valid
identifiers, so only the proven mapping below is applied at generation
and import-emission sites.
"""

from __future__ import annotations

# Canonical external identity -> Python module/import token.
# Do NOT broadly accept arbitrary hyphenated names.
IDENTIFIER_SAFE_EXTERNAL_TO_MODULE: dict[str, str] = {
    "sila-mainnet": "sila_mainnet",
}


def python_module_token(external_name: str) -> str:
    """Return the Python module/import token for an external preset name.

    - Alphanumeric names (e.g. ``minimal``) pass through unchanged.
    - Only the locked external identity ``sila-mainnet`` maps to
      ``sila_mainnet``.
    - Any other non-alphanumeric name is rejected (no general hyphen
      acceptance broadening).
    """
    if external_name in IDENTIFIER_SAFE_EXTERNAL_TO_MODULE:
        return IDENTIFIER_SAFE_EXTERNAL_TO_MODULE[external_name]
    if external_name.isalnum() and external_name.isidentifier():
        return external_name
    raise ValueError(
        "invalid target name for Python module token "
        f"(must be alphanumeric or a locked mapped identity): {external_name!r}"
    )


def is_allowed_external_target_name(name: str) -> bool:
    """Validate external build-target names without broad hyphen acceptance."""
    return name.isalnum() or name in IDENTIFIER_SAFE_EXTERNAL_TO_MODULE
