from fastapi import APIRouter

rotas = APIRouter()

@rotas.get('/')
async def home():
    return {'message': 'Ola Mundo'}

@rotas.get('/dados')
async def dados() -> dict:

    exemplo = {'usuario': 'Cícera',
               'livro': 'O Pequeno Príncipe'}

    return exemplo