# 7port FE2.1

https://www.aliexpress.com/item/1005006303783551.html

CHF 5.1

JLC C39693 USD 1.5

![](https://ae-pic-a1.aliexpress-media.com/kf/S5b5a79c994a04fa3bd3251b4509b9430t/1PCS-USB-2-0-HUB-Module-1-to-7-Port-USB-Hub-Seven-Port-Splitter-Module.jpg)

![](https://ae-pic-a1.aliexpress-media.com/kf/S78909978f66d4d13a93ba5444aa3673e8/1PCS-USB-2-0-HUB-Module-1-to-7-Port-USB-Hub-Seven-Port-Splitter-Module.jpg)


[Products](http://www.terminus-tech.com/en/products.html)
[FE2.1](https://terminus-usa.com/product/fe2-1-usb-2-0-high-speed-7-port-hub-controller)

* Ganged or Individual Power Control Mode select;

[FE2.1 Product Brief](https://terminus-usa.com/wp-content/uploads/2024/06/FE2.1-Product-Brief-Rev.-2.0-2019.pdf)

[FE2.1 Datasheet](https://www.lcsc.com/datasheet/lcsc_datasheet_2208041530_Terminus-Tech-FE2-1-CQFP48A_C39693.pdf)

[FE2.1 Datasheet](https://wmsc.lcsc.com/wmsc/upload/file/pdf/v2/lcsc/2208041530_Terminus-Tech-FE2-1-CQFP48A_C39693.pdf)

[PCBway](https://www.pcbway.com/project/shareproject/USB_HUB_based_on_FE2_1_interface_with_serial_port.html)

```batch
[  784.821184] usb 3-7: USB disconnect, device number 13
[  810.829169] usb 3-7: new high-speed USB device number 14 using xhci_hcd
[  810.955547] usb 3-7: New USB device found, idVendor=1a40, idProduct=0201, bcdDevice= 1.00
[  810.955558] usb 3-7: New USB device strings: Mfr=0, Product=1, SerialNumber=0
[  810.955562] usb 3-7: Product: USB 2.0 Hub [MTT]
[  810.957685] hub 3-7:1.0: USB hub found
[  810.957759] hub 3-7:1.0: 7 ports detected
```


```bash
uhubctl --force 
Current status for hub 3-7 [1a40:0201 USB 2.0 Hub [MTT], USB 2.00, 7 ports, ganged]
  Port 1: 0100 power
  Port 2: 0100 power
  Port 3: 0100 power
  Port 4: 0100 power
  Port 5: 0100 power
  Port 6: 0100 power
  Port 7: 0100 power
...
Current status for hub 3-1 [0bda:5411 Generic USB2.1 Hub, USB 2.10, 4 ports, ppps]
  Port 1: 0303 power lowspeed enable connect [413c:2107 Dell Dell USB Entry Keyboard]
  Port 2: 0303 power lowspeed enable connect [03f0:154a HP HP USB 1000dpi Laser Mouse]
  Port 3: 0507 power highspeed suspend enable connect [0bda:5411 Generic USB2.1 Hub, USB 2.10, 4 ports, ppps]
  Port 4: 0503 power highspeed enable connect [0bda:5411 Generic USB2.1 Hub, USB 2.10, 4 ports, ppps]
Current status for hub 3 [1d6b:0002 Linux 6.8.0-39-generic xhci-hcd xHCI Host Controller 0000:00:14.0, USB 2.00, 12 ports, nops]
  Port 1: 0503 power highspeed enable connect [0bda:5411 Generic USB2.1 Hub, USB 2.10, 4 ports, ppps]
  Port 2: 0100 power
  Port 3: 0107 power suspend enable connect [06cb:00f9 76fca33c4930]
  Port 4: 0507 power highspeed suspend enable connect [13d3:5405 Azurewave Integrated Camera 0000]
  Port 5: 0503 power highspeed enable connect [1a40:0801 USB 2.0 Hub, USB 2.00, 4 ports, ganged]
  Port 6: 0100 power
  Port 7: 0507 power highspeed suspend enable connect [1a40:0201 USB 2.0 Hub [MTT], USB 2.00, 7 ports, ganged]
  Port 8: 0100 power
  Port 9: 0100 power
  Port 10: 0100 power
  Port 11: 0100 power
  Port 12: 0100 power
```


```bash
uhubctl --force -l 3-7 --action=on
Current status for hub 3-7 [1a40:0201 USB 2.0 Hub [MTT], USB 2.00, 7 ports, ganged]
  Port 1: 0000 off
  Port 2: 0000 off
  Port 3: 0000 off
  Port 4: 0000 off
  Port 5: 0000 off
  Port 6: 0000 off
  Port 7: 0000 off
Sent power on request
New status for hub 3-7 [1a40:0201 USB 2.0 Hub [MTT], USB 2.00, 7 ports, ganged]
  Port 1: 0100 power
  Port 2: 0100 power
  Port 3: 0100 power
  Port 4: 0100 power
  Port 5: 0100 power
  Port 6: 0100 power
  Port 7: 0100 power
```

==> NOT TESTED YET WITH EXERNAL POWER SUPPLY