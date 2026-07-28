from ..constants import SIP7928
from .base import BaseSpecBuilder


class SIP7928SpecBuilder(BaseSpecBuilder):
    fork: str = SIP7928

    @classmethod
    def imports(cls, preset_name: str):
        return f"""
from sil2spec.fulu import {preset_name} as fulu
"""
