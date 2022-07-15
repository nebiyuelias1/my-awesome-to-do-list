from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from app.api import deps
from app.schemas.user import UserCreate, User, UserInDBBase
from app.crud import crud_user


router = APIRouter()


@router.post('/', response_model=User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_create: UserCreate
):
    """
    Create a new user.
    """
    user = crud_user.get_user_by_email(db, email=user_create.email)

    if user:
        raise HTTPException(
            status_code=400,
            detail='The user with this username already exists in the system.'
        )
    user = crud_user.create_user(db, user=user_create)
    return user
