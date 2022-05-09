import discord
import asyncio
import json

async def ex(args, message, client, invoke):

    channel = message.channel
    user = message.author

    with open("data/users.json", "r") as f:
        users = json.load(f)

    level = users[user.id]['level']
    exp = round(users[user.id]['experience'])
    xpnext = round(users[user.id]['xp_to_next'])
    booster = users[user.id]['xp_boost']

    field = "{}/{}".format(exp, xpnext+exp)

    embed = discord.Embed(title=" ", description=" ", color=discord.Color.blue())
    embed.add_field(name="Level", value=level, inline=False)
    embed.add_field(name="Exp", value=field, inline=False)
    embed.add_field(name="To next level", value=xpnext, inline=False)
    embed.set_footer(text="Exp Booster: {}x".format(booster))
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    await client.send_message(channel, embed=embed)
