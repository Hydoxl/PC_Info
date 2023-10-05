import os
import socket
import getpass
import ctypes

def get_display_name():
    # For Windows:
    if os.name == "nt":
        try:
            size = 256
            buffer = ctypes.create_unicode_buffer(size)
            ctypes.windll.secur32.GetUserNameExW(3, buffer, ctypes.byref(ctypes.c_ulong(size)))
            return buffer.value
        except:
            return "Could not retrieve the display name on Windows."
    else:
        # Other platforms (this may not work for all platforms):
        return os.getenv("USER")

hostname = socket.gethostname()
username = getpass.getuser()
display_name = get_display_name()

def get_hostname():
    return hostname

def get_username():
    return username

def get_display_name():
    return display_name

if __name__ == "__main__":
    print("Please run main.py")