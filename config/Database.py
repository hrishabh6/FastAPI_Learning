
#These imports are for creating the database models
from sqlalchemy.orm import sessionmaker

#These imports are for creating the database sessions
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


MYSQL_USER = "root"
MYSQL_PASSWORD = "hrishabh%40123"  # '@' is URL encoded as %40
MYSQL_HOST = "localhost"
MYSQL_DB = "fastapi_demo"

# SQLAlchemy setup
#You can use any database of your choice
#Here we are using mysql
#Connection string format is mysql+pymysql://<username>:<password>@<host>/<dbname> this is SQLAlchemy format

DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"

# Create the database engine
# The engine is the starting point for any SQLAlchemy application
# What it does is it manages the connection pool and provides a source of database connections
# You can think of it as a factory for database connections, which can be used to interact with the database
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

