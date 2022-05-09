import discord
import asyncio
import time
import json
from discord.utils import get

async def ex(args, message, client, invoke):
    channel_name = "mod-mail"
    channel = get(message.server.channels, name=channel_name, type=discord.ChannelType.text)
    original = message.author
    time = str(message.timestamp.__format__('%I:%M %p'))

    with open("data/case.json", "r") as f:
        cases = json.load(f)

    case_id_list = []
    for case_id_iterate in cases:
        if case_id_iterate != "caseid":
            case_id_list.append(int(case_id_iterate))

    caseid = max(case_id_list) + 1
    caseid = format(caseid, "04")

    dm_embed=discord.Embed(title="Modmail: #{}".format(caseid), color=discord.Color.green(), description=" ")
    dm_embed.add_field(name="Please declare your problem/question and send it in this channel!", value="**Question must be on one message**\n*You can make a new line if you press Shift + Enter*")
    dm_embed.set_footer(text="Valid for 1 minute")
    await client.send_message(message.author, embed=dm_embed)

    message = await client.wait_for_message(author=original)
    if message.server is None and message.author != client.user:
        question = message.content

        if not caseid in cases:
            cases[caseid] = {}
            cases[caseid]['author'] = message.author.id
            cases[caseid]['message'] = question
            cases[caseid]['message_sent'] = "False"
            cases[caseid]['helped'] = "False"

            with open("data/case.json", "w") as f:
                json.dump(cases, f, indent=4)

        report_embed = discord.Embed(title="New Modmail: #{}".format(caseid) , color=discord.Color.green())
        report_embed.add_field(name="User: ", value=message.author.mention)
        report_embed.add_field(name="Question: ", value=question)
        report_embed.set_footer(text="Today at "+ time)
        await client.send_message(channel, embed=report_embed)
        await client.send_message(original, embed=discord.Embed(color=discord.Color.orange(), description="Your support request has been recieved, you will recieve help shortly."))
