from settings import settings
import discord
import random
from bot_logic import *

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('$delete'):
        await message.channel.send('Adios mundo cruel :c...', delete_after=1.5)
    elif message.content.startswith('$bichota'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$hello'):
        await message.channel.send("Hola¡¡")
    elif message.content.startswith('$bye'):
        await message.channel.send("Bye bye")
    elif message.content.startswith('$pass'):
        length = random.randint(8,15)
        await message.channel.send(gen_pass(length))    
    elif message.content.startswith("$coin"):
        await message.channel.send(flip_coin())
    else:
        await message.channel.send(message.content)

client.run(settings["TOKEN"])
