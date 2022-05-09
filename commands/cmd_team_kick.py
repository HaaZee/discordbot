import discord
import asyncio
import json
from discord.utils import get

async def ex(args, message, client, invoke):
    role_needed = "Captain"

    mentions = message.mentions
    try:
        member = mentions[0]
    except IndexError:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Eror, player mentioned was invalid."))

    author = message.author

    if role_needed.lower() in [y.name.lower() for y in message.author.roles]:
        with open("data/teams.json", "r") as f:
            teams = json.load(f)

        for t_name, t_info in teams.items():
            for key in t_info:
                if t_info[key] == member.id:
                    name = t_name
                    in_team = True

        if in_team:

            async def update_data(teams, name, member):
                team_role = get(author.server.roles, name=name)

                while True:
                    if teams[name]['member1'] == member.id:
                        teams[name]['member1'] = "placeholder"
                        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description="{} has been kicked from {}.".format(member.name, name)))
                        await client.remove_roles(member, team_role)
                        break

                    elif teams[name]['member2'] == member.id:
                        teams[name]['member2'] = "placeholder"
                        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description="{} has been kicked from {}.".format(member.name, name)))
                        await client.remove_roles(member, team_role)
                        break

                    elif teams[name]['member3'] == member.id:
                        teams[name]['member3'] = "placeholder"
                        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description="{} has been kicked from {}.".format(member.name, name)))
                        await client.remove_roles(member, team_role)
                        break

            await update_data(teams, name, member)

            with open("data/teams.json", "w") as f:
                json.dump(teams, f, indent=4)

        else:
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description="Player not in team."))

    else:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description="Must be team captain."))
