from ..constants import SIP6800
from .base import BaseSpecBuilder


class SIP6800SpecBuilder(BaseSpecBuilder):
    fork: str = SIP6800

    @classmethod
    def imports(cls, preset_name: str):
        return f"""
from sil2spec.deneb import {preset_name} as deneb
from sil2spec.utils.ssz.ssz_typing import Bytes31
"""
