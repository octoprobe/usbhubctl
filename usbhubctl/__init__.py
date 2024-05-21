__version__ = "0.0.1"

__all__ = [
    "Hub",
    "HubChip",
    "Path",
    "ProductId",
    "DualProductId",
    "DualConnectedHub",
    "DualConnectedHubs",
    "Topology",
    "ConnectedHub",
    "ConnectedHubs",
    "ConnectedPlug",
    "BackendPowerABC",
]

from .usbhubctl import (
    Hub,
    HubChip,
    Path,
    ProductId,
    DualConnectedHub,
    DualConnectedHubs,
    DualProductId,
    Topology,
    ConnectedHub,
    ConnectedHubs,
    ConnectedPlug,
    BackendPowerABC,
)
from .parser_lsusb import get_real_topology
