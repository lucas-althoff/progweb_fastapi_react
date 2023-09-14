from fastapi import APIRouter

rotas = APIRouter()

def arquivo_pokemon(pokemon=None, acao='leitura'):
    import os
    import json
    fpath = os.getcwd()
    path = fpath + r'\utils\dados.json'
    if acao=='leitura':
        with open(path,'r') as f:
            pokemons = json.load(f)
        return pokemons
    else:
        pokemons = arquivo_pokemon(acao='leitura')
        pokemons.append(pokemon)
        return pokemons

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
def leitura_pokemon():
    pokemons = arquivo_pokemon(acao='leitura')
    print(pokemons, type(pokemons))
    return pokemons

@rotas.post('/pokemon')
def atualizacao_pokemon(entrada):
    ...
    