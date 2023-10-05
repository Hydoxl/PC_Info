import os
import platform
import psutil
import subprocess
try:
    import cpuinfo
except ImportError:
    cpuinfo = None

def get_cpu_info():
    """Gibt die CPU-Informationen zurück."""
    if cpuinfo:
        return cpuinfo.get_cpu_info()['brand_raw']
    return platform.processor()

def get_gpus_info():
    """Gibt Informationen über alle GPUs zurück."""
    try:
        gpu_info = subprocess.check_output("wmic path win32_videocontroller get name", shell=True).decode('utf-8').strip().split("\n")[1:]
        return [gpu.strip() for gpu in gpu_info if gpu.strip()]
    except:
        return []

def get_ram_info():
    """Gibt die RAM-Informationen in GB zurück."""
    virtual_memory = psutil.virtual_memory()
    return virtual_memory.total / (1024 ** 3)

if __name__ == "__main__":
    print("Please run main.py")
