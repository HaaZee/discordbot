import discord
import asyncio
import ffmpeg

role_needed = "Countdown Masters"

async def ex(args, message, client, invoke):

  global role_needed

  voice_channel=message.author.voice.voice_channel

  if voice_channel != None:

      if role_needed.lower() in [y.name.lower() for y in message.author.roles]:

          author = message.author
          time = str(message.timestamp.__format__('%I:%M %p'))

          em = discord.Embed(title='**Match Starting**', color=discord.Color.green())
          em.add_field(name="Alert: ", value="- A snipe match is starting, pay attention!")
          em.add_field(name="Instructions: ", value="- We will do a countdown from 3 sec and you will ready up on go.")
          em.set_footer(text="Today at "+ time)
          await client.send_message(message.channel, embed=em)

          await asyncio.sleep(3)
          vc = await client.join_voice_channel(voice_channel)
          player = vc.create_ffmpeg_player('countdown.mp4')
          player.start()

          while not player.is_done():
              await asyncio.sleep(1)

          player.stop()
          await vc.disconnect()

      else:
          await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="You do not have permission to use this command. You require the **{}** role.".format(role_needed)))
