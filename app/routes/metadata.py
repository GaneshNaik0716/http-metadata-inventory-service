from fastapi import APIRouter, HTTPException

from app.models import URLRequest
from app.services.metadata_service import (
    create_metadata,
    get_metadata
)

router = APIRouter()


@router.post("/metadata")
async def create_metadata_endpoint(request: URLRequest):

    try:
        result = await create_metadata(str(request.url))

        return {
            "message": "Metadata stored successfully",
            "data": result
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


@router.get("/metadata")
async def get_metadata_endpoint(url: str):

    try:
        result = await get_metadata(url)

        if result:
            return {
                "message": "Metadata found",
                "data": result
            }

        return {
            "status": 202,
            "message": "Metadata collection started in background"
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )