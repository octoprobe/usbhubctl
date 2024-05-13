"""
Specify the topology of a Hub
"""

from pyhubctl import Hub, HubChip

rsh_a107 = Hub(
    manufacturer="RSHTECH",
    model="RSH-A107",
    comment="Power control does NOT work!",
    plug_count=7,
    hub_chip=HubChip(
        "2109:2822",
        plug_or_chip=[
            HubChip("2109:2822", plug_or_chip=[7, 6, 5, 4]),
            3,
            2,
            1,
        ],
    ),
)
