from .constants import (
    ALL_PHASES,
    MINIMAL,
    SILA_MAINNET,
    SIP7441,
)
from .typing import (
    PresetBaseName,
    Spec,
    SpecForkName,
)

# NOTE: special case like `ALLOWED_TEST_RUNNER_FORKS`
ALL_EXECUTABLE_SPEC_NAMES = ALL_PHASES + (SIP7441,)

# import the spec for each fork and preset
for fork in ALL_EXECUTABLE_SPEC_NAMES:
    exec(
        f"from sil2spec.{fork} import sila_mainnet as spec_{fork}_sila_mainnet, minimal as spec_{fork}_minimal"
    )

# this is the only output of this file
spec_targets: dict[PresetBaseName, dict[SpecForkName, Spec]] = {
    MINIMAL: {fork: eval(f"spec_{fork}_minimal") for fork in ALL_EXECUTABLE_SPEC_NAMES},
    SILA_MAINNET: {fork: eval(f"spec_{fork}_sila_mainnet") for fork in ALL_EXECUTABLE_SPEC_NAMES},
}
