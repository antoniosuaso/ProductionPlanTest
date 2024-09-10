from pydantic import BaseModel
from models.power_plant import PowerPlantModel
from typing import List, Any


class PayloadModel(BaseModel):
    load: int
    powerplants: List[PowerPlantModel]
    fuels: dict
