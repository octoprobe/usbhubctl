from usbhubctl import Path
from usbhubctl.usbhubctl import BackendPowerABC

from .util_subprocess import subprocess_run


class BackendPowerUhubctl(BackendPowerABC):
    def set_power(self, full_paths: list["Path"], on: bool) -> None:
        """
        uhubctl -l 3-6.1 -p 1 --action on
        """
        # TODO: This is too much simplified!
        assert len(full_paths) == 1
        full_path = full_paths[0]

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

    def get_power(self, full_paths: list["Path"]) -> bool:
        raise NotImplementedError()
