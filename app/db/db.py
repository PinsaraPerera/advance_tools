from dotenv import load_dotenv
import os
import sqlalchemy

from sqlalchemy import create_engine

# Load environment variables from a .env file
load_dotenv()

# Fetch database credentials from environment variables
DB_USER = os.getenv("DB_USER", "postgres")  
DB_PASS = os.getenv("DB_PASS", "test")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432") 
DB_NAME = os.getenv("DB_NAME", "mydatabase")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def connect_with_connector() -> sqlalchemy.engine.base.Engine:
    """
    Initializes a connection pool for a local PostgreSQL instance.
    """
    engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)
    return engine
