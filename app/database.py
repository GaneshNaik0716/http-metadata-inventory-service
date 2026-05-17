from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings

client = AsyncIOMotorClient(settings.mongo_url)

database = client[settings.database_name]

metadata_collection = database[settings.collection_name]