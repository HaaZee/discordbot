import discord

async def ex(args, message, client, invoke):

    #ADMIN COMMANDS
    clear = "**~clear [NUMBER]** - Clears specific number of messages"
    mute = "**~mute [USER] [TIME] [REASON]** - Mutes specific user for time and reason added"
    lock = "**~lock** - Will lock chat, no messages can be seen or sent"
    ban = "**~ban [USER] [REASON]** - Will ban user and remove messages sent by user in the past 7 days"

    #COUNTDOWN MASTER
    poll = "**~poll** - Will start a scrims poll"
    cdstart = "**~cdstart** - Will start a 5 minute countdown"
    vote = "**~vote [TOPIC]** - Allows users to vote yes or no on a topic, results will be totalled 30seconds later"

    #DEFAULT COMMANDS
    fortnite = "**~fortnite [PLATFORM] [USER]** - Returns fortnite stats for specifc user"
    modmail = "**~modmail** - Sends question to all staff members"
    userinfo = "**~userinfo [USER]** - Returns infortmation about specific user"
    serverinfo = "**~serverinfo** - Returns infortmation about the current server"
    botinfo = "**~botinfo** - Returns information regarding bot"
    report = "**~report [USER] [REASON]** - Will report user for specfic reason. Must have a channel named 'reports-log'"


    coins = "**~coins** - Returns current coin balance"
    gamble = "**~gamble [AMOUNT]** - Gambles specific number of coins"
    shop = "**~shop** - Shows shop"
    level = "**~level** - Returns info about current level"
    pay = "**~pay [@PLAYER] [AMOUNT]** - Pays player mentioned the specifc value"
    mine = "**~mine** - Starts a mining trip for 300 coins"
    claim = "**~claim** - Claims rewards from mining trip"

    trivia = "**~trivia** - Gives random question about Computer Science."
    leaderboard = "**~leaderboard** - Shows Trivia leaderboard"


    #TEAM COMMANDS
    team_create = "**~team-create [TEAM NAME]** - Creates a team with specified name"
    team_info = "**~team-info [TEAM NAME*]** - Returns info about own team, * Returns info on team specified"
    team_leave = "**~team-leave** - Leaves current team"
    team_add = "**~team-add [@PLAYER]** - Adds specified player to current team"
    team_kick = "**~team-kick [@PLAYER]** - Kicks player from team"
    team_colour = "**~team-colour [HELP]** - Changes role colour for current team."

    embed = discord.Embed(title="COMMANDS:", description=" ", color=0x00ff00)
    embed.add_field(name="__**Admin Commands**__", value="\n{}\n{}\n{}\n{}".format(clear, mute ,lock, ban), inline=True)
    embed.add_field(name="__**Countdown Master Commands**__", value="\n{}\n{}\n{}".format(poll, cdstart,vote), inline=True)
    embed.add_field(name="__**Team Commands**__", value="\n{}\n{}\n{}\n{}\n{}\n{}".format(team_add, team_kick, team_colour, team_leave, team_info, team_create), inline=True)
    embed.add_field(name="__**Default Commands**__", value="\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(fortnite, modmail, userinfo, serverinfo, botinfo, report, coins, gamble, shop, level, trivia, leaderboard, pay), inline=True)

    await client.send_message(message.author, embed=embed)
