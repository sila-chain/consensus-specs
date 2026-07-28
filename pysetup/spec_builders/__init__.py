from .altair import AltairSpecBuilder
from .bellatrix import BellatrixSpecBuilder
from .capella import CapellaSpecBuilder
from .deneb import SilaDenebSpecBuilder
from .sip6800 import SIP6800SpecBuilder
from .sip7441 import SIP7441SpecBuilder
from .sip7805 import SIP7805SpecBuilder
from .sip7928 import SIP7928SpecBuilder
from .electra import ElectraSpecBuilder
from .fulu import SilaFuluSpecBuilder
from .gloas import GloasSpecBuilder
from .phase0 import Phase0SpecBuilder

spec_builders = {
    builder.fork: builder
    for builder in (
        Phase0SpecBuilder,
        AltairSpecBuilder,
        BellatrixSpecBuilder,
        CapellaSpecBuilder,
        SilaDenebSpecBuilder,
        ElectraSpecBuilder,
        SilaFuluSpecBuilder,
        GloasSpecBuilder,
        SIP6800SpecBuilder,
        SIP7441SpecBuilder,
        SIP7805SpecBuilder,
        SIP7928SpecBuilder,
    )
}
