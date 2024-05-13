# ATEN US234.md

https://www.aten.com/de/de/products/usb-l%C3%B6sungen/docks-und-switches/us234/

![Image](https://assets.aten.com/product/image/us234.mobility-&-usb.usb-peripheral-switches.45.jpg)

![Image](https://assets.aten.com/product/image/us234.mobility-&-usb.usb-peripheral-switches.front.jpg)

## Assessment

* Negative: Switching the PC's only works with the attached button
* Negative: Power switching does NOT work


## Port assignements

`sudo uhubctl --location xx --port xx --action=on``

| plug | location | port
|  - | - | - |
|  1 | 3-1 | 1 |
|  2 | 3-1 | 2 |
|  3 | 3-1 | 3 |
|  4 | 3-1 | 4 |

The port 4 is the one closest to `DC5V`.

## Connecting with two PC's

* Connecting first PC: `dmesg` displays the hub.
* Connecting second PC: No output on `dmesg`
* Press the attached button:
  * First PC: `dmesg`: Hubs disconnect
  * Second PC: `dmesg`: Hubs connect

## Internals

```
sudo uhubctl
Current status for hub 4-1 [0bda:0411 Generic 4-Port USB 3.0 Hub, USB 3.00, 4 ports, ppps]
  Port 1: 02a0 power 5gbps Rx.Detect
  Port 2: 02a0 power 5gbps Rx.Detect
  Port 3: 02a0 power 5gbps Rx.Detect
  Port 4: 02a0 power 5gbps Rx.Detect
Current status for hub 3-5.2 [2109:0812 USB2.0 Hub, USB 2.00, 4 ports, ppps]
  Port 1: 0507 power highspeed suspend enable connect [214b:7250 USB2.0 HUB, USB 2.00, 4 ports, ganged]
  Port 2: 0100 power
  Port 3: 0303 power lowspeed enable connect [03f0:154a HP HP USB 1000dpi Laser Mouse]
  Port 4: 0303 power lowspeed enable connect [413c:2107 Dell Dell USB Entry Keyboard]
Current status for hub 3-1 [0bda:5411 Generic 4-Port USB 2.0 Hub, USB 2.00, 4 ports, ppps]
  Port 1: 0100 power
  Port 2: 0100 power
  Port 3: 0100 power
  Port 4: 0100 power
```

# sudo dmesg --follow

[ 7926.230983] usb 3-1: new high-speed USB device number 64 using xhci_hcd
[ 7926.391358] usb 3-1: New USB device found, idVendor=0bda, idProduct=5411, bcdDevice= 1.21
[ 7926.391374] usb 3-1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 7926.391380] usb 3-1: Product: 4-Port USB 2.0 Hub
[ 7926.391385] usb 3-1: Manufacturer: Generic
[ 7926.393820] hub 3-1:1.0: USB hub found
[ 7926.394616] hub 3-1:1.0: 4 ports detected
[ 7926.507380] usb 4-1: new SuperSpeed USB device number 39 using xhci_hcd
[ 7926.545228] usb 4-1: New USB device found, idVendor=0bda, idProduct=0411, bcdDevice= 1.21
[ 7926.545234] usb 4-1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 7926.545236] usb 4-1: Product: 4-Port USB 3.0 Hub
[ 7926.545237] usb 4-1: Manufacturer: Generic
[ 7926.553051] hub 4-1:1.0: USB hub found
[ 7926.554488] hub 4-1:1.0: 4 ports detected
```

```
sudo lsusb -d 0bda:0411 -v

Bus 004 Device 039: ID 0bda:0411 Realtek Semiconductor Corp. Hub
Device Descriptor:
  bLength                18
  bDescriptorType         1
  bcdUSB               3.00
  bDeviceClass            9 Hub
  bDeviceSubClass         0 
  bDeviceProtocol         3 
  bMaxPacketSize0         9
  idVendor           0x0bda Realtek Semiconductor Corp.
  idProduct          0x0411 Hub
  bcdDevice            1.21
  iManufacturer           1 Generic
  iProduct                2 4-Port USB 3.0 Hub
  iSerial                 0 
  bNumConfigurations      1
  Configuration Descriptor:
    bLength                 9
    bDescriptorType         2
    wTotalLength       0x001f
    bNumInterfaces          1
    bConfigurationValue     1
    iConfiguration          4 USB3.0 Hub
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
      iInterface              5 Interrupt In Interface
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
    ContainerID             {ecf5adf1-5011-4005-91ec-71ca7101b6a2}
Hub Descriptor:
  bLength              12
  bDescriptorType      42
  nNbrPorts             4
  wHubCharacteristic 0x0009
    Per-port power switching
    Per-port overcurrent protection
  bPwrOn2PwrGood       50 * 2 milli seconds
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
