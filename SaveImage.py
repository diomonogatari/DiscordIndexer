from discord.ext import commands
from dotenv import load_dotenv
import os
import uuid
import Utils

#load the env that has the confidential tokens/keys
load_dotenv()
storingPath = "storage"


client = commands.Bot(command_prefix='.')

# something my bot will be listening to
@client.event
async def on_ready():
    print("I'm now online!")


# I'm defining a command that will be named "save" that the bot recognizes 
@client.command()
async def save(context):
    try:
        extension = Utils.getMediaType(context.message.attachments[0].content_type)
        filename = str(uuid.uuid4()) + extension
    except ValueError as e:
        context.message.channel.send(e)

    completeName = os.path.join(storingPath, filename)
    await context.message.attachments[0].save(completeName)

client.run(os.environ.get('secretToken'))