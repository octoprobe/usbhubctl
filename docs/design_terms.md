# Terms

| Context | Term | Origin | Remarks |
| - | - | - | - |
| usbhubctl | Hub | shops | A usb hub with for example 16 plugs (not ports - see below). Internally a usb hub typically consists of multiple HubChips. |
| usbhubctl | plug | invention | 
| usbhubctl | port | USB Spec |
| | bus | USB Spec | A PC has multiple usb buses. Each bus drives a RootHubChip |
| SW Internals | HubChip | USB Spec: HubControler | A chip with one upstream port and multiple downstream ports |
| SW Internals | RootHubChip | USB Spec / lsusb | The HubChip typically internally to a PC connected to the USB bus |
| SW Internals | Downstream | USB Spec | Directon PC to plug |
| SW Internals | Upstream | USB Spec | Directon plug to the PC |
| SW Internals | Topology | invention | Describes how HubChips are connected |
| SW Internals | Internal Topology | invention | Describes how HubChips are connected internally within a hub |
