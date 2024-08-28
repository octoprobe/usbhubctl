"""
Specify the topology of a Hub
"""

from usbhubctl import DualProductId, Hub, HubChip

_PRODUCT = DualProductId.parse("0bda:0411-0bda:5411")

rsh_a10 = Hub(
    manufacturer="RSHTECH",
    model="RSH-A10",
    comment="",
    plug_count=10,
    hub_chip=HubChip(
        _PRODUCT,
        plug_or_chip=[
            1,
            2,
            HubChip(_PRODUCT, plug_or_chip=[7, 8, 9, 10]),
            HubChip(_PRODUCT, plug_or_chip=[3, 4, 5, 6]),
        ],
    ),
)
