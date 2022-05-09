import discord
import asyncio
import json
import datetime
import random

async def ex(args, message, client, invoke):
    user = message.author

    with open("data/users.json", "r") as f:
        users = json.load(f)

    coins = users[user.id]['coins']
    boost = users[user.id]['coin_boost']
    mine_level = users[user.id]['mine_level']
    epoch = datetime.datetime.utcfromtimestamp(0)
    timehours = round(4 / mine_level)
    time = timehours * 60 * 60

    if users[user.id]['mine_time'] != 0:
        time_diff = (datetime.datetime.utcnow() - epoch).total_seconds() - users[user.id]['mine_time']
        if time_diff >= time:
            won = random.randint(200 * mine_level, 400 * mine_level)
            if boost != 1.0:
                extra = round(won * boost)
                embed = discord.Embed(title=" ", description="Your miners returned with {} coins!".format(won), color=discord.Color.gold())
                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.set_footer(text="Your {}x coin booster gave you an extra {} coins!".format(boost, extra))

            else:
                extra = 0
                embed = discord.Embed(title=" ", description="Your miners returned with {} coins!".format(won), color=discord.Color.gold())
                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)

            await client.send_message(message.channel, embed=embed)
            users[user.id]['coins'] += won + extra
            users[user.id]['mine_time'] = 0

            with open('data/users.json', 'w') as f:
                json.dump(users, f, indent=4)

        else:
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Your miners aren't back yet."))

    else:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="You have no active mining trip."))
