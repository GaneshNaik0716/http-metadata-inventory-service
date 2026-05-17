import asyncio

from app.database import metadata_collection
from app.services.fetcher import fetch_metadata
from app.schemas import metadata_serializer


async def create_metadata(url: str):

    existing = await metadata_collection.find_one({"url": url})

    if existing:
        return metadata_serializer(existing)

    metadata = await fetch_metadata(url)

    await metadata_collection.insert_one(metadata)

    return metadata


async def get_metadata(url: str):

    existing = await metadata_collection.find_one({"url": url})

    if existing:
        return metadata_serializer(existing)

    asyncio.create_task(background_inventory_update(url))

    return None


async def background_inventory_update(url: str):

    try:
        existing = await metadata_collection.find_one({"url": url})

        if existing:
            return

        metadata = await fetch_metadata(url)

        await metadata_collection.insert_one(metadata)

    except Exception as error:
        print(f"Background task failed: {error}")