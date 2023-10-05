import psutil


def get_all_partitions():
    # Returns a list of all disk partitions.
    return psutil.disk_partitions()


def get_disk_usage(partition_mountpoint):
    # Returns usage information for a specific partition.
    return psutil.disk_usage(partition_mountpoint)


def get_total_size(usage):
    # Returns the total size of the partition.
    return usage.total


def get_used_space(usage):
    # Returns the used space of the partition.
    return usage.used


def get_free_space(usage):
    # Returns the free space of the partition.
    return usage.free


def get_percent_used(usage):
    # Returns the percentage of used space in the partition.
    return usage.percent


def convert_bytes(num):
    # Converts bytes into a human-readable unit (e.g., KB, MB).
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if abs(num) < 1024.0:
            return "%3.1f %s" % (num, unit)
        num /= 1024.0
    return "%.1f %s" % (num, "PB")


if __name__ == "__main__":
    # Display a message indicating that the main.py file should be run.
    print("Please run main.py")
