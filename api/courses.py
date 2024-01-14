import fastapi
from pydantic import BaseModel
from typing import Optional, List

router = fastapi.APIRouter()


@router.get('/courses')
async def get_courses():
    return {"courses": []}

@router.post('/courses')
async def create_courses():
    return{"courses": []}

@router.get('/courses/{id}')
async def get_course(id: int):
    return {"courses": []}

@router.patch('/courses/{id}')
async def update_course(id: int):
    return {"courses": []}

@router.delete('/courses/:{id}')
async def delete_course(id: int):
    return {"courses": []}

@router.get('/courses/{id}/sections')
async def get_course_sections(id: int):
    return {"courses": []}