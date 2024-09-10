import uvicorn
from fastapi import FastAPI, Request
from api.api import api_router

# from db.init_db import init_db
from constants import SERVER_IP, SERVER_PORT
from constants import URL_PREFIX


# Instance of FastAPI obj

app = FastAPI(docs_url=URL_PREFIX + "/docs")

# Include the api_router to the main router

app.include_router(api_router)


# Execute command
if __name__ == "__main__":
    uvicorn.run(app, host=SERVER_IP, port=SERVER_PORT)
