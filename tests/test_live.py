"""
Test live usb hubs
"""

import time

import pytest

from usbhubctl import DualConnectedHub, DualConnectedHubs
from usbhubctl.known_hubs import octohub4, rsh_a10, rsh_a16, rsh_a107, rsh_st07c
from usbhubctl.util_logging import init_logging


def get_one_or_skip(connected_hubs: DualConnectedHubs) -> DualConnectedHub:
    try:
        return connected_hubs.get_one()
    except IndexError as e:
        pytest.skip(reason=f"Could not connect to '{connected_hubs.hub.model}': {e}")
        raise NotImplementedError() from e


@pytest.mark.live
def test_toggle_octohub4() -> None:
    connected_hubs = octohub4.find_connected_dualhubs()

    connected_hub = get_one_or_skip(connected_hubs)
    for plug in connected_hub.connected_plugs:
        plug.power(on=True)
    for plug in connected_hub.connected_plugs:
        plug.power(on=False)


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

    begin_s = time.monotonic()

    test_toggle_octohub4()
    # test_toggle_rsh_a10()
    # test_toggle_rsh_a107()

    print(f"Duration {time.monotonic()-begin_s:0.3f}s")
