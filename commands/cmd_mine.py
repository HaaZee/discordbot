import discord
import asyncio
import json
import datetime

async def ex(args, message, client, invoke):

    with open("data/users.json", "r") as f:
        users = json.load(f)

    user = message.author

    coins = users[user.id]['coins']
    mine_level = users[user.id]['mine_level']
    epoch = datetime.datetime.utcfromtimestamp(0)
    cost = mine_level * 300
    time = round(4 / mine_level, 1)

    if users[user.id]['mine_time'] == 0:
        if cost <= coins:
            start_embed = discord.Embed(title=" ", description="Check back in {} hours to ~claim your rewards.".format(time), color=discord.Color.gold())
            start_embed.set_author(name="Level {} mining trip started".format(mine_level), icon_url=message.author.avatar_url)
            start_embed.set_footer(text="This cost you {} coins.".format(cost))
            await client.send_message(message.channel, embed=start_embed)

            users[user.id]['coins'] -= cost
            users[user.id]['mine_time'] = (datetime.datetime.utcnow() - epoch).total_seconds()

            with open('data/users.json', 'w') as f:
                json.dump(users, f, indent=4)

        else:
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description=("Insufficient funds! To start a mining trip you need {} coins.".format(cost))))
    else:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description=("You already have a mining trip underway!")))
