from discord_webhook import DiscordWebhook, DiscordEmbed
from config import DEFAULT_COLOR, DISK_INFO_TITLE, DISK_INFO_DESCRIPTION, DEFAULT_WEBHOOK
import disk_info

# Webhook-Konfiguration
webhook_url = DEFAULT_WEBHOOK  # Die URL des Webhooks

# embed-Konfiguration
color = DEFAULT_COLOR  # Die farbe des Embeds
title = DISK_INFO_TITLE # Der Titel des Embeds
description = DISK_INFO_DESCRIPTION  # Die Beschreibung des Embeds

# Alle verfügbaren Partitionen abrufen
partitions = disk_info.get_all_partitions()

# Ein DiscordWebhook-Objekt erstellen
webhook = DiscordWebhook(url=webhook_url, rate_limit_retry=True)

# Ein DiscordEmbed-Objekt erstellen
embed = DiscordEmbed(title=title, description=description, color=color)

# Durch alle Partitionen gehen und ihre Informationen abrufen
for partition in partitions:
    try:
        usage = disk_info.get_disk_usage(partition.mountpoint)
        value = f"```Total Size: {disk_info.convert_bytes(disk_info.get_total_size(usage))}\nUsed: {disk_info.convert_bytes(disk_info.get_used_space(usage))}\nFree: {disk_info.convert_bytes(disk_info.get_free_space(usage))}\nPercentage Used: {disk_info.get_percent_used(usage)}%```"
        # Ein Feld zum Embed hinzufügen, das die Partitionsinformationen enthält
        embed.add_embed_field(name=f"Disk: {partition.device}", value=value, inline=False)
    except Exception:
        pass  # Bei einem Fehler wird die aktuelle Partition übersprungen

# Das Embed-Objekt dem Webhook hinzufügen
webhook.add_embed(embed)

# Den Webhook ausführen (senden)
def send_disk_info():
    response = webhook.execute()
