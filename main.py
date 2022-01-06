from discord.ext import commands
from dotenv import load_dotenv
from pymongo import MongoClient
import os
import uuid
import Utils

#load the .env that has the confidential tokens/keys
load_dotenv()
storingPath = "storage"

#connect to the MongoDb on the given Cluster and Collection
cluster = MongoClient(os.environ.get('dbConnectionUrl'))
db = cluster["MediaIndexer"]
collection = db["Media"]

#discord client/bot that will listen to the '.' prefix for commands
client = commands.Bot(command_prefix='.')

#When the bot is ready it prints:
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
    post = {
        "_id":str(uuid.uuid4()),
        "creator_id":"123",
        "creator_name":"diogo",
        "searchable_filename":"tetas",
        "filename":"gandasTetas",
        "file_extension":extension,
        "discord_url":"",
        "discord_proxy_url":"",
        "local_filepath":"c:/cona"
    }
    collection.insert_one(post)
    await context.message.attachments[0].save(completeName)



#start the bot
client.run(os.environ.get('secretToken'))