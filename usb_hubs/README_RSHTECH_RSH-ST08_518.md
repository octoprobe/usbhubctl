# RSHTECH_RSH-ST07_518.md

**TODO Test with uhubctl**
**TODO test rsh_st07**

The Hub is labeled `518`, however on the RSH web it is named `RSH-ST07`.

https://www.rshtech.com/products/powered-usb-hub-rshtech-7-port-usb-30-usb-c-hub-upgraded-version-aluminum-usb-hub-with-2-in-1-usb-cable5v-3a-power-adapter-rsh-st07


https://de.aliexpress.com/item/1005006316558716.html
USD 24.00

![Image](hhttps://www.rshtech.com/u_file/2303/products/07/f848890f9c.jpg)

![Image](https://www.rshtech.com/u_file/2303/products/07/da7a37b650.jpg)

## Assessment

Are very similar [RSH-ST07C](README_RSHTECH_RSH-ST07C.md)

* **Overall: Usable for power switching**

* Positive: Power on/off works fine on every port
* Negative: LEDs hardly visible
* Negative: Ports are not numbered
* Positive: Enough space to attach port number stickers
* Negative: Switching using uhubctl is slow: 2.5s
* Negative: Power on/off ONLY works when the button is in pressed state

## Links where this HUB is mentioned

* ...

## Hub Topology

See [rsh_st07.py](../usbhubctl/known_hubs/rsh_st07.py)

## Internals

```
sudo uhubctl 
Current status for hub 4-2.1 [0bda:0411 Generic USB3.2 Hub, USB 3.20, 4 ports, ppps]
  Port 1: 02a0 power 5gbps Rx.Detect
  Port 2: 02a0 power 5gbps Rx.Detect
  Port 3: 02a0 power 5gbps Rx.Detect
  Port 4: 02a0 power 5gbps Rx.Detect
Current status for hub 4-2 [0bda:0411 Generic USB3.2 Hub, USB 3.20, 4 ports, ppps]
  Port 1: 0263 power 5gbps U3 enable connect [0bda:0411 Generic USB3.2 Hub, USB 3.20, 4 ports, ppps]
  Port 2: 02a0 power 5gbps Rx.Detect
  Port 3: 02a0 power 5gbps Rx.Detect
  Port 4: 02a0 power 5gbps Rx.Detect
Current status for hub 3-7.1 [0bda:5411 Generic USB2.1 Hub, USB 2.10, 4 ports, ppps]
  Port 1: 0100 power
  Port 2: 0100 power
  Port 3: 0100 power
  Port 4: 0100 power
Current status for hub 3-7 [0bda:5411 Generic USB2.1 Hub, USB 2.10, 4 ports, ppps]
  Port 1: 0507 power highspeed suspend enable connect [0bda:5411 Generic USB2.1 Hub, USB 2.10, 4 ports, ppps]
  Port 2: 0100 power
  Port 3: 0100 power
  Port 4: 0100 power
```

```
# sudo dmesg --follow
[ 1646.105895] usb 3-7: new high-speed USB device number 16 using xhci_hcd
[ 1646.244521] usb 3-7: New USB device found, idVendor=0bda, idProduct=5411, bcdDevice= 0.04
[ 1646.244534] usb 3-7: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 1646.244538] usb 3-7: Product: USB2.1 Hub
[ 1646.244542] usb 3-7: Manufacturer: Generic
[ 1646.247201] hub 3-7:1.0: USB hub found
[ 1646.248391] hub 3-7:1.0: 4 ports detected
[ 1646.350429] usb 4-2: new SuperSpeed USB device number 6 using xhci_hcd
[ 1646.375108] usb 4-2: New USB device found, idVendor=0bda, idProduct=0411, bcdDevice= 0.04
[ 1646.375114] usb 4-2: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 1646.375116] usb 4-2: Product: USB3.2 Hub
[ 1646.375118] usb 4-2: Manufacturer: Generic
[ 1646.382191] hub 4-2:1.0: USB hub found
[ 1646.383450] hub 4-2:1.0: 4 ports detected
[ 1646.533773] usb 3-7.1: new high-speed USB device number 17 using xhci_hcd
[ 1646.635128] usb 3-7.1: New USB device found, idVendor=0bda, idProduct=5411, bcdDevice= 0.04
[ 1646.635141] usb 3-7.1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 1646.635146] usb 3-7.1: Product: USB2.1 Hub
[ 1646.635150] usb 3-7.1: Manufacturer: Generic
[ 1646.637324] hub 3-7.1:1.0: USB hub found
[ 1646.639875] hub 3-7.1:1.0: 4 ports detected
[ 1646.695375] usb 4-2.1: new SuperSpeed USB device number 7 using xhci_hcd
[ 1646.721094] usb 4-2.1: New USB device found, idVendor=0bda, idProduct=0411, bcdDevice= 0.04
[ 1646.721098] usb 4-2.1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
[ 1646.721099] usb 4-2.1: Product: USB3.2 Hub
[ 1646.721100] usb 4-2.1: Manufacturer: Generic
[ 1646.726368] hub 4-2.1:1.0: USB hub found
[ 1646.729127] hub 4-2.1:1.0: 4 ports detected
```

```
sudo lsusb -d 0bda:0411 -v

Bus 004 Device 006: ID 0bda:0411 Realtek Semiconductor Corp. Hub
Couldn't open device, some information will be missing
Negotiated speed: SuperSpeed (5Gbps)
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

Bus 004 Device 007: ID 0bda:0411 Realtek Semiconductor Corp. Hub
Couldn't open device, some information will be missing
Negotiated speed: SuperSpeed (5Gbps)
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
```