import discord
import asyncio
import json

async def ex(args, message, client, invoke):

    case_found = False

    try:
        caseid = args[0]

        with open("data/case.json", "r") as f:
            cases = json.load(f)

        if message.server is None and message.author != client.user:

            for case_id, case_info in cases.items():
                if case_id == caseid:
                    for key in case_info:
                        if case_info[key] == message.author.id:
                            case_found = True
                            break
                        else:
                            caseid = None
            if case_found:
                if caseid != None:

                    for case_id in cases.items():
                        if caseid in case_id:
                            if cases[caseid]['helped'] != "True":
                                cases[caseid]['helped'] = "True"

                                with open("data/case.json", "w") as f:
                                    json.dump(cases, f, indent=4)

                                await client.send_message(message.author, embed=discord.Embed(color=discord.Color.green(), description="Modmail marked as satisfied."))
                            else:
                                await client.send_message(message.author, embed=discord.Embed(color=discord.Color.red(), description="Modmail already marked as helped."))
                else:
                    await client.send_message(message.author, embed=discord.Embed(color=discord.Color.red(), description="This is not your case."))
            else:
                await client.send_message(message.author, embed=discord.Embed(color=discord.Color.red(), description="CaseID not found."))

    except IndexError:
        await client.send_message(message.author, embed=discord.Embed(color=discord.Color.red(), description="Must be formatted ~satisfied {CASEID}"))
