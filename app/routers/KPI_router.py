from fastapi import APIRouter, HTTPException
import mariadb

from app.settings.database import connect, basic_query


router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Working fine"}


@router.get(
    "/character/{id}",
    response_description="Get a single character by its ID",
    #response_model=character_model,
    response_model_by_alias=False,
) 
async def show_character(id: str):
    query = '''SELECT * FROM characters WHERE char_id = ?'''
    values = (id,)
    result = basic_query(query,values)
    if (result):
        return result.fetchone()
    raise HTTPException(status_code=404, detail=f"Data {id} not found")