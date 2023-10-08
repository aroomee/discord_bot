import discord; import random;
from discord.ext import commands
class bomb(discord.Client):
    async def on_ready(self):
        self.score = 0
        self.mode = 'ready'
    
    def newcard(self):
        a = random.randrange(0,8)
        if a == 0:
            a = 'bomb'
            return a
        else:
            self.score=self.score+a
        return a
    async def on_message(self, message):
        command = message.content
        if message.author == client.user:
            return
        print('command:', command, 'mode: ', self.mode)
        if '!게임하자' in command:
            self.mode = 'gaming'
            card = self.newcard()
            await message.channel.send('그럼 시작합니다!')
            await message.channel.send(f'지금 카드는 {card}입니다')
            if card =='bomb':
                await message.channel.send('그러므로 당신은 0점!')
                return
            else:await message.channel.send('계속 하시겠습니까?(응,아니)')
        if '응' in command and self.mode == 'gaming':
            card = self.newcard()
            await message.channel.send(f'지금 카드는 {card} 입니다')
            if card =='bomb':
                await message.channel.send('그러므로 당신은 0점!')
                self.score = 0
                return
            else:await message.channel.send('계속 하시겠습니까?(응,아니)')
        elif '아니' in command and self.mode=='gaming':
            await message.channel.send(f'지금까지의 점수는 {self.score}입니다')
            self.mode = 'ready'
            self.score = 0


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = bomb(intents=intents)

client.run('your token')