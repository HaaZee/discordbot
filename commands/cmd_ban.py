import discord
import asyncio
from discord.utils import get

role_needed = "admin"

async def ex(args, message, client, invoke):
    global role_needed

    mentions = message.mentions

    user = mentions[0]
    days = 7

    reason = [""]
    for i in range (1,len(args)):
        reason.append(args[i])
    reason = " ".join(reason)

    name = "reports-log"
    channel = get(message.server.channels, name=name, type=discord.ChannelType.text)

    time_sent = str(message.timestamp.__format__('%A, %d. %B %Y @ %H:%M:%S'))

    if role_needed.lower() in [y.name.lower() for y in message.author.roles]:
        if user != client:

            await client.ban(user, days)

            embed = discord.Embed(title="BAN", description=" ", color=discord.Color.red())
            embed.add_field(name="Banned User:", value=user, inline=True)
            embed.add_field(name="Muted By:", value=message.author.mention, inline=True)
            embed.add_field(name="Length:", value=days + " days", inline=True)
            embed.add_field(name="Reason:", value=reason, inline=True)
            embed.add_field(name="Time:", value=time_sent, inline=True)

            await client.delete_message(message)
            await client.send_message(channel, embed=embed)
        else:
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="The bot cannot ban itself."))

    else:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="You do not have permission to use this command. You require the **{}** role.".format(role_needed)))
