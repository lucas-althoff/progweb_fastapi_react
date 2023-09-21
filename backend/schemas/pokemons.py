from pydantic import BaseModel

class Pokemon(BaseModel):
    nome: str
    habilidade: str
    idade: int
    exp: int
    vida: int
    forca: int