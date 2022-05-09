import discord
import asyncio
import json

class Client:
    def __init__(self):
        with open("data/users.json", "r") as f:
            self.users = json.load(f)

    def add_money(self, message, amt):
        self.users[message.author.id]['coins'] += amt

        with open('data/users.json', 'w') as f:
            json.dump(self.users, f, indent=4)
