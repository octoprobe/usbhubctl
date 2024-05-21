from usbhubctl import Topology, get_real_topology

from .util_subprocess import subprocess_run


def lsusb() -> Topology:
    args = ["lsusb", "--tree", "--verbose"]
    lsusb_output = subprocess_run(args=args)
    return get_real_topology(lsusb_output=lsusb_output)
