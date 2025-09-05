"""
Specify the topology of a Hub
"""

#######################################
###    NOT TESTED YET
#######################################
from usbhubctl import DualProductId, Hub, HubChip

_PRODUCT1 = DualProductId.parse("0bda:0411-0bda:5411")


rsh_st07 = Hub(
    manufacturer="RSHTECH",
    model="RSH-ST07",
    comment="Plugs 1,2,3: Power control does NOT work!",
    plug_count=7,
    hub_chip=HubChip(
        _PRODUCT1,
        plug_or_chip=[
            HubChip(_PRODUCT1, plug_or_chip=[4, 5, 6, 7]),
            1,
            2,
            3,
        ],
    ),
)
