
from model import TrucksRequest
from persistence import TrucksRepository

class TrucksUseCase:
    def __init__(self, repository: TrucksRepository):
        self._repository = repository

class GetTrucks(TrucksUseCase):
    def execute(self, dto: TrucksRequest):
        return self._repository.get(dto)