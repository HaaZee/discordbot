import discord
import asyncio
import requests
import json
import random

async def ex(args, message, client, invoke):
    async def update_data(points, user, amt_won):
        point_value = None
        exists = False

        for member, point in points.items():
            if member == user:
                exists = True

        if not user in points and exists == False:
            points[user] = 1

        elif user in points and exists == True:
            for member, point_val in points.items():
                if member == user:
                    point_value = point_val

            points[user] = point_value + amt_won

    try:
        url = "https://opentdb.com/api.php?amount=1&category=18"
        incorrect_answers = []
        author = message.author

        r = requests.get(url)
        won = 0

        for res in r.json()['results']:
            difficulty = res['difficulty']
            question = res['question']
            correct = res['correct_answer']

        for key in r.json()['results']:
            for value in key:
                if value == "incorrect_answers":
                    for i in range(0,len(key[value])):
                        incorrect_answers.append(key[value][i])

        print(correct)

        answers = []
        for answer in incorrect_answers:
            answers.append(answer)
        answers.append(correct)
        random.shuffle(answers)

        if difficulty == "easy":
            won = 1
        elif difficulty == "medium":
            won = 2
        elif difficulty == "hard":
            won = 3

        display = {"Difficulty:": difficulty.capitalize() + " - {} Point(s)".format(won),
                   "Question:": question,
                   "1.": answers[0],
                   "2.": answers[1],
                   "3.": answers[2],
                   "4.": answers[3],
                  }

        for item in display:
            if item == "1.":
                answer = display[item]
                if answer == correct:
                    correct_num = 1
            if item == "2.":
                answer = display[item]
                if answer == correct:
                    correct_num = 2
            if item == "3.":
                answer = display[item]
                if answer == correct:
                    correct_num = 3
            if item == "4.":
                answer = display[item]
                if answer == correct:
                    correct_num = 4

        em = discord.Embed(title="Trivia: Computer Science", description=" ", color=discord.Color.orange())
        for key in display:
            em.add_field(name=key.capitalize(), value=display[key], inline=True)

        em.set_footer(text="NOTE: You have 30 seconds to answer.")
        await client.send_message(message.channel, embed=em)

        guess = await client.wait_for_message(author=author, timeout=30)
        if guess.content.lower() == correct.lower():
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description="You were correct, well done!"))

            with open ("data/points.json", "r") as f:
                points = json.load(f)
            await update_data(points, author.id, won)

            with open("data/points.json", "w") as f:
                json.dump(points, f, indent=4)

        elif guess.content == str(correct_num):
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description="Correct! You gained **{}** point(s)!".format(won)))

            with open ("data/points.json", "r") as f:
                points = json.load(f)
            await update_data(points, author.id, won)

            with open("data/points.json", "w") as f:
                json.dump(points, f, indent=4)

        else:
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Incorrect. The answer was: ```{} or {}```".format(correct, correct_num)))
    except IndexError:
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="API error. Please try again"))
