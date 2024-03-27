![image](https://github.com/MonforteGG/soe-bot/assets/148546500/a3b99af9-7aa3-41a6-a5b0-32d9c3c517e7)


Este es un bot para Discord diseñado para proporcionar diversas funcionalidades relacionadas con el juego Tibia.
En este caso está configurado para funcionar en el servidor Mortalis de soerpg.com

## Descripción

El bot está programado en Python utilizando la biblioteca **discord.py** para interactuar con la API de Discord utlizando operaciones asíncronas. Proporciona funciones como **añadir un nombre a la lista** y haciendo uso de la biblioteca **Beatufil Soup** podemos hacer **Web Scrapping** para verificar **las subidas de niveles de los personajes**, **las muertes de los personajes** o **consultar quien está online**. También es posible **consultar la ubicación actual de Rashid** o gracias a la biblioteca **OpenCV** con la que podemos procesar las imagenes adjuntas y **clasificar el loot por lugares de venta** entre otras cosas.

## Instalación

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias utilizando el comando `pip install -r requirements.txt`.
3. Asegúrate de tener un archivo `.env` con las variables de entorno necesarias, incluyendo el token del bot de Discord.
4. Ejecuta el bot utilizando el comando `python bot.py`.

## Uso

Una vez que el bot esté en funcionamiento y añadido a tu servidor de Discord, puedes utilizar los comandos disponibles para obtener información sobre los personajes, muertes recientes, ubicación de Rashid y más. Asegúrate de asignar los permisos necesarios al bot para que pueda acceder a los canales y ejecutar comandos.

Comandos:

`!addname`: Al usar este comando seguido un nombre, se añadira a la lista de personajes a los que se hara tracking de las muertes, de las súbidas de nivel, y se podra comprobar si está online. Ej: `!addname Monforte`.

![image](https://github.com/MonforteGG/soe-bot/assets/148546500/b0007c5a-28b8-4bab-bd78-7440eb30d90f)

`!loot`: Si usamos este comando y adjuntamos una imagen, el bot nos clasificara por colores el loot (Azul -> Blue Djinn, Verde -> Green Djinn, Amarillo -> Rashid).

![image](https://github.com/MonforteGG/soe-bot/assets/148546500/f9c0ed8a-77be-4fe5-ac60-8c7e33eb4b4c)

`!online`: Este comando nos mostrara los personajes de nuestra lista que están online.

![image](https://github.com/MonforteGG/soe-bot/assets/148546500/393c7ea8-2f36-4587-afe7-f70597a011d8)

`!rashid`: Con este comando podremos ver la ubicación del NPC Rashid el día de hoy (Hora del Server Save: 10 am).

![image](https://github.com/MonforteGG/soe-bot/assets/148546500/ba19a96d-b1b2-4cf9-9c69-327e597f962c)


Funciones pasivas:

`dead_list()`: Tracking de las muertes de los personajes de nuestra lista.

![image](https://github.com/MonforteGG/soe-bot/assets/148546500/a512e47d-74ee-47b6-b984-ecb89af98255)

`lvl_check()`: Tracking de las subidas de nivel de los personajes de nuestra lista.

![image](https://github.com/MonforteGG/soe-bot/assets/148546500/f58394be-780f-433f-9dd2-f0ca508fbb97)





## Créditos

Este proyecto fue creado por **@MonforteGG**.


