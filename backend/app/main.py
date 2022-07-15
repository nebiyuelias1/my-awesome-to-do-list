from typing import Union

from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.api_v1.api import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api_router, prefix='/api/v1')
