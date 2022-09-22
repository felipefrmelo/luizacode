from fastapi import Depends, APIRouter
from pydantic import BaseModel

from src.server.database import db

from src.models.user import create_user


router = APIRouter(
          prefix="/user",
          tags=["user"],
        )

class User(BaseModel):
    email: str
    password: str
    is_active: bool
    is_admin: bool



@router.post("/")
async def create(user: User):

    users_collection = db.users_collection
    result = await create_user(users_collection, user.dict())
    del result["_id"]
    return result

