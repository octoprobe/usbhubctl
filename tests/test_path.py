from usbhubctl import Topology
from usbhubctl.known_hubs import rsh_a16

import pytest

_EFFECTIVE_TOPOLOGY_WITH_RSH_A15 = """
05E3:0626 1-3
0BDA:0411 1-3.1
0BDA:0411 1-3.1.3
0BDA:0411 1-3.1.3.3
0BDA:0411 1-3.1.3.4
0BDA:0411 1-3.1.4
05E3:0610 2-6
0BDA:5411 2-6.1
0BDA:5411 2-6.1.3
0BDA:5411 2-6.1.3.3
0BDA:5411 2-6.1.3.4
0BDA:5411 2-6.1.4
"""


def test_find_rsh_a16() -> None:
    effective_topology = Topology.short_with_product_factory(
        _EFFECTIVE_TOPOLOGY_WITH_RSH_A15
    )
    connected_hubs = rsh_a16.find_connected_hubs(effective_topology)

    assert connected_hubs.short == "2-6.1"


def test_topology_rsh_a16() -> None:
    short_with_product = rsh_a16.topology.short_with_product

    expected_short_with_product = """
0BDA:5411 None-
0BDA:5411 None-3
0BDA:5411 None-3.3
0BDA:5411 None-3.4
0BDA:5411 None-4
""".strip()

    assert short_with_product == expected_short_with_product


@pytest.mark.parametrize(
    "plug_number,expected_internal_path",
    (
        (
            1,
            [1],
        ),
        (
            2,
            [2],
        ),
        (16, [3, 3, 4]),
    ),
)
def test_plug_rsh_a16(
    plug_number: int,
    expected_internal_path: list[int],
) -> None:
    plug = rsh_a16.get_plug(plug_number=plug_number)
    assert plug.internal_path == expected_internal_path
