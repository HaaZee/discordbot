import discord
import asyncio
import json

async def ex(args, message, client, invoke):

    author = message.author.id
    run = True
    found = False
    own_team = True

    team = [""]
    for i in range (0,len(args)):
        team.append(args[i])
    team = " ".join(team)

    team = team.strip()

    team_list = team.split()
    if len(team_list) > 1:
        own_team = False

    with open("data/teams.json", "r") as f:
        teams = json.load(f)

    server = message.server

    if own_team == False:
        for t_name, t_info in teams.items():
            if run == True:
                if t_name == team:
                    teaminfo = discord.Embed(title="Team: "+t_name, description=" ", color=0x00ff00)
                    for key in t_info:
                        id = t_info[key]
                        found = True
                        run = False
                        if id != "placeholder":
                            user = discord.Server.get_member(server, user_id=id)
                            teaminfo.add_field(name=key.capitalize(), value="<@" + id+ ">", inline=True)

                        else:
                            teaminfo.add_field(name=key.capitalize(), value="Empty", inline=True)
    else:
        for t_name, t_info in teams.items():
            if run == True:
                for key in t_info:
                    if t_info[key] == author:
                        teaminfo = discord.Embed(title="Team: "+t_name, description=" ", color=0x00ff00)
                        for key in t_info:
                            id = t_info[key]
                            found = True
                            run = False
                            if id != "placeholder":
                                user = discord.Server.get_member(server, user_id=id)
                                teaminfo.add_field(name=key.capitalize(), value="<@" + id+ ">", inline=True)

                            else:
                                teaminfo.add_field(name=key.capitalize(), value="Empty", inline=True)

    if found == False:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Team not found."))


    try:
        await client.send_message(message.channel, embed=teaminfo)
    except UnboundLocalError:
        pass
