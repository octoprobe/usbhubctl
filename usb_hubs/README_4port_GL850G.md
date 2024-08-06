# USBHUB USB2.0 hub HUB 4-port controller USB expansion module GL850G chip

**==> DOES NOT POWER SWITCH!**

* Aliexpress

  USBHUB USB2.0 hub HUB 4-port controller USB expansion module GL850G chip

  CHF 2.5


![](https://ae-pic-a1.aliexpress-media.com/kf/S7bebf8ccf4f84642830dfe58f3f3962bI/USBHUB-USB2-0-hub-HUB-4-port-controller-USB-expansion-module-GL850G-chip.jpg)


```bash
[   32.825827] usb 3-7: new high-speed USB device number 13 using xhci_hcd
[   32.953222] usb 3-7: New USB device found, idVendor=05e3, idProduct=0608, bcdDevice=85.36
[   32.953234] usb 3-7: New USB device strings: Mfr=0, Product=1, SerialNumber=0
[   32.953239] usb 3-7: Product: USB2.0 Hub
[   32.958799] hub 3-7:1.0: USB hub found
[   32.959070] hub 3-7:1.0: 4 ports detected
```

```bash
lsusb -tv
    |__ Port 007: Dev 013, If 0, Class=Hub, Driver=hub/4p, 480M
        ID 05e3:0608 Genesys Logic, Inc. Hub
```

```bash
uhubctl --force
  Port 7: 0507 power highspeed suspend enable connect [05e3:0608 USB2.0 Hub, USB 2.00, 4 ports, ganged]
```

```bash
uhubctl --force -l 3-7
Current status for hub 3-7 [05e3:0608 USB2.0 Hub, USB 2.00, 4 ports, ganged]
  Port 1: 0100 power
  Port 2: 0100 power
  Port 3: 0100 power
  Port 4: 0100 power
```

```bash
uhubctl --force -l 3-7 --action=off
```

==> Does NOT power switch
