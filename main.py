#Now demo is over.. Lets build a todo app

#Features of todo
#1. Add a task
#2. View all tasks

#Apis we will expost
#1. POST /tasks - to add a task
#2. GET /tasks - to view all tasks

#Database schema will have
#1. id - int - primary key
#2. title - str - title of the task
#3. description - str - description of the task


from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import List, Optional

#These imports are for connecting to the database
from sqlalchemy import create_engine, Column, Integer, String, Boolean

#These imports are for creating the database models
from sqlalchemy.ext.declarative import declarative_base

#These imports are for creating the database sessions
from sqlalchemy.orm import sessionmaker, Session

app = FastAPI()

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

# SQLAlchemy model
class Task(Base):   
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), index=True, nullable=False)
    description = Column(String(255), index=True, nullable=False)
    isCompleted = Column(Boolean, default=False)  

Base.metadata.create_all(bind=engine)

# Pydantic models
#This model will be used to validate the request body when creating a new task
# This model is incoming model
class TaskCreate(BaseModel):
    title: str
    description: str    
    # Optional field with default valu
    isCompleted :  Optional[bool] = False

#This model will be used to validate the response body when returning a task
# This model is outgoing model
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    isCompleted :  Optional[bool] = False

    # This is to tell pydantic to work with ORM models
    class Config:
        orm_mode = True

# DB session dependency
#this function will be called everytime a request is made to the api
#What this do is it will create a new session for each request and close it once the request is done
# Further optimizations can be done like using connection pool etc....
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routes
# Why List[TaskResponse] - because we are returning a list of tasks
# response_model is used to validate the response body
@app.get("/tasks", response_model=List[TaskResponse])
def read_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()


# We have to put Database session in the function parameters
# because we need to interact with the database to add a new task   
@app.post("/add_task", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

#Api to delete a task
@app.delete("/delete_task/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        return {"message": "Task deleted successfully"}
    else:
        return {"message": "Task not found"}
    

