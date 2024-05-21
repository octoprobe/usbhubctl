from usbhubctl import Path
from usbhubctl.usbhubctl import BackendPowerABC

from .util_subprocess import subprocess_run


class BackendPowerUhubctl(BackendPowerABC):
    def power(self, full_path: "Path", on: bool) -> None:
        """
        uhubctl -l 3-6.1 -p 1 --action on
        """
        action = "on" if on else "off"
        args = [
            "uhubctl",
            f"--location={full_path.uhubctl_location}",
            f"--ports={full_path.uhubctl_port}",
            # f"--vendor={full_path.product_id.text}",
            # "--nosysfs",
            f"--action={action}",
        ]
        subprocess_run(args=args)
