from pydantic import BaseModel, Extra
from typing import Dict, Any,Optional
from datetime import datetime

class ConfigurationBase(BaseModel):
    country_code:str
    country_name:Optional[str]
    company_name:str
    requirements: Dict[str, Any]


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

class Configuration(ConfigurationBase):
    id: int
    createdAt: datetime
    updatedAt: Optional[datetime]

    class Config:
        orm_mode = True


class Configuration(ConfigurationBase2):
    id: int
    createdAt: datetime
    updatedAt: Optional[datetime]

    class Config:
        orm_mode = True
