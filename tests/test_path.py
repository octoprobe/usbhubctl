import dataclasses

import pytest

from usbhubctl import Hub, Topology, known_hubs

_EFFECTIVE_TOPOLOGY_WITH_RSH_A10_A = """
05E3:0626 2-3
0BDA:0411 2-3.3
0BDA:0411 2-3.3.3
0BDA:0411 2-3.3.4
05E3:0610 3-6
0BDA:5411 3-6.3
0BDA:5411 3-6.3.3
0BDA:5411 3-6.3.4
"""

_EFFECTIVE_TOPOLOGY_WITH_RSH_A10_B = """
1A40:0801 3-5
2109:0812 3-5.2
214B:7250 3-5.2.1
0424:2514 3-5.2.2
0BDA:5411 3-5.2.3
0BDA:5411 3-5.2.3.3
0BDA:5411 3-5.2.3.4
"""
"""
Hub behind chip 7 port hub: USB2 chips (0BDA:0411) are missing. Why?
"""

_EFFECTIVE_TOPOLOGY_WITH_RSH_A16_A = """
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

_EFFECTIVE_TOPOLOGY_WITH_OCTOHUB4 = """
0424:2514 3-1
1A40:0801 3-5
0BDA:5411 3-5.2
0BDA:5411 3-5.2.3
0BDA:5411 3-5.2.4
0A12:4010 3-5.2.4.3
"""

_EFFECTIVE_TOPOLOGY_WITH_TWO_OCTOHUB4 = """
0BDA:5411 3-1
0BDA:5411 3-1.3
0BDA:5411 3-1.4
1A40:0801 3-5
0424:2514 3-5.2
0424:2514 3-5.3
0BDA:0411 4-1
0BDA:0411 4-1.3
0BDA:0411 4-1.4
"""


@dataclasses.dataclass(frozen=True)
class FindHubTestParam:
    hub: Hub
    is_usb2: bool
    effective_topology: str
    effective_topology_label: str
    expected_connected_hub: str

    def __post_init__(self) -> None:
        assert isinstance(self.hub, Hub)
        assert isinstance(self.is_usb2, bool)
        assert isinstance(self.effective_topology, str)
        assert isinstance(self.effective_topology_label, str)
        assert isinstance(self.expected_connected_hub, str)

    @property
    def testname(self) -> str:
        return f"{self.hub.model}_{'usb2' if self.is_usb2 else 'usb3'}_{self.effective_topology_label}_{self.expected_connected_hub}"


@pytest.mark.parametrize(
    "param",
    (
        FindHubTestParam(
            known_hubs.rsh_a10, True, _EFFECTIVE_TOPOLOGY_WITH_RSH_A10_A, "a", "2-3.3"
        ),
        FindHubTestParam(
            known_hubs.rsh_a10, False, _EFFECTIVE_TOPOLOGY_WITH_RSH_A10_A, "a", "3-6.3"
        ),
        FindHubTestParam(
            known_hubs.rsh_a10,
            False,
            _EFFECTIVE_TOPOLOGY_WITH_RSH_A10_B,
            "b",
            "3-5.2.3",
        ),
        FindHubTestParam(
            known_hubs.rsh_a10,
            False,
            _EFFECTIVE_TOPOLOGY_WITH_RSH_A10_B,
            "b",
            "3-5.2.3",
        ),
        FindHubTestParam(
            known_hubs.rsh_a16, True, _EFFECTIVE_TOPOLOGY_WITH_RSH_A16_A, "a", "1-3.1"
        ),
        FindHubTestParam(
            known_hubs.rsh_a16, False, _EFFECTIVE_TOPOLOGY_WITH_RSH_A16_A, "a", "2-6.1"
        ),
        FindHubTestParam(
            known_hubs.octohub4, False, _EFFECTIVE_TOPOLOGY_WITH_OCTOHUB4, "a", "3-1"
        ),
        FindHubTestParam(
            known_hubs.octohub4,
            False,
            _EFFECTIVE_TOPOLOGY_WITH_TWO_OCTOHUB4,
            "two_a",
            "3-5.2/3-5.3",
        ),
    ),
    ids=lambda param: param.testname,
)
def test_find_hub(param: FindHubTestParam) -> None:
    effective_topology = Topology.short_with_product_factory(param.effective_topology)
    connected_hubs = param.hub.find_connected_hubs(
        is_usb2=param.is_usb2,
        actual_usb_topology=effective_topology,
    )

    assert connected_hubs.locations == param.expected_connected_hub


_EXPECTED_SHORT_WITH_PRODUCT_RSH_A10_USB2 = """
0BDA:0411 None-
0BDA:0411 None-3
0BDA:0411 None-4
"""

_EXPECTED_SHORT_WITH_PRODUCT_RSH_A10_USB3 = """
0BDA:5411 None-
0BDA:5411 None-3
0BDA:5411 None-4
"""

_EXPECTED_SHORT_WITH_PRODUCT_RSH_A16_USB2 = """
0BDA:0411 None-
0BDA:0411 None-3
0BDA:0411 None-3.3
0BDA:0411 None-3.4
0BDA:0411 None-4
"""

_EXPECTED_SHORT_WITH_PRODUCT_RSH_A16_USB3 = """
0BDA:5411 None-
0BDA:5411 None-3
0BDA:5411 None-3.3
0BDA:5411 None-3.4
0BDA:5411 None-4
"""


@dataclasses.dataclass(frozen=True)
class TopologyTestParam:
    hub: Hub
    is_usb2: bool
    expected_short_with_product: str

    def __post_init__(self) -> None:
        assert isinstance(self.hub, Hub)
        assert isinstance(self.is_usb2, bool)
        assert isinstance(self.expected_short_with_product, str)

    @property
    def testname(self) -> str:
        return f"{self.hub.model}_{'usb2' if self.is_usb2 else 'usb3'}"


@pytest.mark.parametrize(
    "param",
    (
        TopologyTestParam(
            known_hubs.rsh_a10, True, _EXPECTED_SHORT_WITH_PRODUCT_RSH_A10_USB2
        ),
        TopologyTestParam(
            known_hubs.rsh_a10, False, _EXPECTED_SHORT_WITH_PRODUCT_RSH_A10_USB3
        ),
        TopologyTestParam(
            known_hubs.rsh_a16, True, _EXPECTED_SHORT_WITH_PRODUCT_RSH_A16_USB2
        ),
        TopologyTestParam(
            known_hubs.rsh_a16, False, _EXPECTED_SHORT_WITH_PRODUCT_RSH_A16_USB3
        ),
    ),
    ids=lambda param: param.testname,
)
def test_topology(
    param: TopologyTestParam,
) -> None:
    short_with_product = param.hub.get_topology(
        is_usb2=param.is_usb2
    ).short_with_product

    assert short_with_product == param.expected_short_with_product.strip()


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
    plug = known_hubs.rsh_a16.get_plug(plug_number=plug_number)
    assert plug.internal_path == expected_internal_path


if __name__ == "__main__":
    pass
