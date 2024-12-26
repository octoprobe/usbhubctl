from __future__ import annotations

import usb.core
import usb.util
from usb.legacy import CLASS_HUB

from usbhubctl.usbhubctl import Location

from . import ConnectedHub, DualConnectedHub, Path
from .known_hubs import OCTOHUB4_PRODUCT_ID, octohub4


def path_2_connected_hub(path: Path) -> DualConnectedHub:
    """
    Example path: Path(product_id=ProductId(vendor=1060, product=9492), bus=3, path=[1, 4, 2])
    """
    return DualConnectedHub(
        hub=octohub4,
        connected_hub_usb2=ConnectedHub(hub=octohub4, root_path=path),
        connected_hub_usb3=None,
    )


def location_2_connected_hub(location: Location) -> DualConnectedHub:
    """
    Example path: Path(product_id=ProductId(vendor=1060, product=9492), bus=3, path=[1, 4, 2])
    """
    path = location.path_factory(product_id=OCTOHUB4_PRODUCT_ID)
    return path_2_connected_hub(path)


def location_2_path(location: str) -> Path:
    """
    TODO: Where the place this method?

    Example location: '3-1.4.1.1:1.0'
    This is returnemd from the 'location' property of the 'Device' object of the 'serial' library.
    """
    _location = Location.factory(device=location)
    return Path(
        product_id=OCTOHUB4_PRODUCT_ID,
        bus=_location.bus,
        path=_location.path,
    )


class Octohubs:
    """
    Find all octohub4.

    Set power on all octohub4.
    """

    def __init__(self) -> None:
        self._usb_paths = [
            Path(product_id=OCTOHUB4_PRODUCT_ID, bus=d.bus, path=d.port_numbers)
            for d in self.find_devices()
        ]
        """
        A list of USB usbhubctl.Path
        For example:
        [
          Path(product_id=ProductId(vendor=1060, product=9492), bus=3, path=[1, 4, 1]),
          Path(product_id=ProductId(vendor=1060, product=9492), bus=3, path=[1, 4, 2]),
        ]
        """

        self.hubs = [path_2_connected_hub(path) for path in self._usb_paths]

    @staticmethod
    def find_devices() -> list[usb.core.Device]:
        def find_octohub4(device: usb.core.Device) -> bool:
            if device.bDeviceClass == CLASS_HUB:
                if device.idVendor == OCTOHUB4_PRODUCT_ID.vendor:
                    if device.idProduct == OCTOHUB4_PRODUCT_ID.product:
                        return True
            return False

        devices = usb.core.find(find_all=1, custom_match=find_octohub4)
        return list(devices)

    def reset_power(self) -> None:
        """
        Power all Hubs:
          Plug1: on
          all other plugs: off
        """
        self.set_power(plug_on={1: True}, default_on=False)

    def set_power(
        self,
        plug_on: dict[int, bool],
        default_on: None | bool = None,
    ) -> None:
        """
        Set the power as specified in 'plug_on'.
        All other plugs will be set to 'default_on':
          True: power on
          False: power off
        if 'default_on' is None, the power will not be changed.
        """
        for hub in self.hubs:
            for plug0 in range(octohub4.plug_count):
                plug = plug0 + 1
                on = plug_on.get(plug, default_on)
                if on is not None:
                    hub.get_plug(plug).power(on=on)

    def find(self, usb_path_rp2: Path) -> DualConnectedHub:
        """
        The path for the rp2 is given.
        We now find the usb hub on the tentacle.
        """
        usb_path_for_hub = usb_path_rp2.path[:-1]
        for hub in self.hubs:
            if hub.connected_hub_usb2.root_path.bus == usb_path_rp2.bus:
                if hub.connected_hub_usb2.root_path.path == usb_path_for_hub:
                    return hub
        raise IndexError(f"Hub for RP2 with path {usb_path_rp2} not found")
