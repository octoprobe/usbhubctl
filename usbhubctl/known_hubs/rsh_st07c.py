"""
Specify the topology of a Hub
"""

from usbhubctl import Hub, HubChip

rsh_st07c = Hub(
    manufacturer="RSHTECH",
    model="RSH-ST07C",
    comment="Plugs 1,2,3: Power control does NOT work!",
    plug_count=7,
    hub_chip=HubChip(
        "2109:2822",
        # "2109:0822",
        plug_or_chip=[
            1,
            2,
            3,
            HubChip("0bda:5411", plug_or_chip=[4, 5, 6, 7]),
            # HubChip("0bda:0411", plug_or_chip=[4, 5, 6, 7]),
        ],
    ),
)
