import discord
import asyncio
import json
import time
from discord.utils import get

role_needed = "Captain"

async def ex(args, message, client, invoke):
    global role_needed

    mentions = message.mentions
    role = "member"
    try:
        member = mentions[0]
    except IndexError:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Error, player mentioned was invalid."))

    author = message.author
    accepted = False

    if role_needed.lower() in [y.name.lower() for y in message.author.roles]:
        with open("data/teams.json", "r") as f:
            teams = json.load(f)

        for t_name, t_info in teams.items():
            for key in t_info:
                if t_info[key] == author.id:
                    name = t_name

        async def update_data(teams, name, member):
            in_team = False
            team_role = get(author.server.roles, name=name)

            for team_name, team_info in teams.items():
                for team_key in team_info:
                    if member.id in team_info[team_key]:
                        in_team = True

            while True:
                if teams[name]['member1'] == "placeholder" and in_team == False:
                    teams[name]['member1'] = member.id
                    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description="{} added to {} as a {}.".format(member.name, name, role)))
                    await client.add_roles(member, team_role)
                    break

                elif teams[name]['member2'] == "placeholder" and in_team == False:
                    teams[name]['member2'] = member.id
                    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description="{} added to {} as a {}.".format(member.name, name, role)))
                    await client.add_roles(member, team_role)
                    break

                elif teams[name]['member3'] == "placeholder" and in_team == False:
                    teams[name]['member3'] = member.id
                    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description="{} added to {} as a {}.".format(member.name, name, role)))
                    await client.add_roles(member, team_role)
                    break

                elif in_team == True:
                    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Player already in team."))
                    break

                else:
                    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="No space in team."))
                    break


        async def send_dm(member, author, name, accepted):
                choices = ["✅",
                           "❌"]
                yes = False
                no = False
                message_1 = await client.send_message(member, embed=discord.Embed(color=discord.Color.orange(), description="You have been invited to join {} by Captain {}, do you accept.".format(name, author.name)))
                for choice in choices:
                    await client.add_reaction(message_1, choice)

                res1 = await client.wait_for_reaction(emoji="✅", message=message_1, timeout=30)
                res2 = await client.wait_for_reaction(emoji="❌", message=message_1, timeout=30)
                if not res1.user == None or not res2.user == None:
                    if not res1.user.id == client.user or res2.user.id == client.user:
                        if res1:
                            yes = True
                        elif res2:
                            no = False

                if yes:
                    await client.send_message(member, embed=discord.Embed(color=discord.Color.orange(), description="You have joined team {}".format(name)))
                    accepted = True
                if not yes:
                    await client.send_message(member, embed=discord.Embed(color=discord.Color.orange(), description="You have declined the team invitation."))
                    accepted = False

                if accepted == True:
                    await update_data(teams, name, member)

                    with open("data/teams.json", "w") as f:
                        json.dump(teams, f, indent=4)

                else:
                    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Player declined your invite."))

        await send_dm(member, author, name, accepted)


    else:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="You must be captain of a team."))
