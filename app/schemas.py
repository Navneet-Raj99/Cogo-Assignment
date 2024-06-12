from pydantic import BaseModel, Extra
from typing import Dict, Any

class ConfigurationBase(BaseModel):
    country_code:str
    requirements: Dict[str, Any]

    class Config:
        extra = Extra.forbid

class ConfigurationCreate(ConfigurationBase):
    pass

class ConfigurationUpdate(ConfigurationBase):
    pass

class Configuration(ConfigurationBase):
    id: int

    class Config:
        orm_mode = True
