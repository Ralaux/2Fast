from datetime import date
from pydantic import BaseModel, Field


class character_model(BaseModel):
    id: int = Field(...)
    classe: str = Field(...)
    nom: str = Field(...)
    serveur: str = Field(...)
    isDeleted: bool = Field(...)
    creation_date: date = Field(...)
    modification_date: date = Field(...)