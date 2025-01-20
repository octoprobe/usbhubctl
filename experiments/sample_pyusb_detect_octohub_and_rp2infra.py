# type: ignore
"""
https://en.wikipedia.org/wiki/USB
https://github.com/pyusb/pyusb/blob/master/docs/tutorial.rst


Find all rp3 in application mode (serial)
  *
Find all rp2 in programming mode (pyusb)
"""

from __future__ import annotations

from typing import Any

import serial
import usb.core
import usb.util
from serial.tools import list_ports
from usb.legacy import CLASS_HUB

# lsusb -d 2e8a:0005 -v

RP2_VENDOR = 0x2E8A
RP2_PRODUCT_BOOT_MODE = 0x0003
RP2_PRODUCT_APPLICATION_MODE = 0x0005

# TODO: Reuse constants from usbhubctl/known_hubs/octohub4.py
OCTOHUB4_VENDOR = 0x0424
OCTOHUB4_PRODUCT = 0x2514

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


class find_octohub4:
    def __init__(self) -> None:
        pass

    def __call__(self, device) -> bool:
        # first, let's check the device
        if device.bDeviceClass == CLASS_HUB:
            if device.idVendor == OCTOHUB4_VENDOR:
                if device.idProduct == OCTOHUB4_PRODUCT:
                    return True

        # ok, transverse all devices to find an
        # interface that matches our class
        # for cfg in device:
        #     # find_descriptor: what's it?
        #     intf = usb.util.find_descriptor(cfg, bInterfaceClass=self._class)
        #     if intf is not None:
        #         return True

        return False


class find_rp2:
    def __init__(self) -> None:
        pass

    def __call__(self, device) -> bool:
        # first, let's check the device
        if device.idVendor == RP2_VENDOR:
            if device.idProduct in (
                RP2_PRODUCT_APPLICATION_MODE,
                RP2_PRODUCT_BOOT_MODE,
            ):
                return True

        return False


def serial_ports_ordered() -> list[serial.Serial]:
    """
    return ordered list of comports. Ignore the ones which do not have vid/pid defined.
    """
    ports = list(list_ports.comports())
    ports.sort(key=lambda p: p.device)

    return [p for p in ports if p.vid and p.pid]


def serial_find_rp2() -> list[Any]:
    for port in serial_ports_ordered():
        if RP2_VENDOR != port.vid:
            continue
        if RP2_PRODUCT_APPLICATION_MODE != port.pid:
            continue
        yield port


class QuerySerial:
    """
    Algorithm:
      * Query
        * list_rp2_mode_application
        * list_rp2_mode_boot
        * list_octohub
      * Given: serials of required tentacles
        * find in list_rp2_mode_application
        * verify if hub is there
        * if serials are missing
          Message:
           * list_rp2_mode_boot
           * Hubs which are not powered as needed
      * Result
        * For every serial number a location for rp2 and hub

      * Fixing:
        * [x] Allow to power the hubs
        * [x] Allow to restart rp2 on hub port 1

    Modules
      * Query list_rp2_mode_application
      * Query list_rp2_mode_boot
      * list_octohub

      * Power all Hubs: Plug1 on, Plug2 on, Plug3 off, Plug4 off
    """

    def __init__(self):
        self.list_rp2_mode_application = self._query_rp2_application_mode()
        self.list_rp2_mode_boot = self._query_rp2_boot_mode()
        pass

    def _query_rp2_application_mode(self) -> list[serial.core.SysFs]:
        def inner():
            for port in list_ports.comports():
                if port.vid != RP2_VENDOR:
                    continue
                if port.pid != RP2_PRODUCT_APPLICATION_MODE:
                    continue
                yield port

        return list(inner())

    def _query_rp2_boot_mode(self) -> list[Any]:
        devices = usb.core.find(
            idVendor=RP2_VENDOR, idProduct=RP2_PRODUCT_BOOT_MODE, find_all=True
        )
        return list(devices)

    def print_rp2_application_mode(self) -> list[Any]:
        for rp2 in self.list_rp2_mode_application:
            print(f"Application Mode: {rp2.device} {rp2.location} {rp2.serial_number}")

    def print_rp2_boot_mode(self) -> list[Any]:
        for rp2 in self.list_rp2_mode_boot:
            print(f"Boot Mode: {rp2.bus}-{rp2.port_numbers}")
            hub = rp2.parent
            if (hub.idVendor != OCTOHUB4_VENDOR) or (hub.idProduct != OCTOHUB4_PRODUCT):
                # Not connected to octohub
                print("  Not connected to octohub!")
                continue


def main() -> None:
    # rp2s = serial_find_rp2()
    # for rp2 in rp2s:
    #     print(rp2)

    qs = QuerySerial()
    qs.print_rp2_application_mode()
    qs.print_rp2_boot_mode()

    devices_octohub4 = usb.core.find(find_all=1, custom_match=find_octohub4())
    devices_octohub4 = list(devices_octohub4)

    for device_octohub in devices_octohub4:
        ports = ".".join(map(str, device_octohub.port_numbers))
        print(f"Octohub4 {device_octohub.bus}-{ports}")

    # devices_rp2 = usb.core.find(find_all=1, custom_match=find_rp2())
    devices_rp2 = usb.core.find(
        idVendor=RP2_VENDOR, idProduct=RP2_PRODUCT_APPLICATION_MODE, find_all=True
    )
    if False:
        for device_rp2 in devices_rp2:
            sn = usb.util.get_string(device_rp2, device_rp2.iSerialNumber, langid=1033)

    devices_rp2 = list(devices_rp2)

    for device_rp2 in devices_rp2:
        ports = ".".join(map(str, device_rp2.port_numbers))
        print(f"RP2 {device_rp2.bus}-{ports}")

        def find_octohub(device_rp2):
            for device_octohub in devices_octohub4:
                if device_rp2.bus != device_octohub.bus:
                    continue
                if device_rp2.port_numbers[:-1] == device_octohub.port_numbers:
                    return device_octohub
            raise IndexError("Not found")

        # https://github.com/pyusb/pyusb/issues/139#issuecomment-241149806
        # device_rp2._langids = (1033,)

        print(f"Serial: {device_rp2._get_full_descriptor_str()}")
        try:
            sn = usb.util.get_string(device_rp2, device_rp2.iSerialNumber, langid=1033)
            print(f"Serial2: {sn}")
        except Exception as e:
            print(f"ValueError {e}")

        device_octohub = find_octohub(device_rp2=device_rp2)
        print(f"  Octohub4: {device_octohub.bus}-{device_octohub.port_numbers}")


if __name__ == "__main__":
    main()
