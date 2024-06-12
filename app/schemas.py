
##################### HANDELLING REQUEST AND RESPONSE VALIDATION IN FASTAPI ###############################

# INITIAL IMPORTS

from pydantic import BaseModel, Extra
from typing import Dict, Any,Optional
from datetime import datetime


# CONFIGURATION BASE FOR REQUESTS FOR CREATING CONFIGURATION. 

class ConfigurationBase(BaseModel):
    country_code:str # MOST IMPORTANT
    country_name:Optional[str]
    company_name:str # NECESSARY
    requirements: Dict[str, Any]


# CONFIGURATION BASE FOR REQUESTS FOR UPDATING CONFIGURATION. 

class ConfigurationBase2(BaseModel):
    country_code:str
    country_name:Optional[str]
    company_name:Optional[str]
    requirements: Dict[str, Any]

#     # class Config:
#     #     extra = Extra.forbid

class ConfigurationCreate(ConfigurationBase):
    pass

class ConfigurationUpdate(ConfigurationBase2):
    pass


# CONFIG ATTRIBUTES WHICH AUTOMATICALLY GET ADDED TO CONFIG.(LIKE PRIMARY KEY, CREATION TIME, UPDATION TIME)

# CONFIGURATION BASE FOR RESPONSE FOR CREATING CONFIGURATION

class Configuration(ConfigurationBase):
    id: int
    createdAt: datetime
    updatedAt: Optional[datetime]

    class Config:
        orm_mode = True


# CONFIGURATION BASE FOR RESPONSE FOR UPDATING CONFIGURATION

class Configuration(ConfigurationBase2):
    id: int
    createdAt: datetime
    updatedAt: Optional[datetime]

    class Config:
        orm_mode = True
