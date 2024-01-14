import fastapi
from pydantic import BaseModel
from typing import Optional, List

router = fastapi.APIRouter()

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str] = None


@router.get('/users', response_model=List[User])
async def get_users():
    return users

@router.post('/users')
async def create_user():
    users.append(user)

    return{"created": True}

@router.get('/user/{id}')
async def return_user():
    return {
        "user": users[id]
    }