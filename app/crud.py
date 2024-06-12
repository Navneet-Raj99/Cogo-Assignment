

##################### MAIN FUNCTIONING OF THE ROUTES ######################################

# INITIAL IMPORTS

from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime, timezone



# CONTROLLER FUNCTION FOR GETTING CONFIGURATION

def get_configuration(db: Session, country_code: str):
    return db.query(models.Configuration).filter(models.Configuration.country_code == country_code).first()


# CONTROLLER FUNCTION FOR GETTING CONFIGURATION

def create_configuration(db: Session, config: schemas.ConfigurationCreate):
    print("entered")
    current_time = datetime.now(timezone.utc)

    # Setting creation time
    db_config = models.Configuration(**config.dict(), createdAt=current_time)
    db.add(db_config)
    # db_config.createdAt = datetime.now(timezone.utc)
    db.commit()
    db.refresh(db_config)
    return db_config


# CONTROLLER FUNCTION FOR UPDATING CONFIGURATION

def update_configuration(db: Session, country_code:str, config: schemas.ConfigurationUpdate):
    print("entered")
    db_config = get_configuration(db,country_code)
    if db_config:

        #Running a Loop to set different Attributes coming via Request
        for key, value in config.dict().items():
            setattr(db_config, key, value)

        # Setting Updation time    
        db_config.updatedAt = datetime.now(timezone.utc)
        db.commit()
        db.refresh(db_config)
        return db_config
    return None


# CONTROLLER FUNCTION FOR DELETING CONFIGURATION

def delete_configuration(db: Session, country_code: str):
    db_config = get_configuration(db, country_code)
    if db_config:
        db.delete(db_config)
        db.commit()
        return True
    return False
