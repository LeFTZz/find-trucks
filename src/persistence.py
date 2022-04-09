from model import TrucksRequest
from trucks import Trucks

class TrucksRepository:
    def __init__(self):
        self.trucks = Trucks()

    def get(self, dto: TrucksRequest):
        nearestTrucks = self.trucks.getNearestTrucks(dto)
        return nearestTrucks