from sil_consensus_specs.test.context import spec_state_test, with_all_phases
from sil_consensus_specs.test.helpers.epoch_processing import (
    run_epoch_processing_with,
)
from sil_consensus_specs.test.helpers.state import transition_to


def run_process_sil1_data_reset(spec, state):
    yield from run_epoch_processing_with(spec, state, "process_sil1_data_reset")


@with_all_phases
@spec_state_test
def test_sil1_vote_no_reset(spec, state):
    assert spec.EPOCHS_PER_SIL1_VOTING_PERIOD > 1
    # skip ahead to the end of the epoch
    transition_to(spec, state, spec.SLOTS_PER_EPOCH - 1)

    for _i in range(state.slot + 1):  # add a vote for each skipped slot.
        state.sil1_data_votes.append(
            spec.Sil1Data(
                deposit_root=b"\xaa" * 32,
                deposit_count=state.sil1_deposit_index,
                block_hash=b"\xbb" * 32,
            )
        )

    yield from run_process_sil1_data_reset(spec, state)

    assert len(state.sil1_data_votes) == spec.SLOTS_PER_EPOCH


@with_all_phases
@spec_state_test
def test_sil1_vote_reset(spec, state):
    # skip ahead to the end of the voting period
    state.slot = (spec.EPOCHS_PER_SIL1_VOTING_PERIOD * spec.SLOTS_PER_EPOCH) - 1
    for _i in range(state.slot + 1):  # add a vote for each skipped slot.
        state.sil1_data_votes.append(
            spec.Sil1Data(
                deposit_root=b"\xaa" * 32,
                deposit_count=state.sil1_deposit_index,
                block_hash=b"\xbb" * 32,
            )
        )

    yield from run_process_sil1_data_reset(spec, state)

    assert len(state.sil1_data_votes) == 0
