from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List

rotas = APIRouter()

def manipulacao_arq_json(fpath, acao='leitura'):
    import json
    if acao == 'leitura':
        with open(fpath,'r') as f:
            resultado = f.read()
        resultado = json.loads(resultado)
        return resultado
    else:
        ...

def coletar_caminho():
    import os
    root_path = os.getcwd()
    fpath = r'\progweb_fastapi_react\backend\utils\dados.json'
    path = root_path + fpath
    return path

@rotas.get('/', include_in_schema=False)
def home():
    return {'message': 'Ola Mundo'}

@rotas.get('/pikachu', tags=['Consultas'], name='Leitura de Pikachus', description='Dicionário contendo pikachus, devolve dois pikachus.')
def pokemon(numero=10):
    p = "pikachu"
    lista = []
    for i in range(int(numero)):
        lista.append(p)
    s = str(lista)
    return lista

# @rotas.get('/pokemon/arquivo')
# def leitura_pokemon():
#     caminho_arq_json = coletar_caminho()
#     resultado = manipulacao_arq_json(fpath=caminho_arq_json, acao='leitura')
#     print("RESULTADO: ", resultado, type(resultado))
#     return resultado

class Pokemon(BaseModel):
    nome: str = "Pikachu"
    habilidade: Optional[str]
    idade: int = 10
    exp: int = 0
    vida: int = 10
    forca: int = 5

class Pokemons(BaseModel):
    Lista: List[Pokemon]
    
        
@rotas.post('/pokemon', tags=['Inserções'], name='Incluir Pokemon', description='Receber objeto Pokemon e guardar no arquivo.')
def atualizacao_pokemon(entrada: Pokemon):
    # Receber novo pokemon [ok]
    # Abrir arquivo 
    # Incluir pokemon
    # Salvar novo arquivo
    # Devolver lista de pokemons atualizada
    print(entrada, type(entrada))
    return entrada

@rotas.post('/pokemons', tags=['Inserções'], name='Incluir múltiplos Pokemons', description='Receber objeto Pokemon e guardar no arquivo.')
def atualizacao_pokemon(entrada: Pokemons):
    return entrada