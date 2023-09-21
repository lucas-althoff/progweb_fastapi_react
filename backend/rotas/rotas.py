from fastapi import APIRouter
from modelos.schemas import UserSchema, UserPublic, UserDB
from tinydb import TinyDB

rotas = APIRouter()
database = []


@rotas.get('/home')
def home():
    return {'message': 'Ola Mundo'}


@rotas.get('/')
def raiz():
    return {'message': 'Ola Mundo'}


@rotas.post('/usuarios', status_code=201, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    for item in database:
        print(item)
    return user

@rotas.get('/dados')
async def dados() -> dict:

    exemplo = {'usuario': 'Cícera',
               'livro': 'O Pequeno Príncipe'}

    return exemplo