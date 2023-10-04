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
    print(f"CPU: {get_cpu_info()}")
    
    gpus = get_gpus_info()
    if gpus:
        for index, gpu_name in enumerate(gpus, 1):
            print(f"GPU {index}: {gpu_name}")
    else:
        print("GPU-Informationen sind nicht verfügbar.")

    print(f"RAM: {get_ram_info():.1f} GB")
    
    print("HWIDs (Volume Serial Numbers) für alle Partitionen:")
    serial_numbers = get_volume_serial_numbers()
    for drive, hwid in serial_numbers.items():
        print(f"  Laufwerk {drive}: {hwid}")
