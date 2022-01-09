from discord.ext import commands
import discord
from dotenv import load_dotenv
from pymongo import MongoClient
import os
import uuid
import Utils


class MediaIndexerBot(discord.Client,MongoClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)