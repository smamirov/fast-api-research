from fastapi import APIRouter
from resources.recordings.recording import Recording

router = APIRouter()
recordings_instance = Recording()

@router.get("/")
def list_recordings():
    """Returns list of recordings
    """
    return recordings_instance.get_recordings()
