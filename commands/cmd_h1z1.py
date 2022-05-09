import discord
import asyncio
import requests
import json

async def ex(args, message, client, invoke):

    steamid = args[0]
    #433850
    url =  "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=721E1DBC94F54A914E9B0AE1250B1C5D&steamid={}&format=json".format(steamid)

    r = requests.get(url)

    try:
        for game in r.json()['response']['games']:
            if game['appid'] == 433850:
                minutes = game['playtime_forever']

        game_time = minutes / 60
        game_time = str(round(game_time, 1))
        time = game_time + " Hours"

        em = discord.Embed(title='**H1Z1 Hours:**', color=discord.Color.green())
        em.add_field(name="Hours: ", value=time)

        await client.send_message(message.channel, embed=em)

    except KeyError:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Profile must be set to public so game hours can be viewed."))
