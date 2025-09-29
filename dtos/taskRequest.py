from pydantic import BaseModel
from typing import Optional

# Pydantic models
#This model will be used to validate the request body when creating a new task
# This model is incoming model
class TaskCreate(BaseModel):
    title: str
    description: str    
    # Optional field with default valu
    isCompleted :  Optional[bool] = False