# usbhubctl_sysfs

The binary `usbhubctl_sysfs` has to be installed as `root`.

It will control the powerswitches by writing to `/sys/bus/usb/devices/...`

## Compile and install

```bash
sudo apt install -y make gcc
```

```bash
cd usbhubctl_sysfs
make
sudo make install
```

## Test

```bash
cd ~
usbhubctl_sysfs
-> usbhubctl_sysfs v0.0.1
```
