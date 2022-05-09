import discord
import asyncio
import json
from discord.utils import get

async def ex(args, message, client, invoke):
    channel_name = "mod-mail"
    channel = get(message.server.channels, name=channel_name, type=discord.ChannelType.text)
    valid = True
    found = False
    already_helped = False

    choices = ["✅",
               "❌"]

    message_reply = message
    reply = []

    with open("data/case.json", "r") as f:
        cases = json.load(f)

    caseid = args[0]
    if not caseid.isdigit() or len(args) <= 1:
        await client.send_message(channel, embed=discord.Embed(color=discord.Color.red(), description="Must be formatted ~reply {CASEID} {HELP}"))
        valid = False

    if valid:

        for case_id in cases.items():
            if caseid in case_id:
                author = cases[caseid]['author']
                found = True

        for case_id, case_info in cases.items():
            if caseid in case_id:
                for key in case_info:
                    if case_info[key] == "True":
                        already_helped = True

        if not already_helped:

            if found:
                cases[caseid]['message_sent'] = "True"

                with open("data/case.json", "w") as f:
                    json.dump(cases, f, indent=4)

                author = discord.utils.get(client.get_all_members(), id=author)
                if len(args[1:]) > 1:
                    for word in args[1:]:
                        reply.append(word)
                    reply = ' '.join(reply)
                elif len(args[1:]) == 1:
                    reply = args[1]
                else:
                    await client.send_message(channel, embed=discord.Embed(color=discord.Color.red(), description="Must be formatted ~reply {CASEID} {HELP}"))

                reply_embed = discord.Embed(title="Admin Replied: #{}".format(caseid) , color=discord.Color.green())
                reply_embed.add_field(name="Admin: ", value=message_reply.author.mention)
                reply_embed.add_field(name="Help: ", value=reply)
                reply_embed.set_footer(text="If satisfied reply with ~satisfied {caseid}.\n*If not, create a new mod mail being more specific.*")

                await client.send_message(author, embed=reply_embed)
                await client.send_message(channel, embed=discord.Embed(color=discord.Color.green(), description="Your reply to case #{} has been sent.".format(caseid)))

            else:
                await client.send_message(channel, embed=discord.Embed(color=discord.Color.red(), description="CaseID invalid."))

        else:
            await client.send_message(channel, embed=discord.Embed(color=discord.Color.red(), description="Case has already been helped."))
