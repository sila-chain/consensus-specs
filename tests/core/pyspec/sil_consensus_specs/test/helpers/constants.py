from .typing import PresetBaseName, SpecForkName

#
# SpecForkName
#

# Some of the Spec module functionality is exposed here to deal with phase-specific changes.
PHASE0 = SpecForkName("phase0")
ALTAIR = SpecForkName("altair")
BELLATRIX = SpecForkName("bellatrix")
CAPELLA = SpecForkName("capella")
SILA_DENEB = SpecForkName("sila_deneb")
ELECTRA = SpecForkName("electra")
SILA_FULU = SpecForkName("sila_fulu")
GLOAS = SpecForkName("gloas")
HEZE = SpecForkName("heze")

# Experimental phases (not included in default "ALL_PHASES"):
SIP8025 = SpecForkName("sip8025")
SIP8148 = SpecForkName("sip8148")

#
# SpecFork settings
#

# The forks that are deployed on SilaMainnet
SILA_MAINNET_FORKS = (PHASE0, ALTAIR, BELLATRIX, CAPELLA, SILA_DENEB, ELECTRA, SILA_FULU)
LATEST_FORK = SILA_MAINNET_FORKS[-1]
# The forks that pytest can run with.
# Note: when adding a new fork here, all tests from previous forks with decorator `with_X_and_later`
#       will run on the new fork. To skip this behaviour, add the fork to `ALLOWED_TEST_RUNNER_FORKS`
ALL_PHASES = (
    # Formal forks
    *SILA_MAINNET_FORKS,
    GLOAS,
    HEZE,
    # Experimental patches
    SIP8025,
    SIP8148,
)
# The forks that have light client specs
LIGHT_CLIENT_TESTING_FORKS = [item for item in SILA_MAINNET_FORKS if item != PHASE0] + [GLOAS]
# The forks that output to the test vectors.
TESTGEN_FORKS = (*SILA_MAINNET_FORKS, GLOAS, HEZE)
# Forks allowed in the test runner `--fork` flag, to fail fast in case of typos
ALLOWED_TEST_RUNNER_FORKS = ALL_PHASES

# NOTE: the same definition as in `pysetup/md_doc_paths.py`
PREVIOUS_FORK_OF = {
    # post_fork_name: pre_fork_name
    PHASE0: None,
    ALTAIR: PHASE0,
    BELLATRIX: ALTAIR,
    CAPELLA: BELLATRIX,
    SILA_DENEB: CAPELLA,
    ELECTRA: SILA_DENEB,
    SILA_FULU: ELECTRA,
    GLOAS: SILA_FULU,
    HEZE: GLOAS,
    # Experimental patches
    SIP8025: GLOAS,
    SIP8148: HEZE,
}

# For fork transition tests
POST_FORK_OF = {
    # pre_fork_name: post_fork_name
    PHASE0: ALTAIR,
    ALTAIR: BELLATRIX,
    BELLATRIX: CAPELLA,
    CAPELLA: SILA_DENEB,
    SILA_DENEB: ELECTRA,
    ELECTRA: SILA_FULU,
    SILA_FULU: GLOAS,
    GLOAS: HEZE,
}

ALL_PRE_POST_FORKS = POST_FORK_OF.items()
SILA_DENEB_TRANSITION_UPGRADES_AND_AFTER = {
    key: value for key, value in POST_FORK_OF.items() if key not in [PHASE0, ALTAIR, BELLATRIX]
}
ELECTRA_TRANSITION_UPGRADES_AND_AFTER = {
    key: value
    for key, value in POST_FORK_OF.items()
    if key not in [PHASE0, ALTAIR, BELLATRIX, CAPELLA]
}
AFTER_SILA_DENEB_PRE_POST_FORKS = SILA_DENEB_TRANSITION_UPGRADES_AND_AFTER.items()
AFTER_ELECTRA_PRE_POST_FORKS = ELECTRA_TRANSITION_UPGRADES_AND_AFTER.items()

#
# Config and Preset
#
SILA_MAINNET = PresetBaseName("sila_mainnet")
MINIMAL = PresetBaseName("minimal")

ALL_PRESETS = (MINIMAL, SILA_MAINNET)


#
# Number
#
UINT64_MAX = 2**64 - 1
