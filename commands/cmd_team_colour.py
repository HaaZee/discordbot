import discord
import asyncio
import json
import random
from discord.utils import get

async def ex(args, message, client, invoke):

    help = False
    role_needed = "Captain"
    author = message.author
    colour = args[0].lower()

    if role_needed.lower() in [y.name.lower() for y in author.roles]:

        with open("teams.json", "r") as f:
            teams = json.load(f)

        for t_name, t_info in teams.items():
            for key in t_info:
                if t_info[key] == author.id:
                    name = t_name

    colours = { "red" : 0xFFFFFF,
                "silver": 0xC0C0C0,
                "gray": 0x808080,
                "black": 0x000000,
                "red": 0xFF0000,
                "maroon": 0x800000,
                "yellow": 0xFFFF00,
                "olive": 0x808000,
                "lime": 0x00FF00,
                "green": 0x008000,
                "aqua":	0x00FFFF,
                "teal":	0x008080,
                "blue":	0x0000FF,
                "navy":	0x000080,
                "fuchsia": 0xFF00FF,
                "purple": 0x800080
            }

    colour_list = ["red",
                    "silver",
                    "gray",
                    "black",
                    "red",
                    "maroon",
                    "yellow",
                    "olive",
                    "lime",
                    "green",
                    "aqua",
                    "teal",
                    "blue",
                    "navy",
                    "fuchsia",
                    "purple"]

    if colour == "help":
        colours_embed = discord.Embed(title="Team Colour Help: ", description=" ", color=0x00ff00)
        colours_embed.add_field(name="Available:", value="{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n"
        .format(colour_list[0],colour_list[1],colour_list[2],colour_list[3],colour_list[4],colour_list[5],colour_list[6],colour_list[7],colour_list[8],colour_list[9],colour_list[10],colour_list[11],colour_list[12],colour_list[13],colour_list[14],colour_list[15])
        , inline=True)
        await client.send_message(message.channel, embed=colours_embed)
        help = True

    if help == False:
        team_role = get(author.server.roles, name=name)
        try:
            await client.edit_role(server=message.server, role=team_role, color=discord.Color(colours[colour]))
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description="Team colour changed."))

        except KeyError:

            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Colour specified isn't available."))
