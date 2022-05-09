import discord
import asyncio
import json

async def ex(args, message, client, invoke):

    channel = message.channel
    user = message.author

    with open("data/users.json", "r") as f:
        users = json.load(f)

    coins = users[user.id]['coins']
    upgrade_cost = users[user.id]['upgrade_cost']
    mine_level = users[user.id]['mine_level']

    embed = discord.Embed(title=" ", description="You currently have **{}** coins.".format(coins), color=discord.Color.gold())
    embed.add_field(name="1: 1.5x Coin Booster", value="200 Coins", inline=False)
    embed.add_field(name="2: 2x Exp Booster", value="250 Coins", inline=False)
    embed.add_field(name="3: Simple Crate", value="300 Coins", inline=False)
    embed.add_field(name="4: Auto Daily", value="1000 Coins", inline=False)
    embed.add_field(name="5: Upgrade Mine (Current Level: {})".format(mine_level), value="{} Coins".format(upgrade_cost), inline=False)
    embed.set_footer(text="To buy, reply with item ID")
    embed.set_author(name="Offical Shop", icon_url=client.user.avatar_url)
    await client.send_message(user, embed=embed)

    reply = await client.wait_for_message(author=user)
    if reply.server is None and reply.author != client.user:
        try:
            id = int(reply.content)
            if id == 1:

                if users[user.id]['coin_boost'] != 1.5:
                    if 200 <= coins:
                        users[user.id]['coins'] -= 200
                        users[user.id]['coin_boost'] = 1.5
                        await client.send_message(user, embed=discord.Embed(color=discord.Color.green(), description="You have purchased a 1.5x Coin Booster!"))
                        with open('data/users.json', 'w') as f:
                            json.dump(users, f, indent=4)
                    else:
                        await client.send_message(user, embed=discord.Embed(color=discord.Color.red(), description="You do not have enough money!"))
                else:
                    await client.send_message(user, embed=discord.Embed(color=discord.Color.red(), description="You already have a 1.5x Coin Booster!"))


            elif id == 2:

                if users[user.id]['xp_boost'] != 2:
                    if 250 <= coins:
                        users[user.id]['coins'] -= 250
                        users[user.id]['xp_boost'] = 2
                        await client.send_message(user, embed=discord.Embed(color=discord.Color.green(), description="You have purchased a 2x Exp Booster!"))
                        with open('data/users.json', 'w') as f:
                            json.dump(users, f, indent=4)
                    else:
                        await client.send_message(user, embed=discord.Embed(color=discord.Color.red(), description="You do not have enough money!"))
                else:
                    await client.send_message(user, embed=discord.Embed(color=discord.Color.red(), description="You already have a 2x Exp Booster!"))


            elif id == 3:

                if users[user.id]['crates_owned']['simple'] < 10:
                    if 300 <= coins:
                        users[user.id]['coins'] -= 300
                        users[user.id]['crates_owned']['simple'] += 1
                        await client.send_message(user, embed=discord.Embed(color=discord.Color.green(), description="You have purchased a Simple Crate!"))
                        with open('data/users.json', 'w') as f:
                            json.dump(users, f, indent=4)
                    else:
                        await client.send_message(user, embed=discord.Embed(color=discord.Color.red(), description="You do not have enough money!"))
                else:
                    await client.send_message(user, embed=discord.Embed(color=discord.Color.red(), description="You can't own more than 10 crates."))

            elif id == 4:

                if users[user.id]['auto_daily'] == 0:
                    if 1000 <= coins:
                        users[user.id]['coins'] -= 1000
                        users[user.id]['auto_daily'] = 1
                        await client.send_message(user, embed=discord.Embed(color=discord.Color.green(), description="You have purchased a Auto Daily!"))
                        with open('data/users.json', 'w') as f:
                            json.dump(users, f, indent=4)
                    else:
                        await client.send_message(user, embed=discord.Embed(color=discord.Color.red(), description="You do not have enough money!"))
                else:
                    await client.send_message(user, embed=discord.Embed(color=discord.Color.red(), description="You already own Auto Daily."))

            elif id == 5:

                if upgrade_cost <= coins:
                    users[user.id]['coins'] -= upgrade_cost
                    users[user.id]['upgrade_cost'] = upgrade_cost * 2
                    users[user.id]['mine_level'] += 1
                    await client.send_message(user, embed=discord.Embed(color=discord.Color.green(), description="You have purchased an Upgraded Mine! Your mine is now level {}.".format(mine_level + 1)))
                    with open('data/users.json', 'w') as f:
                        json.dump(users, f, indent=4)
                else:
                    await client.send_message(user, embed=discord.Embed(color=discord.Color.red(), description="You do not have enough money!"))


            else:
                await client.send_message(user, embed=discord.Embed(color=discord.Color.red(), description="Item ID not found."))

        except ValueError:
            await client.send_message(user, embed=discord.Embed(color=discord.Color.red(), description="Reply must be an item ID."))
