import os
from urllib.parse import quote_plus
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient

# Username and passwords can be stored in an dynamic env file as secrets and can be accessed using settings.
url = os.getenv("DATABASE_URL", "")
username = os.getenv("DATABASE_USERNAME", "")
password = os.getenv("DATABASE_PASSWORD", "")
db_name = os.getenv("DATABASE_NAME", "")
uri = f"mongodb://{username}:{password}@{quote_plus(url)}/{db_name}"
client = MongoClient(uri, tlsInsecure=True)
db = client[db_name]
