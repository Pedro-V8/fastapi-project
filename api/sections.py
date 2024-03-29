import fastapi
from pydantic import BaseModel
from typing import Optional, List

router = fastapi.APIRouter()


@router.get('/sections/{id}')
async def get_sections():
    return {"courses": []}

@router.get('/sections/{id}/content-blocks')
async def read_section_content_blocks():
    return{"courses": []}

@router.get('/content-blocks/:id')
async def read_content_block(id: int):
    return {"courses": []}