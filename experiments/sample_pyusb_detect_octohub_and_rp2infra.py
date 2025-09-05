# type: ignore
"""
https://en.wikipedia.org/wiki/USB
https://github.com/pyusb/pyusb/blob/master/docs/tutorial.rst


Find all rp3 in application mode (serial)
  *
Find all rp2 in programming mode (pyusb)
"""

from __future__ import annotations

import dataclasses
import logging
import time
import typing

import usb.core
import usb.util
from usb.legacy import CLASS_HUB

from usbhubctl.usbhubctl import Location

logger = logging.Logger(__file__)

OCTOHUB4_PORT_RP2_INFRA = 1
OCTOHUB4_PORT_RP2_BOOTMODE = 2
OCTOHUB4_PORT_DUT = 3
OCTOHUB4_PORT_LED_ERROR = 4

# lsusb -d 2e8a:0005 -v

RP2_VENDOR = 0x2E8A
RP2_PRODUCT_BOOT_MODE = 0x0003
RP2_PRODUCT_APPLICATION_MODE = 0x0005

# TODO: Reuse constants from usbhubctl/known_hubs/octohub4.py
OCTOHUB4_VENDOR = 0x0424
OCTOHUB4_PRODUCT = 0x2514


@dataclasses.dataclass
class Rp2:
    location: Location
    application_mode: bool
    port: int

    @staticmethod
    def factory(device: usb.core.Device, application_mode: bool) -> Location:
        return Rp2(
            location=Location.factory(device=device),
            application_mode=application_mode,
            port=OCTOHUB4_PORT_RP2_INFRA,
        )


@dataclasses.dataclass
class Tentacle:
    octohub4_location: Location

    rp2_infra: Rp2


class UsbTentacleQuery:
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
        def query_rp2() -> typing.Iterator[Rp2]:
            for device in usb.core.find(idVendor=RP2_VENDOR, find_all=True):
                assert device.idVendor == RP2_VENDOR
                if device.idProduct == RP2_PRODUCT_BOOT_MODE:
                    yield Rp2.factory(
                        device=device,
                        application_mode=False,
                    )
                if device.idProduct == RP2_PRODUCT_APPLICATION_MODE:
                    yield Rp2.factory(
                        device=device,
                        application_mode=True,
                    )

        self.list_rp2 = list(query_rp2())

        self.list_location_octohub4 = [
            Location.factory(d)
            for d in usb.core.find(
                find_all=True,
                bDeviceClass=CLASS_HUB,
                idVendor=OCTOHUB4_VENDOR,
                idProduct=OCTOHUB4_PRODUCT,
            )
        ]

        def get_rp2_infra(octohub4_location: Location) -> Tentacle | None:
            for rp2 in self.list_rp2:
                if rp2.location.is_my_hub(octohub4_location):
                    return Tentacle(octohub4_location=octohub4_location, rp2_infra=rp2)
            return None

        self.tentacles: list[Tentacle] = []
        for loc in self.list_location_octohub4:
            rp2_infra = get_rp2_infra(loc)
            if rp2_infra is None:
                continue
            self.tentacles.append(Tentacle(octohub4_location=loc, rp2_infra=rp2_infra))

        print("Hallo")


def main() -> None:
    time_start_s = time.monotonic()

    qs = UsbTentacleQuery()
    # qs.print_rp2_application_mode()
    # qs.print_rp2_boot_mode()
    print(f"{time.monotonic()-time_start_s:0.3f}s")


if __name__ == "__main__":
    main()
