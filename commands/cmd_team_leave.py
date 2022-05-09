import discord
import asyncio
import json
from discord.utils import get

async def ex(args, message, client, invoke):
    global role_needed
    in_team = False

    author = message.author

    with open("data/teams.json", "r") as f:
        teams = json.load(f)

    for t_name, t_info in teams.items():
        for key in t_info:
            if t_info[key] == author.id:
                name = t_name
                in_team = True

    if in_team:

        async def update_data(teams, name, member):
            team_role = get(author.server.roles, name=name)
            captain = get(author.server.roles, name='Captain')

            while True:
                if teams[name]['captain'] == member.id:
                    del teams[name]
                    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description="{} has disbanded team {}.".format(member.name, name)))
                    await client.remove_roles(member, team_role)
                    await client.remove_roles(member, captain)
                    await client.delete_role(author.server, name=team_role)
                    break

                elif teams[name]['member1'] == member.id:
                    teams[name]['member1'] = "placeholder"
                    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description="{} has left {}.".format(member.name, name)))
                    await client.remove_roles(member, team_role)
                    break

                elif teams[name]['member2'] == member.id:
                    teams[name]['member2'] = "placeholder"
                    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description="{} has left {}.".format(member.name, name)))
                    await client.remove_roles(member, team_role)
                    break

                elif teams[name]['member3'] == member.id:
                    teams[name]['member3'] = "placeholder"
                    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description="{} has left {}.".format(member.name, name)))
                    await client.remove_roles(member, team_role)
                    break


        await update_data(teams, name, author)

        with open("data/teams.json", "w") as f:
            json.dump(teams, f, indent=4)

    else:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="You are not in a team."))
