from discord.ext import commands
import uuid
import requests
import shutil


client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print("Bot is ready")

# I'm defining a command that will be named "save" that the bot recognizes 
@client.command()
async def save(context):
    imageName = str(uuid.uuid4()) + '.jpg'
    await context.message.attachments[0].save(imageName)

client.run('TOKEN')