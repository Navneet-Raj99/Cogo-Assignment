
#INITIAL IMPORTS

from sqlalchemy import Column, Integer, String, JSON, DateTime, func
from .database import Base
from datetime import datetime, timezone


#SPECIFYING MODEL STRUCTURE FOR "configurations" TABLE

class Configuration(Base):
    __tablename__ = "configurations"
    id = Column(Integer, primary_key=True, index=True) # Primary Key
    country_code = Column(String, unique=True, index=True)
    country_name = Column(String, unique=False, index=True)
    company_name = Column(String, unique=False, index=True)


    # For considering Different Different Key Value Pair for Business depending on Country Code JSON DATA TYPE IS USED
    requirements = Column(JSON, nullable=False) 


    createdAt = Column(DateTime, default= datetime.now(timezone.utc))
    updatedAt = Column(DateTime, default=None, onupdate=datetime.now(timezone.utc))
