# bot.py
import random #Para poder seleccionar un random de nuestra lista
from discord.ext import commands # Importamos commands de la libreria
TOKEN = "ODY0OTk4MjU1OTU5ODY3NDAw.YO9mZw.RBPHaZjRp_A6WaH_0BuZFk4oVWk" #El token secreto de nuestro BOT
bot = commands.Bot(command_prefix='b!') # Le Decimos con que prefijo el bot #va a empezar escuchar para saber cual es el comando
@bot.command(name='meme') #Nombre del comando
async def randomMeme(ctx): #Funcion del comando
    lista = [
        'https://media.discordapp.net/attachments/860703960604475423/865041096890384414/Cuando_te_dicen_que_le_sabes_demasiado_.mp4'
    ] #La lista con los gifs
    response = random.choice(lista) #Seleccionamos un random de la # lista
    await ctx.send(response) #Enviamos la respuesta