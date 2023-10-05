import requests
import geocoder
from getmac import get_mac_address

# Function to retrieve the public IP address
def get_own_ip():
    try:
        response = requests.get('https://httpbin.org/ip')
        return response.json().get('origin')
    except Exception as e:
        print(f"Error while fetching the IP address: {e}")
        return None

# Function to get the country based on the IP address
def get_country():
    try:
        response = requests.get(f'http://ip-api.com/json/{get_own_ip()}')
        return response.json().get('country')
    except Exception as e:
        print(f"Error while fetching country: {e}")
        return None

# Function to get the region based on the IP address
def get_region():
    try:
        response = requests.get(f'http://ip-api.com/json/{get_own_ip()}')
        return response.json().get('regionName')
    except Exception as e:
        print(f"Error while fetching region: {e}")
        return None

# Function to get the city based on the IP address
def get_city():
    try:
        response = requests.get(f'http://ip-api.com/json/{get_own_ip()}')
        return response.json().get('city')
    except Exception as e:
        print(f"Error while fetching city: {e}")
        return None

# Function to get the ZIP code based on the IP address
def get_zip():
    try:
        response = requests.get(f'http://ip-api.com/json/{get_own_ip()}')
        return response.json().get('zip')
    except Exception as e:
        print(f"Error while fetching ZIP code: {e}")
        return None

# Function to get the ISP (Internet Service Provider) based on the IP address
def get_isp():
    try:
        response = requests.get(f'http://ip-api.com/json/{get_own_ip()}')
        return response.json().get('isp')
    except Exception as e:
        print(f"Error while fetching ISP: {e}")
        return None

# Function to get the MAC (Media Access Control) address of the device
def get_mac():
    return get_mac_address()

# Function to get the geographical location coordinates (latitude and longitude)
def get_location():
    location = geocoder.ip('me')
    return location.latlng

# Function to create a Google Maps link based on latitude and longitude coordinates
def create_google_maps_link(latlng):
    return f"https://www.google.com/maps?q={latlng[0]},{latlng[1]}"

if __name__ == "__main__":
    print("Please run main.py")
