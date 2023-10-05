import requests
import base64


def set_webhook_avatar_from_url(webhook_url, image_url):
    # Download an image from a given URL
    response = requests.get(image_url)

    # Check if the image download was successful
    if response.status_code != 200:
        print(f"Error downloading the image: {response.status_code} - {response.text}")
        return False

    # Convert the image to Base64 encoding
    img_str = base64.b64encode(response.content)

    # Update a webhook's avatar using the provided image
    headers = {
        "Content-Type": "application/json",
    }

    data = {"avatar": "data:image/jpeg;base64," + img_str.decode("utf-8")}

    # Send a PATCH request to update the webhook's avatar
    response = requests.patch(webhook_url, headers=headers, json=data)

    # Check if the update was successful
    if response.status_code == 200:
        return True
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return False


if __name__ == "__main__":
    print("Please run main.py")