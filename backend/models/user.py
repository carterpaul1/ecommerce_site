from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: Optional[str]
    name: str
    email: EmailStr