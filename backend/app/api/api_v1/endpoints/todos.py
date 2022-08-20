from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.models.user import User

from app.schemas.todo import TodoCreate, TodoOut
from app.api import deps
from app.crud import crud_todo


router = APIRouter()


@router.post('/', response_model=TodoOut)
def create_todo(
    *,
    db: Session = Depends(deps.get_db),
    todo_create: TodoCreate,
    current_user: User = Depends(deps.get_current_user),
):
    """
    Create a new todo.
    """
    todo = crud_todo.create_todo(
        db=db, todo=todo_create, creator_id=current_user.id)
    return todo


@router.get('/me', response_model=List[TodoOut])
def get_me_todos(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 10,
    current_user: User = Depends(deps.get_current_user),
):
    """
    Get me todos.
    """
    return crud_todo.get_me_todos(db=db, creator_id=current_user.id, skip=skip, limit=limit)


@router.post('/done/{id}', response_model=TodoOut)
def mark_as_done(*, db: Session = Depends(deps.get_db), id: int, current_user: User = Depends(deps.get_current_user)):
    todo = crud_todo.get_todo_by_id(db, id)
    if not todo:
        raise HTTPException(404, detail='Todo not found.')
    
    if current_user.id != todo.creator_id:
        raise HTTPException(400, detail='Not allowed to update todo.')
    
    todo = crud_todo.mark_todo_as_done(db, id)
    
    return todo
