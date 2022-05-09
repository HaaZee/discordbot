import discord
import asyncio

role_needed = "Admin"

async def ex(args, message, client, invoke):

    global role_needed
    if role_needed.lower() in [y.name.lower() for y in message.author.roles]:

        try:
            ammount = int(args[0]) + 1

        except:
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Please enter a valid value for message ammount!"))
            return

        messages = []
        async for m in client.logs_from(message.channel, limit=ammount):
            messages.append(m)

        await client.delete_messages(messages)

        return_msg = await client.send_message(message.channel, "Deleted %s messages." % ammount)
        await asyncio.sleep(4)
        await client.delete_message(return_msg)

    else:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="You do not have permission to use this command. You require the **{}** role.".format(role_needed)))
