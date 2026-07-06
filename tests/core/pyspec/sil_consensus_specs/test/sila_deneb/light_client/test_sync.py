from sil_consensus_specs.test.context import (
    spec_test,
    with_config_overrides,
    with_matching_spec_config,
    with_phases,
    with_presets,
    with_state,
)
from sil_consensus_specs.test.helpers.constants import (
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


@with_phases(phases=[SILA_DENEB], other_phases=[ELECTRA])
@spec_test
@with_config_overrides(
    {
        "ELECTRA_FORK_EPOCH": 3,  # Test setup advances to epoch 2
    },
)
@with_state
@with_matching_spec_config(emitted_fork=ELECTRA)
@with_presets([MINIMAL], reason="too slow")
def test_electra_fork(spec, phases, state):
    yield from run_lc_sync_test_single_fork(spec, phases, state, ELECTRA)


@with_phases(phases=[SILA_DENEB], other_phases=[ELECTRA, SILA_FULU, GLOAS])
@spec_test
@with_config_overrides(
    {
        "ELECTRA_FORK_EPOCH": 3,  # Test setup advances to epoch 2
        "SILA_FULU_FORK_EPOCH": 4,
        "GLOAS_FORK_EPOCH": 5,
    },
)
@with_state
@with_matching_spec_config(emitted_fork=GLOAS)
@with_presets([MINIMAL], reason="too slow")
def test_electra_gloas_fork(spec, phases, state):
    yield from run_lc_sync_test_multi_fork(spec, phases, state, ELECTRA, GLOAS)
