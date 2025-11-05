#!/usr/bin/env python3
"""
Simple Discord Bot
A basic Discord bot using discord.py
"""

import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get bot token from environment
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

if not DISCORD_BOT_TOKEN:
    print("Error: DISCORD_BOT_TOKEN not found in environment variables")
    print("Create a .env file with: DISCORD_BOT_TOKEN=your_bot_token_here")
    exit(1)

# Set up bot with command prefix
intents = discord.Intents.default()
intents.message_content = True  # Required for reading message content
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    """Called when bot is ready and connected to Discord."""
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is in {len(bot.guilds)} server(s)')
    for guild in bot.guilds:
        print(f'  - {guild.name} (id: {guild.id})')


@bot.event
async def on_message(message):
    """Called when a message is sent."""
    # Ignore messages from bots
    if message.author == bot.user:
        return
    
    # Log message
    print(f'Message from {message.author}: {message.content}')
    
    # Process commands
    await bot.process_commands(message)


@bot.command(name='hello')
async def hello(ctx):
    """Respond to !hello command."""
    await ctx.send(f'Hello, {ctx.author.mention}!')


@bot.command(name='ping')
async def ping(ctx):
    """Respond to !ping command with latency."""
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! Latency: {latency}ms')


@bot.command(name='info')
async def info(ctx):
    """Display bot information."""
    embed = discord.Embed(
        title="Bot Information",
        description="A simple Discord bot example",
        color=discord.Color.blue()
    )
    embed.add_field(name="Server", value=ctx.guild.name, inline=True)
    embed.add_field(name="Latency", value=f"{round(bot.latency * 1000)}ms", inline=True)
    await ctx.send(embed=embed)


@bot.event
async def on_command_error(ctx, error):
    """Handle command errors."""
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Use !help to see available commands.")
    else:
        print(f"Error: {error}")
        await ctx.send(f"An error occurred: {error}")


if __name__ == "__main__":
    try:
        bot.run(DISCORD_BOT_TOKEN)
    except discord.LoginFailure:
        print("Error: Invalid bot token. Please check your .env file.")
    except Exception as e:
        print(f"Error starting bot: {e}")

