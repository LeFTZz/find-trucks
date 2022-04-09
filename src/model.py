from pydantic import BaseModel

class TrucksRequest(BaseModel):
    longitude: float
    latitude: float
    count: int