import discord
import asyncio

is_locked = False
role_needed = "admin"

async def ex(args, message, client, invoke):

    global is_locked
    global role_needed

    if role_needed.lower() in [y.name.lower() for y in message.author.roles]:

        if is_locked == False:

            channel = message.channel
            default = message.server.default_role
            lock_overwrite = discord.PermissionOverwrite(read_messages=False, send_messages=False)
            await client.edit_channel_permissions(channel, default, lock_overwrite)
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Locked down #{}".format(message.channel)))
            is_locked = True

        else:
            channel_unlock = message.channel
            default_unlock = message.server.default_role
            unlock_overwrite = discord.PermissionOverwrite(read_messages=True, send_messages=True)
            await client.edit_channel_permissions(channel_unlock, default_unlock, unlock_overwrite)
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Unlocked #{}".format(message.channel)))
            is_locked = False

    else:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="You do not have permission to use this command. You require the **{}** role.".format(role_needed)))
