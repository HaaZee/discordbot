import discord
import asyncio

async def ex(args, message, client, invoke):

    channel = message.channel
    role_count = len(message.server.roles)

    online = 0
    for i in message.server.members:
        if str(i.status) == 'online' or str(i.status) == 'idle' or str(i.status) == 'dnd':
            online += 1
    all_users = []

    for user in message.server.members:
        all_users.append('{}#{}'.format(user.name, user.discriminator))
    all_users.sort()
    all = '\n'.join(all_users)

    embed = discord.Embed(title="Server info:", description=" ", color=0x00ff00)
    embed.add_field(name="Name:", value=message.server, inline=True)
    embed.add_field(name="Owners:", value=message.server.owner, inline=True)
    embed.add_field(name="Members: ", value=message.server.member_count, inline=True)
    embed.add_field(name="Users Online: ", value=online, inline=True)
    embed.add_field(name="Number Of Roles: ", value=role_count, inline=True)
    embed.add_field(name="Highest Role: ", value=message.server.role_hierarchy[0], inline=False)
    embed.add_field(name="Region: ", value=message.server.region, inline=False)
    embed.add_field(name="Date Created: ", value=message.server.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
    embed.set_thumbnail(url=message.server.icon_url)
    await client.send_message(channel, embed=embed)
