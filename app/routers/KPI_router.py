from bson import ObjectId
from fastapi import APIRouter, HTTPException
import mariadb

from app.models.data import character_model
from app.settings import database
from app.settings.database import connect


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
    conn = connect()
    cursor = conn.cursor()
    querry = '''SELECT * FROM characters WHERE ID = ?'''
    values = (id,)
    try: 
        cursor.execute(querry, values)
    except mariadb.Error as e: 
        print(f"Error: {e}")
    conn.commit()
    conn.close()
    result = cursor.fetchone()
    if (result):
        return result

    raise HTTPException(status_code=404, detail=f"Data {id} not found")