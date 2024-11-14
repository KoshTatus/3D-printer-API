from pydantic import BaseModel, Field, EmailStr


class UserForm(BaseModel):
    email: EmailStr = Field(title="Email", default="user@example.com")
    password: str = Field(title="Password", min_length=8, max_length=255, default="12345678")

class UserCreate(BaseModel):
    email: str
    password_hash: str

class UserInfo(BaseModel):
    id: int
    group_id: int | None

class UserModel(UserCreate, UserInfo):
    name: str | None


