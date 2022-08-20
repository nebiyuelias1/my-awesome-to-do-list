from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: Optional[str]
    deadline: datetime
    
class TodoCreate(TodoBase):
    pass

class TodoOut(TodoBase):
    id: int
    is_completed: bool
    created_at: datetime
    
    class Config:
        orm_mode = True
    