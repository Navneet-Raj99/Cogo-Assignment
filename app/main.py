from fastapi import FastAPI
from .database import engine, database, Base
from .routes import configuration
import logging

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.on_event("startup")    
async def startup():
    print("Connected at http://localhost:8000")
    await database.connect()
    print('Connected to PostGreSQL Server')

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    print('Disconnected from Postgres SQL')

@app.get("/status")
def status():
    return {"status": "Server is running!"}


app.include_router(configuration.router, prefix="/api")



# Set logging
# logging.basicConfig(filename='app.log', level=logging.INFO)
