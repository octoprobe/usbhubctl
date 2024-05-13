from pyhubctl import Path
from pyhubctl.pyhubctl import BackendPowerABC


class BackendPowerSysFs(BackendPowerABC):
    def power(self, full_path: "Path", on: bool) -> None:
        pass
