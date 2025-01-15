import logging
import pathlib

from .usbhubctl import BackendPowerABC, Path
from .util_subprocess import subprocess_run

logger = logging.getLogger(__file__)

FILENAME_USBHUBCTL_SYSFS = "usbhubctl_sysfs"

_DIRECT_WRITE = True


class BackendPowerSysFs(BackendPowerABC):
    def power(self, full_paths: list["Path"], on: bool) -> None:
        """
        usbhubctl_sysfs /sys/bus/usb/devices/4-1:1.0/4-1-port1/disable 1
        """
        assert isinstance(full_paths, list)
        for full_path in full_paths:
            assert isinstance(full_path, Path)

        value = "0" if on else "1"

        if _DIRECT_WRITE:
            for full_path in full_paths:
                pathlib.Path(full_path.sysfs_path).write_text(value)
                return

        args = [FILENAME_USBHUBCTL_SYSFS]
        for full_path in full_paths:
            # path = f"/sys/bus/usb/devices/{full_path.uhubctl_location}:1.0/{full_path.uhubctl_location}-port{full_path.uhubctl_port}/disable"
            args.append(full_path.sysfs_path)
            args.append(value)

        try:
            subprocess_run(args=args)
        except FileNotFoundError as e:
            a = f"The binary '{FILENAME_USBHUBCTL_SYSFS}' was not found in the PATH."
            b = "You have to compile and install it manually: https://github.com/octoprobe/usbhubctl/blob/main/usbhubctl_sysfs/README.md"
            raise FileNotFoundError(f"{a}\n{b}") from e
