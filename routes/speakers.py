from fastapi import APIRouter
from data.store import speakers
from schemas.speaker import Speaker

router = APIRouter(prefix="/speakers", tags=["Speakers"])

@router.get("/", response_model=list[Speaker])
def list_speakers():
    return list(speakers.values())
