from typing import List
from sqlalchemy.orm import Session
from app.models.todo import Todo

from app.schemas.todo import TodoCreate


def create_todo(db: Session, todo: TodoCreate, creator_id: int) -> Todo:
    todo = Todo(**todo.dict(), creator_id=creator_id)
    db.add(todo)
    db.commit()
    db.refresh(todo)

    return todo


def get_me_todos(db: Session, creator_id: int, skip: int = 0, limit: int = 10) -> List[Todo]:
    return db.query(Todo).filter(Todo.creator_id == creator_id).offset(skip).limit(limit).all()

def get_todo_by_id(db: Session, todo_id: int) -> Todo:
    return db.query(Todo).filter(Todo.id == todo_id).first()

def mark_todo_as_done(db: Session, todo_id: int) -> Todo:
    todo = get_todo_by_id(db, todo_id)
    
    if not todo:
        return None
    
    todo.is_completed = True
    db.commit()
    
    return todo
