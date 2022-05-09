import discord
import asyncio
import time

async def ex(args, message, client, invoke):
    role_needed = "Countdown Masters"

    description = []
    for i in range (0,len(args)):
      description.append(args[i])
    description = " ".join(description)


    user = str(message.author.name)
    choices = {"✅": "Yes",
               "❌": "No"}

    if role_needed.lower() in [y.name.lower() for y in message.author.roles]:

        vote = discord.Embed(title="**[POLL]**", description=description, color=0x00ff00)
        value = "\n".join("- {} {}".format(*item) for item in choices.items())
        vote.add_field(name="Please vote for your choice:", value=value, inline=True)
        vote.set_footer(text="Poll started by: {}".format(user))

        message_1 = await client.send_message(message.channel, embed=vote)

        await client.add_reaction(message_1, "✅")
        await client.add_reaction(message_1, "❌")

        t_end = time.time() + 30
        while time.time() < t_end:
            react = await client.wait_for_reaction(emoji=None,message=message_1,timeout=5)
            try:
                if react.reaction.emoji != "✅":
                    if react.reaction.emoji != "❌":
                        await client.remove_reaction(message=message_1,emoji=react.reaction.emoji,member=react.user)
            except AttributeError:
                pass
    else:
        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="You do not have permission to use this command. You require the **{}** role.".format(role_needed)))
