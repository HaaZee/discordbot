import discord
import asyncio
from discord.utils import get

channel = None
role_needed = "Countdown Masters"

async def ex(args, message, client, invoke):

    global role_needed
    if role_needed.lower() in [y.name.lower() for y in message.author.roles]:

        channel = message.channel
        choices = {"🇦": "Solos",
                   "🇧": "Duos",
                   "🇨": "Squads"}

        vote = discord.Embed(title="**[POLL]**", description=" ", color=0x00ff00)
        value = "\n".join("- {} {}".format(*item) for item in choices.items())
        vote.add_field(name="Please vote for the match type:", value=value, inline=True)

        message_1 = await client.send_message(channel, embed=vote)

        for choice in choices:
            await client.add_reaction(message_1, choice)

        await asyncio.sleep(10)
        message_1 = await client.get_message(channel, message_1.id)

        counts = {react.emoji: react.count for react in message_1.reactions}
        winner = max(choices, key=counts.get)

        await client.send_message(channel, "POLL CLOSED. The next match will be {}".format(choices[winner]))

    else:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="You do not have permission to use this command. You require the **{}** role.".format(role_needed)))
