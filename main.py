from fastapi import FastAPI
from resources.recordings.routes import router as recordings_router
from resources.conversions.routes import router as coversions_router

app = FastAPI()


app.include_router(recordings_router, prefix="/recordings")
app.include_router(coversions_router, prefix="/conversions")

