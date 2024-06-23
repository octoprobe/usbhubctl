from usbhubctl import Topology, get_real_topology

LSUSB_OUTPUT_RSH_A16 = """
/:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/1p, 480M
    ID 1d6b:0002 Linux Foundation 2.0 root hub
/:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/4p, 10000M
    ID 1d6b:0003 Linux Foundation 3.0 root hub
    |__ Port 003: Dev 002, If 0, Class=Hub, Driver=hub/4p, 5000M
        ID 05e3:0626 Genesys Logic, Inc. Hub
        |__ Port 001: Dev 003, If 0, Class=Hub, Driver=hub/4p, 5000M
            ID 0bda:0411 Realtek Semiconductor Corp. Hub
            |__ Port 003: Dev 005, If 0, Class=Hub, Driver=hub/4p, 5000M
                ID 0bda:0411 Realtek Semiconductor Corp. Hub
                |__ Port 003: Dev 007, If 0, Class=Hub, Driver=hub/4p, 5000M
                    ID 0bda:0411 Realtek Semiconductor Corp. Hub
                |__ Port 004: Dev 008, If 0, Class=Hub, Driver=hub/4p, 5000M
                    ID 0bda:0411 Realtek Semiconductor Corp. Hub
            |__ Port 004: Dev 006, If 0, Class=Hub, Driver=hub/4p, 5000M
                ID 0bda:0411 Realtek Semiconductor Corp. Hub
        |__ Port 004: Dev 004, If 0, Class=Vendor Specific Class, Driver=r8152, 5000M
            ID 0bda:8153 Realtek Semiconductor Corp. RTL8153 Gigabit Ethernet Adapter
/:  Bus 003.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/12p, 480M
    ID 1d6b:0002 Linux Foundation 2.0 root hub
    |__ Port 001: Dev 002, If 0, Class=Human Interface Device, Driver=usbhid, 12M
        ID 046d:c534 Logitech, Inc. Unifying Receiver
    |__ Port 001: Dev 002, If 1, Class=Human Interface Device, Driver=usbhid, 12M
        ID 046d:c534 Logitech, Inc. Unifying Receiver
    |__ Port 003: Dev 003, If 0, Class=Vendor Specific Class, Driver=[none], 12M
        ID 06cb:00f9 Synaptics, Inc. 
    |__ Port 004: Dev 004, If 0, Class=Video, Driver=uvcvideo, 480M
        ID 13d3:5405 IMC Networks 
    |__ Port 004: Dev 004, If 1, Class=Video, Driver=uvcvideo, 480M
        ID 13d3:5405 IMC Networks 
    |__ Port 004: Dev 004, If 2, Class=Video, Driver=uvcvideo, 480M
        ID 13d3:5405 IMC Networks 
    |__ Port 004: Dev 004, If 3, Class=Video, Driver=uvcvideo, 480M
        ID 13d3:5405 IMC Networks 
    |__ Port 004: Dev 004, If 4, Class=Application Specific Interface, Driver=[none], 480M
        ID 13d3:5405 IMC Networks 
    |__ Port 006: Dev 005, If 0, Class=Hub, Driver=hub/4p, 480M
        ID 05e3:0610 Genesys Logic, Inc. Hub
        |__ Port 001: Dev 007, If 0, Class=Hub, Driver=hub/4p, 480M
            ID 0bda:5411 Realtek Semiconductor Corp. RTS5411 Hub
            |__ Port 003: Dev 008, If 0, Class=Hub, Driver=hub/4p, 480M
                ID 0bda:5411 Realtek Semiconductor Corp. RTS5411 Hub
                |__ Port 003: Dev 010, If 0, Class=Hub, Driver=hub/4p, 480M
                    ID 0bda:5411 Realtek Semiconductor Corp. RTS5411 Hub
                |__ Port 004: Dev 011, If 0, Class=Hub, Driver=hub/4p, 480M
                    ID 0bda:5411 Realtek Semiconductor Corp. RTS5411 Hub
            |__ Port 004: Dev 009, If 0, Class=Hub, Driver=hub/4p, 480M
                ID 0bda:5411 Realtek Semiconductor Corp. RTS5411 Hub
/:  Bus 004.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/4p, 10000M
    ID 1d6b:0003 Linux Foundation 3.0 root hub
"""

LSUSB_OUTPUT_RSH_A16_EXPECTED_SHORT = """
2-3
2-3.1
2-3.1.3
2-3.1.3.3
2-3.1.3.4
2-3.1.4
3-6
3-6.1
3-6.1.3
3-6.1.3.3
3-6.1.3.4
3-6.1.4
""".strip()


LSUSB_OUTPUT_RSH_A10 = """
/:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/1p, 480M
    ID 1d6b:0002 Linux Foundation 2.0 root hub
/:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/4p, 10000M
    ID 1d6b:0003 Linux Foundation 3.0 root hub
    |__ Port 003: Dev 002, If 0, Class=Hub, Driver=hub/4p, 5000M
        ID 05e3:0626 Genesys Logic, Inc. Hub
        |__ Port 003: Dev 003, If 0, Class=Hub, Driver=hub/4p, 5000M
            ID 0bda:0411 Realtek Semiconductor Corp. Hub
            |__ Port 003: Dev 005, If 0, Class=Hub, Driver=hub/4p, 5000M
                ID 0bda:0411 Realtek Semiconductor Corp. Hub
            |__ Port 004: Dev 006, If 0, Class=Hub, Driver=hub/4p, 5000M
                ID 0bda:0411 Realtek Semiconductor Corp. Hub
        |__ Port 004: Dev 004, If 0, Class=Vendor Specific Class, Driver=r8152, 5000M
            ID 0bda:8153 Realtek Semiconductor Corp. RTL8153 Gigabit Ethernet Adapter
/:  Bus 003.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/12p, 480M
    ID 1d6b:0002 Linux Foundation 2.0 root hub
    |__ Port 003: Dev 003, If 0, Class=Vendor Specific Class, Driver=[none], 12M
        ID 06cb:00f9 Synaptics, Inc. 
    |__ Port 004: Dev 004, If 0, Class=Video, Driver=uvcvideo, 480M
        ID 13d3:5405 IMC Networks 
    |__ Port 004: Dev 004, If 1, Class=Video, Driver=uvcvideo, 480M
        ID 13d3:5405 IMC Networks 
    |__ Port 004: Dev 004, If 2, Class=Video, Driver=uvcvideo, 480M
        ID 13d3:5405 IMC Networks 
    |__ Port 004: Dev 004, If 3, Class=Video, Driver=uvcvideo, 480M
        ID 13d3:5405 IMC Networks 
    |__ Port 004: Dev 004, If 4, Class=Application Specific Interface, Driver=[none], 480M
        ID 13d3:5405 IMC Networks 
    |__ Port 006: Dev 006, If 0, Class=Hub, Driver=hub/4p, 480M
        ID 05e3:0610 Genesys Logic, Inc. Hub
        |__ Port 003: Dev 007, If 0, Class=Hub, Driver=hub/4p, 480M
            ID 0bda:5411 Realtek Semiconductor Corp. RTS5411 Hub
            |__ Port 001: Dev 008, If 0, Class=Mass Storage, Driver=usb-storage, 12M
                ID 2e8a:0003  
            |__ Port 001: Dev 008, If 1, Class=Vendor Specific Class, Driver=[none], 12M
                ID 2e8a:0003  
            |__ Port 003: Dev 009, If 0, Class=Hub, Driver=hub/4p, 480M
                ID 0bda:5411 Realtek Semiconductor Corp. RTS5411 Hub
            |__ Port 004: Dev 010, If 0, Class=Hub, Driver=hub/4p, 480M
                ID 0bda:5411 Realtek Semiconductor Corp. RTS5411 Hub
    |__ Port 007: Dev 012, If 0, Class=Human Interface Device, Driver=usbhid, 12M
        ID 046d:c534 Logitech, Inc. Unifying Receiver
    |__ Port 007: Dev 012, If 1, Class=Human Interface Device, Driver=usbhid, 12M
        ID 046d:c534 Logitech, Inc. Unifying Receiver
/:  Bus 004.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/4p, 10000M
    ID 1d6b:0003 Linux Foundation 3.0 root hub
"""

LSUSB_OUTPUT_RSH_A10_EXPECTED_SHORT = """
2-3
2-3.3
2-3.3.3
2-3.3.4
3-6
3-6.3
3-6.3.3
3-6.3.4
""".strip()

LSUSB_OUTPUT_OCTOHUB4 = """
/:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/1p, 480M
    ID 1d6b:0002 Linux Foundation 2.0 root hub
/:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/4p, 10000M
    ID 1d6b:0003 Linux Foundation 3.0 root hub
/:  Bus 003.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/12p, 480M
    ID 1d6b:0002 Linux Foundation 2.0 root hub
    |__ Port 001: Dev 026, If 0, Class=Hub, Driver=hub/4p, 480M
        ID 0424:2514 Microchip Technology, Inc. (formerly SMSC) USB 2.0 Hub
        |__ Port 001: Dev 027, 12M
            ID f055:9800  
        |__ Port 003: Dev 028, 12M
            ID 2e8a:0005  
    |__ Port 003: Dev 002, If 0, Class=Vendor Specific Class, Driver=[none], 12M
        ID 06cb:00f9 Synaptics, Inc. 
    |__ Port 004: Dev 003, If 0, Class=Video, Driver=uvcvideo, 480M
        ID 13d3:5405 IMC Networks 
    |__ Port 004: Dev 003, If 1, Class=Video, Driver=uvcvideo, 480M
        ID 13d3:5405 IMC Networks 
    |__ Port 004: Dev 003, If 2, Class=Video, Driver=uvcvideo, 480M
        ID 13d3:5405 IMC Networks 
    |__ Port 004: Dev 003, If 3, Class=Video, Driver=uvcvideo, 480M
        ID 13d3:5405 IMC Networks 
    |__ Port 004: Dev 003, If 4, Class=Application Specific Interface, Driver=[none], 480M
        ID 13d3:5405 IMC Networks 
    |__ Port 005: Dev 012, If 0, Class=Hub, Driver=hub/4p, 480M
        ID 1a40:0801 Terminus Technology Inc. 
        |__ Port 002: Dev 018, If 0, Class=Hub, Driver=hub/4p, 480M
            ID 0bda:5411 Realtek Semiconductor Corp. RTS5411 Hub
            |__ Port 003: Dev 019, If 0, Class=Hub, Driver=hub/4p, 480M
                ID 0bda:5411 Realtek Semiconductor Corp. RTS5411 Hub
                |__ Port 001: Dev 021, If 0, Class=Human Interface Device, Driver=usbhid, 1.5M
                    ID 413c:2107 Dell Computer Corp. KB212-B Quiet Key Keyboard
                |__ Port 002: Dev 022, If 0, Class=Human Interface Device, Driver=usbhid, 1.5M
                    ID 03f0:154a HP, Inc Laser Mouse
            |__ Port 004: Dev 020, If 0, Class=Hub, Driver=hub/4p, 480M
                ID 0bda:5411 Realtek Semiconductor Corp. RTS5411 Hub
                |__ Port 003: Dev 023, If 0, Class=Hub, Driver=hub/4p, 12M
                    ID 0a12:4010 Cambridge Silicon Radio, Ltd 
                    |__ Port 001: Dev 025, If 0, Class=Audio, Driver=snd-usb-audio, 12M
                        ID 0b0e:24c8 GN Netcom 
                    |__ Port 001: Dev 025, If 1, Class=Audio, Driver=snd-usb-audio, 12M
                        ID 0b0e:24c8 GN Netcom 
                    |__ Port 001: Dev 025, If 2, Class=Audio, Driver=snd-usb-audio, 12M
                        ID 0b0e:24c8 GN Netcom 
                    |__ Port 001: Dev 025, If 3, Class=Human Interface Device, Driver=usbhid, 12M
                        ID 0b0e:24c8 GN Netcom 
                |__ Port 004: Dev 024, If 0, Class=Vendor Specific Class, Driver=usbfs, 480M
                    ID 2717:ff40 Xiaomi Inc. Mi/Redmi series (MTP)
        |__ Port 004: Dev 013, If 0, Class=Vendor Specific Class, Driver=r8152, 480M
            ID 0bda:8152 Realtek Semiconductor Corp. RTL8152 Fast Ethernet Adapter
/:  Bus 004.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/4p, 10000M
    ID 1d6b:0003 Linux Foundation 3.0 root hub
"""


LSUSB_OUTPUT_OCTOHUB4_EXPECTED_SHORT = """
3-1
3-5
3-5.2
3-5.2.3
3-5.2.4
3-5.2.4.3
""".strip()


def test_parser_lsusb_A16() -> None:
    topology = get_real_topology(lsusb_output=LSUSB_OUTPUT_RSH_A16)
    assert topology.short == LSUSB_OUTPUT_RSH_A16_EXPECTED_SHORT


def test_parser_lsusb_A10() -> None:
    topology = get_real_topology(lsusb_output=LSUSB_OUTPUT_RSH_A10)
    assert topology.short == LSUSB_OUTPUT_RSH_A10_EXPECTED_SHORT


def test_parser_lsusb_Octohub4() -> None:
    topology = get_real_topology(lsusb_output=LSUSB_OUTPUT_OCTOHUB4)
    assert topology.short == LSUSB_OUTPUT_OCTOHUB4_EXPECTED_SHORT
