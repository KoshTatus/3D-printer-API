from pydantic import BaseModel, Field, EmailStr


class UserForm(BaseModel):
    email: EmailStr = Field(title="Email")
    password: str = Field(title="Password", min_length=8, max_length=255)

class UserCreate(BaseModel):
    email: str
    password_hash: str
class UserModel(UserCreate):
    id: int
    id_group: int | None
    name: str | None