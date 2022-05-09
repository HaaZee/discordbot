import discord

channel = None

async def ex(args, message, client, invoke):

    global channel
    channel = message.channel

    if "@" in message.content:
        mentions = message.mentions
        user = mentions[0]
    else:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Please mention the user with @{USER}"))
    try:
        embed = discord.Embed(title="{}'s info:".format(user.name), description="Here's what I could find:", color=0x00ff00)
        embed.add_field(name="Name:", value=user.name, inline=True)
        embed.add_field(name="ID:", value=user.id, inline=True)
        embed.add_field(name="Status:", value=user.status, inline=True)
        embed.add_field(name="Highest Role:", value=user.top_role, inline=True)
        embed.add_field(name="Joined Server:", value=user.joined_at.__format__('%A, %d. %B %Y'), inline=True)
        embed.add_field(name="Account Created:", value=user.created_at.__format__('%A, %d. %B %Y'), inline=True)
        embed.set_thumbnail(url=user.avatar_url)
        await client.send_message(channel, embed=embed)
    except:
        pass
