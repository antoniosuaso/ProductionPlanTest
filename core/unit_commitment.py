from fastapi import HTTPException
from models.payload import PayloadModel
from models.power_plant import PowerPlantType, PowerPlantModel
from core.response_dict_gen import generate_response_dict


# Calculate the amount of power each plant has to produce based on the merit order and the remaining energy to be generated
def production_set(data: PayloadModel, merit_order: list):
    try:
        power_assign = []
        load_left = data.load
        # Iterate over the plants in order
        for plant in merit_order:
            aux_p = 0
            if plant.type == PowerPlantType.WIND:
                # Wind production is limited by the amount of wind available unlike the rest, just based on the cost
                aux_p = plant.pmax * (data.fuels["wind(%)"] / 100)
            else:
                # If there's no more energy to be covered, we don't need more production
                if load_left <= 0 or plant.pmin > load_left:
                    aux_p = 0
                # If Pmin is lower than the remaining energy to be generated, there's room for more production
                # so we choose the min between the remaining energy and the Pmax.
                elif plant.pmin < load_left:
                    aux_p = min(load_left, plant.pmax)
                # Otherwise, Pmin is greater than
                else:
                    aux_p = plant.pmin

            load_left -= aux_p
            power_assign.append(generate_response_dict(name=plant.name, p=aux_p))

        return power_assign

    except KeyError as keyErr:
        raise HTTPException(
            detail="Missing " + str(keyErr) + "key in fuels dict.", status_code=400
        )
