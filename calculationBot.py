import discord
from datetime import datetime
import random
from discord.ext import commands
import cv2

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        self.mode = 'wait'
        self.problems = []
        self.currentCount = 0

    def makeProblem(self):
        one = random.randrange(0,11)
        two = random.randrange(0,11)
        self.problems.append([one, two])
        return [one, two]
    def takephoto(self, filename):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cv2.imwrite(filename, frame)
        cap.release()
    async def on_message(self, message):
        print(message)
        if message.author == client.user:
            return
        command = message.content
        print('command', command)
        print('mode: ', self.mode)
        if '%photo' in command:
            day = datetime.now()
            today = f"{day.month}_{day.day}.png"
            self.takephoto(today)
            await message.channel.send(file=discord.File(today))
        if self.mode !='game' and '%play' in command:
            await message.channel.send('10문제를 내겠습니다.')
            self.mode = 'game'
            problem = self.makeProblem()
            await message.channel.send(f'{problem[0]} + {problem[1]}')
        elif self.mode == 'game' and command and command.isdigit():
            answer = int(command)
            if answer == self.problems[self.currentCount][0] + self.problems[self.currentCount][1]:
                await message.channel.send('okay')
            else:
                await message.channel.send('no')
            self.currentCount +=1
            if self.currentCount == 10:
                self.mode= 'wait'
                self.currentCount =0
                self.problems=[]
                await message.channel.send('finished. good job!!')
                return
            prob = self.makeProblem()
            await message.channel.send(f'{prob[0]} + {prob[1]}')
        if '%add' in command:
            command =command.split()
            await message.channel.send(int(command[1]) + int(command[2]))
        if '%subtract' in command:
            command =command.split()
            await message.channel.send(int(command[1]) - int(command[2]))
        if '%divide' in command:
            command =command.split()
            await message.channel.send(int(command[1]) / int(command[2]))
        if '%multiply' in command:
            command =command.split()
            await message.channel.send(int(command[1]) * int(command[2]))
        
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = MyClient(intents=intents)

client.run('MTE1NzU1MTYwNDY1NzA0MTQ5OQ.GsQEJk.b0mOQfcy4EwU-uEevFvmcA3-MhD7AUPpXXN9u4')