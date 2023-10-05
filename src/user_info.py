# Import necessary modules
import os
import socket
import getpass
import ctypes

# Function to retrieve the user's display name
def get_display_name():
    # Check the operating system
    if os.name == "nt":  # For Windows:
        try:
            size = 256
            buffer = ctypes.create_unicode_buffer(size)
            ctypes.windll.secur32.GetUserNameExW(
                3, buffer, ctypes.byref(ctypes.c_ulong(size))
            )
            return buffer.value  # Return the user's display name
        except:
            return "Could not retrieve the display name on Windows."  # Return an error message if unable to retrieve
    else:  # For other platforms (this may not work for all platforms):
        return os.getenv(
            "USER"
        )  # Return the user's display name from the USER environment variable


# Get the hostname of the system
hostname = socket.gethostname()

# Get the username of the current user
username = getpass.getuser()

# Get the display name of the user
display_name = get_display_name()

# Function to get the hostname
def get_hostname():
    return hostname  # Return the hostname of the system


# Function to get the username
def get_username():
    return username  # Return the username of the current user


# Function to get the display name
def get_display_name():
    return display_name  # Return the user's display name


# Main code block
if __name__ == "__main__":
    print("Please run main.py")  # Print a message instructing to run main.py