from fastapi import APIRouter, Depends, HTTPException
from models.payload import PayloadModel
from core.merit_order import merit_order_sort
from core.unit_commitment import production_set

router = APIRouter()


@router.get("/")
async def endpoint_root():

    return {"Message": "Welcome to the test root endpoint!"}


"""
    Method: POST

    Description: This endpoint calculate the merit order or different types of power plants
                 and the power each plant must supply to reach the desired load.
    
    Exceptions: 
        - 400 --> "Missing 'X'key in fuels dict."
        - 422 --> Unprocessable Entity (Error in Plant.type parse)
        - 500 --> Server error

"""


@router.post("/productionPlan")
async def endpoint_production_plan(req: PayloadModel):
    try:

        merit_order = merit_order_sort(req)

        return production_set(data=req, merit_order=merit_order)

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Server Error: " + str(e))
