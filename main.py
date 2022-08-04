import discord
import discord.ext.commands
from dotenv import load_dotenv
import os
import requests
import time

load_dotenv()

client = discord.Client()
TOKEN = os.getenv("TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
WEBHOOK_NAME = ""
WEBHOOK_AVATAR = ""

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$grab-emotes'):
        m = await message.channel.send('grabing. . .')
        
        print(client.emojis)
        print("-------------")

        string = [""]
        num = 0

        for a in client.emojis:
            if a.animated:
                if checks(num, string, f"<a:{a.name}:{a.id}> -> `<a:{a.name}:{a.id}>`\n"):
                    string[num]+=f"<a:{a.name}:{a.id}> -> `<a:{a.name}:{a.id}>`\n"
                    print(f"<a:{a.name}:{a.id}> -> `<a:{a.name}:{a.id}>`\n")
                else:
                    num+=1
                    string.append("")
                    string[num]+=f"<a:{a.name}:{a.id}> -> `<a:{a.name}:{a.id}>`\n"
                    print(f"<a:{a.name}:{a.id}> -> `<a:{a.name}:{a.id}>`\n") 
            else:
                if checks(num, string, f"<:{a.name}:{a.id}> -> `<:{a.name}:{a.id}>`\n"):
                    string[num]+=f"<:{a.name}:{a.id}> -> `<:{a.name}:{a.id}>`\n"
                    print(f"<:{a.name}:{a.id}> -> `<:{a.name}:{a.id}>`\n")
                else:
                    num+=1
                    string.append("")
                    string[num]+=f"<:{a.name}:{a.id}> -> `<:{a.name}:{a.id}>`\n"
                    print(f"<:{a.name}:{a.id}> -> `<:{a.name}:{a.id}>`\n")


        print("-------------")
        print(string)
        print("-------------")


        for indx, b in enumerate(string):
            print(b)
            data = {
                "username": WEBHOOK_NAME,
                "avatar_url": WEBHOOK_AVATAR,
                "content": string[indx]
            }


            res = requests.post(WEBHOOK_URL, json=data)
            time.sleep(5)

        try:
            res.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print(f"[WEB HOOK] Successfully sent, Code {res.status_code}")

        await m.edit(content="Done!")

        
def checks(num, arr, new_string):
    if len(arr[num]+new_string) < 2000:
        return True
    else:
        return False

client.run(TOKEN)
