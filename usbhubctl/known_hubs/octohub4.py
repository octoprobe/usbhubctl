"""
Specify the topology of a Hub
"""

from usbhubctl import Hub, HubChip, ProductId

octohub4 = Hub(
    manufacturer="Maerki Informatik",
    model="Octohub4 v0.2",
    comment="",
    plug_count=4,
    hub_chip=HubChip(
        ProductId.parse("0424:2514"),
        plug_or_chip=[
            1,
            2,
            3,
            4,
        ],
    ),
)
