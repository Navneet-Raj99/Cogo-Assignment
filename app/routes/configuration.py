from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create_configuration", response_model=schemas.Configuration)
async def create_configuration(config: schemas.ConfigurationCreate, db: Session = Depends(get_db)):
    db_config = crud.get_configuration(db, country_code=config.country_code)
    if db_config:
        raise HTTPException(status_code=400, detail="Configuration already exists")
    return crud.create_configuration(db, config)

@router.get("/get_configuration/{country_code}", response_model=schemas.Configuration)
async def get_configuration(country_code: str, db: Session = Depends(get_db)):
    db_config = crud.get_configuration(db, country_code)
    if not db_config:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_config

@router.post("/update_configuration", response_model=schemas.Configuration)
async def update_configuration(config: schemas.ConfigurationUpdate, db: Session = Depends(get_db)):
    db_config = crud.update_configuration(db, config.country_code, config)
    if not db_config:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_config

@router.delete("/delete_configuration", response_model=dict)
async def delete_configuration(country_code: str, db: Session = Depends(get_db)):
    success = crud.delete_configuration(db, country_code)
    if not success:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return {"detail": "Configuration deleted"}
