import discord
import asyncio
import psutil

async def ex(args, message, client, invoke):
    em = discord.Embed(title='**Bot Status:**', color=0x32441c)
    try:
        mem_usage = '{:.2f} MB'.format(__import__('psutil').Process().memory_full_info().uss / 1024 ** 2 * 1.049)
    except AttributeError:
        # OS doesn't support retrieval of USS (probably BSD or Solaris)
        mem_usage = '{:.2f} MB'.format(__import__('psutil').Process().memory_full_info().rss / 1024 ** 2 * 1.049)
    em.add_field(name=u'\U0001F4BE RAM usage:', value=mem_usage +" / 500 MB")

    await client.send_message(message.channel, embed=em)
