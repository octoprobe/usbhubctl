# RSHTECH_RSH-A16.md

https://de.rshtech.com/products/16-ports-aluminum-usb-30-data-hub-with-12v-83a-with-uk-power-adapterrsh-a16

https://www.amazon.de/gp/product/B09YH7VPKR
EUR63

![Image](https://de.rshtech.com/u_file/2011/products/12/c24d6de5bd.jpg)

![Image](https://de.rshtech.com/u_file/2011/products/12/064aaeecf5.jpg)

## Assessment

Are very similar RSH-A10 / RSH-A16

* **Overall: Usable for power switching**

* Positive: Power on/off works fine on every port
* Negative: LEDs hardly visible
* Negative: Ports are not numbered
* Negative: Switching using uhubctl is slow: 2.5s
* Negative: Power on/off ONLY works when the button is in pressed state

## Links where this HUB is mentioned

* https://github.com/mvp/uhubctl/blob/master/README.md
* https://github.com/mvp/uhubctl/issues/276
* https://github.com/mvp/uhubctl/issues/417

## Hub Topology

See [rsh_a16.py](../pyhubctl/known_hubs/rsh_a16.py)

## Internals

```
sudo uhubctl 
Current status for hub 4-1.4 [0bda:0411 Generic USB3.2 Hub, USB 3.20, 4 ports, ppps]
  Port 1: 02a0 power 5gbps Rx.Detect
  Port 2: 02a0 power 5gbps Rx.Detect
  Port 3: 02a0 power 5gbps Rx.Detect
  Port 4: 02a0 power 5gbps Rx.Detect
Current status for hub 4-1.3.4 [0bda:0411 Generic USB3.2 Hub, USB 3.20, 4 ports, ppps]
  Port 1: 02a0 power 5gbps Rx.Detect
  Port 2: 02a0 power 5gbps Rx.Detect
  Port 3: 02a0 power 5gbps Rx.Detect
  Port 4: 02a0 power 5gbps Rx.Detect
Current status for hub 4-1.3.3 [0bda:0411 Generic USB3.2 Hub, USB 3.20, 4 ports, ppps]
  Port 1: 02a0 power 5gbps Rx.Detect
  Port 2: 02a0 power 5gbps Rx.Detect
  Port 3: 02a0 power 5gbps Rx.Detect
  Port 4: 02a0 power 5gbps Rx.Detect
Current status for hub 4-1.3 [0bda:0411 Generic USB3.2 Hub, USB 3.20, 4 ports, ppps]
  Port 1: 02a0 power 5gbps Rx.Detect
  Port 2: 02a0 power 5gbps Rx.Detect
  Port 3: 0263 power 5gbps U3 enable connect [0bda:0411 Generic USB3.2 Hub, USB 3.20, 4 ports, ppps]
  Port 4: 0263 power 5gbps U3 enable connect [0bda:0411 Generic USB3.2 Hub, USB 3.20, 4 ports, ppps]
Current status for hub 4-1 [0bda:0411 Generic USB3.2 Hub, USB 3.20, 4 ports, ppps]
  Port 1: 02a0 power 5gbps Rx.Detect
  Port 2: 02a0 power 5gbps Rx.Detect
  Port 3: 0263 power 5gbps U3 enable connect [0bda:0411 Generic USB3.2 Hub, USB 3.20, 4 ports, ppps]
  Port 4: 0263 power 5gbps U3 enable connect [0bda:0411 Generic USB3.2 Hub, USB 3.20, 4 ports, ppps]
Current status for hub 3-1.4 [0bda:5411 Generic USB2.1 Hub, USB 2.10, 4 ports, ppps]
  Port 1: 0100 power
  Port 2: 0100 power
  Port 3: 0100 power
  Port 4: 0100 power
Current status for hub 3-1.3.4 [0bda:5411 Generic USB2.1 Hub, USB 2.10, 4 ports, ppps]
  Port 1: 0100 power
  Port 2: 0100 power
  Port 3: 0100 power
  Port 4: 0100 power
Current status for hub 3-1.3.3 [0bda:5411 Generic USB2.1 Hub, USB 2.10, 4 ports, ppps]
  Port 1: 0100 power
  Port 2: 0100 power
  Port 3: 0100 power
  Port 4: 0100 power
Current status for hub 3-1.3 [0bda:5411 Generic USB2.1 Hub, USB 2.10, 4 ports, ppps]
  Port 1: 0100 power
  Port 2: 0100 power
  Port 3: 0507 power highspeed suspend enable connect [0bda:5411 Generic USB2.1 Hub, USB 2.10, 4 ports, ppps]
  Port 4: 0507 power highspeed suspend enable connect [0bda:5411 Generic USB2.1 Hub, USB 2.10, 4 ports, ppps]
Current status for hub 3-1 [0bda:5411 Generic USB2.1 Hub, USB 2.10, 4 ports, ppps]
  Port 1: 0100 power
  Port 2: 0100 power
  Port 3: 0507 power highspeed suspend enable connect [0bda:5411 Generic USB2.1 Hub, USB 2.10, 4 ports, ppps]
  Port 4: 0507 power highspeed suspend enable connect [0bda:5411 Generic USB2.1 Hub, USB 2.10, 4 ports, ppps]
```

```
# sudo dmesg --follow
[ 1666.061134] usb 3-1: new high-speed USB device number 28 using xhci_hcd
[ 1666.224422] usb 3-1: New USB device found, idVendor=0bda, idProduct=5411, bcdDevice= 0.04
[ 1666.224433] usb 3-1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 1666.224438] usb 3-1: Product: USB2.1 Hub
[ 1666.224441] usb 3-1: Manufacturer: Generic
[ 1666.227084] hub 3-1:1.0: USB hub found
[ 1666.229445] hub 3-1:1.0: 4 ports detected
[ 1666.341561] usb 4-1: new SuperSpeed USB device number 12 using xhci_hcd
[ 1666.381556] usb 4-1: New USB device found, idVendor=0bda, idProduct=0411, bcdDevice= 0.04
[ 1666.381565] usb 4-1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 1666.381567] usb 4-1: Product: USB3.2 Hub
[ 1666.381569] usb 4-1: Manufacturer: Generic
[ 1666.387103] hub 4-1:1.0: USB hub found
[ 1666.389916] hub 4-1:1.0: 4 ports detected
[ 1666.521128] usb 3-1.3: new high-speed USB device number 29 using xhci_hcd
[ 1666.635002] usb 3-1.3: New USB device found, idVendor=0bda, idProduct=5411, bcdDevice= 0.04
[ 1666.635015] usb 3-1.3: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 1666.635019] usb 3-1.3: Product: USB2.1 Hub
[ 1666.635022] usb 3-1.3: Manufacturer: Generic
[ 1666.637491] hub 3-1.3:1.0: USB hub found
[ 1666.638784] hub 3-1.3:1.0: 4 ports detected
[ 1666.713976] usb 4-1.3: new SuperSpeed USB device number 13 using xhci_hcd
[ 1666.749832] usb 4-1.3: New USB device found, idVendor=0bda, idProduct=0411, bcdDevice= 0.04
[ 1666.749843] usb 4-1.3: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 1666.749847] usb 4-1.3: Product: USB3.2 Hub
[ 1666.749850] usb 4-1.3: Manufacturer: Generic
[ 1666.756949] hub 4-1.3:1.0: USB hub found
[ 1666.758395] hub 4-1.3:1.0: 4 ports detected
[ 1666.821133] usb 3-1.4: new high-speed USB device number 30 using xhci_hcd
[ 1666.936679] usb 3-1.4: New USB device found, idVendor=0bda, idProduct=5411, bcdDevice= 0.04
[ 1666.936692] usb 3-1.4: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 1666.936696] usb 3-1.4: Product: USB2.1 Hub
[ 1666.936699] usb 3-1.4: Manufacturer: Generic
[ 1666.939718] hub 3-1.4:1.0: USB hub found
[ 1666.941110] hub 3-1.4:1.0: 4 ports detected
[ 1667.009794] usb 4-1.4: new SuperSpeed USB device number 14 using xhci_hcd
[ 1667.043710] usb 4-1.4: New USB device found, idVendor=0bda, idProduct=0411, bcdDevice= 0.04
[ 1667.043714] usb 4-1.4: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 1667.043715] usb 4-1.4: Product: USB3.2 Hub
[ 1667.043716] usb 4-1.4: Manufacturer: Generic
[ 1667.051265] hub 4-1.4:1.0: USB hub found
[ 1667.053349] hub 4-1.4:1.0: 4 ports detected
[ 1667.113091] usb 3-1.3.3: new high-speed USB device number 31 using xhci_hcd
[ 1667.225908] usb 3-1.3.3: New USB device found, idVendor=0bda, idProduct=5411, bcdDevice= 0.04
[ 1667.225915] usb 3-1.3.3: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 1667.225917] usb 3-1.3.3: Product: USB2.1 Hub
[ 1667.225918] usb 3-1.3.3: Manufacturer: Generic
[ 1667.228721] hub 3-1.3.3:1.0: USB hub found
[ 1667.229858] hub 3-1.3.3:1.0: 4 ports detected
[ 1667.310066] usb 4-1.3.3: new SuperSpeed USB device number 15 using xhci_hcd
[ 1667.346760] usb 4-1.3.3: New USB device found, idVendor=0bda, idProduct=0411, bcdDevice= 0.04
[ 1667.346772] usb 4-1.3.3: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 1667.346776] usb 4-1.3.3: Product: USB3.2 Hub
[ 1667.346778] usb 4-1.3.3: Manufacturer: Generic
[ 1667.349589] hub 4-1.3.3:1.0: USB hub found
[ 1667.352598] hub 4-1.3.3:1.0: 4 ports detected
[ 1667.421122] usb 3-1.3.4: new high-speed USB device number 32 using xhci_hcd
[ 1667.537187] usb 3-1.3.4: New USB device found, idVendor=0bda, idProduct=5411, bcdDevice= 0.04
[ 1667.537199] usb 3-1.3.4: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 1667.537203] usb 3-1.3.4: Product: USB2.1 Hub
[ 1667.537205] usb 3-1.3.4: Manufacturer: Generic
[ 1667.540339] hub 3-1.3.4:1.0: USB hub found
[ 1667.541635] hub 3-1.3.4:1.0: 4 ports detected
[ 1667.613915] usb 4-1.3.4: new SuperSpeed USB device number 16 using xhci_hcd
[ 1667.649480] usb 4-1.3.4: New USB device found, idVendor=0bda, idProduct=0411, bcdDevice= 0.04
[ 1667.649484] usb 4-1.3.4: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 1667.649485] usb 4-1.3.4: Product: USB3.2 Hub
[ 1667.649486] usb 4-1.3.4: Manufacturer: Generic
[ 1667.652195] hub 4-1.3.4:1.0: USB hub found
[ 1667.653592] hub 4-1.3.4:1.0: 4 ports detected
```

```
sudo lsusb -d 0bda:0411 -v

Bus 004 Device 029: ID 0bda:0411 Realtek Semiconductor Corp. Hub
Device Descriptor:
  bLength                18
  bDescriptorType         1
  bcdUSB               3.20
  bDeviceClass            9 Hub
  bDeviceSubClass         0 
  bDeviceProtocol         3 
  bMaxPacketSize0         9
  idVendor           0x0bda Realtek Semiconductor Corp.
  idProduct          0x0411 Hub
  bcdDevice            0.04
  iManufacturer           1 Generic
  iProduct                2 USB3.2 Hub
  iSerial                 0 
  bNumConfigurations      1
  Configuration Descriptor:
    bLength                 9
    bDescriptorType         2
    wTotalLength       0x001f
    bNumInterfaces          1
    bConfigurationValue     1
    iConfiguration          0 
    bmAttributes         0xe0
      Self Powered
      Remote Wakeup
    MaxPower                0mA
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        0
      bAlternateSetting       0
      bNumEndpoints           1
      bInterfaceClass         9 Hub
      bInterfaceSubClass      0 
      bInterfaceProtocol      0 Full speed (or root) hub
      iInterface              0 
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x81  EP 1 IN
        bmAttributes           19
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Feedback
        wMaxPacketSize     0x0002  1x 2 bytes
        bInterval               8
        bMaxBurst               0
Binary Object Store Descriptor:
  bLength                 5
  bDescriptorType        15
  wTotalLength       0x002a
  bNumDeviceCaps          3
  USB 2.0 Extension Device Capability:
    bLength                 7
    bDescriptorType        16
    bDevCapabilityType      2
    bmAttributes   0x0000f41e
      BESL Link Power Management (LPM) Supported
    BESL value     1024 us 
    Deep BESL value    61440 us 
  SuperSpeed USB Device Capability:
    bLength                10
    bDescriptorType        16
    bDevCapabilityType      3
    bmAttributes         0x00
    wSpeedsSupported   0x000e
      Device can operate at Full Speed (12Mbps)
      Device can operate at High Speed (480Mbps)
      Device can operate at SuperSpeed (5Gbps)
    bFunctionalitySupport   1
      Lowest fully-functional device speed is Full Speed (12Mbps)
    bU1DevExitLat          10 micro seconds
    bU2DevExitLat        1023 micro seconds
  Container ID Device Capability:
    bLength                20
    bDescriptorType        16
    bDevCapabilityType      4
    bReserved               0
    ContainerID             {20b9cde5-7039-e011-a935-0002a5d5c51b}
Hub Descriptor:
  bLength              12
  bDescriptorType      42
  nNbrPorts             4
  wHubCharacteristic 0x0009
    Per-port power switching
    Per-port overcurrent protection
  bPwrOn2PwrGood        0 * 2 milli seconds
  bHubContrCurrent      8 milli Ampere
  bHubDecLat          0.2 micro seconds
  wHubDelay          3202 nano seconds
  DeviceRemovable    0x00
 Hub Port Status:
   Port 1: 0000.02a0 5Gbps power Rx.Detect
   Port 2: 0000.02a0 5Gbps power Rx.Detect
   Port 3: 0000.02a0 5Gbps power Rx.Detect
   Port 4: 0000.02a0 5Gbps power Rx.Detect
Device Status:     0x000d
  Self Powered
  U1 Enabled
  U2 Enabled

Bus 004 Device 031: ID 0bda:0411 Realtek Semiconductor Corp. Hub
Device Descriptor:
  bLength                18
  bDescriptorType         1
  bcdUSB               3.20
  bDeviceClass            9 Hub
  bDeviceSubClass         0 
  bDeviceProtocol         3 
  bMaxPacketSize0         9
  idVendor           0x0bda Realtek Semiconductor Corp.
  idProduct          0x0411 Hub
  bcdDevice            0.04
  iManufacturer           1 Generic
  iProduct                2 USB3.2 Hub
  iSerial                 0 
  bNumConfigurations      1
  Configuration Descriptor:
    bLength                 9
    bDescriptorType         2
    wTotalLength       0x001f
    bNumInterfaces          1
    bConfigurationValue     1
    iConfiguration          0 
    bmAttributes         0xe0
      Self Powered
      Remote Wakeup
    MaxPower                0mA
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        0
      bAlternateSetting       0
      bNumEndpoints           1
      bInterfaceClass         9 Hub
      bInterfaceSubClass      0 
      bInterfaceProtocol      0 Full speed (or root) hub
      iInterface              0 
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x81  EP 1 IN
        bmAttributes           19
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Feedback
        wMaxPacketSize     0x0002  1x 2 bytes
        bInterval               8
        bMaxBurst               0
Binary Object Store Descriptor:
  bLength                 5
  bDescriptorType        15
  wTotalLength       0x002a
  bNumDeviceCaps          3
  USB 2.0 Extension Device Capability:
    bLength                 7
    bDescriptorType        16
    bDevCapabilityType      2
    bmAttributes   0x0000f41e
      BESL Link Power Management (LPM) Supported
    BESL value     1024 us 
    Deep BESL value    61440 us 
  SuperSpeed USB Device Capability:
    bLength                10
    bDescriptorType        16
    bDevCapabilityType      3
    bmAttributes         0x00
    wSpeedsSupported   0x000e
      Device can operate at Full Speed (12Mbps)
      Device can operate at High Speed (480Mbps)
      Device can operate at SuperSpeed (5Gbps)
    bFunctionalitySupport   1
      Lowest fully-functional device speed is Full Speed (12Mbps)
    bU1DevExitLat          10 micro seconds
    bU2DevExitLat        1023 micro seconds
  Container ID Device Capability:
    bLength                20
    bDescriptorType        16
    bDevCapabilityType      4
    bReserved               0
    ContainerID             {20b9cde5-7039-e011-a935-0002a5d5c51b}
Hub Descriptor:
  bLength              12
  bDescriptorType      42
  nNbrPorts             4
  wHubCharacteristic 0x0009
    Per-port power switching
    Per-port overcurrent protection
  bPwrOn2PwrGood        0 * 2 milli seconds
  bHubContrCurrent      8 milli Ampere
  bHubDecLat          0.2 micro seconds
  wHubDelay          3202 nano seconds
  DeviceRemovable    0x00
 Hub Port Status:
   Port 1: 0000.02a0 5Gbps power Rx.Detect
   Port 2: 0000.02a0 5Gbps power Rx.Detect
   Port 3: 0000.02a0 5Gbps power Rx.Detect
   Port 4: 0000.02a0 5Gbps power Rx.Detect
Device Status:     0x0001
  Self Powered

Bus 004 Device 030: ID 0bda:0411 Realtek Semiconductor Corp. Hub
Device Descriptor:
  bLength                18
  bDescriptorType         1
  bcdUSB               3.20
  bDeviceClass            9 Hub
  bDeviceSubClass         0 
  bDeviceProtocol         3 
  bMaxPacketSize0         9
  idVendor           0x0bda Realtek Semiconductor Corp.
  idProduct          0x0411 Hub
  bcdDevice            0.04
  iManufacturer           1 Generic
  iProduct                2 USB3.2 Hub
  iSerial                 0 
  bNumConfigurations      1
  Configuration Descriptor:
    bLength                 9
    bDescriptorType         2
    wTotalLength       0x001f
    bNumInterfaces          1
    bConfigurationValue     1
    iConfiguration          0 
    bmAttributes         0xe0
      Self Powered
      Remote Wakeup
    MaxPower                0mA
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        0
      bAlternateSetting       0
      bNumEndpoints           1
      bInterfaceClass         9 Hub
      bInterfaceSubClass      0 
      bInterfaceProtocol      0 Full speed (or root) hub
      iInterface              0 
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x81  EP 1 IN
        bmAttributes           19
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Feedback
        wMaxPacketSize     0x0002  1x 2 bytes
        bInterval               8
        bMaxBurst               0
Binary Object Store Descriptor:
  bLength                 5
  bDescriptorType        15
  wTotalLength       0x002a
  bNumDeviceCaps          3
  USB 2.0 Extension Device Capability:
    bLength                 7
    bDescriptorType        16
    bDevCapabilityType      2
    bmAttributes   0x0000f41e
      BESL Link Power Management (LPM) Supported
    BESL value     1024 us 
    Deep BESL value    61440 us 
  SuperSpeed USB Device Capability:
    bLength                10
    bDescriptorType        16
    bDevCapabilityType      3
    bmAttributes         0x00
    wSpeedsSupported   0x000e
      Device can operate at Full Speed (12Mbps)
      Device can operate at High Speed (480Mbps)
      Device can operate at SuperSpeed (5Gbps)
    bFunctionalitySupport   1
      Lowest fully-functional device speed is Full Speed (12Mbps)
    bU1DevExitLat          10 micro seconds
    bU2DevExitLat        1023 micro seconds
  Container ID Device Capability:
    bLength                20
    bDescriptorType        16
    bDevCapabilityType      4
    bReserved               0
    ContainerID             {20b9cde5-7039-e011-a935-0002a5d5c51b}
Hub Descriptor:
  bLength              12
  bDescriptorType      42
  nNbrPorts             4
  wHubCharacteristic 0x0009
    Per-port power switching
    Per-port overcurrent protection
  bPwrOn2PwrGood        0 * 2 milli seconds
  bHubContrCurrent      8 milli Ampere
  bHubDecLat          0.2 micro seconds
  wHubDelay          3202 nano seconds
  DeviceRemovable    0x00
 Hub Port Status:
   Port 1: 0000.02a0 5Gbps power Rx.Detect
   Port 2: 0000.02a0 5Gbps power Rx.Detect
   Port 3: 0000.02a0 5Gbps power Rx.Detect
   Port 4: 0000.02a0 5Gbps power Rx.Detect
Device Status:     0x0001
  Self Powered

Bus 004 Device 028: ID 0bda:0411 Realtek Semiconductor Corp. Hub
Device Descriptor:
  bLength                18
  bDescriptorType         1
  bcdUSB               3.20
  bDeviceClass            9 Hub
  bDeviceSubClass         0 
  bDeviceProtocol         3 
  bMaxPacketSize0         9
  idVendor           0x0bda Realtek Semiconductor Corp.
  idProduct          0x0411 Hub
  bcdDevice            0.04
  iManufacturer           1 Generic
  iProduct                2 USB3.2 Hub
  iSerial                 0 
  bNumConfigurations      1
  Configuration Descriptor:
    bLength                 9
    bDescriptorType         2
    wTotalLength       0x001f
    bNumInterfaces          1
    bConfigurationValue     1
    iConfiguration          0 
    bmAttributes         0xe0
      Self Powered
      Remote Wakeup
    MaxPower                0mA
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        0
      bAlternateSetting       0
      bNumEndpoints           1
      bInterfaceClass         9 Hub
      bInterfaceSubClass      0 
      bInterfaceProtocol      0 Full speed (or root) hub
      iInterface              0 
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x81  EP 1 IN
        bmAttributes           19
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Feedback
        wMaxPacketSize     0x0002  1x 2 bytes
        bInterval               8
        bMaxBurst               0
Binary Object Store Descriptor:
  bLength                 5
  bDescriptorType        15
  wTotalLength       0x002a
  bNumDeviceCaps          3
  USB 2.0 Extension Device Capability:
    bLength                 7
    bDescriptorType        16
    bDevCapabilityType      2
    bmAttributes   0x0000f41e
      BESL Link Power Management (LPM) Supported
    BESL value     1024 us 
    Deep BESL value    61440 us 
  SuperSpeed USB Device Capability:
    bLength                10
    bDescriptorType        16
    bDevCapabilityType      3
    bmAttributes         0x00
    wSpeedsSupported   0x000e
      Device can operate at Full Speed (12Mbps)
      Device can operate at High Speed (480Mbps)
      Device can operate at SuperSpeed (5Gbps)
    bFunctionalitySupport   1
      Lowest fully-functional device speed is Full Speed (12Mbps)
    bU1DevExitLat          10 micro seconds
    bU2DevExitLat        1023 micro seconds
  Container ID Device Capability:
    bLength                20
    bDescriptorType        16
    bDevCapabilityType      4
    bReserved               0
    ContainerID             {20b9cde5-7039-e011-a935-0002a5d5c51b}
Hub Descriptor:
  bLength              12
  bDescriptorType      42
  nNbrPorts             4
  wHubCharacteristic 0x0009
    Per-port power switching
    Per-port overcurrent protection
  bPwrOn2PwrGood        0 * 2 milli seconds
  bHubContrCurrent      8 milli Ampere
  bHubDecLat          0.2 micro seconds
  wHubDelay          3202 nano seconds
  DeviceRemovable    0x00
 Hub Port Status:
   Port 1: 0000.02a0 5Gbps power Rx.Detect
   Port 2: 0000.02a0 5Gbps power Rx.Detect
   Port 3: 0000.0263 5Gbps power suspend enable connect
   Port 4: 0000.0263 5Gbps power suspend enable connect
Device Status:     0x000d
  Self Powered
  U1 Enabled
  U2 Enabled

Bus 004 Device 027: ID 0bda:0411 Realtek Semiconductor Corp. Hub
Device Descriptor:
  bLength                18
  bDescriptorType         1
  bcdUSB               3.20
  bDeviceClass            9 Hub
  bDeviceSubClass         0 
  bDeviceProtocol         3 
  bMaxPacketSize0         9
  idVendor           0x0bda Realtek Semiconductor Corp.
  idProduct          0x0411 Hub
  bcdDevice            0.04
  iManufacturer           1 Generic
  iProduct                2 USB3.2 Hub
  iSerial                 0 
  bNumConfigurations      1
  Configuration Descriptor:
    bLength                 9
    bDescriptorType         2
    wTotalLength       0x001f
    bNumInterfaces          1
    bConfigurationValue     1
    iConfiguration          0 
    bmAttributes         0xe0
      Self Powered
      Remote Wakeup
    MaxPower                0mA
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        0
      bAlternateSetting       0
      bNumEndpoints           1
      bInterfaceClass         9 Hub
      bInterfaceSubClass      0 
      bInterfaceProtocol      0 Full speed (or root) hub
      iInterface              0 
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x81  EP 1 IN
        bmAttributes           19
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Feedback
        wMaxPacketSize     0x0002  1x 2 bytes
        bInterval               8
        bMaxBurst               0
Binary Object Store Descriptor:
  bLength                 5
  bDescriptorType        15
  wTotalLength       0x002a
  bNumDeviceCaps          3
  USB 2.0 Extension Device Capability:
    bLength                 7
    bDescriptorType        16
    bDevCapabilityType      2
    bmAttributes   0x0000f41e
      BESL Link Power Management (LPM) Supported
    BESL value     1024 us 
    Deep BESL value    61440 us 
  SuperSpeed USB Device Capability:
    bLength                10
    bDescriptorType        16
    bDevCapabilityType      3
    bmAttributes         0x00
    wSpeedsSupported   0x000e
      Device can operate at Full Speed (12Mbps)
      Device can operate at High Speed (480Mbps)
      Device can operate at SuperSpeed (5Gbps)
    bFunctionalitySupport   1
      Lowest fully-functional device speed is Full Speed (12Mbps)
    bU1DevExitLat          10 micro seconds
    bU2DevExitLat        1023 micro seconds
  Container ID Device Capability:
    bLength                20
    bDescriptorType        16
    bDevCapabilityType      4
    bReserved               0
    ContainerID             {20b9cde5-7039-e011-a935-0002a5d5c51b}
Hub Descriptor:
  bLength              12
  bDescriptorType      42
  nNbrPorts             4
  wHubCharacteristic 0x0009
    Per-port power switching
    Per-port overcurrent protection
  bPwrOn2PwrGood        0 * 2 milli seconds
  bHubContrCurrent      8 milli Ampere
  bHubDecLat          0.2 micro seconds
  wHubDelay          3202 nano seconds
  DeviceRemovable    0x00
 Hub Port Status:
   Port 1: 0000.02a0 5Gbps power Rx.Detect
   Port 2: 0000.02a0 5Gbps power Rx.Detect
   Port 3: 0000.0263 5Gbps power suspend enable connect
   Port 4: 0000.0263 5Gbps power suspend enable connect
Device Status:     0x000d
  Self Powered
  U1 Enabled
  U2 Enabled
```