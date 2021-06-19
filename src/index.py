import os
import discord 
from discord.ext import commands
import datetime
import aiohttp
import random 

bot = commands.Bot(command_prefix='!',description='Suchibot')
# TOKEN = os.getenv('DISCORD_TOKEN')
# print(TOKEN+"___________________")

saludo = [
      "Que mrda quieres?",
      "Hola :D",
      "Creo que ya te saludé >:v",
      "Hoy es un buen día para matar zurdos :D",
      "No me molestes >:v",
      "Holaaaaaaaaaaa",
      ".l."
]
@bot.command()
async def ping(ctx):
   await ctx.send('PONG')
@bot.command()
async def hi(ctx):
   await ctx.send(random.choice(saludo))
@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}",url="https://st2.depositphotos.com/1298561/9120/v/450/depositphotos_91206962-stock-illustration-greek-deity-theme-elements-icon.jpg",
     description="Hola soy nuevo y estoy aprendiendo. Por favor tenme paciencia :c", timestamp=datetime.datetime.utcnow())
    await ctx.send(embed=embed)
@bot.command(name='helpme')
async def helpme(ctx):
    embed = discord.Embed(title="Estoy preparando mi lista de comandos :D",url="https://docs.google.com/document/d/1otOuj1nlSl-DZ_v7C20gq23FcVZumKv9vkWeJVgduUs/edit?usp=sharing", 
    description="tu me haces ping y yo te hago pong >:v")
    embed.add_field(name="!ping",value="PONG", inline=False)
    embed.add_field(name="!hi",value="Holaaaaa", inline=False)
    embed.add_field(name="!sleep",value="Conoce los secretos del método Suchilás para dormir fast fast", inline=False)
    embed.add_field(name="!qcho",value="Qchao!", inline=False)
    embed.add_field(name="!dog",value="Quieres ver un perrito?", inline=False)
    await ctx.send(embed=embed)
# General commands
@bot.command()
async def sleep(ctx):
    embed = discord.Embed(title="Método Suchilás para dormir fast fast", 
    description="Sigue estos pasos para adroctinarte en el arte del sueño", color= 0x34ebeb)
    embed.add_field(name="1. Elige una hora para despertar",value="Esta será la hora promedio en la que te despertarás", inline=False)
    embed.add_field(name="2. Pon tu alarma a esa hora",value="Sin importar cuanto hayas dormido despiertate y pasa inmediatamente al paso 3", inline=False)
    embed.add_field(name="3. Voltea tu colchón",value="Pon tu colchon contra la pared de manera que no puedas acostarte inconscientemente", inline=False)
    embed.add_field(name="4. Mantente ocupado",value="Será mejor tengas cosas planeadas para este momento, será un día de sufrimiento", inline=False)
    embed.add_field(name="5. No toques tu cama!",value="No toques tu cama por nada ni mucho menos te duermas hasta tu hora de dormir", inline=False)
    embed.add_field(name="6. Nada de luz!",value="Sella todos los posibles accesos de luz de tu habitación, todos los que puedas!", inline=False)
    embed.add_field(name="7. Cero interrupciones",value="Deja el celular lejos de tu alcance y con los datos y conexión wifi apagados", inline=False)
    embed.set_footer(text="pdt: si planeas tu día antes de irte a dormir dormirás mejor")
    await ctx.send(embed=embed)
@bot.command()
async def qchao(ctx):
    embed = discord.Embed(title="Qchao!", color=discord.Color.red()) #creates embed
    file = discord.File(".\src\\assets\img\kuchao.png", filename="image.png")
    embed.set_image(url="attachment://image.png")
    await ctx.send(file=file, embed=embed)

@bot.command()
async def dog(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/dog') # Make a request
      dogjson = await request.json() # Convert it to a JSON dictionary
   embed = discord.Embed(title="Doggo!", color=discord.Color.purple()) # Create embed
   embed.set_image(url=dogjson['link']) # Set the embed image to the value of the 'link' key
   await ctx.send(embed=embed) # Send the embed
# Events
@bot.event
async def on_ready():
    # await  bot.change_presence(activity=discord.Streaming(name="Coding", url="http://www.twitch.tv"), status="!helpme")
    await  bot.change_presence(activity = discord.Activity(type=discord.ActivityType.listening, name="!helpme"))
    print('Bot ready')
bot.run('ODUzNzc0MDE4OTAxMTgwNDM2.YMaRBA.VAl6CcLUZBVohsiv6LsxDTuqZ4s')