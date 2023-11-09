from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List
from fastapi.responses import HTMLResponse

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

def coletar_caminho(file_name):
    import os
    root_path = os.getcwd()
    fpath = f'\\database\\{file_name}'
    path = root_path + fpath
    return path

@rotas.get('/', include_in_schema=False)
def home():
    html = """
            <!DOCTYPE html>
            <html lang="pt-br">
            <head>
                <link rel="shortcut icon" href="favicon.ico">
                <title>Biblioteca de Pokemons</title>
            </head>
            <body>
                <div class="header"> 
                    <div class="inner-header flex">
                        <div class="logo-container">
                            <img src="/static/logo2.png" alt="OCA" class="logo">
                        </div>
                        <h1>Biblioteca de Pokemons API</h1>
            
                    </div>
                    <h2>Seja bem vindo a API de comunicação com a PokeAPI. <br>
                        Esse sistema tem o objetivo de facilitar a manipulação de dados relacionados a uma biblioteca de pokemons.<br>
                        Para maiores informacoes visite: /docs 
                    </h2> 
                </div>
                    <div class="content flex">
                    <p>@CEUB 2023. </p>
                </div>
            </body>
            </html>
            """
    return HTMLResponse(html)

@rotas.get('/pikachu',
           tags=['Consultas'],
           name='Leitura de Pikachus',
           description='Dicionário contendo pikachus, devolve o número de pikachus de entrada.')
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

import random
class Pokemon(BaseModel):
    nome: str = "Pikachu"
    habilidade: Optional[str] = ""
    idade: int = 10
    exp: int = 0
    vida: int = random.randint(10,100)
    forca: int = random.randint(10,50)

class Pokemons(BaseModel):
    Lista: List[Pokemon]
    
        
@rotas.post('/pokemon',
            tags=['Inserções'],
            name='Incluir Pokemon',
            description='Receber objeto Pokemon e guardar no arquivo.')
def atualizacao_pokemon(entrada: Pokemon):
    # Receber novo pokemon [ok]
    # Abrir arquivo [ok]
    # Incluir pokemon [ok]
    # Salvar novo arquivo [ok]
    # Formatar pokemon como json
    # Devolver lista de pokemons atualizada
    import json
    
    path = coletar_caminho("lista_pokemon.txt")
    
    entrada_fmt = str(entrada).split(' ')
    entrada_fmt = json.dumps(entrada_fmt)
    arq = open(path,'a')
    arq.write(str(entrada_fmt)+'\n')
    arq.close()
    print(entrada_fmt, type(entrada_fmt))
    return entrada_fmt

@rotas.post('/pokemons', tags=['Inserções'],
            name='Incluir múltiplos Pokemons',
            description='Receber objeto Pokemon e guardar no arquivo.')
def atualizacao_pokemon(entrada: Pokemons):
    return entrada