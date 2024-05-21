# usbhubctl

`usbhubctl` extends [uhubctl](https://github.com/mvp/uhubctl).

## State of this project

Still alpha. The concept/solution seems fine.

To be improved

* Much too slow (`uhubctl` may take seconds just to switch one plug)
* Implementation to complicated (uses `lsusb -tv`, `uhubctl`, root rights, ...)

## Use Case

![Image](https://de.rshtech.com/u_file/2011/products/12/c24d6de5bd.jpg.240x240.jpg)

I would like to switch on power on plug 3 on my RSH_A16 hub.

### Problem
`uhubctl` allows me to do this - but I have to know which usb device id corresponds to plug 3.



* I have to first figure out the topology (internal structure) of my RSH_A16 hub. Spoiler: there are 5 hubs chips with 4 ports each.
* Now I have to figure out, which port is connected to each plug.
* When I reconnect the RSH_A16 to another USB connected on my compunter, the whole assignement changes again.

Now I can issue `uhubctl -l 3-4.6.1 -p 3 --action on`.

### Solution with `usbhubctl/uhbuctl`

This is the topology of the RSH_A16.


```python
rsh_a16 = Hub(
    manufacturer="RSHTECH",
    model="RSH-A16",
    comment="",
    plug_count=16,
    hub_chip=HubChip(
        "0bda:5411",
        plug_or_chip=[
            1,
            2,
            HubChip(
                "0bda:5411",
                plug_or_chip=[
                    7,
                    8,
                    HubChip("0bda:5411", plug_or_chip=[13, 14, 15, 16]),
                    HubChip("0bda:5411", plug_or_chip=[9, 10, 11, 12]),
                ],
            ),
            HubChip("0bda:5411", plug_or_chip=[3, 4, 5, 6]),
        ],
    ),
)
```

Here you see the 5 internal hub-chips and to which usb-plugs the are connected.



This code will power on usb-plug number 3:

```python
from usbhubctl.known_hubs import rsh_a10, rsh_a16

# Call `lsusb -tv` and find all connected RSH_A16
hubs = rsh_a16.find_connected_hubs()

if len(hubs) > 1:
    print("More than one RSH_A16 hub detected: unambiguously")
    return
if len(hubs) == 0:
    print("No RSH_A16 hub detected")
    return
hub = hubs.hubs[0]

# Finally power on
# Internally, this will call `uhubctl -l 3-4.6.1 -p 3 --action on`
hub.get_plug(3).on()
```

*Benefit*

No matter, where you connected the RSH-A16 hub, the method `find_connected_hubs` will find it and call `uhubctl -l 3-4.6.1 -p 3 --action on` with the correct parameters.


