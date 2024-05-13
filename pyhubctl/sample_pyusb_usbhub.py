"""
https://en.wikipedia.org/wiki/USB
https://github.com/pyusb/pyusb/blob/master/docs/tutorial.rst
"""
import time
from typing import Dict, List
import usb.core
import usb.util
from usb.legacy import CLASS_HUB

# lsusb -d 2e8a:0005 -v

RP2_VENDOR = 0x2E8A
RP2_PRODUCT_BOOT_MODE = 0x0003
RP2_PRODUCT_APPLICATION_MODE = 0x0005

"""
<DEVICE ID 0bda:5411 on Bus 003 Address 046>
  parent=<DEVICE ID 0bda:5411 on Bus 003 Address 044>
<DEVICE ID 0bda:5411 on Bus 003 Address 049>
  parent=<DEVICE ID 0bda:5411 on Bus 003 Address 045>
<DEVICE ID 0bda:5411 on Bus 003 Address 047>
  parent=<DEVICE ID 0bda:5411 on Bus 003 Address 045>
<DEVICE ID 0bda:5411 on Bus 003 Address 045>
  parent=<DEVICE ID 0bda:5411 on Bus 003 Address 044>
<DEVICE ID 0bda:5411 on Bus 003 Address 044>
  parent=<DEVICE ID 1d6b:0002 on Bus 003 Address 001>

<DEVICE ID 0bda:0411 on Bus 004 Address 010>
  parent=<DEVICE ID 0bda:0411 on Bus 004 Address 008>
<DEVICE ID 0bda:0411 on Bus 004 Address 013>
  parent=<DEVICE ID 0bda:0411 on Bus 004 Address 009>
<DEVICE ID 0bda:0411 on Bus 004 Address 011>
  parent=<DEVICE ID 0bda:0411 on Bus 004 Address 009>
<DEVICE ID 0bda:0411 on Bus 004 Address 009>
  parent=<DEVICE ID 0bda:0411 on Bus 004 Address 008>
<DEVICE ID 0bda:0411 on Bus 004 Address 008>
  parent=<DEVICE ID 1d6b:0003 on Bus 004 Address 001>

Root hubs:
<DEVICE ID 1d6b:0002 on Bus 001 Address 001>
<DEVICE ID 1d6b:0003 on Bus 002 Address 001>
<DEVICE ID 1d6b:0002 on Bus 003 Address 001>
<DEVICE ID 1d6b:0003 on Bus 004 Address 001>
*********** duration=11.724s

"""


class find_class:
    def __init__(self, class_: int):
        self._class = class_

    def __call__(self, device):
        # first, let's check the device
        if device.bDeviceClass == self._class:
            return True
        # ok, transverse all devices to find an
        # interface that matches our class
        for cfg in device:
            # find_descriptor: what's it?
            intf = usb.util.find_descriptor(cfg, bInterfaceClass=self._class)
            if intf is not None:
                return True

        return False


class Universe:
    def __init__(self):
        self.busses: Dict[int, usb.Bus] = {}

    def populate(self, hub_devices: List[usb.Device]) -> bool:
        """
        Try to build the tree from the busses, root_hubs, etc.
        return False if no elements could be added.
        """
        added = False
        for hub_device in hub_devices:
            if hub_device.bus not in self.busses:
                self.busses[hub_device.bus] = Bus(nr=hub_device.bus)
            bus = self.busses[hub_device.bus]

            if bus.populate(hub_device=hub_device):
                added = True
        return added

    def print_tree(self) -> None:
        for bus in sorted(self.busses):
            self.busses[bus].print_tree()


class Bus:
    def __init__(self, nr: int):
        self.nr = nr
        self.root_hub: "Hub" = None
        self.hubs: Dict[str:"Hub"] = {}

    def add_hub_(self, hub: "Hub") -> None:
        assert hub.repr_hub_device not in self.hubs
        self.hubs[repr(hub.hub_device)] = hub

    def populate(self, hub_device: usb.Device) -> bool:
        """
        Try to build the tree from the busses, root_hubs, etc.
        return False if no elements could be added.
        """
        if hub_device.parent is None:
            # This is a root hub
            if self.root_hub is not None:
                # The root hub has already been added
                assert hub_device is self.root_hub.hub_device
                return False
            assert len(self.hubs) == 0
            self.root_hub = Hub(bus=self, hub_device=hub_device)
            return True

        if repr(hub_device.parent) in self.hubs:
            # The parent was already added
            parent = self.hubs[repr(hub_device.parent)]
            # Try to add ourselves
            return parent.populate(hub_device)

        # The parent is not populated yet
        return True

    def print_tree(self) -> None:
        print(f"BUS {self.nr}")
        self.root_hub.print_tree(indent="  ")


class Hub:
    def __init__(self, bus: Bus, hub_device: usb.Device):
        self.bus = bus
        self.hub_device = hub_device
        self.repr_hub_device = repr(hub_device)
        self.children: Dict[str:Hub] = {}
        self.port_child: Dict[int:Hub] = {}

        bus.add_hub_(self)

    def _find_port(self, child_hub: "Hub") -> int:
        pass

    def populate(self, hub_device: usb.Device) -> bool:
        """
        Try to build the tree from the busses, root_hubs, etc.
        return False if no elements could be added.
        """
        assert repr(hub_device.parent) == self.repr_hub_device
        if repr(hub_device) in self.children:
            # We have already be added
            return False

        hub = Hub(bus=self.bus, hub_device=hub_device)
        assert hub.repr_hub_device not in self.children
        self.children[repr(hub_device)] = hub
        if False:
            port = self._find_port(hub)
            assert port not in self.port_child
            self.port_child[port] = hub
        return True

    @property
    def children_sorted(self) -> List["Hub"]:
        return self.children.values()

    def print_tree(self, indent: str) -> None:
        print(
            f"{indent} {self.hub_device!r} port_number={self.hub_device.port_number}({self.hub_device.port_numbers})"
        )
        for child in self.children_sorted:
            child.print_tree(indent + "  ")


def main():
    begin_s = time.monotonic()

    hub_devices = usb.core.find(find_all=1, custom_match=find_class(CLASS_HUB))
    hub_devices = list(hub_devices)

    if True:
        u = Universe()
        while u.populate(hub_devices=hub_devices):
            u.print_tree()
            print("-------------")
    for hub in hub_devices:
        if hub.port_number is None:
            print("Päng")
        else:
            print(f"  port_number={hub.port_number}({hub.port_numbers})")
        print(hub)
        continue
        try:
            serial_number = hub.serial_number
        except ValueError:
            serial_number = None
        print(f"{hub!r}")
        if hub.parent is not None:
            print(f"  parent={hub.parent!r}")
        if False:
            print(
                f"  {hub.idVendor:04X}:{hub.idProduct:04X} serial_number={serial_number} port_number={hub.port_number}({hub.port_numbers})"
            )
            print(
                f"  bus={hub.bus} parent.address={hub.address} bcdDevice={hub.bcdDevice} "
            )
            if hub.parent is not None:
                print(f"  parent.bcdDevice={hub.parent.bcdDevice}")

    print(f"*********** duration={time.monotonic()-begin_s:0.3f}s")


if __name__ == "__main__":
    main()
