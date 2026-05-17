from fastapi import FastAPI

from app.routes.metadata import router
from app.database import metadata_collection

app = FastAPI(
    title="HTTP Metadata Inventory Service",
    version="1.0.0"
)


@app.on_event("startup")
async def startup_db_indexes():
    await metadata_collection.create_index("url", unique=True)


@app.get("/")
async def health_check():
    return {
        "status": "healthy"
    }


app.include_router(router)