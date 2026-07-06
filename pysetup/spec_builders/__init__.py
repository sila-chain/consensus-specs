from .altair import AltairSpecBuilder
from .bellatrix import BellatrixSpecBuilder
from .capella import CapellaSpecBuilder
from .sila_deneb import SilaDenebSpecBuilder
from .sip8025 import SIP8025SpecBuilder
from .sip8148 import SIP8148SpecBuilder
from .electra import ElectraSpecBuilder
from .sila_fulu import SilaFuluSpecBuilder
from .gloas import GloasSpecBuilder
from .heze import HezeSpecBuilder
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
        HezeSpecBuilder,
        SIP8025SpecBuilder,
        SIP8148SpecBuilder,
    )
}
