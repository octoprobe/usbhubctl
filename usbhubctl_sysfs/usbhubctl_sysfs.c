#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#ifdef __gnu_linux__
#include <fcntl.h> /* for open() / O_WRONLY */
#endif

static const char *expected_prefix = "/sys/bus/usb/devices/";

int starts_with(const char *path, const char *prefix)
{
    size_t lenstr = strlen(path);
    size_t lenprefix = strlen(prefix);
    if (lenstr < lenprefix)
    {
        return 0;
    }
    return strncmp(path, prefix, lenprefix) == 0;
}

static int error(int rc)
{
    fprintf(stderr, "usbhubctl_sysfs v%s exit(%d)\n", PROGRAM_VERSION, rc);
    exit(rc);
}

static void write_sysfs(char *path, char *value)
{
    // Test if starts with
    if (!starts_with(path, expected_prefix))
    {
        fprintf(stderr, "Expected '%s' to start with '%s' !\n", path, expected_prefix);
        error(2);
    }

    int fd = open(path, O_WRONLY);
    if (fd < 0)
    {
        fprintf(stderr, "Failed to open '%s' !\n", path);
        error(3);
    }
    int bytes = strlen(value);
    int bytes_written = write(fd, value, bytes);
    close(fd);
    if (bytes_written != bytes)
    {
        fprintf(stderr, "Failed to write '%s' to '%s'. Expected %d, written %d !\n", value, path, bytes, bytes_written);
        error(3);
    }
}

int main(int argc, char *argv[])
{
    if (argc == 1)
    {
        printf("usbhubctl_sysfs v%s\n", PROGRAM_VERSION);
        exit(0);
    }

    if ((argc % 2) != 1)
    {
        fprintf(stderr, "Expected even argument count but got %d!\n", argc);
        error(1);
    }

    for (int i = 1; i < argc; i += 2)
    {
        write_sysfs(argv[i], argv[i + 1]);
    }
}