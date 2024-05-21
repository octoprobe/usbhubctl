from usbhubctl import Path
from usbhubctl.usbhubctl import BackendPowerABC


class BackendPowerSysFs(BackendPowerABC):
    def power(self, full_path: "Path", on: bool) -> None:
        pass
