import requests
import geocoder
from getmac import get_mac_address

def get_own_ip():
    try:
        response = requests.get('https://httpbin.org/ip')
        return response.json().get('origin')
    except Exception as e:
        print(f"Fehler beim Ermitteln der IP-Adresse: {e}")
        return None
    

def get_country():
    try:
        response = requests.get(f'http://ip-api.com/json/{get_own_ip()}')
        return response.json().get('country')
    except Exception as e:
        print(f"Fehler beim Ermitteln von country  {e}")
        return None
    
def get_region():
    try:
        response = requests.get(f'http://ip-api.com/json/{get_own_ip()}')
        return response.json().get('regionName')
    except Exception as e:
        print(f"Fehler beim Ermitteln von region  {e}")
        return None
    
def get_city():
    try:
        response = requests.get(f'http://ip-api.com/json/{get_own_ip()}')
        return response.json().get('city')
    except Exception as e:
        print(f"Fehler beim Ermitteln von city  {e}")
        return None
    
def get_zip():
    try:
        response = requests.get(f'http://ip-api.com/json/{get_own_ip()}')
        return response.json().get('zip')
    except Exception as e:
        print(f"Fehler beim Ermitteln der plz  {e}")
        return None

def get_isp():
    try:
        response = requests.get(f'http://ip-api.com/json/{get_own_ip()}')
        return response.json().get('isp')
    except Exception as e:
        print(f"Fehler beim Ermitteln von ISP  {e}")
        return None

def get_mac():
    return get_mac_address()

def get_location():
    location = geocoder.ip('me')
    return location.latlng

def create_google_maps_link(latlng):
    return f"https://www.google.com/maps?q={latlng[0]},{latlng[1]}"
    

if __name__ == "__main__":
    print(f"IP: {get_own_ip()}")
    print(f"Country: {get_country()}")
    print(f"Region: {get_region()}")
    print(f"City: {get_city()} zip: {get_zip()}")
    print(f"ISP: {get_isp()}")