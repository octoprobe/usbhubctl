# RSHTECH_RSH-A10.md

https://de.rshtech.com/products/10-ports-aluminum-usb-30-data-hub-with-12v-3a-power-adapterrsh-a10

https://www.aliexpress.com/item/1005006336855327.html?spm=a2g0o.order_list.order_list_main.5.80661802FV8g4n
USD35

![Image](https://de.rshtech.com/u_file/2008/products/03/e085bb3047.jpg)

![Image](https://de.rshtech.com/u_file/2008/products/03/31a8be0fca.jpg)

![Image](https://de.rshtech.com/u_file/2008/products/03/7ad8d5b99e.jpg)

## Assessment

Are very similar RSH-A10 / RSH-A16

* **Overall: Usable for power switching**

* Positive: Power on/off works fine on every port
* Negative: LEDs hardly visible
* Negative: Ports are not numbered
* Negative: Switching using uhubctl is slow: 2.5s
* Negative: Power on/off ONLY works when the button is in pressed state

## Links where this HUB is mentioned

* ...

## Hub Topology

See [rsh_a10.py](../pyhubctl/known_hubs/rsh_a10.py)


## Internals

```
sudo uhubctl 
uhubctl 
Current status for hub 4-1.4 [0bda:0411 Generic USB3.2 Hub, USB 3.20, 4 ports, ppps]
  Port 1: 02a0 power 5gbps Rx.Detect
  Port 2: 02a0 power 5gbps Rx.Detect
  Port 3: 02a0 power 5gbps Rx.Detect
  Port 4: 02a0 power 5gbps Rx.Detect
Current status for hub 4-1.3 [0bda:0411 Generic USB3.2 Hub, USB 3.20, 4 ports, ppps]
  Port 1: 02a0 power 5gbps Rx.Detect
  Port 2: 02a0 power 5gbps Rx.Detect
  Port 3: 02a0 power 5gbps Rx.Detect
  Port 4: 02a0 power 5gbps Rx.Detect
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
Current status for hub 3-1.3 [0bda:5411 Generic USB2.1 Hub, USB 2.10, 4 ports, ppps]
  Port 1: 0100 power
  Port 2: 0100 power
  Port 3: 0100 power
  Port 4: 0100 power
Current status for hub 3-1 [0bda:5411 Generic USB2.1 Hub, USB 2.10, 4 ports, ppps]
  Port 1: 0100 power
  Port 2: 0100 power
  Port 3: 0507 power highspeed suspend enable connect [0bda:5411 Generic USB2.1 Hub, USB 2.10, 4 ports, ppps]
  Port 4: 0507 power highspeed suspend enable connect [0bda:5411 Generic USB2.1 Hub, USB 2.10, 4 ports, ppps]
```

```
# sudo dmesg --follow
[ 4549.356778] usb 3-1: new high-speed USB device number 23 using xhci_hcd
[ 4549.500217] usb 3-1: New USB device found, idVendor=0bda, idProduct=5411, bcdDevice= 0.04
[ 4549.500230] usb 3-1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 4549.500234] usb 3-1: Product: USB2.1 Hub
[ 4549.500238] usb 3-1: Manufacturer: Generic
[ 4549.502867] hub 3-1:1.0: USB hub found
[ 4549.505345] hub 3-1:1.0: 4 ports detected
[ 4549.606443] usb 4-1: new SuperSpeed USB device number 5 using xhci_hcd
[ 4549.632013] usb 4-1: New USB device found, idVendor=0bda, idProduct=0411, bcdDevice= 0.04
[ 4549.632023] usb 4-1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 4549.632026] usb 4-1: Product: USB3.2 Hub
[ 4549.632029] usb 4-1: Manufacturer: Generic
[ 4549.638320] hub 4-1:1.0: USB hub found
[ 4549.639640] hub 4-1:1.0: 4 ports detected
[ 4549.792685] usb 3-1.3: new high-speed USB device number 24 using xhci_hcd
[ 4549.898881] usb 3-1.3: New USB device found, idVendor=0bda, idProduct=5411, bcdDevice= 0.04
[ 4549.898892] usb 3-1.3: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 4549.898895] usb 3-1.3: Product: USB2.1 Hub
[ 4549.898898] usb 3-1.3: Manufacturer: Generic
[ 4549.900809] hub 3-1.3:1.0: USB hub found
[ 4549.902072] hub 3-1.3:1.0: 4 ports detected
[ 4549.964463] usb 4-1.3: new SuperSpeed USB device number 6 using xhci_hcd
[ 4549.991655] usb 4-1.3: New USB device found, idVendor=0bda, idProduct=0411, bcdDevice= 0.04
[ 4549.991667] usb 4-1.3: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 4549.991671] usb 4-1.3: Product: USB3.2 Hub
[ 4549.991674] usb 4-1.3: Manufacturer: Generic
[ 4549.998876] hub 4-1.3:1.0: USB hub found
[ 4550.000264] hub 4-1.3:1.0: 4 ports detected
[ 4550.059615] usb 3-1.4: new high-speed USB device number 25 using xhci_hcd
[ 4550.168069] usb 3-1.4: New USB device found, idVendor=0bda, idProduct=5411, bcdDevice= 0.04
[ 4550.168082] usb 3-1.4: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 4550.168086] usb 3-1.4: Product: USB2.1 Hub
[ 4550.168089] usb 3-1.4: Manufacturer: Generic
[ 4550.170490] hub 3-1.4:1.0: USB hub found
[ 4550.171710] hub 3-1.4:1.0: 4 ports detected
[ 4550.231361] usb 4-1.4: new SuperSpeed USB device number 7 using xhci_hcd
[ 4550.258661] usb 4-1.4: New USB device found, idVendor=0bda, idProduct=0411, bcdDevice= 0.04
[ 4550.258675] usb 4-1.4: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 4550.258681] usb 4-1.4: Product: USB3.2 Hub
[ 4550.258685] usb 4-1.4: Manufacturer: Generic
[ 4550.266586] hub 4-1.4:1.0: USB hub found
[ 4550.268088] hub 4-1.4:1.0: 4 ports detected
```

```
sudo lsusb -d 0bda:0411 -v

Bus 004 Device 005: ID 0bda:0411 Realtek Semiconductor Corp. Hub
Device Descriptor:
  bLength                18
  bDescriptorType         1
  bcdUSB               3.20
  bDeviceClass            9 Hub
  bDeviceSubClass         0 [unknown]
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
      bInterfaceSubClass      0 [unknown]
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

Bus 004 Device 006: ID 0bda:0411 Realtek Semiconductor Corp. Hub
Device Descriptor:
  bLength                18
  bDescriptorType         1
  bcdUSB               3.20
  bDeviceClass            9 Hub
  bDeviceSubClass         0 [unknown]
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
      bInterfaceSubClass      0 [unknown]
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

Bus 004 Device 007: ID 0bda:0411 Realtek Semiconductor Corp. Hub
Device Descriptor:
  bLength                18
  bDescriptorType         1
  bcdUSB               3.20
  bDeviceClass            9 Hub
  bDeviceSubClass         0 [unknown]
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
      bInterfaceSubClass      0 [unknown]
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

```