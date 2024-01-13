from fastapi import FastAPI, Path , Query
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()
users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str] = None

@app.get('/users', response_model=List[User])
async def get_users():
    return users

@app.post('/users')
async def create_user(user: User):
    users.append(user)

    return{"created": True}

@app.get('/user/{id}')
async def return_user(
    id: int = Path(..., description = "The Id of the User", gt=2), #First Parameter of Path is to define a reqirable parameter, then the second is the description, finally the third is the minimum value, for example we are expecting with gt=2 values grater than 2.
    query: str = Query(None, max_lenght=5)
    
    ):
    return {
        "user": users[id],
        "query": query
    }
