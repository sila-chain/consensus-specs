"""
Tests for SIP-7928 block access list field.
"""

from sil2spec.test.context import (
    spec_state_test,
    with_sip7928_and_later,
)
from sil2spec.test.helpers.execution_payload import (
    build_empty_execution_payload,
    compute_el_block_hash,
)
from sil2spec.test.helpers.state import next_slot


@with_sip7928_and_later
@spec_state_test
def test_execution_payload_with_block_access_list(spec, state):
    """Test that execution payload correctly includes block access list field."""
    next_slot(spec, state)
    execution_payload = build_empty_execution_payload(spec, state)

    # Verify field exists and can be set
    assert hasattr(execution_payload, "block_access_list")
    execution_payload.block_access_list = spec.ByteList[spec.MAX_BYTES_PER_TRANSACTION](
        b"\xc0" * 100
    )
    execution_payload.block_hash = compute_el_block_hash(spec, execution_payload, state)

    # Process payload
    body = spec.BeaconBlockBody(execution_payload=execution_payload)
    spec.process_execution_payload(state, body, spec.NoopExecutionEngine())

    # Verify header contains the root
    assert state.latest_execution_payload_header.block_access_list_root == spec.hash_tree_root(
        execution_payload.block_access_list
    )
