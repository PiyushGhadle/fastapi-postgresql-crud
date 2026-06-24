from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load variables from .env
load_dotenv()

# Get database URL
db_url = os.getenv("DATABASE_URL")

engine = create_engine(db_url)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)