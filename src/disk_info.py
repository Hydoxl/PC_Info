import psutil

def get_all_partitions():
    """Gibt eine Liste aller Partitionen zurück."""
    return psutil.disk_partitions()

def get_disk_usage(partition_mountpoint):
    """Gibt die Nutzungsinformationen für eine bestimmte Partition zurück."""
    return psutil.disk_usage(partition_mountpoint)

def get_total_size(usage):
    """Gibt die Gesamtgröße der Partition zurück."""
    return usage.total

def get_used_space(usage):
    """Gibt den genutzten Speicherplatz der Partition zurück."""
    return usage.used

def get_free_space(usage):
    """Gibt den freien Speicherplatz der Partition zurück."""
    return usage.free

def get_percent_used(usage):
    """Gibt den Prozentsatz des genutzten Speicherplatzes der Partition zurück."""
    return usage.percent

def convert_bytes(num):
    """Konvertiert Bytes in eine lesbare Einheit."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if abs(num) < 1024.0:
            return "%3.1f %s" % (num, unit)
        num /= 1024.0
    return "%.1f %s" % (num, 'PB')

if __name__ == "__main__":
    partitions = get_all_partitions()
    for partition in partitions:
        try:
            usage = get_disk_usage(partition.mountpoint)
            print(f"Disk: {partition.device}")
            print(f"  Mountpoint: {partition.mountpoint}")
            print(f"  Total Size: {convert_bytes(get_total_size(usage))}")
            print(f"  Used: {convert_bytes(get_used_space(usage))}")
            print(f"  Free: {convert_bytes(get_free_space(usage))}")
            print(f"  Percentage Used: {get_percent_used(usage)}%")
            print("---------------------------")
        except PermissionError as e:
            print(f"Unable to access {partition.device} due to permission issues: {e}")
        except Exception as e:
            print(f"An error occurred while accessing {partition.device}: {e}")
