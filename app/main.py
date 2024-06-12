

############################ PYTHON VIRTUAL ENVIRONMENT IS USED IN IT #########################################

# Importe all packages via requirements.txt
# For Running main.py use Bash Terminal
# Entering in Virtual Env------>  source cogoport/scripts/activate
# CMD---->  uvicorn app.main:app --reload


#INITIAL IMPORTS

from fastapi import FastAPI
from .database import engine, database, Base
from .routes import configuration
import logging


# USED BY SQLALCHEMY TO CREATE DATABASES ON GIVEN ENGINE CONFIGURATION

Base.metadata.create_all(bind=engine)


#STARTING AN OBJECT OF FASTAPI CLASS 

app = FastAPI()


#@app OBJECT ON STARTUP 

@app.on_event("startup")    
async def startup():
    print("Connected at http://localhost:8000")
    await database.connect()
    print('Connected to PostGreSQL Server')


#@app OBJECT ON SHUTDOWN     

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    print('Disconnected from Postgres SQL')



#HEALTH CHECKING API OF THE SERVER

@app.get("/status")
def status():
    return {"status": "Server is running!"}


#CALLING DIFFERENT ROUTER UNDER /api Prefix( Generally useful during NGINX Setup (Running Frontend and Backend on Same URl))

app.include_router(configuration.router, prefix="/api")



# Set logging
# logging.basicConfig(filename='app.log', level=logging.INFO)
