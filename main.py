# FIXED CODE!
# https://github.com/Azizishot/Lookup-BOT/
# t.me/azizisblack for support
import discord
from discord.ext import commands
import os

TOKEN = '' 
txt = 'data.txt'
blacklist = ['nigg']

intents = discord.Intents.default()
intents.message_content = True  
az = commands.Bot(command_prefix='>', intents=intents)

async def countt():
    count = 0
    if os.path.exists(txt):
        with open(txt, 'r') as file:
            for line in file:
                count += 1
    return count

async def lookup(query):
    found = []
    if os.path.exists(txt):
        with open(txt, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if query in line and not any(nig in line for nig in blacklist):
                    found.append(line.strip())
    return found

@az.event
async def on_ready():
    await az.change_presence(activity=discord.Streaming(name="github.com/azizishot", url="http://twitch.tv/kaicenat"))
    print(f'Lookup > {az.user}')

@az.command(name='search')
async def search(ctx, *, query: str):
    if any(nig in query for nig in blacklist):
        await ctx.send("blacklisted word.")
        return
    results = await lookup(query)
    if results:
        for result in results:
            embed = discord.Embed(title="Result", description=f"```{result}```")
            embed.set_footer(text="github.com/azizishot > " + str(ctx.author))
            embed.set_thumbnail(url="https://sukuna.bio/media/logo2.png")
            await ctx.send(embed=embed)
    else:
        await ctx.send(":sob:")

@az.command(name='lines')
async def count(ctx):
    lines = await countt()
    embed = discord.Embed(title="Lines Count", description=f"```{lines}```")
    embed.set_footer(text="By github.com/azizishot")
    embed.set_thumbnail(url="https://sukuna.bio/media/logo2.png")
    await ctx.send(embed=embed)

az.run(TOKEN)
