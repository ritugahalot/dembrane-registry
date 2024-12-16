from urllib.parse import quote_plus
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient

# Username and passwords can be stored in an env file as secrets and can be accessed using settings.
uri = "mongodb://trh:hemligt@localhost:27017/registry"
client = MongoClient(uri, tlsInsecure=True)
db = client["registry"]
