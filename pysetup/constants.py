# Definitions in context.py
PHASE0 = "phase0"
ALTAIR = "altair"
BELLATRIX = "bellatrix"
CAPELLA = "capella"
DENEB = "deneb"
ELECTRA = "electra"
FULU = "fulu"
GLOAS = "gloas"
SIP6800 = "sip6800"
SIP7441 = "sip7441"
SIP7805 = "sip7805"
SIP7928 = "sip7928"


# The helper functions that are used when defining constants
CONSTANT_DEP_SUNDRY_CONSTANTS_FUNCTIONS = """
def ceillog2(x: int) -> uint64:
    if x < 1:
        raise ValueError(f"ceillog2 accepts only positive values, x={x}")
    return uint64((x - 1).bit_length())


def floorlog2(x: int) -> uint64:
    if x < 1:
        raise ValueError(f"floorlog2 accepts only positive values, x={x}")
    return uint64(x.bit_length() - 1)
"""


OPTIMIZED_BLS_AGGREGATE_PUBKEYS = """
def sil_aggregate_pubkeys(pubkeys: Sequence[BLSPubkey]) -> BLSPubkey:
    return bls.AggregatePKs(pubkeys)
"""
