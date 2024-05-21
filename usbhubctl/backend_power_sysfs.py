from .usbhubctl import BackendPowerABC, Path
from .util_subprocess import subprocess_run


class BackendPowerSysFs(BackendPowerABC):
    def power(self, full_paths: list["Path"], on: bool) -> None:
        """
        /usr/sbin/usbhubctl_sysfs /sys/bus/usb/devices/4-1:1.0/4-1-port1/disable 1
        """
        assert isinstance(full_paths, list)
        for full_path in full_paths:
            assert isinstance(full_path, Path)

        value = "0" if on else "1"

        args = ["usbhubctl_sysfs"]
        for full_path in full_paths:
            # path = f"/sys/bus/usb/devices/{full_path.uhubctl_location}:1.0/{full_path.uhubctl_location}-port{full_path.uhubctl_port}/disable"
            args.append(full_path.sysfs_path)
            args.append(value)
        subprocess_run(args=args)
