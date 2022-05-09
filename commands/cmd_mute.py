import discord
import asyncio
from discord.utils import get

is_muted= False
role_needed = "admin"

async def ex(args, message, client, invoke):

    global is_muted
    global role_needed

    mentions = message.mentions
    name = "reports-log"
    channel = get(message.server.channels, name=name, type=discord.ChannelType.text)

    user = mentions[0]
    time = args[1]
    time_sent = str(message.timestamp.__format__('%A, %d. %B %Y @ %H:%M:%S'))

    reason = [""]
    for i in range (2,len(args)):
        reason.append(args[i])
    reason = " ".join(reason)

    embed = discord.Embed(title="MUTE", description=" ", color=discord.Color.red())
    embed.add_field(name="Muted User:", value=user.mention, inline=True)
    embed.add_field(name="Muted By:", value=message.author.mention, inline=True)
    embed.add_field(name="Length:", value=time+ " seconds", inline=True)
    embed.add_field(name="Reason:", value=reason, inline=True)
    embed.add_field(name="Time:", value=time_sent, inline=True)

    await client.delete_message(message)

    if role_needed in [y.name.lower() for y in message.author.roles]:

        if is_muted == False:

            await client.send_message(channel, embed=embed)

            channel = message.channel
            mute_overwrite = discord.PermissionOverwrite(read_messages=True, send_messages=False)
            await client.edit_channel_permissions(channel, user, mute_overwrite)
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="{} has been muted for {} seconds.".format(user.mention, time)))
            is_locked = True

            await asyncio.sleep(int(time))

            channel_unmute = message.channel
            user_unmute = user
            unmute_overwrite = discord.PermissionOverwrite(read_messages=True, send_messages=True)
            await client.edit_channel_permissions(channel_unmute, user_unmute, unmute_overwrite)
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description=user.mention+" has been unmuted"))
            is_locked = False

        else:
            
            await client.edit_channel_permissions(channel_unmute, user_unmute, unmute_overwrite)
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description=user.mention+" has been unmuted"))
            is_locked = False


    else:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="You do not have permission to use this command. You require the **{}** role.".format(role_needed)))
