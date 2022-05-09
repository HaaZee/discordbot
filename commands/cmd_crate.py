import discord
import asyncio
import json
import random
import math

async def ex(args, message, client, invoke):
    count = 1
    extra = 0
    author = message.author
    with open("data/users.json", "r") as f:
        users = json.load(f)

    balance = users[message.author.id]['coins']
    boost = users[message.author.id]['coin_boost']
    simple_amt = users[message.author.id]['crates_owned']['simple']

    if simple_amt >= 1:

        users[message.author.id]['crates_owned']['simple'] -= 1

        left = int(round(random.randint(100,700), -2))
        prize = int(round(random.randint(100,700), -2))
        right = int(round(random.randint(100,700), -2))
        while prize == left or prize == right:
            prize = int(round(random.randint(100,700), -2))

        while right == prize or right == left:
            new = int(round(random.randint(100,700), -2))

        embed = discord.Embed(title="", description="**{}** | **{}** | **{}**".format(left,prize,right), color=discord.Color.gold())
        embed.set_author(name="Simple Crate", icon_url=author.avatar_url)
        message = await client.send_message(message.channel, embed=embed)


        while count < 10:
            new = int(round(random.randint(100,700), -2))
            while new == right or new == left or new == prize:
                new = int(round(random.randint(100,700), -2))

            await asyncio.sleep(0.25)
            left = prize
            prize = right
            right = new

            embed = discord.Embed(title="", description="**{}** | **{}** | **{}**".format(left, prize, right), color=discord.Color.gold())
            embed.set_author(name="Simple Crate", icon_url=author.avatar_url)
            await client.edit_message(message, embed=embed)


            count  += 1

        await asyncio.sleep(1)

        if boost == 1.5:
            extra = round(prize * boost)

            new_bal = balance + prize + extra
            users[author.id]['coins'] = new_bal

            embed = discord.Embed(title="", description="You won {} coins!.".format(prize), color=discord.Color.gold())
            embed.set_author(name="Simple Crate", icon_url=author.avatar_url)
            embed.set_footer(text="You won an additional {} coins from your {}x coin booster!".format(extra, boost))
            await client.edit_message(message, embed=embed)

        elif boost == 1.0:
            new_bal = balance + prize
            users[author.id]['coins'] = new_bal

            embed = discord.Embed(title="", description="You won {} coins!.".format(prize), color=discord.Color.gold())
            embed.set_author(name="Simple Crate", icon_url=author.avatar_url)
            await client.edit_message(message, embed=embed)


        with open('data/users.json', 'w') as f:
            json.dump(users, f, indent=4)

    else:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="You don't own any crates. You can buy them with the shop command."))
