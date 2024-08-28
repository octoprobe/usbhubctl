"""
Elaborate the real topology using `lsusb -tv
"""

import itertools
import re
from collections.abc import Iterator

from usbhubctl import Path, ProductId, Topology

RE_BUS1 = re.compile(
    r"^/:  Bus (?P<bus>\d+).Port (?P<port>\d+): Dev \d+, Class=root_hub,"
)
"""
Example: '/:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/4p, 10000M'
"""

RE_PORT1 = re.compile(
    r"^(?P<indent1> +\|__ )Port (?P<port>\d+)(.*?Class=(?P<class>.*?),)?"
)
"""
Example: '    |__ Port 003: Dev 002, If 0, Class=Hub, Driver=hub/4p, 5000M'
         '    |__ Port 001: Dev 027, 12M'
"""

RE_ID2 = re.compile(r"^(?P<indent2> +)ID (?P<vendor_product>\w\w\w\w:\w\w\w\w)")
"""
Example: '    ID 1d6b:0003 Linux Foundation 3.0 root hub'
"""


def _parse(lsusb_output: str) -> Topology:
    def iter_parse() -> Iterator[Path]:
        lines = lsusb_output.strip().splitlines()
        assert len(lines) % 2 == 0
        current_nesting = 1
        current_bus: None | int = None
        current_path: list[int] = []
        for line1, line2 in itertools.batched(lines, n=2):
            match2 = RE_ID2.match(line2)
            assert match2 is not None
            indent2_len = len(match2.group("indent2"))

            match1 = RE_BUS1.match(line1)
            if match1 is not None:
                # Bus
                assert indent2_len == 4
                current_nesting = 1
                current_bus = int(match1.group("bus"))
                port = int(match1.group("port"))
                assert port == 1
                # print(f"{current_nesting=} {current_bus=} {port=}")
                current_path = []
                continue

            match1 = RE_PORT1.match(line1)
            assert match1 is not None, line1
            # Port
            indent1_len = len(match1.group("indent1"))
            port = int(match1.group("port"))
            device_class = match1.group("class")
            indent2_len = len(match2.group("indent2"))
            assert indent1_len == indent2_len

            new_nesting = indent2_len // 4
            # The nesting must never increase more than one
            assert new_nesting <= new_nesting + 1
            current_nesting = new_nesting

            if device_class == "Hub":
                vendor_product = match2.group("vendor_product")
                current_path = current_path[: current_nesting - 2]
                current_path.append(port)
                # print(
                #     f"{current_nesting=} {current_bus=} {current_path=} {port=} {device_class=} {vendor_product}"
                # )
                yield Path(
                    bus=current_bus,
                    path=current_path,
                    product_id=ProductId.parse(vendor_product),
                )

    return Topology(list(iter_parse()))


def get_real_topology(lsusb_output: str) -> Topology:
    return _parse(lsusb_output=lsusb_output)
