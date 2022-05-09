import discord
from discord import Game, Embed
import subprocess
import json
import os
import psutil
import datetime
import sys
import subprocess
import time
import STATICS
from commands import (cmd_pay, cmd_crate, cmd_gamble, cmd_shop, cmd_coins, cmd_daily, cmd_level, cmd_leaderboard, cmd_trivia, cmd_satisfied, cmd_reply,
cmd_help, cmd_cdstart, cmd_poll, cmd_vote, cmd_fortnite, cmd_team_create, cmd_team_add, cmd_team_info, cmd_team_leave, cmd_team_kick, cmd_team_colour,
cmd_modmail, cmd_status, cmd_h1z1, cmd_ban, cmd_botinfo, cmd_clear, cmd_lock, cmd_mute, cmd_report, cmd_serverinfo, cmd_userinfo, cmd_mine, cmd_claim,
cmd_eval, cmd_test)

client = discord.Client()

commands = {

    "help": cmd_help,
    "cdstart": cmd_cdstart,
    "poll": cmd_poll,
    "vote": cmd_vote,
    "fortnite": cmd_fortnite,
    "team-create": cmd_team_create,
    "team-add": cmd_team_add,
    "team-info": cmd_team_info,
    "team-leave": cmd_team_leave,
    "team-kick": cmd_team_kick,
    "team-colour": cmd_team_colour,
    "modmail": cmd_modmail,
    "status": cmd_status,
    "h1z1": cmd_h1z1,
    "reply": cmd_reply,
    "satisfied": cmd_satisfied,
    "trivia": cmd_trivia,
    "leaderboard": cmd_leaderboard,
    "level": cmd_level,
    "daily": cmd_daily,
    "coins": cmd_coins,
    "shop": cmd_shop,
    "gamble": cmd_gamble,
    "crate": cmd_crate,
    "pay": cmd_pay,
    "ban": cmd_ban,
    "botinfo": cmd_botinfo,
    "clear": cmd_clear,
    "lock": cmd_lock,
    "mute": cmd_mute,
    "report": cmd_report,
    "serverinfo": cmd_serverinfo,
    "userinfo": cmd_userinfo,
    "mine": cmd_mine,
    "claim": cmd_claim,
    "eval": cmd_eval,
    "test": cmd_test
}


@client.event
async def on_ready():
    print("Bot is logged in successfully. Running on servers:\n")
    [(lambda s: print("  - %s (%s)" % (s.name, s.id)))(s) for s in client.servers]
    await client.change_presence(game=Game(name="~help"))

@client.event
async def on_member_join(member):
    if not member.bot:
        with open("data/users.json", "r") as f:
            users = json.load(f)

        await update_data(users, member)

        with open("data/users.json", "w") as f:
            json.dump(users, f, indent=4)


@client.event
async def on_message(message):
    if not message.author.bot:

        with open("data/users.json", "r") as f:
            users = json.load(f)

        user = message.author

        await update_data(users, message.author)
        await add_experience(users, message.author, 5)
        await level_up(users, message.author, message.channel)

        if users[user.id]['auto_daily'] == 1:

            epoch = datetime.datetime.utcfromtimestamp(0)
            time_diff = (datetime.datetime.utcnow() - epoch).total_seconds() - users[user.id]['daily_time']
            boost = users[message.author.id]['coin_boost']

            if time_diff >= 86400:
                users[user.id]['daily_time'] = (datetime.datetime.utcnow() - epoch).total_seconds()
                amt = round(25 * boost)
                users[user.id]['coins'] += amt
                extra = amt - 25

                embed = discord.Embed(title=" ", description="You have claimed your daily bonus of 25 coins!", color=discord.Color.gold())
                embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                embed.set_footer(text="Your {}x coin booster gave you an extra {} coins!".format(boost, extra))
                await client.send_message(message.channel, embed=embed)


        with open("data/users.json", "w") as f:
            json.dump(users, f, indent=4)

        ownerid = "234319310670004224"

        if message.author.id == ownerid:
            if message.content == "~restart":
                os.system('cls')
                restart_embed = discord.Embed(title=" ", description="Bot restarting.", color=discord.Color.orange())
                restart_embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                await client.send_message(message.channel, embed=restart_embed)
                await client.logout()
                subprocess.call([sys.executable, "main.py"])


        if message.content.startswith(STATICS.PREFIX):
            invoke = message.content[len(STATICS.PREFIX):].split(" ")[0]
            args = message.content.split(" ")[1:]
            if commands.__contains__(invoke):
                await commands.get(invoke).ex(args, message, client, invoke)
            else:
                await client.send_message(message.channel, embed=Embed(color=discord.Color.red(), description=("The command `%s` is not valid!" % invoke)))

async def update_data(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]['experience'] = 0
        users[user.id]['level'] = 1
        users[user.id]['xp_to_next'] = 20
        users[user.id]['xp_boost'] = 1.0
        users[user.id]['coin_boost'] = 1.0
        users[user.id]['coins'] = 50
        users[user.id]['daily_time'] = 0
        users[user.id]['auto_daily'] = 0
        users[user.id]['mine_time'] = 0
        users[user.id]['upgrade_cost'] = 1000
        users[user.id]['mine_level'] = 1
        users[user.id]['crates_owned'] = {}
        users[user.id]['crates_owned']['simple'] = 0

async def add_experience(users, user, exp):
    lvl = users[user.id]['level']
    boost = users[user.id]['xp_boost']
    users[user.id]['experience'] += exp * boost
    experience = users[user.id]['experience']

    if users[user.id]['xp_to_next'] - 5 != 0:
        next_level = lvl + 1
        next_level_xp = next_level ** 4 + 4
        dif = next_level_xp - experience
        users[user.id]['xp_to_next'] = dif
    else:
        next_level = lvl + 2
        next_level_xp = next_level ** 4 + 4
        dif = next_level_xp - experience
        users[user.id]['xp_to_next'] = dif

async def level_up(users, user, channel):
    experience = users[user.id]['experience']
    lvl_start = users[user.id]['level']
    lvl_end = int(experience ** (1/4))

    if lvl_start < lvl_end:
        await client.send_message(channel, "{} has leveled up to level {}.".format(user.mention, lvl_end))
        users[user.id]['level'] = lvl_end

token = os.environ['TOKEN']
client.run(token)
