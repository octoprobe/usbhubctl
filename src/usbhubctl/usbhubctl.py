"""
Sequence:
  Create definition of hub
  Query usb and create hub structure
  Find hub definition in hub structure: Create 'hub mount point'.
  Access hub using 'hub mount point'
"""

from __future__ import annotations

import abc
import dataclasses
import logging
import re
from collections.abc import Iterator

import serial
import usb

logger = logging.getLogger(__file__)

# from usbhubctl.backend_power_uhubctl import BackendPowerUhubctl
# backend_power = BackendPowerUhubctl()
# from usbhubctl.backend_power_sysfs import BackendPowerSysFs
# backend_power = BackendPowerSysFs()


class BackendPower:
    _backend_power: BackendPowerABC | None = None

    @property
    def backend_power(self) -> BackendPowerABC:
        if self._backend_power is None:
            from .backend_power_sysfs import BackendPowerSysFs  # pylint: disable=C0415

            self._backend_power = BackendPowerSysFs()
        return self._backend_power


_BACKEND_POWER = BackendPower()


class Cache:
    _cache: Cache | None = None

    def __init__(self) -> None:
        self._actual_usb_topology: Topology | None = None

    @property
    def actual_usb_topology(self) -> Topology:
        if self._actual_usb_topology is None:
            from usbhubctl import backend_query_lsusb  # pylint: disable=C0415

            self._actual_usb_topology = backend_query_lsusb.lsusb()

        return self._actual_usb_topology


_CACHE = Cache()

_RE_PARSE_SHORT_WITH_PRODUCT = re.compile(
    r"^(?P<vendor_product>\w\w\w\w:\w\w\w\w) (?P<bus>\d+)-(?P<path>[\d.]+)$"
)
"""
Example: '05E3:0626 1-3.4.5'
"""


class BackendPowerABC(abc.ABC):
    @abc.abstractmethod
    def power(self, full_paths: list[Path], on: bool) -> None: ...


@dataclasses.dataclass(frozen=True, repr=True, eq=True)
class ProductId:
    vendor: int
    product: int

    def __post_init__(self) -> None:
        assert isinstance(self.vendor, int)
        assert isinstance(self.product, int)

    @property
    def compact(self) -> str:
        return f"{self.vendor:04X}:{self.product:04X}"

    @staticmethod
    def parse(product: str) -> ProductId:
        """
        Example 'product': "0bda:5411"
        """
        v, p = product.split(":", 2)
        return ProductId(vendor=int(v, base=16), product=int(p, base=16))


@dataclasses.dataclass(frozen=True, repr=True, eq=True)
class DualProductId:
    usb2: ProductId
    usb3: ProductId

    def __post_init__(self) -> None:
        assert isinstance(self.usb2, ProductId)
        assert isinstance(self.usb3, ProductId)

    def get_product_id(self, is_usb2: bool) -> ProductId:
        return self.usb2 if is_usb2 else self.usb3

    @property
    def compact(self) -> str:
        return f"{self.usb2.compact}-{self.usb3.compact}"

    @staticmethod
    def parse(dual_product: str) -> ProductId | DualProductId:
        """
        Example 'dual_product': "0bda:0411-0bda:5411"
        Left: usb2
        Right: usb3
        If only one: usb2
        """
        try:
            usb2, usb3 = dual_product.split("-", 2)
        except ValueError:
            return ProductId.parse(dual_product)
        return DualProductId(
            usb2=ProductId.parse(usb2),
            usb3=ProductId.parse(usb3),
        )


@dataclasses.dataclass
class Location:
    bus: int
    path: list[int]

    @staticmethod
    def factory(
        device: serial.tools.list_ports_linux.SysFS | usb.core.Device,
    ) -> Location:
        """
        Example location: '3-1.4.1.1:1.0'
        This is returnemd from the 'location' property of the 'Device' object of the 'serial' library.
        """
        if isinstance(device, serial.tools.list_ports_linux.SysFS):
            # This is a RP2 in application mode.
            # Returned from package 'list_ports', method 'serial.list_ports'
            location, _, _ = device.location.partition(":")
            bus_str, _, path_str = location.partition("-")
            bus = int(bus_str)
            path = [int(p) for p in path_str.split(".")]
            return Location(
                bus=bus,
                path=path,
            )

        if isinstance(device, usb.core.Device):
            # This is a RP2 in boot mode.
            # Returned from package 'usb', method 'usb.core.find()'
            return Location(bus=device.bus, path=list(device.port_numbers))

        assert False, f"Unknown type of {device}!"

    def is_my_hub(self, hub_location: Location) -> bool:
        """
        Expected:
          'this' is the location of the rp2 on the tentacle
          'hub_location' is the location of the hub on the same tentacle
        """
        if self.bus != hub_location.bus:
            return False
        if self.path[:-1] == hub_location.path:
            assert (
                self.path[-1] == 1
            ), f"The rp2 is always connected on port 1, but not {self.short}!"
            return True
        return False

    def path_factory(self, product_id: ProductId) -> Path:
        return Path(product_id=product_id, bus=self.bus, path=self.path)

    @property
    def short(self) -> str:
        path = ".".join(map(str, self.path))
        return f"{self.bus}-{path}"


@dataclasses.dataclass
class Path:
    """
    A USB hub chip and the downstream path leading to this chip.
    """

    product_id: ProductId
    bus: None | int
    path: list[int]

    def __post_init__(self) -> None:
        assert isinstance(self.product_id, ProductId)
        assert isinstance(self.bus, None | int)
        if isinstance(self.path, tuple):
            self.path = list(self.path)
        assert isinstance(self.path, list)

    @property
    def text(self) -> str:
        return f"{','.join(map(str,self.path))}-{self.product_id.compact}"

    def is_top_path(self, sub_path: Path) -> bool:
        assert isinstance(sub_path, Path)
        assert len(sub_path.path) == 0
        return self.product_id == sub_path.product_id

    def equals(self, solution_path: Path, path: Path) -> bool:
        assert isinstance(solution_path, Path)
        assert isinstance(path, Path)
        if self.product_id != path.product_id:
            return False
        full_path = solution_path.path + path.path
        return self.path == full_path

    @property
    def short(self) -> str:
        """
        Example:
            4-1
            4-1.4
            4-1.3
            4-1.3
            4-1.3.4
        """
        path = ".".join(map(str, self.path))
        return f"{self.bus}-{path}"

    @property
    def short_with_product(self) -> str:
        return f"{self.product_id.compact} {self.short}"

    @staticmethod
    def short_with_product_factory(line: str) -> Path:
        """
        Example line: '05E3:0626 1-3'
        """
        match = _RE_PARSE_SHORT_WITH_PRODUCT.match(line)
        assert match
        vendor_product = match.group("vendor_product")
        bus = int(match.group("bus"))
        path_text = match.group("path")
        path = [int(port) for port in path_text.split(".")]
        return Path(ProductId.parse(vendor_product), bus, path)

    @property
    def uhubctl_location(self) -> str:
        """
        Example:
            4-1
            4-1.4
            4-1.3
            4-1.3
            4-1.3.4
        """
        path = ".".join(map(str, self.path[:-1]))
        return f"{self.bus}-{path}"

    @property
    def location(self) -> Location:
        """
        Example:
            4-1
            4-1.4
            4-1.3
            4-1.3
            4-1.3.4
        """
        assert self.bus is not None
        return Location(bus=self.bus, path=self.path)

    @property
    def uhubctl_port(self) -> str:
        return f"{self.path[-1]}"

    @property
    def sysfs_path(self) -> str:
        return f"/sys/bus/usb/devices/{self.uhubctl_location}:1.0/{self.uhubctl_location}-port{self.uhubctl_port}/disable"


@dataclasses.dataclass
class ConnectedPlug:
    connected_hub: ConnectedHub
    plug: Plug

    @property
    def full_path(self) -> Path:
        root_path = self.connected_hub.root_path
        return Path(
            product_id=root_path.product_id,
            bus=root_path.bus,
            path=root_path.path + self.plug.internal_path,
        )


@dataclasses.dataclass
class DualConnectedPlug:
    connected_plug_usb2: ConnectedPlug
    connected_plug_usb3: ConnectedPlug | None

    def __post_init__(self) -> None:
        assert isinstance(self.connected_plug_usb2, ConnectedPlug)
        assert isinstance(self.connected_plug_usb3, ConnectedPlug | None)

    def power(self, on: bool, backend_power: None | BackendPowerABC = None) -> None:
        # self.connected_plug_usb2.power(on=on, backend_power=backend_power)
        # self.connected_plug_usb3.power(on=on, backend_power=backend_power)

        backend_power = _BACKEND_POWER.backend_power
        full_paths = [self.connected_plug_usb2.full_path]
        if self.connected_plug_usb3 is not None:
            full_paths.append(self.connected_plug_usb3.full_path)
        backend_power.power(full_paths=full_paths, on=on)


@dataclasses.dataclass
class ConnectedHub:
    hub: Hub
    root_path: Path

    @property
    def connected_plugs(self) -> list[ConnectedPlug]:
        return [ConnectedPlug(connected_hub=self, plug=plug) for plug in self.hub.plugs]

    @property
    def path_short(self) -> str:
        return self.root_path.short

    def get_plug(self, plug_number: int) -> ConnectedPlug:
        return ConnectedPlug(connected_hub=self, plug=self.hub.get_plug(plug_number))


@dataclasses.dataclass
class ConnectedHubs:
    hub: Hub
    is_usb2: bool
    hubs: list[ConnectedHub]

    def __post_init__(self) -> None:
        assert isinstance(self.hub, Hub)
        assert isinstance(self.is_usb2, bool)
        assert isinstance(self.hubs, list)

    def assert_one(self) -> None:
        if len(self.hubs) > 1:
            paths = "/".join(h.path_short for h in self.hubs)
            usb_version = 2 if self.is_usb2 else 3
            raise IndexError(
                f"More than one '{self.hub.model}' USB{usb_version} hubs detected: Paths {paths}: unambiguously"
            )
            return
        if len(self.hubs) == 0:
            print(f"No hub '{self.hub.model}' detected")
            return

    @property
    def count(self) -> int:
        return len(self.hubs)

    @property
    def locations(self) -> str:
        return "/".join([hub.root_path.short for hub in self.hubs])

    @property
    def text_found(self) -> str:
        usb_version = 2 if self.is_usb2 else 3
        return f"{self.count} USB{usb_version}-hubs at {self.locations}"

    # def expect_one(self) -> ConnectedHub:
    #     """
    #     Raise IndexError
    #     """
    #     self.assert_one()
    #     try:
    #         return self.hubs[0]
    #     except IndexError as e:
    #         usb_version = 2 if self.is_usb2 else 3
    #         raise IndexError(f"No corresponing USB{usb_version} hub found!") from e

    @property
    def model_vendor_product(self) -> str:
        usb_version = 2 if self.is_usb2 else 3
        product_id = self.hub.hub_chip.product_id
        assert isinstance(product_id, ProductId)
        return f"{self.hub.model}(USB{usb_version} {product_id.vendor}:{product_id.product})"


@dataclasses.dataclass
class DualConnectedHub:
    hub: Hub
    connected_hub_usb2: ConnectedHub
    connected_hub_usb3: ConnectedHub | None

    def __post_init__(self) -> None:
        assert isinstance(self.connected_hub_usb2, ConnectedHub)
        assert isinstance(self.connected_hub_usb3, ConnectedHub | None)

    @property
    def connected_plugs(self) -> list[DualConnectedPlug]:
        return [self.get_plug(plug_number=plug.number) for plug in self.hub.plugs]

    def get_plug(self, plug_number: int) -> DualConnectedPlug:
        if self.connected_hub_usb3 is None:
            connected_plug_usb3 = None
        else:
            connected_plug_usb3 = self.connected_hub_usb3.get_plug(
                plug_number=plug_number
            )
        return DualConnectedPlug(
            connected_plug_usb2=self.connected_hub_usb2.get_plug(
                plug_number=plug_number
            ),
            connected_plug_usb3=connected_plug_usb3,
        )


@dataclasses.dataclass
class DualConnectedHubs:
    hub: Hub
    hubs_usb2: ConnectedHubs
    hubs_usb3: ConnectedHubs | None

    def __post_init__(self) -> None:
        assert isinstance(self.hub, Hub)
        assert isinstance(self.hubs_usb2, ConnectedHubs)
        assert isinstance(self.hubs_usb3, ConnectedHubs | None)

    @property
    def usb2_only(self) -> bool:
        return self.hubs_usb3 is None

    def assert_one(self) -> None:
        self.hubs_usb2.assert_one()
        if self.hubs_usb3 is None:
            return
        self.hubs_usb3.assert_one()

    @property
    def text_hubs_found(self) -> str:
        list_found = [self.hubs_usb2.text_found]
        if self.hubs_usb3 is not None:
            list_found.append(self.hubs_usb3.text_found)
        return " / ".join(list_found)

    def expect_one(self) -> DualConnectedHub:
        """
        Raise IndexError
        """

        success = self.hubs_usb2.count == 1
        if self.hubs_usb3 is not None:
            success &= self.hubs_usb3.count == 1
        if not success:
            raise IndexError(
                f"Expect exactly 1 hub '{self.hub.model}({self.hub.hub_chip.product_id_compact})' but found {self.text_hubs_found}"
            )

        hubs_usb2 = self.hubs_usb2.hubs[0]
        if self.hubs_usb3 is None:
            hubs_usb3 = None
        else:
            hubs_usb3 = self.hubs_usb3.hubs[0]
        return DualConnectedHub(
            hub=self.hub,
            connected_hub_usb2=hubs_usb2,
            connected_hub_usb3=hubs_usb3,
        )

    @property
    def compact(self) -> str:
        if self.hubs_usb3 is None:
            return f"USB2({self.hubs_usb2})"
        return f"USB2/3({self.hubs_usb2}/{self.hubs_usb3})"


@dataclasses.dataclass
class Topology:
    list_path: list[Path]

    def __post_init__(self) -> None:
        assert isinstance(self.list_path, list)
        self.list_path.sort(key=lambda path: (path.bus, path.path))

    def find_connected_hubs(self, actual_usb_topology: Topology) -> list[Path]:
        """
        'self' is the hub topology.
        'actual_usb_topology' is the usb topology connected to the PC.
        """

        def try_solution(i_candidate: int) -> None | Path:
            solution_path = None
            for i, path in enumerate(self.list_path):
                try:
                    candiate = actual_usb_topology.list_path[i_candidate + i]
                except IndexError:
                    return None
                if i == 0:
                    if not candiate.is_top_path(path):
                        return None
                    solution_path = candiate
                    continue

                assert solution_path is not None
                if not candiate.equals(solution_path, path):
                    return None

            return solution_path

        def iter_solution() -> Iterator[Path]:
            for i_candidate in range(len(actual_usb_topology.list_path)):
                solution_path = try_solution(i_candidate=i_candidate)
                if solution_path is not None:
                    yield solution_path
                    continue

        return list(iter_solution())

    @staticmethod
    def short_with_product_factory(multiline: str) -> Topology:
        multiline = multiline.strip()
        list_path = [
            Path.short_with_product_factory(line) for line in multiline.splitlines()
        ]
        return Topology(list_path=list_path)

    @property
    def short(self) -> str:
        """
        Example:
            4-1
            4-1.4
            4-1.3
            4-1.3
            4-1.3.4
        """
        return "\n".join([path.short for path in self.list_path])

    @property
    def short_with_product(self) -> str:
        """
        Example:
            4-1
            4-1.4
            4-1.3
            4-1.3
            4-1.3.4
        """
        return "\n".join([path.short_with_product for path in self.list_path])


@dataclasses.dataclass
class HubChip:
    """
    A USB Hub chip.
    In the 'USB Spec', this would be a 'USB controller'.
    There is exactly one upstream port and typically 4 downstream ports.
    Every downstram port is connected to a downstream usb hub chip or to
    a plug on the 'Hub'.
    """

    product_id: None | ProductId | DualProductId
    plug_or_chip: list[int | HubChip]

    def __post_init__(self) -> None:
        assert isinstance(self.product_id, None | ProductId | DualProductId)
        assert isinstance(self.plug_or_chip, list)
        for port in self.plug_or_chip:
            assert isinstance(port, int | HubChip)

    def _register(self, hub: Hub, path: list[int]) -> None:
        for port_number0, plug_or_chip in enumerate(self.plug_or_chip):
            _path = path + [port_number0 + 1]
            if isinstance(plug_or_chip, int):
                hub._register_plug(Plug(number=plug_or_chip, internal_path=_path))  # pylint: disable=W0212
                continue

            assert isinstance(plug_or_chip, HubChip)
            plug_or_chip._register(hub, _path)  # pylint: disable=W0212

    @property
    def usb2_only(self) -> bool:
        return isinstance(self.product_id, ProductId)

    @property
    def product_id_compact(self) -> str:
        if isinstance(self.product_id, ProductId):
            return self.product_id.compact

        assert isinstance(self.product_id, DualProductId)
        return self.product_id.compact

    def get_product_id(self, is_usb2: bool) -> ProductId:
        if isinstance(self.product_id, ProductId):
            return self.product_id

        assert isinstance(self.product_id, DualProductId)
        return self.product_id.get_product_id(is_usb2=is_usb2)


@dataclasses.dataclass
class Plug:
    number: int
    internal_path: list[int]

    def __post_init__(self) -> None:
        assert isinstance(self.number, int)
        if isinstance(self.internal_path, tuple):
            self.internal_path = list(self.internal_path)
        assert isinstance(self.internal_path, list)


@dataclasses.dataclass
class Hub:
    """
    A Hub consists of one more more 'Chips'.
    """

    manufacturer: str
    model: str
    comment: str
    plug_count: int
    hub_chip: HubChip

    _dict_plugs: dict[int, Plug] = dataclasses.field(default_factory=dict)
    """
    The key is the plug number (starting from 1).
    """

    def __post_init__(self) -> None:
        assert isinstance(self.manufacturer, str)
        assert isinstance(self.model, str)
        assert isinstance(self.plug_count, int)
        assert isinstance(self.hub_chip, HubChip)

        self.hub_chip._register(self, path=[])  # pylint: disable=W0212

        sorted_ports = sorted(self._dict_plugs.keys())
        if len(sorted_ports) != self.plug_count:
            raise ValueError(
                f"Expected {self.plug_count} plugs, but only {len(sorted_ports)} plugs have been defined: {sorted_ports}"
            )

        for port0, port in enumerate(sorted_ports):
            if port0 + 1 != port:
                raise ValueError(
                    f"Not all ports from 1 to {self.plug_count} have been defined: {sorted_ports}"
                )

    @property
    def plugs(self) -> list[Plug]:
        return [
            self._dict_plugs[plug_number]
            for plug_number in sorted(self._dict_plugs.keys())
        ]

    @property
    def usb2_only(self) -> bool:
        return self.hub_chip.usb2_only

    def _register_plug(self, plug: Plug) -> None:
        assert plug.number not in self._dict_plugs
        self._dict_plugs[plug.number] = plug

    def get_plug(self, plug_number: int) -> Plug:
        return self._dict_plugs[plug_number]

    def get_topology(self, is_usb2: bool) -> Topology:
        list_internal_path: list[Path] = []

        def downstream(hub_chip: HubChip, path: list[int]) -> None:
            assert hub_chip.product_id is not None

            list_internal_path.append(
                Path(
                    product_id=hub_chip.get_product_id(is_usb2=is_usb2),
                    bus=None,
                    path=path,
                )
            )
            for port_number0, plug_or_chip in enumerate(hub_chip.plug_or_chip):
                if isinstance(plug_or_chip, HubChip):
                    _path = path + [port_number0 + 1]
                    downstream(plug_or_chip, _path)

        downstream(self.hub_chip, path=[])

        return Topology(list_internal_path)

    def find_connected_hubs(
        self,
        is_usb2: bool,
        actual_usb_topology: Topology | None = None,
    ) -> ConnectedHubs:
        assert isinstance(actual_usb_topology, None | Topology)
        assert isinstance(is_usb2, bool)

        if actual_usb_topology is None:
            actual_usb_topology = _CACHE.actual_usb_topology

        return ConnectedHubs(
            hub=self,
            is_usb2=is_usb2,
            hubs=[
                ConnectedHub(hub=self, root_path=path)
                for path in self.get_topology(is_usb2=is_usb2).find_connected_hubs(
                    actual_usb_topology=actual_usb_topology
                )
            ],
        )

    def find_connected_dualhubs(
        self,
        actual_usb_topology: Topology | None = None,
    ) -> DualConnectedHubs:
        if self.usb2_only:
            hubs_usb3 = None
        else:
            hubs_usb3 = self.find_connected_hubs(
                is_usb2=False, actual_usb_topology=actual_usb_topology
            )

        return DualConnectedHubs(
            hub=self,
            hubs_usb2=self.find_connected_hubs(
                is_usb2=True, actual_usb_topology=actual_usb_topology
            ),
            hubs_usb3=hubs_usb3,
        )

    def __repr__(self) -> str:
        return f"USB Hub '{self.model}' with {self.plug_count} plugs"
