from fastapi import HTTPException
from models.payload import PayloadModel
from models.power_plant import PowerPlantType
from constants import CO2_EMISSIONS_STATISTIC_GAS


# Calculate the merit order based on efficiency and costs
def merit_order_sort(data: PayloadModel):
    try:
        plants = []

        # Iterate over the list of plants
        for plant in data.powerplants:

            merit_value = 1000000

            # Gas cost = (Gas price / gas plant efficiency) + (co2 emitions price / average co2 emitions)
            if plant.type == PowerPlantType.GAS:
                merit_value = (data.fuels["gas(euro/MWh)"] / plant.efficiency) + (
                    data.fuels["co2(euro/ton)"] * CO2_EMISSIONS_STATISTIC_GAS
                )
            # jet cost = (jet price / jet plant efficiency)
            elif plant.type == PowerPlantType.JET:
                merit_value = (data.fuels["kerosine(euro/MWh)"] / plant.efficiency)
            # Wind cost = 0
            elif plant.type == PowerPlantType.WIND:
                merit_value = 0
            else:
                raise Exception("Unsupported type of plant given.")

            # Set the merit value to the obj
            plant.merit_value = merit_value
            plants.append(plant)

        # Sort the plants based on the merit_value (asc)
        sorted_plants = sorted(plants, key=lambda x: x.merit_value)

        return sorted_plants

    except Exception as keyErr:
        raise HTTPException(
            detail="Missing " + str(keyErr) + "key in fuels dict.", status_code=400
        )
