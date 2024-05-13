"""
Specify the topology of a Hub
"""

from pyhubctl import Hub, HubChip

rsh_a10 = Hub(
    manufacturer="RSHTECH",
    model="RSH-A10",
    comment="",
    plug_count=10,
    hub_chip=HubChip(
        "0bda:5411",
        plug_or_chip=[
            1,
            2,
            HubChip("0bda:5411", plug_or_chip=[7, 8, 9, 10]),
            HubChip("0bda:5411", plug_or_chip=[3, 4, 5, 6]),
        ],
    ),
)
