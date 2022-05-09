import discord
import asyncio
import json

async def ex(args, message, client, invoke):
    with open("data/users.json", "r") as f:
        users = json.load(f)

    try:
        mentions = message.mentions
        amt = int(args[1])
        try:
            member = mentions[0]

            their_bal = users[member.id]['coins']
            self_bal = users[message.author.id]['coins']

            if amt <= self_bal:
                their_new_bal = their_bal + amt
                self_new_bal = self_bal - amt

                users[member.id]['coins'] = their_new_bal
                users[message.author.id]['coins'] = self_new_bal

                await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description="You successfully payed {} {} coins.".format(member.mention, amt)))

                with open('data/users.json', 'w') as f:
                    json.dump(users, f, indent=4)

            else:
                await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Insufficient funds."))

        except IndexError:
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Erorr, player mentioned was invalid."))

    except ValueError:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Error, Ammount must be an integer."))
