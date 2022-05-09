import discord
import asyncio
import json
import operator

async def ex(args, message, client, invoke):
    # run = True
    count = 1
    # page = 1
    server = message.server

    with open ("data/points.json") as f:
        points = json.load(f)

    cd = sorted(points.items(),key=operator.itemgetter(1),reverse=True)

    leaderboard_embed = discord.Embed(title="Trivia Leaderboard: ", description=" ", color=discord.Color.blue())
    for member, point_val in cd:
        if count <= 5:
            user = discord.Server.get_member(server, user_id=member)
            leaderboard_embed.add_field(name=str(count) + " - > " + user.name, value="**Points:** {}".format(point_val), inline=False)
            count += 1

    temp_cd = dict(cd)
    count = list(temp_cd.keys()).index(message.author.id)

    for member, point_val in cd:
        if member == message.author.id:
            leaderboard_embed.add_field(name="\u200b", value="**....**", inline=False)
            leaderboard_embed.add_field(name=str(count+1) + " - > " + message.author.name, value="**Points:** {}".format(point_val), inline=False)


    message_1 = await client.send_message(message.channel, embed=leaderboard_embed)

    # ---Reaction to switch page---
    # reactions = ["◀",
    #            "▶"]
    # max = len(cd)
    # for reaction in reactions:
    #     await client.add_reaction(message_1, reaction)
    # forward = await client.wait_for_reaction(emoji="▶", message=message_1)
    # react = await client.wait_for_reaction(emoji=None, message=message_1)
    #
    # if forward:
    #     loc = page * 5
    #     page += 1
    #     new_embed = discord.Embed(title="Trivia Leaderboard: Page {} ".format(page), description=" ", color=discord.Color.blue())
    #     for member, point_val in cd[loc:]:
    #         if count <= count+5:
    #             user = discord.Server.get_member(server, user_id=member)
    #             new_embed.add_field(name=str(count) + " - > " + user.name, value="**Points:** {}".format(point_val), inline=True)
    #             count += 1
    #     new_embed.set_footer(text="Valid for 15seconds.")
    #     await client.edit_message(message_1, embed=new_embed)
    #
    # backward = await client.wait_for_reaction(emoji="◀", message=message_1)
