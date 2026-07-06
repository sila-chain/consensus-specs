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
    MINIMAL,
)
from sil_consensus_specs.test.helpers.light_client_data_collection import (
    run_lc_data_collection_test_multi_fork,
)


@with_phases(phases=[CAPELLA], other_phases=[SILA_DENEB, ELECTRA])
@spec_test
@with_config_overrides(
    {
        "SILA_DENEB_FORK_EPOCH": 1 * 8,  # SyncCommitteePeriod 1
        "ELECTRA_FORK_EPOCH": 2 * 8,  # SyncCommitteePeriod 2
    },
)
@with_state
@with_matching_spec_config(emitted_fork=ELECTRA)
@with_presets([MINIMAL], reason="too slow")
def test_sila_deneb_electra_reorg_aligned(spec, phases, state):
    yield from run_lc_data_collection_test_multi_fork(spec, phases, state, SILA_DENEB, ELECTRA)


@with_phases(phases=[CAPELLA], other_phases=[SILA_DENEB, ELECTRA])
@spec_test
@with_config_overrides(
    {
        "SILA_DENEB_FORK_EPOCH": 1 * 8 + 4,  # SyncCommitteePeriod 1 (+ 4 epochs)
        "ELECTRA_FORK_EPOCH": 3 * 8 + 4,  # SyncCommitteePeriod 3 (+ 4 epochs)
    },
)
@with_state
@with_matching_spec_config(emitted_fork=ELECTRA)
@with_presets([MINIMAL], reason="too slow")
def test_sila_deneb_electra_reorg_unaligned(spec, phases, state):
    yield from run_lc_data_collection_test_multi_fork(spec, phases, state, SILA_DENEB, ELECTRA)
