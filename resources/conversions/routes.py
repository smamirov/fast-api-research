from fastapi import APIRouter
from resources.conversions.conversion import Conversion

router = APIRouter()
conversion_instance = Conversion()

@router.get("/")
def list_recordings():
    """Returns list of conversions
    """
    return conversion_instance.get_conversions()