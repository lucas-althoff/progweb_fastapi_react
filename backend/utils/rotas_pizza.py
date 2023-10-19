from fastapi import APIRouter

rotas = APIRouter()

@rotas.get('/')
def home():
    return {'mensagem': 'Seja bem vindo a nossa aplicação'}

@rotas.get('/casa')
def casa():
    return {'mensagem': 'Ola casa'}

@rotas.get('/dados')
def dados():
    l = [1,2,3,4,5,6,7]
    return {'conteudo': l}

@rotas.get('/pokemon')
def pokemon(numero: int, nome: str):
    p = nome
    l =[]
    for i in range(numero):
        l.append(p+str(i))
    return {'conteudo': l}


@rotas.post('/pokedex')
def pokemon():
    p = nome
    l =[]
    for i in range(numero):
        l.append(p+str(i))
    return {'conteudo': l}