import discord
import random
import dice as dc

#code base:
class MyCLient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} on action!')
        print('___/(0-0)\___')
    
    async def on_message(self, message):
        if message.author == client.user:
            return

#Defining functions:
        if message.content.startswith('-help'):
            await message.channel.send('```python\n@Commands:\n D4 = Four-sided die.\n D6 = Six-sided die.\n D8 = Eight-sided die.\n D10 = Ten-sided die\n D12 = Twelve-sided die.\n D20 = Twenty-sided die.\n -d100 = One hundred-sided die.```')

        if message.content.startswith('D4'):
            dice = random.choice(dc.d4)
            await message.channel.send(f'> {message.author.mention}\n> `Took out: {dice}`')

        if message.content.startswith('D6'):
            dice = random.choice(dc.d6)
            await message.channel.send(f'> {message.author.mention}\n> `Took out: {dice}`')

        if message.content.startswith('D8'):
            dice = random.choice(dc.d8)
            await message.channel.send(f'> {message.author.mention}\n> `Took out: {dice}`')

        if message.content.startswith('D10'):
            dice = random.choice(dc.d10)
            await message.channel.send(f'> {message.author.mention}\n> `Took out: {dice}`')

        if message.content.startswith('D12'):
            dice = random.choice(dc.d12)
            await message .channel.send(f'> {message.author.mention}\n> `Took out: {dice}`')
        
        if message.content.startswith('D20'):
            dice = random.choice(dc.d20)
            await message.channel.send(f'> {message.author.mention}\n> `Took out: {dice}`')

        if message.content.startswith('-d100'):
            dice = random.choice(dc.d100)
            
            await message.channel.send(f'> {message.author.mention}\n> `Took out: {dice}`')
        
#starting the bot:
client = MyCLient()
client.run('Your code here')