import discord
import asyncio
import json
import random

async def ex(args, message, client, invoke):
    try:
        amt = int(args[0])

        user = message.author

        with open("data/users.json", "r") as f:
            users = json.load(f)

        balance = users[user.id]['coins']
        boost_actual = users[user.id]['coin_boost']
        rand = random.randint(1,2)
        win = amt

        if amt <= 200:
            if amt != 0:
                if amt <= balance:
                    if rand == 1:
                        if boost_actual == 1.0:
                            win_embed = discord.Embed(title=" ", description="You won {} coins and your original bet!".format(win), color=discord.Color.green())
                            win_embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                            await client.send_message(message.channel, embed=win_embed)
                            new_bal = balance + win + amt

                        else:
                            extra = round(win * boost_actual)
                            win_embed = discord.Embed(title=" ", description="You won {} coins and your original bet!".format(win), color=discord.Color.green())
                            win_embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                            win_embed.set_footer(text="You won an additional {} coins from your {}x coin booster!".format(extra, boost_actual))
                            await client.send_message(message.channel, embed=win_embed)
                            new_bal = balance + win + amt + extra

                    elif rand == 2:
                        lose_embed = discord.Embed(title=" ", description="You lost {} coins!".format(amt), color=discord.Color.red())
                        lose_embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                        await client.send_message(message.channel, embed=lose_embed)
                        new_bal = balance - amt

                    users[user.id]['coins'] = new_bal
                    with open('data/users.json', 'w') as f:
                        json.dump(users, f, indent=4)

                else:
                    error_embed = discord.Embed(title=" ", description="You do not have enough money.", color=discord.Color.red())
                    error_embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                    await client.send_message(message.channel, embed=error_embed)

            else:
                await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="You cannot gamble 0 coins."))

        else:
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="You cannot gamble more than 200 coins."))

    except IndexError:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Command should be formatted **~gamble [AMOUNT]**"))
