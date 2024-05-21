# uhubctl Makefile
#
UNAME_S := $(shell uname -s)

DESTDIR ?=
prefix  ?= /usr
sbindir ?= $(prefix)/sbin

INSTALL		:= install
# 755: -rwxr-xr-x
INSTALL_DIR	:= $(INSTALL) -m 755 -d
# 4755: -rwsr-xr-x
INSTALL_PROGRAM	:= $(INSTALL) -m 4755
RM		:= rm -rf

CC ?= gcc
CFLAGS ?= -g -O0
CFLAGS += -Wall -Wextra -std=c99 -pedantic
GIT_VERSION := $(shell git describe --match "v[0-9]*" --abbrev=8 --dirty --tags | cut -c2-)
ifeq ($(GIT_VERSION),)
	GIT_VERSION := $(shell cat VERSION)
endif
CFLAGS += -DPROGRAM_VERSION=\"$(GIT_VERSION)\"

# Use hardening options on Linux
ifeq ($(UNAME_S),Linux)
	LDFLAGS += -Wl,-zrelro,-znow
endif

PROGRAM = usbhubctl_sysfs

$(PROGRAM): $(PROGRAM).c
	$(CC) $(CPPFLAGS) $(CFLAGS) $@.c -o $@ $(LDFLAGS)

install:
	$(INSTALL_DIR) $(DESTDIR)$(sbindir)
	$(INSTALL_PROGRAM) $(PROGRAM) $(DESTDIR)$(sbindir)

clean:
	$(RM) $(PROGRAM).o $(PROGRAM).dSYM $(PROGRAM)