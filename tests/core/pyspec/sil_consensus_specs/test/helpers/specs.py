from .constants import (
    ALL_PHASES,
    SILA_MAINNET,
    MINIMAL,
)
from .typing import (
    PresetBaseName,
    Spec,
    SpecForkName,
)

ALL_EXECUTABLE_SPEC_NAMES = ALL_PHASES

# import the spec for each fork and preset
for fork in ALL_EXECUTABLE_SPEC_NAMES:
    exec(
        f"from sil_consensus_specs.{fork} import sila_mainnet as spec_{fork}_sila_mainnet, minimal as spec_{fork}_minimal"
    )

# this is the only output of this file
spec_targets: dict[PresetBaseName, dict[SpecForkName, Spec]] = {
    MINIMAL: {fork: eval(f"spec_{fork}_minimal") for fork in ALL_EXECUTABLE_SPEC_NAMES},
    SILA_MAINNET: {fork: eval(f"spec_{fork}_sila_mainnet") for fork in ALL_EXECUTABLE_SPEC_NAMES},
}
