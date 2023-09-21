from pydantic import BaseModel, EmailStr


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserDB(BaseModel):
    id: int
    password: str

    class Config:
        orm_mode = True


class UserPublic(BaseModel):
    username: str
    email: EmailStr

    class Config:
        orm_mode = True


class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    items: list[Item] = []
    
    class Config:
        orm_mode = True
