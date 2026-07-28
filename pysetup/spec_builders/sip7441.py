from ..constants import SIP7441
from .base import BaseSpecBuilder


class SIP7441SpecBuilder(BaseSpecBuilder):
    fork: str = SIP7441

    @classmethod
    def imports(cls, preset_name: str):
        return f"""
from sil2spec.capella import {preset_name} as capella
import curdleproofs
import json
"""

    @classmethod
    def hardcoded_ssz_dep_constants(cls) -> dict[str, str]:
        constants = {
            "EXECUTION_PAYLOAD_GINDEX": "GeneralizedIndex(41)",
        }
        return {**super().hardcoded_ssz_dep_constants(), **constants}
