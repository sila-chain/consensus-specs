from sil_consensus_specs.test.context import (
    spec_test,
    with_config_overrides,
    with_matching_spec_config,
    with_phases,
    with_presets,
    with_state,
)
from sil_consensus_specs.test.helpers.constants import (
    CAPELLA,
    SILA_DENEB,
    ELECTRA,
    SILA_FULU,
    GLOAS,
    MINIMAL,
)
from sil_consensus_specs.test.helpers.light_client_sync import (
    run_lc_sync_test_multi_fork,
    run_lc_sync_test_single_fork,
)


@with_phases(phases=[CAPELLA], other_phases=[SILA_DENEB])
@spec_test
@with_config_overrides(
    {
        "SILA_DENEB_FORK_EPOCH": 3,  # Test setup advances to epoch 2
    },
)
@with_state
@with_matching_spec_config(emitted_fork=SILA_DENEB)
@with_presets([MINIMAL], reason="too slow")
def test_sila_deneb_fork(spec, phases, state):
    yield from run_lc_sync_test_single_fork(spec, phases, state, SILA_DENEB)


@with_phases(phases=[CAPELLA], other_phases=[SILA_DENEB, ELECTRA])
@spec_test
@with_config_overrides(
    {
        "SILA_DENEB_FORK_EPOCH": 3,  # Test setup advances to epoch 2
        "ELECTRA_FORK_EPOCH": 4,
    },
)
@with_state
@with_matching_spec_config(emitted_fork=ELECTRA)
@with_presets([MINIMAL], reason="too slow")
def test_sila_deneb_electra_fork(spec, phases, state):
    yield from run_lc_sync_test_multi_fork(spec, phases, state, SILA_DENEB, ELECTRA)


@with_phases(phases=[CAPELLA], other_phases=[SILA_DENEB, ELECTRA, SILA_FULU, GLOAS])
@spec_test
@with_config_overrides(
    {
        "SILA_DENEB_FORK_EPOCH": 3,  # Test setup advances to epoch 2
        "ELECTRA_FORK_EPOCH": 4,
        "SILA_FULU_FORK_EPOCH": 5,
        "GLOAS_FORK_EPOCH": 6,
    },
)
@with_state
@with_matching_spec_config(emitted_fork=GLOAS)
@with_presets([MINIMAL], reason="too slow")
def test_sila_deneb_gloas_fork(spec, phases, state):
    yield from run_lc_sync_test_multi_fork(spec, phases, state, SILA_DENEB, GLOAS)
