import discord
import asyncio
import requests

async def ex(args, message, client, invoke):

    username = []

    try:
        platform = args[0]
        for i in range(1, len(args)):
            username.append(args[i])
    except IndexError:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Please use the correct format. ~fortnite {PLATFORM} {USERNAME}"))

    username = ' '.join(username)
    username.replace(" ", "%20")

    url = "https://api.fortnitetracker.com/v1/profile/{}/{}".format(platform, username)
    headers = {'TRN-Api-Key' : '8257ed18-77dd-4918-9816-fa41c6312ad3'}

    r = requests.get(url, headers=headers)

    tempory_dict = {}

    #p2 = Solo
    #p10 = Duo
    #p9 = Squad

    try:

        #SOLOS
        solo_wins = r.json()['stats']['p2']['top1']['value']
        solo_kills = r.json()['stats']['p2']['kills']['value']
        solo_kd = r.json()['stats']['p2']['kd']['value']
        solo_matches = r.json()['stats']['p2']['matches']['value']

        #DUOS
        duo_wins = r.json()['stats']['p10']['top1']['value']
        duo_kills = r.json()['stats']['p10']['kills']['value']
        duo_kd = r.json()['stats']['p10']['kd']['value']
        duo_matches = r.json()['stats']['p10']['matches']['value']

        #SQUADS
        squad_wins = r.json()['stats']['p9']['top1']['value']
        squad_kills = r.json()['stats']['p9']['kills']['value']
        squad_kd = r.json()['stats']['p9']['kd']['value']
        squad_matches = r.json()['stats']['p9']['matches']['value']


        embed = discord.Embed(title="**Fortnite Stats For:**", description=username, color=0x00ff00, inline=True)
        embed.add_field(name="__**Solo**__", value="\n**Wins**: {}\n**Kills**: {}\n**K/D**: {}\n**Matches Played**: {}".format(solo_wins, solo_kills, solo_kd, solo_matches))
        embed.add_field(name="__**Duo**__", value="\n**Wins**: {}\n**Kills**: {}\n**K/D**: {}\n**Matches Played**: {}".format(duo_wins, duo_kills, duo_kd, duo_matches))
        embed.add_field(name="__**Squad**__", value="\n**Wins**: {}\n**Kills**: {}\n**K/D**: {}\n**Matches Played**: {}".format(squad_wins, squad_kills, squad_kd, squad_matches))

        await client.send_message(message.channel, embed=embed)

    except KeyError:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Username or platform not found."))
