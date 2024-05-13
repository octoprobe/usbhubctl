# UHUBCTL

https://github.com/mvp/uhubctl/tree/master

https://github.com/orgs/micropython/discussions/13464#discussioncomment-8252334
```
andrewleech

Many of the target devices here use USB as their standard firmware install mechanism, I would not trust that a USB1 style connection would be possible and have this work in a realiable fashion. Also, I'd expect most tests to be run ultimately via mpremote / pyboard.py which would typically also need to use a usb repl for communication.

inkbus: USB over ribbon wire only works on USB 1.0 Low Speed 1.5 Mbit/s. This is easy to implement with 2 resistors.

Can you use resistors to force a device to only connect in USB 1.0 mode? I'm used to devices always attempting to connect in USB2 mode and failing if the cable isn't good enough.

I was thinking that I then could just take a make a simple USB2 adapter female - male and just not wire in the GND, D+ and D- and not connect V-Bus(+5v))

This definitely works; I've got a powered USB hub with a switch on each port; All the switch does is cut eh 5V line on the usb port, all other pins are always connected. This works fine for power cycling devices (manually).

Also, this could help: https://github.com/mvp/uhubctl - if we can find something from that list then we could just have a bunch of them daisy chained together for all DUT's

Or, each of the tentacles could be based on this which includes both usb hub and debugger "inline" with the single usb port: https://www.hackster.io/news/negimeister-s-clever-usb-debug-probe-built-using-an-rp2040-compute-module-simplifies-swd-2e1f5a74d5d7
```

## Links

https://github.com/mvp/uhubctl/tree/master
https://github.com/codazoda/hub-ctrl.c

https://www.gniibe.org/development/ac-power-control-by-USB-hub/

https://git.gniibe.org/cgit/gnuk/gnuk.git/tree/tool/hub_ctrl.py
https://github.com/crazystick/py-hub-ctrl/blob/master/hub_ctrl.py


https://www.baeldung.com/linux/control-usb-power-supply

`echo "on" > "/sys/bus/usb/devices/1-3:1.0/power/control"`


## USB Hub Descriptor

https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/usbspec/ns-usbspec-_usb_hub_descriptor

The USB_HUB_DESCRIPTOR structure contains a hub descriptor. The members of this structure are described in the Universal Serial Bus 3.1 Specification available at USB Document Library. See section 10.15.2.1.
https://www.usb.org/documents

https://www.usb.org/document-library/usb-32-revision-11-june-2022, USB 3.2 Revision 1.1.pdf


## Evaluating Hubs for the prototype

### AmazonBasics HUC9002V1SBL, 10 port, USB 3.2, EUR50

https://www.amazon.de/AmazonBasics-USB-Hub-USB-Anschl%C3%BCssen-Netzadapter/dp/B076YRSWGW

### Coolgear USBG-12U2ML, 12 port, USB 2, CHF 191

https://www.distrelec.ch/de/industrieller-usb-hub-12x-usb-buchse-5gbps-exsys-ex-1112hms/p/30089399

### D-Link DUB-H7, 7 port, USB 2, CHF 40

https://www.digitec.ch/de/s1/product/d-link-dub-h7-usb-b-dockingstation-usb-hub-353665

https://www.interdiscount.ch/de/computer-gaming/peripherie/usb-hubs--c526100/d-link-7-port-schnittstellenhub-usb-2-0-schwarz--p0000211865

### Plugable, USBC-HUB7BC, 6(7)port, USB 3.0, USD 45

https://plugable.com/products/usbc-hub7bc


### Rosonway, RSH-A16, 16 port

Currently not available

https://de.rshtech.com/products/16-ports-aluminum-usb-30-data-hub-with-12v-83a-with-uk-power-adapterrsh-a16


https://www.amazon.de/RSHTECH-Aluminium-Verteiler-Aus-Schalter-RSH-A10/dp/B082SQT12J/ref=asc_df_B082SQT12J/ 10port, USB3 3.0, EUR42


### RSHTECH, 16 Port USB Hub Aktiv 3.0 mit 100W

https://www.amazon.de/gp/product/B09YH7VPKR

EUR63

==> bought

## Digitec - to be tested

### Delock SuperSpeed Hub, 16 port, USB 2, CHF 97

https://www.digitec.ch/en/s1/product/delock-superspeed-hub-usb-b-docking-stations-usb-hubs-17951397


### i-tec Hub, 16 port, USB 2, CHF 62

USB 3.0 Type-A (16x)

https://www.digitec.ch/en/s1/product/i-tec-hub-usb-b-docking-stations-usb-hubs-12422259

### Icy Box IB-AC6113, 13 port, USB 3 5Gbit/s, CHF 91

https://www.digitec.ch/en/s1/product/icy-box-ib-ac6113-usb-b-docking-stations-usb-hubs-3824644

## Sipoar A832, 32 port

https://de.aliexpress.com/item/1005005196121014.html

## Ssk industrial, 16 port, USD 66

https://de.aliexpress.com/item/1005006284964310.html

VL817, https://www.via-labs.com/product_show.php?id=83
https://datasheet.lcsc.com/lcsc/1808111624_VIA-Tech-VL817-Q7-B0_C209756.pdf


## USB2.0, 4 port, CHF 2.10

GL850G

https://www.aliexpress.com/item/1005005939066237.html

==> bought
