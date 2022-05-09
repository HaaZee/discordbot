import discord
import asyncio
import json

async def ex(args, message, client, invoke):

    channel = message.channel
    user = message.author

    with open("data/users.json", "r") as f:
        users = json.load(f)

    coins = round(users[user.id]['coins'])
    booster = users[user.id]['coin_boost']

    embed = discord.Embed(title=" ", description="You currently have **{}** coins.".format(coins), color=discord.Color.gold())
    embed.set_footer(text="Coin Booster: {}x".format(booster))
    embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
    await client.send_message(channel, embed=embed)
