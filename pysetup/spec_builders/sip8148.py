from pysetup.constants import SIP8148

from .base import BaseSpecBuilder


class SIP8148SpecBuilder(BaseSpecBuilder):
    fork: str = SIP8148

    @classmethod
    def imports(cls, preset_name: str):
        return f"""
from sil_consensus_specs.heze import {preset_name} as heze
"""
