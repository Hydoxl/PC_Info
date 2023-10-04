import requests
import base64

def set_webhook_avatar_from_url(webhook_url, image_url):
    # Bild von URL herunterladen
    response = requests.get(image_url)
    if response.status_code != 200:
        print(f"Fehler beim Herunterladen des Bildes: {response.status_code} - {response.text}")
        return False

    # Bild in Base64 konvertieren
    img_str = base64.b64encode(response.content)

    # Webhook aktualisieren
    headers = {
        'Content-Type': 'application/json',
    }

    data = {
        'avatar': 'data:image/jpeg;base64,' + img_str.decode('utf-8')
    }

    response = requests.patch(webhook_url, headers=headers, json=data)
   
    if response.status_code == 200:
        return True
    else:
        print(f"Fehler: {response.status_code} - {response.text}")
        return False
