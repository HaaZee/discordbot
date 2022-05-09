import discord
from discord.utils import get

async def ex(args, message, client, invoke):

  name = "reports-log"
  channel = get(message.server.channels, name=name, type=discord.ChannelType.text)
  mentions = message.mentions

  try:
      user = mentions[0]
      time = str(message.timestamp.__format__('%A, %d. %B %Y @ %H:%M:%S'))

      reason = []
      for i in range (1,len(args)):
        reason.append(args[i])
      reason = " ".join(reason)

      embed = discord.Embed(title="REPORT", description=" ", color=discord.Color.red())
      embed.add_field(name="Reported User:", value=user.mention, inline=False)
      embed.add_field(name="Reported By:", value=message.author.mention, inline=False)
      embed.add_field(name="Time:", value=time, inline=False)
      embed.add_field(name="Reason:", value=reason, inline=False)
      await client.send_message(channel, embed=embed)
      await client.send_message(message.author, embed=discord.Embed(color=discord.Color.red(), description="Your report of "+user.mention+" has been noted. Thanks."))

      await client.delete_message(message)

  except IndexError:
      await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="To report a user make sure you do ~report {@USER} {REASON}."))
