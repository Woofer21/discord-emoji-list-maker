import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import requests
import time

load_dotenv()

client = discord.Client()
client = commands.Bot(command_prefix="$")
TOKEN = os.getenv("TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
WEBHOOK_NAME = ""
WEBHOOK_AVATAR = ""

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.command(name="grab-emotes")
async def grabEmote(ctx, channel, *args):
    channel = channel

    try:
        if channel == "-w":
            channel = "webhook"
        else:
            channel = channel.replace("<#", "")
            channel = channel.replace(">", "")
            a = ctx.guild.get_channel(int(channel))
            channel = a
    except ValueError as err:
        em = discord.Embed(title="Invalid Argument", color=discord.Colour.from_rgb(241, 79, 64), description="Invalid argument in position 1. Please provide a valid argument.\n```\n\"-w\" uses configured webook\n\"channel mention\" uses mentioned channel\n\nEX: $grab-emotes #emotes -g\nEX2: $grab-emotes -w -l```")
        await ctx.channel.send(embed=em)
        print(err)
        return

    try:
        if args[0] == "-g":    
            await get_all(ctx, channel)
        elif args[0] == "-l":
            await get_guild(ctx, channel)
    except IndexError as err:
        em = discord.Embed(title="Invalid Argument", color=discord.Colour.from_rgb(241, 79, 64), description="Invalid argument in position 2. Please provide a valid argument.\n```\n\"-g\" searches global\n\"-l\" searches only this server\n\nEX: $grab-emotes #emotes -g\nEX2: $grab-emotes -w -l```")
        await ctx.channel.send(embed=em)
        print(err)


async def get_all(message, channel):
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

    if channel == "webhook":
        for indx, b in enumerate(string):
            print(b)
            data = {
                "username": WEBHOOK_NAME,
                "avatar_url": WEBHOOK_AVATAR,
                "content": string[indx]
            }


            res = requests.post(WEBHOOK_URL, json=data)
            time.sleep(1)

            try:
                res.raise_for_status()
            except requests.exceptions.HTTPError as err:
                print(err)
            else:
                print(f"[WEB HOOK] Successfully sent, Code {res.status_code}")
    else:
        for indx, b in enumerate(string):
            await channel.send(string[indx])
            time.sleep(1)

    await m.edit(content="Done!")

async def get_guild(message, channel):
    m = await message.channel.send('grabing. . .')

    print(message.guild.emojis)
    print("-------------")

    string = [""]
    num = 0

    for a in message.guild.emojis:
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

    if channel == "webhook":
        for indx, b in enumerate(string):
            print(b)
            data = {
                "username": WEBHOOK_NAME,
                "avatar_url": WEBHOOK_AVATAR,
                "content": string[indx]
            }


            res = requests.post(WEBHOOK_URL, json=data)
            time.sleep(1)

            try:
                res.raise_for_status()
            except requests.exceptions.HTTPError as err:
                print(err)
            else:
                print(f"[WEB HOOK] Successfully sent, Code {res.status_code}")
    else:
        for indx, b in enumerate(string):
            await channel.send(string[indx])
            time.sleep(1)


    await m.edit(content="Done!")

        
def checks(num, arr, new_string):
    if len(arr[num]+new_string) < 2000:
        return True
    else:
        return False

if __name__ == "__main__":
    client.run(TOKEN)
