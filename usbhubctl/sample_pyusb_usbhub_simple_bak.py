"""
https://en.wikipedia.org/wiki/USB
https://github.com/pyusb/pyusb/blob/master/docs/tutorial.rst
"""

import dataclasses
import time
from typing import Dict, List
import usb.core
import usb.util
from usb.legacy import CLASS_HUB


"""
Hub(vendor=8523, product=29264, bus=3, path=(5, 2, 1), address=9)
Hub(vendor=8457, product=2066, bus=3, path=(5, 2), address=6)
Hub(vendor=6720, product=2049, bus=3, path=(5,), address=4)

lsusb -tv
/:  Bus 003.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/12p, 480M
    ID 1d6b:0002 Linux Foundation 2.0 root hub
    |__ Port 005: Dev 004, If 0, Class=Hub, Driver=hub/4p, 480M
        ID 1a40:0801 Terminus Technology Inc. 
        |__ Port 002: Dev 006, If 0, Class=Hub, Driver=hub/4p, 480M
            ID 2109:0812 VIA Labs, Inc. VL812 Hub
            |__ Port 001: Dev 009, If 0, Class=Hub, Driver=hub/4p, 480M
                ID 214b:7250 Huasheng Electronics 

ls -1 /sys/bus/usb/devices
3-5
3-5:1.0
3-5.2
3-5.2.1
3-5.2:1.0
3-5.2.1.1
3-5.2.1:1.0
3-5.2.1.1:1.0
3-5.2.1.4
3-5.2.1.4:1.0

Example 3-5.2.1

readlink -f /sys/bus/usb/devices/3-5.2.1
/sys/devices/pci0000:00/0000:00:14.0/usb3/3-5/3-5.2/3-5.2.1

cat /sys/devices/pci0000:00/0000:00:14.0/usb3/3-5/3-5.2/3-5.2.1/idVendor
214b

cat /sys/devices/pci0000:00/0000:00:14.0/usb3/3-5/3-5.2/3-5.2.1/bDeviceClass
09     # Hub
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


@dataclasses.dataclass
class Hub:
    vendor: int
    product: int
    bus: int
    path: List[int]
    address: int


def main():
    begin_s = time.monotonic()

    hub_devices = usb.core.find(find_all=1, custom_match=find_class(CLASS_HUB))
    hub_devices = list(hub_devices)

    hubs: List[Hub] = []
    for hub in hub_devices:
        # print(f"  port_number={hub.port_number}({hub.port_numbers})")
        # print(hub)
        if hub.port_numbers is None:
            continue
        h = Hub(
            vendor=hub.idVendor,
            product=hub.idProduct,
            bus=hub.bus,
            path=hub.port_numbers,
            address=hub.address,
        )
        hubs.append(h)

    for h in hubs:
        print(h)
    print(f"*********** duration={time.monotonic()-begin_s:0.3f}s")


if __name__ == "__main__":
    main()
