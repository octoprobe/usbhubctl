"""
https://en.wikipedia.org/wiki/USB
https://github.com/pyusb/pyusb/blob/master/docs/tutorial.rst
"""

import dataclasses
import time

import usb.control
import usb.core
import usb.legacy
import usb.util


class FindUsbClass:
    def __init__(self, class_: int):
        self._class = class_

    def __call__(self, device: usb.core.Device) -> bool:
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
    path: list[int]
    address: int

    @property
    def pattern(self) -> tuple[list[int], str]:
        return (self.path, f"{self.vendor:04X}:{self.product:04X}")


def main() -> None:
    begin_s = time.monotonic()

    hub_devices = usb.core.find(
        find_all=1, custom_match=FindUsbClass(usb.legacy.CLASS_HUB)
    )
    hub_devices = list(hub_devices)

    dev = usb.core.find(idVendor=0x0BDA, idProduct=0x0411)
    print("_str(): ", dev._str())
    print("_get_full_descriptor_str(): ", dev._get_full_descriptor_str())
    print("dev", dev)

    def get_descriptor(dev, desc_size, desc_type, desc_index, wIndex=0):
        r"""Return the specified descriptor.

        dev is the Device object to which the request will be
        sent to.

        desc_size is the descriptor size.

        desc_type and desc_index are the descriptor type and index,
        respectively. wIndex index is used for string descriptors
        and represents the Language ID. For other types of descriptors,
        it is zero.
        """
        wValue = desc_index | (desc_type << 8)

        bmRequestType = usb.util.build_request_type(
            usb.util.CTRL_IN,
            usb.util.CTRL_TYPE_STANDARD,
            usb.util.CTRL_RECIPIENT_DEVICE,
        )

        desc = dev.ctrl_transfer(
            bmRequestType=bmRequestType,
            bRequest=0x06,
            wValue=wValue,
            wIndex=wIndex,
            data_or_wLength=desc_size,
        )

        if len(desc) < 2:
            raise usb.core.USBError("Invalid descriptor")

        return desc

    desc = get_descriptor(
        dev, desc_size=2, desc_type=usb.legacy.DT_HUB << 8, desc_index=0
    )
    print("desc:", desc)
    return

    # ret = dev.ctrl_transfer(0xC0, CTRL_LOOPBACK_READ, 0, 0, len(msg))

    # dev.set_configuration()

    cfg: usb.core.Configuration = dev.get_active_configuration()
    print("cfg: ", cfg)
    print("type(cfg): ", type(cfg))
    intf: usb.core.Interface = cfg[(0, 0)]

    print("intf: ", intf)
    print("type(intf): ", type(intf))

    return

    hubs: list[Hub] = []
    for hub in hub_devices:
        # print(f"  port_number={hub.port_number}({hub.port_numbers})")
        # print(hub)
        if hub.port_numbers is None:
            continue

        if (hub.idVendor == 0x0BDA) and (hub.idProduct == 0x0411):
            cfg = hub.get_active_configuration()
            intf = cfg[(0, 0)]

            alt = usb.util.find_descriptor(cfg, find_all=True, bInterfaceNumber=0)
            assert alt is not None
            for a in alt:
                print(f"{a=} {type(a)}")
                for i in a:
                    print(f"{i=}")

            if False:
                ep = usb.util.find_descriptor(
                    intf,
                    # match the first OUT endpoint
                    custom_match=lambda e: usb.util.endpoint_direction(
                        e.bEndpointAddress
                    )
                    == usb.util.ENDPOINT_OUT,
                )

                assert ep is not None

                # # write the data
                # ep.write("test")

        h = Hub(
            vendor=hub.idVendor,
            product=hub.idProduct,
            bus=hub.bus,
            path=hub.port_numbers,
            address=hub.address,
        )
        hubs.append(h)

    list_pattern = sorted([h.pattern for h in hubs])
    for pattern in list_pattern:
        print(pattern)
    print(f"*********** duration={time.monotonic()-begin_s:0.3f}s")


if __name__ == "__main__":
    main()
