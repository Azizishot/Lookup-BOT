import discord
from discord.ext import commands
import os

TOKEN = 'token'
txt = 'data.txt'
blacklist = ['steam', 'ip', 'identifier', 'discord', '....', '....', '....'] 

intents = discord.Intents.default()
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
        await ctx.send("You cannot search for that word.")
        return
    results = await lookup(query)
    if results:
        chunks = [results[i:i+25] for i in range(0, len(results), 25)]  
        for chunk in chunks:
            embed = discord.Embed(title="Results")
            for result in chunk:
                embed.add_field(name="", value=f"```{result}```", inline=False)
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
