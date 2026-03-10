# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=["!", "melonn", "mel", "."], intents=intents)

@bot.event
async def on_ready():
	print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
	await ctx.send("Pong!")

@bot.command()
async def statement(ctx):
	await ctx.send("Your god is me. NOW GET ON YOUR KNEES AND WORSHIP ME!!!")

# Run using token from environment variable
load_dotenv()
bot.run(os.getenv("TOKEN"))