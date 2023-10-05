import os
import platform
import psutil
import subprocess

try:
    import cpuinfo
except ImportError:
    cpuinfo = None


def get_cpu_info():
    # Get CPU information using the 'cpuinfo' library if available, otherwise use 'platform.processor()'
    if cpuinfo:
        return cpuinfo.get_cpu_info()["brand_raw"]
    return platform.processor()


def get_gpus_info():
    try:
        # Use 'wmic' command to retrieve GPU information on Windows
        gpu_info = (
            subprocess.check_output(
                "wmic path win32_videocontroller get name", shell=True
            )
            .decode("utf-8")
            .strip()
            .split("\n")[1:]
        )
        return [gpu.strip() for gpu in gpu_info if gpu.strip()]
    except:
        # Return an empty list if GPU information cannot be retrieved
        return []


def get_ram_info():
    # Get RAM information in gigabytes (GB) using the 'psutil' library
    virtual_memory = psutil.virtual_memory()
    return virtual_memory.total / (1024**3)


if __name__ == "__main__":
    # Display a message indicating that this script should not be run directly
    print("Please run main.py")
