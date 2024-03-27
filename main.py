import asyncio
import datetime
import json
import os
import re
from dotenv import load_dotenv
import cv2
import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands

import image_recognition

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Crear un set con los nombres de los personajes de chars.txt para utilizarlo posteriormente
with open('chars.txt', 'r') as file:
    nombres_concatenados = file.readline().strip()

chars = set(nombres_concatenados.split(','))
web_chars = [char.replace(' ', '+') for char in chars]  # Lista sin espacios para buscar correctamente en la web el nombre

registro_muertes = []
levels_check = {}
levels = {}
updated_levels = {}

# Evento que se ejecuta cuando el bot está listo
@bot.event
async def on_ready():
    print("Bot is online!")
    await asyncio.gather(dead_list(), lvl_check())

# Función para verificar los niveles de los personajes
async def lvl_check():
    # Verifica los niveles inicialmente

    for name in web_chars:
        url = f'https://mortalis.soerpg.com/characterprofile.php?name={name}'
        response = requests.get(url)
        html = response.text
        soup2 = BeautifulSoup(html, 'html.parser')
        cp_header_desc = soup2.find('div', id='cp_header_desc')
        if cp_header_desc:
            tibiafont = cp_header_desc.text.strip()
            level_number = re.search(r'\d+', tibiafont)
            if level_number:
                levels[name] = level_number.group()

    # Verifica los niveles constantemente

    while True:
        for name in web_chars:
            url = f'https://mortalis.soerpg.com/characterprofile.php?name={name}'
            response = requests.get(url)
            html = response.text
            soup2 = BeautifulSoup(html, 'html.parser')
            cp_header_desc = soup2.find('div', id='cp_header_desc')
            if cp_header_desc:
                tibiafont = cp_header_desc.text.strip()
                level_number = re.search(r'\d+', tibiafont)
                if level_number:
                    updated_levels[name] = level_number.group()

                    # Verifica si el nivel ha aumentado
                    if int(updated_levels[name]) > int(levels[name]):
                        channel = bot.get_channel(int(os.getenv('AVISOS')))
                        original_name = name.replace('+', ' ')
                        await channel.send(
                            f'{original_name} has leveled up from level {levels[name]} to level {updated_levels[name]}! :chart_with_upwards_trend: ')
                        levels[name] = updated_levels[name]
                        # Si ha muerto y ha bajado de nivel actualiza el nivel para poder notificar si vuelve a subir al nivel que tenia antes
                    elif int(updated_levels[name]) < int(levels[name]):
                        levels[name] = updated_levels[name]
            await asyncio.sleep(10)

# Función para verificar las muertes en el juego
async def dead_list():
    while True:
        website = "https://mortalis.soerpg.com/deaths.php"
        resultado = requests.get(website)
        content = resultado.text

        # Patrones de expresiones regulares para extraer información de las muertes
        patron_nombre = r'<tr>\s*<td><a href="characterprofile\.php\?name=[\w\s\'".,-]+?".*?>(.*?)</a>'
        patron_nivel = r'killed at level \d+'
        patron_fecha = r'(\d{2}\s\w+\s\d{4})\s\((\d{2}:\d{2})\)'
        patron_asesino = r'<td>(?:<a href="characterprofile\.php\?name=[\w\s]+">([\w\s]+)</a>|([\w\s]+))</td>'

        muertes = re.findall(patron_nombre, content)
        niveles = re.findall(patron_nivel, content)
        fechas = re.findall(patron_fecha, content)
        asesinos = re.findall(patron_asesino, content)
        asesinos_filtrado = []
        for (x, y) in asesinos:
            if x == '':
                asesinos_filtrado.append('a ' + y)
            elif y == '':
                asesinos_filtrado.append(x)

        muertes_con_fechas = list(zip(muertes, niveles, asesinos_filtrado, fechas))

        for (nombre, nivel, asesino, fecha) in muertes_con_fechas:
            if nombre in chars and (nombre, fecha) not in registro_muertes:
                channel = bot.get_channel(int(os.getenv('AVISOS')))
                await channel.send(f'{nombre} {nivel} by {asesino} at {fecha} :skull: ')
                registro_muertes.append((nombre, fecha))

        await asyncio.sleep(60)

# Comnando para saber en que rango de niveles puedes sharear experiencia
@bot.command()
async def share(ctx,level: int):
    min_level = int(level * (2 / 3))
    max_level = int(level * (3 / 2))
    await ctx.send(f'You can share exp with levels in range of: ({min_level}-{max_level})')

# Comando para añadir nombres a la lista de personajes
@bot.command()
async def addname(ctx, *, new_name):  # El argumento new_name captura todo el contenido del mensaje
    with open('chars.txt', 'a') as file:
        file.write(',' + new_name)

    await ctx.send(f'"{new_name}" have been added to the list.')  # Envía un mensaje de confirmación al canal
    print(f'Se ha añadido el nombre "{new_name}" al archivo.')  # Imprime un mensaje en la consola del bot

    # Actualizamos el set global con los nombres de los personajes de chars.txt para utilizarlo posteriormente
    with open('chars.txt', 'r') as file:
        nombres_concatenados = file.readline().strip()

    global chars
    chars = set(nombres_concatenados.split(','))

    global web_chars
    web_chars = [char.replace(' ', '+') for char in
                 chars]  # Lista sin espacios para buscar correctamente en la web el nombre

    # Busca el nivel del nuevo personaje y lo añade al diccionario global 'levels'
    name_replace = new_name.replace(' ', '+')
    url = f'https://mortalis.soerpg.com/characterprofile.php?name={name_replace}'
    response = requests.get(url)
    html = response.text
    soup2 = BeautifulSoup(html, 'html.parser')

    cp_header_desc = soup2.find('div', id='cp_header_desc')
    if cp_header_desc:
        tibiafont = cp_header_desc.text.strip()
        level_number = re.search(r'\d+', tibiafont)
        if level_number:
            level = level_number.group()
            levels[name_replace] = level


# Comando para obtener la ubicación de Rashid (Cambia la ubicación después del Server Save a las 10 am)
@bot.command()
async def rashid(ctx):
    date = datetime.datetime.now().weekday()
    hour = datetime.datetime.now().time()
    hour_ss = datetime.time(10, 5, 0)
    if hour < hour_ss:
        date -= 1

    match date:
        case 0:
            await ctx.send("Svargrond, Dankwart's tavern - south of the temple")
        case 1:
            await ctx.send("Liberty Bay, Lyonel's tavern - west of the depot")
        case 2:
            await ctx.send("Port Hope, Clyde's tavern - west of the depot")
        case 3:
            await ctx.send("Ankrahmun, Arito's tavern - above the post office (+1)")
        case 4:
            await ctx.send("Darashia, Miraia's tavern - south of the guildhalls")
        case 5:
            await ctx.send("Edron, Mirabell's tavern - above the depot (+1)")
        case 6:
            await ctx.send("Carlin, above the depot (+1)")

# Comando para analizar un mensaje adjunto y detectar elementos en una imagen
@bot.command()
async def loot(ctx):
    if len(ctx.message.attachments) > 0:
        attachment = ctx.message.attachments[0]

        if (
                attachment.filename.endswith(".jpg")
                or attachment.filename.endswith(".jpeg")
                or attachment.filename.endswith(".png")
        ):
            img_data = requests.get(attachment.url).content
            with open("bp.png", "wb") as handler:
                handler.write(img_data)
                bp = cv2.imread('bp.png', cv2.IMREAD_UNCHANGED)

    image_recognition.detect_items(bp, image_recognition.blue_item_images, image_recognition.green_item_images,
                                   image_recognition.rashid_item_images)

    channel = bot.get_channel(int(os.getenv('COMANDOS')))
    await channel.send(file=discord.File('result.jpg'))

# Comando para verificar qué personajes están en línea
@bot.command()
async def online(ctx):
    url = "https://mortalis.soerpg.com/sub.php?page=onlinelist"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    json_script = soup.find('script', type="json")
    json_data = json.loads(json_script.string)

    for name, value in json_data.items():
        if name in chars:
            match value['vocation']:
                case 'Elite Knight':
                    vocation = 'EK :crossed_swords: '
                case 'Royal Paladin':
                    vocation = 'RP :bow_and_arrow: '
                case 'Master Sorcerer':
                    vocation = 'MS :man_mage: '
                case 'Elder Druid':
                    vocation = 'ED :snowflake: '

            await ctx.send(f"{name} | {vocation} level {value['level']}")
            levels_check[name] = value['level']


# Ejecuta el bot con el token obtenido de las variables de entorno
bot.run(os.getenv('TOKEN'))
