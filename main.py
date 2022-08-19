import discord
import random

#configurando o dado:
 

#codigo base:
class MyCLient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    
    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('-'):
            await message.channel.send('This command is incomplete or wrong! Use  "-help" to learn more about the commands.')

        if message.content.startswith('-d8'):
            d8 = random.choice([1,2,3,4,5,6,7,8])
            await message.channel.send(f'{message.author.mention} tirou {d8}')
#ligando o bot
client = MyCLient()
#token do bot
client.run('Your token here.')