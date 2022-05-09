import discord
import asyncio
import json
import datetime


async def ex(args, message, client, invoke):
    with open("data/users.json", "r") as f:
        users = json.load(f)

    user = message.author
    boost = users[message.author.id]['coin_boost']
    epoch = datetime.datetime.utcfromtimestamp(0)

    time_diff = (datetime.datetime.utcnow() - epoch).total_seconds() - users[user.id]['daily_time']
    if time_diff >= 86400:

        users[user.id]['daily_time'] = (datetime.datetime.utcnow() - epoch).total_seconds()
        amt = round(25 * boost)
        extra = amt - 25
        users[user.id]['coins'] += amt

        embed = discord.Embed(title=" ", description="You have claimed your daily bonus of 25 coins!", color=discord.Color.gold())
        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        embed.set_footer(text="Your {}x coin booster gave you an extra {} coins!".format(boost, extra))
        await client.send_message(message.channel, embed=embed)

        with open('data/users.json', 'w') as f:
            json.dump(users, f, indent=4)

    else:
        error_embed = discord.Embed(title=" ", description="You cannot do that yet.", color=discord.Color.red())
        error_embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
        await client.send_message(message.channel, embed=error_embed)
