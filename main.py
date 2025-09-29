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
from typing import List
from sqlalchemy.orm import Session
from config.Database import SessionLocal, engine
from models.todo import Task
from dtos.taskRequest import TaskCreate
from dtos.taskResponse import TaskResponse


app = FastAPI()


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
    

