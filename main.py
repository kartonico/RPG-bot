import discord
import random
import dice as dc

#code base:
class MyCLient(discord.Client):
#client commands:
    async def on_ready(self):
        await client.change_presence(status=discord.Status.dnd,activity=discord.Game('-help'))
        print(f'{self.user} on action!')
        print('___/(0-0)\___')

#Defining functions:
    async def on_message(self, message):
        if message.author == client.user:
            return

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

        #embeds:
        if message.content.startswith('-help'):
            embed=discord.Embed(title="Commands:",description="D4 = Four-sided die.\n D6 = Six-sided die.\n D8 = Eight-sided die.\n D10 = Ten-sided die.\n D12 = Twelve-sided die.\n D20 = Twenty-sided die.\n -d100 = One hundred-sided die.", color=0x0000FF)
            embed.add_field(name="Versão em português:", value="-ajuda", inline=False)
            await message.channel.send(embed=embed)

        if message.content.startswith('-ajuda'):
            embed=discord.Embed(title="Comandos:",description="D4 = Dado de quatro lados.\n D6 = Dado de seis lados.\n D8 = Dado de oito lados.\n D10 = Dado de dez lados.\n D12 = Dado de doze lados.\n D20 = Dado de vinte lados.\n -d100 = Dado de cem lados.", color=0x00CC00)
            embed.add_field(name="English version:", value="-help", inline=False)
            await message.channel.send(embed=embed)

#starting the bot:
client = MyCLient()
client.run('Your code here.')