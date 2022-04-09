from typing import Optional

from fastapi import FastAPI, status
from starlette.responses import Response
from core import GetTrucks
from persistence import TrucksRepository

from model import TrucksRequest

app = FastAPI()
repository = TrucksRepository()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/trucks/" )
def get_trucks(current_longitude: float = 37.5, current_latitude: float = 122.5, required_count: int = 5):
    dto: TrucksRequest = {
        "longitude": current_longitude,
        "latitude": current_latitude,
        "count": required_count
    }
    resp = GetTrucks(repository).execute(dto)
    return resp

@app.post(
    "",
    status_code=status.HTTP_201_CREATED,
)
async def fetch_trucks(dto: TrucksRequest):
    return {"Hello": "World"}
    # resp = GetTrucks(repository).execute(dto)
    # return resp