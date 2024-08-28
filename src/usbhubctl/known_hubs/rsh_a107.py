"""
Specify the topology of a Hub
"""

from usbhubctl import DualProductId, Hub, HubChip

_PRODUCT = DualProductId.parse("2109:0822-2109:2822")

rsh_a107 = Hub(
    manufacturer="RSHTECH",
    model="RSH-A107",
    comment="Power control does NOT work!",
    plug_count=7,
    hub_chip=HubChip(
        _PRODUCT,
        plug_or_chip=[
            HubChip(_PRODUCT, plug_or_chip=[7, 6, 5, 4]),
            3,
            2,
            1,
        ],
    ),
)
