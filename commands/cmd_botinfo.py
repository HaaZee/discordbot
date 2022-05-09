import discord
import asyncio


async def ex(args, message, client, invoke):

    time = str(client.user.created_at.__format__('%A, %d. %B %Y'))

    embed = discord.Embed(title="Bot info:", description="", color=0x00ff00)
    embed.add_field(name="Name:", value="Helper Bot", inline=False)
    embed.add_field(name="Created:", value=time, inline=False)
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.set_footer(text="Created by: HaZe#7197")
    await client.send_message(message.channel, embed=embed)
