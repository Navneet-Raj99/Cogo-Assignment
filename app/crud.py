from sqlalchemy.orm import Session
from . import models, schemas

def get_configuration(db: Session, country_code: str):
    return db.query(models.Configuration).filter(models.Configuration.country_code == country_code).first()

def create_configuration(db: Session, config: schemas.ConfigurationCreate):
    print("entered")
    db_config = models.Configuration(**config.dict())
    db.add(db_config)
    db.commit()
    db.refresh(db_config)
    return db_config

def update_configuration(db: Session, country_code:str, config: schemas.ConfigurationUpdate):
    print("entered")
    db_config = get_configuration(db,country_code)
    # print(db_config)
    if db_config:
        for key, value in config.dict().items():
            setattr(db_config, key, value)
        db.commit()
        db.refresh(db_config)
        return db_config
    return None

def delete_configuration(db: Session, country_code: str):
    db_config = get_configuration(db, country_code)
    if db_config:
        db.delete(db_config)
        db.commit()
        return True
    return False
