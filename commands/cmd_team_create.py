import discord
import asyncio
import json
from discord.utils import get

async def ex(args, message, client, invoke):

    user = message.author.id
    mentions = message.mentions

    name_list = [""]
    for i in range (0,len(args)):
        name_list.append(args[i])
    name_list = " ".join(name_list)

    name = name_list.strip()
    if len(name) > 0:

        async def update_data(teams, name):
            exists = False
            team_role_exists = False
            team_role_needed = str(name)

            for t_name, t_info in teams.items():
                for key in t_info:
                    if t_info[key] == user:
                        exists = True

            if not name in teams and exists == False:
                teams[name] = {}
                teams[name]['captain'] = user
                teams[name]['member1'] = "placeholder"
                teams[name]['member2'] = "placeholder"
                teams[name]['member3'] = "placeholder"

                author = message.author

                cap_role = get(author.server.roles, name="Captain")
                await client.add_roles(author, cap_role)

                if team_role_needed.lower() in [y.name.lower() for y in author.server.roles]:
                    team_role_exists = True

                if team_role_exists == False:
                    await client.create_role(author.server, name=name)

                team_role = get(author.server.roles, name=name)
                await client.add_roles(author, team_role)

                await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description="Team created"))

            elif exists == True:
                await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description="You are already in a team."))

            else:
                await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Team already exists"))

        with open("data/teams.json", "r") as f:
            teams = json.load(f)

        await update_data(teams, name)

        with open("data/teams.json", "w") as f:
            json.dump(teams, f, indent=4)

    else:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="This command should be formatted **~team-create {TEAM NAME}**"))
