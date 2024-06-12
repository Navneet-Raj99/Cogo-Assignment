
# INITIAL IMPORTS

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database

# CREATING OBJECT OF APIROUTER() CLASS

router = APIRouter()


# ACCESSING DATABASE CONFIG TO GET ACCESSIBILTY TO DATABASE

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ROUTE FOR Creating Configuration 

@router.post("/create_configuration", response_model=schemas.Configuration)
async def create_configuration(config: schemas.ConfigurationCreate, db: Session = Depends(get_db)):


    # checking config with same unique attributes is previously there or not
    db_config = crud.get_configuration(db, country_code=config.country_code)
    
    # If not there, performing Exception Handelling
    if db_config:
        raise HTTPException(status_code=400, detail="Configuration already exists")
    return crud.create_configuration(db, config)


# ROUTE FOR Getting Configuration via country_code

@router.get("/get_configuration/{country_code}", response_model=schemas.Configuration)
async def get_configuration(country_code: str, db: Session = Depends(get_db)):
    db_config = crud.get_configuration(db, country_code)

    # If not there, performing Exception Handelling
    if not db_config:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_config


# ROUTE FOR Updating Configuration 

@router.post("/update_configuration", response_model=schemas.Configuration)
async def update_configuration(config: schemas.ConfigurationUpdate, db: Session = Depends(get_db)):
    db_config = crud.update_configuration(db, config.country_code, config)

    # If not there, performing Exception Handelling
    if not db_config:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_config


# ROUTE FOR Deleting Configuration 

@router.delete("/delete_configuration", response_model=dict)
async def delete_configuration(country_code: str, db: Session = Depends(get_db)):
    success = crud.delete_configuration(db, country_code)

    # If not there, performing Exception Handelling
    if not success:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return {"detail": "Configuration deleted"}
