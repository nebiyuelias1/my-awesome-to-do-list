from fastapi import APIRouter
from app.api.api_v1.endpoints.users import router

api_router = APIRouter()

api_router.include_router(router, prefix='/users', tags=['users'])