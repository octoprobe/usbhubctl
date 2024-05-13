"""
Specify the topology of a Hub
"""

from pyhubctl import Hub, HubChip

rsh_a16 = Hub(
    manufacturer="RSHTECH",
    model="RSH-A16",
    comment="",
    plug_count=16,
    hub_chip=HubChip(
        "0bda:5411",
        plug_or_chip=[
            1,
            2,
            HubChip(
                "0bda:5411",
                plug_or_chip=[
                    7,
                    8,
                    HubChip("0bda:5411", plug_or_chip=[13, 14, 15, 16]),
                    HubChip("0bda:5411", plug_or_chip=[9, 10, 11, 12]),
                ],
            ),
            HubChip("0bda:5411", plug_or_chip=[3, 4, 5, 6]),
        ],
    ),
)
