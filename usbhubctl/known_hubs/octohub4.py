"""
Specify the topology of a Hub
"""

from usbhubctl import Hub, HubChip, ProductId

OCTOHUB4_PRODUCT_ID = ProductId(vendor=0x0424, product=0x2514)

octohub4 = Hub(
    manufacturer="Maerki Informatik",
    model="Octohub4 v0.2",
    comment="",
    plug_count=4,
    hub_chip=HubChip(
        OCTOHUB4_PRODUCT_ID,
        plug_or_chip=[
            1,
            2,
            3,
            4,
        ],
    ),
)
