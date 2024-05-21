"""
Test live usb hubs
"""

import pytest

from usbhubctl import DualConnectedHub, DualConnectedHubs
from usbhubctl.known_hubs import rsh_a10, rsh_a16, rsh_a107, rsh_st07c
from usbhubctl.util_logging import init_logging


def get_one_or_skip(connected_hubs: DualConnectedHubs) -> DualConnectedHub:
    try:
        return connected_hubs.get_one()
    except Exception as e:
        pytest.skip(msg=f"Could not connect to '{connected_hubs.hub}': {e}")


@pytest.mark.live
def test_toggle_rsh_a10() -> None:
    connected_hubs = rsh_a10.find_connected_dualhubs()

    connected_hub = get_one_or_skip(connected_hubs)
    for plug in connected_hub.connected_plugs:
        plug.power(on=True)
    for plug in connected_hub.connected_plugs:
        plug.power(on=False)


@pytest.mark.live
def test_toggle_rsh_a16() -> None:
    connected_hubs = rsh_a16.find_connected_dualhubs()

    connected_hub = get_one_or_skip(connected_hubs)
    for plug in connected_hub.connected_plugs:
        plug.power(on=True)

    for plug in connected_hub.connected_plugs:
        plug.power(on=False)


@pytest.mark.live
def test_toggle_rsh_a16_plug1() -> None:
    connected_hubs = rsh_a16.find_connected_dualhubs()

    connected_hub = get_one_or_skip(connected_hubs)
    plug = connected_hub.get_plug(1)
    plug.power(on=True)
    plug.power(on=False)


@pytest.mark.live
def test_toggle_rsh_st07c() -> None:
    connected_hubs = rsh_st07c.find_connected_dualhubs()

    connected_hub = get_one_or_skip(connected_hubs)
    for plug in connected_hub.connected_plugs:
        plug.power(on=True)
    for plug in connected_hub.connected_plugs:
        plug.power(on=False)


@pytest.mark.live
def test_toggle_rsh_a107() -> None:
    connected_hubs = rsh_a107.find_connected_dualhubs()

    connected_hub = get_one_or_skip(connected_hubs)
    for plug in connected_hub.connected_plugs:
        plug.power(on=True)
    for plug in connected_hub.connected_plugs:
        plug.power(on=False)


if __name__ == "__main__":
    init_logging()

    # test_toggle_rsh_a10()
    # test_toggle_rsh_a107()
    test_toggle_rsh_st07c()


"""
/sys/devices/pci0000:00/0000:00:14.0/usb3/3-6/3-6.1/power
echo on > control


/sys/devices/pci0000:00/0000:00:14.0/usb3/3-6/3-6.1/3-6.1:1.0/3-6.1-port1/power

/sys/devices/pci0000:00/0000:00:14.0/usb3/3-6/3-6.1/3-6.1:1.0/3-6.1-port1/disable
  echo 1 / 0
  ==> Only works after 'uhubctl -l 3-6.1 -p 1 --action on'

uhubctl -l 3-6.1 -p 1 --action on


------------------------
cd /sys/bus/usb/devices/3-6.1:1.0
cd 3-6.1-port1

=========usb2

cd /sys/bus/usb/devices/2-3.1:1.0
cd 2-3.1-port1
echo 1 > disable

=====================
echo 1 > /sys/bus/usb/devices/2-3.1:1.0/2-3.1-port1/disable
echo 1 > /sys/bus/usb/devices/3-6.1:1.0/3-6.1-port1/disable

"""
