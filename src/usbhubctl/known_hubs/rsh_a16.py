"""
Specify the topology of a Hub
"""

from usbhubctl import DualProductId, Hub, HubChip

_PRODUCT = DualProductId.parse("0bda:0411-0bda:5411")

rsh_a16 = Hub(
    manufacturer="RSHTECH",
    model="RSH-A16",
    comment="",
    plug_count=16,
    hub_chip=HubChip(
        _PRODUCT,
        plug_or_chip=[
            1,
            2,
            HubChip(
                _PRODUCT,
                plug_or_chip=[
                    7,
                    8,
                    HubChip(_PRODUCT, plug_or_chip=[13, 14, 15, 16]),
                    HubChip(_PRODUCT, plug_or_chip=[9, 10, 11, 12]),
                ],
            ),
            HubChip(_PRODUCT, plug_or_chip=[3, 4, 5, 6]),
        ],
    ),
)
