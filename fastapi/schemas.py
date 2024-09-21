from datetime import datetime
from pydantic import BaseModel
from typing import Dict

class CategorySchema(BaseModel):
    name: str
    description: str

    class Config:
        from_attributes = True

class SubcategorySchema(CategorySchema):
    pass

class ProblemSchema(BaseModel):
    title: str
    difficulty: int
    description: str
    example: Dict[str, str]
    constraints: str
    
    class Config:
        from_attributes = True

class SubmissionSchema(BaseModel):
    content: str
    created_at: datetime

    class Config:
        from_attributes = True