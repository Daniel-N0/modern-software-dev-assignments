from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class NoteCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    content: str = Field(..., min_length=1)


class NoteRead(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class NotePatch(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    content: Optional[str] = Field(None, min_length=1)


class ActionItemCreate(BaseModel):
    description: str


class ActionItemRead(BaseModel):
    id: int
    description: str
    completed: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ActionItemPatch(BaseModel):
    description: Optional[str] = None
    completed: Optional[bool] = None


class CategoryCreate(BaseModel):
    name: str


class CategoryRead(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True