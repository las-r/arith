import discord
from discord.ext import commands
from dotenv import load_dotenv as env
import os
import requests
from urllib.parse import quote_plus as parse

# load env
env()

# bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# ready
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"ready as {bot.user.name}")

# ask command
@bot.hybrid_command(name="ask", description="Ask Arith a question.")
async def ask(ctx, *, query: str):
    res = requests.get(f"https://api.wolframalpha.com/v1/result?appid={os.getenv("WOLFRAMID")}&i={parse(query)}")
    
    if res.status_code == 200:
        await ctx.reply(res.text)
    else:
        await ctx.reply("No answer found")
        
# run bot
bot.run(os.getenv("BOTTOKEN"))
