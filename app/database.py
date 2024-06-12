
#INITIAL IMPORTS

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import databases
import os

# USING DOTENV PACKAGE TO HIDE CRUCIAL USER SPECIFIC DATA

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")


# CHECKING IF DATABASE_URL EXISTS OR NOT

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL is not set in the environment")



database = databases.Database(DATABASE_URL)
metadata = MetaData()

# CREATING ENGINE WHICH WILL BE USED BY SQLALCHEMY FOR GENERATING TABLES

engine = create_engine(DATABASE_URL) 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


#CREATING BASE CLASS FOR ORM MAPPING

Base = declarative_base()
