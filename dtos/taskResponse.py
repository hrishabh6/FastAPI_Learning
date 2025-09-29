from pydantic import BaseModel
from typing import Optional

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