"""
Test live usb hubs
"""

from usbhubctl.util_octohub4 import Octohubs


def main() -> None:
    hubs = Octohubs()
    hubs.reset_power()


if __name__ == "__main__":
    main()
