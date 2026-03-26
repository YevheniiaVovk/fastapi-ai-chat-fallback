
from pydantic import BaseModel, Field, EmailStr, ConfigDict

class UserCreate(BaseModel): 
    email: EmailStr
    password: str = Field(min_length=8)
    username: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str
    model_config = ConfigDict(from_attributes=True)
    

class UserLogin(BaseModel): 
    email: EmailStr
    password: str


