import discord
import asyncio
import inspect
import json

async def ex(args, message, client, invoke):
    class User:
        def __init__(self):
            with open("data/users.json", "r") as f:
                self.users = json.load(f)

        def add_money(self, user, amt):
            self.users[user]['coins'] += int(amt)

            with open('data/users.json', 'w') as f:
                json.dump(self.users, f, indent=4)

        def add_xp(self, user, amt):
            self.users[user]['experience'] += int(amt)

            with open('data/users.json', 'w') as f:
                json.dump(self.users, f, indent=4)

    User = User()
    mentions = message.mentions

    ownerid = "234319310670004224"
    blocked_words = ['.delete()', 'os', 'subprocess', 'history()', "token"]
    commands = ["user.add_money",
                "user.add_xp"]
    banned = False
    if message.author.id == ownerid:
        for word in blocked_words:
            if word in message.content:
                banned = True

        if not banned:
            reason = []
            for i in range (0,len(args)):
                if args[i] != "await":
                    reason.append(args[i])
            command = " ".join(reason)
            command = command.strip("`")

            if "user" not in command:
                try:
                    cmd = eval(command)
                    if inspect.isawaitable(cmd):
                        try:
                            await cmd
                            embed = discord.Embed(title=" ", description="Code Evaluation: ", color=discord.Color.green())
                            embed.add_field(name=":inbox_tray: Input", value="```{}```".format(command), inline=False)
                            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                            await client.send_message(message.channel, embed=embed)
                        except Exception as ex:
                            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                            error_message = template.format(type(ex).__name__, ex.args)
                            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="You encountered an error: \n```{}```".format(error_message)))

                except SyntaxError:
                    try:
                        cmd = "\n".join(f"    {i}" for i in command.splitlines())
                        func = "def eval_cmd():\n"+cmd
                        print(func)
                        exec(func)
                        embed = discord.Embed(title=" ", description="Code Evaluation: ", color=discord.Color.green())
                        embed.add_field(name=":inbox_tray: Input", value="```{}```".format(command), inline=False)
                        embed.add_field(name=":outbox_tray: Output", value="```{}```".format(eval_cmd()), inline=False)
                        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                        await client.send_message(message.channel, embed=embed)

                    except Exception as ex:
                        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                        error_message = template.format(type(ex).__name__, ex.args)
                        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="You encountered an error: \n```{}```".format(error_message)))

            else:
                if "user.add_money" in message.content:
                    try:
                        user = mentions[0]
                        amt=message.content[message.content.find("(")+1:message.content.find(")")].split(",")[1].strip()
                        User.add_money(user.id, amt)
                        embed = discord.Embed(title=" ", description="Code Evaluation: ", color=discord.Color.green())
                        embed.add_field(name=":inbox_tray: Input", value="```{}```".format(command), inline=True)
                        embed.add_field(name=":outbox_tray: Output", value="```{} coins were added to {}'s balance```".format(amt, user.name), inline=True)
                        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                        await client.send_message(message.channel, embed=embed)
                    except IndexError:
                        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="You encountered an error: \n```Object User has no function: \n{}```".format(func)))


                elif "user.add_xp" in message.content:
                    try:
                        user = mentions[0]
                        amt=message.content[message.content.find("(")+1:message.content.find(")")].split(",")[1].strip()
                        User.add_money(user.id, amt)
                        embed = discord.Embed(title=" ", description="Code Evaluation: ", color=discord.Color.green())
                        embed.add_field(name=":inbox_tray: Input", value="```{}```".format(command), inline=True)
                        embed.add_field(name=":outbox_tray: Output", value="```{} xp was added to {}'s account.```".format(amt, user.name), inline=True)
                        embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                        await client.send_message(message.channel, embed=embed)
                    except IndexError:
                        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="You encountered an error: \n```No mentions in message.```"))


                elif "user" in message.content:
                    func=message.content[message.content.find(".")+1:]
                    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="You encountered an error: \n```Object User has no function: \n{}```".format(func)))
