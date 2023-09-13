from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
    
class Pokemon(BaseModel):
    id: int
    nome: str
    habilidade: str
