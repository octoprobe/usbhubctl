"""
Specify the topology of a Hub
"""

from usbhubctl import DualProductId, Hub, HubChip

_PRODUCT1 = DualProductId.parse("2109:0822-2109:2822")
_PRODUCT2 = DualProductId.parse("0bda:0411-0bda:5411")


rsh_st07c = Hub(
    manufacturer="RSHTECH",
    model="RSH-ST07C",
    comment="Plugs 1,2,3: Power control does NOT work!",
    plug_count=7,
    hub_chip=HubChip(
        _PRODUCT1,
        plug_or_chip=[
            1,
            2,
            3,
            HubChip(_PRODUCT2, plug_or_chip=[4, 5, 6, 7]),
        ],
    ),
)
