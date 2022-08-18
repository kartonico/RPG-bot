import discord
import random

#configurando o dado:
d8 = random.randrange(8)

#codigo base:
class MyCLient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    
    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('?hi'):
            await message.channel.send('HI brother! ')

        if message.content.startswith('?d8'):
            await message.channel.send(f'@{message.author}: {d8}')

#ligando o bot
client = MyCLient()
#token do bot
client.run('Your token here.')