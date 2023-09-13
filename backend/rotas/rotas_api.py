from fastapi import APIRouter

rotas = APIRouter()

@rotas.get('/')
def home():
    return {'message': 'Ola Mundo'}

@rotas.get('/dados')
def dados():
    return {'conteudo': 'Um tomate pequeno.'}

@rotas.get('/pokemon')
def pokemon():
    p = "pikachu"
    s = str([p,p])
    return {'conteudo': s}

@rotas.get('/pokemon/arquivo')
def poke_arq():
    import os
    import json
    fpath = os.getcwd()
    path = fpath + r'\utils\dados.json'
    with open(path,'r') as f:
        pokemons = json.load(f)
    print(pokemons, type(pokemons))
    return pokemons