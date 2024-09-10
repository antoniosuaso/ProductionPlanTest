from pydantic import BaseModel
from enum import Enum


class PowerPlantType(Enum):
    WIND = "windturbine"
    GAS = "gasfired"
    JET = "turbojet"


class PowerPlantModel(BaseModel):
    name: str
    type: PowerPlantType
    efficiency: float
    merit_value = 0
    pmin: int
    pmax: int
