```
▄▄▄▄▄▪  ▄▄▄▄· ▪   ▄▄▄·     ·▄▄▄▄  ▪  .▄▄ ·  ▄▄·       ▄▄▄  ·▄▄▄▄      ▄▄▄▄·       ▄▄▄▄▄
•██  ██ ▐█ ▀█▪██ ▐█ ▀█     ██▪ ██ ██ ▐█ ▀. ▐█ ▌▪▪     ▀▄ █·██▪ ██     ▐█ ▀█▪▪     •██  
 ▐█.▪▐█·▐█▀▀█▄▐█·▄█▀▀█     ▐█· ▐█▌▐█·▄▀▀▀█▄██ ▄▄ ▄█▀▄ ▐▀▀▄ ▐█· ▐█▌    ▐█▀▀█▄ ▄█▀▄  ▐█.▪
 ▐█▌·▐█▌██▄▪▐█▐█▌▐█ ▪▐▌    ██. ██ ▐█▌▐█▄▪▐█▐███▌▐█▌.▐▌▐█•█▌██. ██     ██▄▪▐█▐█▌.▐▌ ▐█▌·
 ▀▀▀ ▀▀▀·▀▀▀▀ ▀▀▀ ▀  ▀     ▀▀▀▀▀• ▀▀▀ ▀▀▀▀ ·▀▀▀  ▀█▄▀▪.▀  ▀▀▀▀▀▀•     ·▀▀▀▀  ▀█▄▀▪ ▀▀▀ 
```


This is a Discord bot designed to provide various functionalities related to the Tibia game. In this case, it is configured to work on the Mortalis server of soerpg.com.

## Description

The bot is programmed in Python using the **discord.py** library to interact with the Discord API using asynchronous operations. It provides functions such as **adding a name to the list**, and by using the **Beautiful Soup** library, we can perform **Web Scraping** to check **character level ups**, **character deaths**, or **check who is online**. It is also possible to **check the current location of NPC Rashid** or, thanks to the **OpenCV** library, process attached images and **classify loot by selling places** among other things.

## Installation

1. Clone this repository to your local machine.
2. Install the necessary dependencies using the command `pip install -r requirements.txt`.
3. Ensure you have a `.env` file with the necessary environment variables, including the Discord bot token and the IDs of the Announcement and Command channels.
4. Run the bot using the command `python bot.py`.

## Usage

Once the bot is up and running and added to your Discord server, you can use the available commands to get information about characters, recent deaths, Rashid's location, and more. Make sure to assign the necessary permissions to the bot so it can access channels and execute commands.

Commands:

`!addname`: Using this command followed by a name will add it to the list of characters for which tracking of deaths, level ups, and online status will be done. Example: `!addname Monforte`.

![image](https://github.com/MonforteGG/soe-bot/assets/148546500/b0007c5a-28b8-4bab-bd78-7440eb30d90f)

`!loot`: If we use this command and attach an image, the bot will classify the loot by colors (Blue -> Blue Djinn, Green -> Green Djinn, Yellow -> Rashid).

![image](https://github.com/MonforteGG/soe-bot/assets/148546500/f9c0ed8a-77be-4fe5-ac60-8c7e33eb4b4c)

`!online`: This command will show us the characters from our list that are online.

![image](https://github.com/MonforteGG/soe-bot/assets/148546500/393c7ea8-2f36-4587-afe7-f70597a011d8)

`!rashid`: With this command, we can see the location of NPC Rashid today (Server Save Time: 10 am).

![image](https://github.com/MonforteGG/soe-bot/assets/148546500/ba19a96d-b1b2-4cf9-9c69-327e597f962c)

Passive Functions:

`dead_list()`: Tracking of character deaths from our list.

![image](https://github.com/MonforteGG/soe-bot/assets/148546500/a512e47d-74ee-47b6-b984-ecb89af98255)

`lvl_check()`: Tracking of character level ups from our list.

![image](https://github.com/MonforteGG/soe-bot/assets/148546500/f58394be-780f-433f-9dd2-f0ca508fbb97)



