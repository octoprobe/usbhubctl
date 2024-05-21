# Goal

Technically do the same as `uhubctl` does. But the implementation is very different.

run `sudo lsusb -v` and `lsusb -tv` and store output.

run `sudo echo xy > /sys/xxx` to switch power on/off.

To switch power on/off with `uhubctl` might take several seconds depending on the complexity of the usb topology.

With above solution, it will take fractals of a second.

## Preparation

```bash
sudo lsusb -v > out_lsusb-v.txt
lsusb -tv > out_lsusb-tv.txt
```

## Analyze files

out_lsusb-tv.txt: We choose `Bus 3 Dev 009, If 0` / `Bus 3-6.3.4.1`. It is plug 6.

This corresponds to
```bash
sudo ls -l /sys/bus/usb/devices/3-6.3.4/
drwxr-xr-x 8 root root     0 Mai 15 07:36 3-6.3.4:1.0
-rw-r--r-- 1 root root  4096 Mai 15 11:39 authorized
-rw-r--r-- 1 root root  4096 Mai 15 11:39 avoid_reset_quirk
-r--r--r-- 1 root root  4096 Mai 15 07:36 bcdDevice
-rw-r--r-- 1 root root  4096 Mai 15 07:36 bConfigurationValue
-r--r--r-- 1 root root  4096 Mai 15 07:36 bDeviceClass
-r--r--r-- 1 root root  4096 Mai 15 09:12 bDeviceProtocol
-r--r--r-- 1 root root  4096 Mai 15 09:12 bDeviceSubClass
-r--r--r-- 1 root root  4096 Mai 15 09:12 bmAttributes
-r--r--r-- 1 root root  4096 Mai 15 09:12 bMaxPacketSize0
-r--r--r-- 1 root root  4096 Mai 15 09:12 bMaxPower
-r--r--r-- 1 root root  4096 Mai 15 09:12 bNumConfigurations
-r--r--r-- 1 root root  4096 Mai 15 09:12 bNumInterfaces
-r--r--r-- 1 root root  4096 Mai 15 07:36 busnum
-r--r--r-- 1 root root  4096 Mai 15 09:12 configuration
-r--r--r-- 1 root root 65553 Mai 15 07:36 descriptors
-r--r--r-- 1 root root  4096 Mai 15 11:39 dev
-r--r--r-- 1 root root  4096 Mai 15 07:36 devnum
-r--r--r-- 1 root root  4096 Mai 15 11:39 devpath
lrwxrwxrwx 1 root root     0 Mai 15 07:36 driver -> ../../../../../../../bus/usb/drivers/usb
drwxr-xr-x 3 root root     0 Mai 15 11:39 ep_00
-r--r--r-- 1 root root  4096 Mai 15 07:36 idProduct
-r--r--r-- 1 root root  4096 Mai 15 07:36 idVendor
-r--r--r-- 1 root root  4096 Mai 15 11:39 ltm_capable
-r--r--r-- 1 root root  4096 Mai 15 07:36 manufacturer
-r--r--r-- 1 root root  4096 Mai 15 09:12 maxchild
lrwxrwxrwx 1 root root     0 Mai 15 11:39 port -> ../3-6.3:1.0/3-6.3-port4
drwxr-xr-x 2 root root     0 Mai 15 11:39 power
-r--r--r-- 1 root root  4096 Mai 15 07:36 product
-r--r--r-- 1 root root  4096 Mai 15 11:39 quirks
-r--r--r-- 1 root root  4096 Mai 15 11:39 removable
--w------- 1 root root  4096 Mai 15 11:39 remove
-r--r--r-- 1 root root  4096 Mai 15 09:12 rx_lanes
-r--r--r-- 1 root root  4096 Mai 15 07:36 speed
lrwxrwxrwx 1 root root     0 Mai 15 07:36 subsystem -> ../../../../../../../bus/usb
-r--r--r-- 1 root root  4096 Mai 15 09:12 tx_lanes
-rw-r--r-- 1 root root  4096 Mai 15 07:36 uevent
-r--r--r-- 1 root root  4096 Mai 15 11:39 urbnum
-r--r--r-- 1 root root  4096 Mai 15 09:12 version


sudo ls -l /sys/bus/usb/devices/3-6.3.4:1.0/
drwxr-xr-x 3 root root    0 Mai 15 09:12 3-6.3.4-port1
drwxr-xr-x 3 root root    0 Mai 15 11:40 3-6.3.4-port2
drwxr-xr-x 3 root root    0 Mai 15 11:40 3-6.3.4-port3
drwxr-xr-x 3 root root    0 Mai 15 11:40 3-6.3.4-port4
-rw-r--r-- 1 root root 4096 Mai 15 11:40 authorized
-r--r--r-- 1 root root 4096 Mai 15 09:12 bAlternateSetting
-r--r--r-- 1 root root 4096 Mai 15 07:36 bInterfaceClass
-r--r--r-- 1 root root 4096 Mai 15 07:36 bInterfaceNumber
-r--r--r-- 1 root root 4096 Mai 15 09:12 bInterfaceProtocol
-r--r--r-- 1 root root 4096 Mai 15 09:12 bInterfaceSubClass
-r--r--r-- 1 root root 4096 Mai 15 09:12 bNumEndpoints
lrwxrwxrwx 1 root root    0 Mai 15 07:36 driver -> ../../../../../../../../bus/usb/drivers/hub
drwxr-xr-x 3 root root    0 Mai 15 11:40 ep_81
-r--r--r-- 1 root root 4096 Mai 15 11:40 modalias
drwxr-xr-x 2 root root    0 Mai 15 11:40 power
lrwxrwxrwx 1 root root    0 Mai 15 07:36 subsystem -> ../../../../../../../../bus/usb
-r--r--r-- 1 root root 4096 Mai 15 11:40 supports_autosuspend
-rw-r--r-- 1 root root 4096 Mai 15 07:36 uevent

sudo ls -l /sys/bus/usb/devices/3-6.3.4:1.0/3-6.3.4-port4/
-r--r--r-- 1 root root 4096 Mai 15 11:42 connect_type
-rw-r--r-- 1 root root 4096 Mai 15 11:42 disable
-rw-r--r-- 1 root root 4096 Mai 15 11:42 early_stop
-r--r--r-- 1 root root 4096 Mai 15 11:42 location
-r--r--r-- 1 root root 4096 Mai 15 11:42 over_current_count
drwxr-xr-x 2 root root    0 Mai 15 11:42 power
-rw-r--r-- 1 root root 4096 Mai 15 11:42 quirks
-r--r--r-- 1 root root 4096 Mai 15 11:42 state
-rw-r--r-- 1 root root 4096 Mai 15 11:42 uevent

sudo ls -l /sys/bus/usb/devices/3-6.3.4:1.0/3-6.3.4-port4/power/
total 0
-rw-r--r-- 1 root root 4096 Mai 15 11:43 async
-rw-r--r-- 1 root root 4096 Mai 15 11:43 autosuspend_delay_ms
-rw-r--r-- 1 root root 4096 Mai 15 11:43 control
-rw-r--r-- 1 root root 4096 Mai 15 11:43 pm_qos_no_power_off
-r--r--r-- 1 root root 4096 Mai 15 11:43 runtime_active_kids
-r--r--r-- 1 root root 4096 Mai 15 11:43 runtime_active_time
-r--r--r-- 1 root root 4096 Mai 15 11:43 runtime_enabled
-r--r--r-- 1 root root 4096 Mai 15 11:43 runtime_status
-r--r--r-- 1 root root 4096 Mai 15 11:43 runtime_suspended_time
-r--r--r-- 1 root root 4096 Mai 15 11:43 runtime_usage
```

Search for `Bus 003 Device 009` in `out_lsusb-v.txt`.
A few lines later we find `ContainerID {20b9cde5-7039-e011-a935-0002a5d5c51b}`

Search for `{20b9cde5-7039-e011-a935-0002a5d5c51b}` in `out_lsusb-v.txt`.
We find:
```
Bus 002 Device 007: ID 0bda:0411 Realtek Semiconductor Corp. Hub
Bus 002 Device 009: ID 0bda:0411 Realtek Semiconductor Corp. Hub
Bus 002 Device 010: ID 0bda:0411 Realtek Semiconductor Corp. Hub
Bus 003 Device 006: ID 0bda:5411 Realtek Semiconductor Corp. RTS5411 Hub
Bus 003 Device 008: ID 0bda:5411 Realtek Semiconductor Corp. RTS5411 Hub
Bus 003 Device 009: ID 0bda:5411 Realtek Semiconductor Corp. RTS5411 Hub
```

Try to power on/off
```bash
sudo su
echo 1 > /sys/bus/usb/devices/3-6.3.4:1.0/3-6.3.4-port4/disable
echo 1 > /sys/bus/usb/devices/2-3.3.4:1.0/2-3.3.4-port4/disable
```