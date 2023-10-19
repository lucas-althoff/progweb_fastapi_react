from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

# Instanciando aplicação
servidor = FastAPI()

# Definindo rotas
@servidor.get("/", include_in_schema=False)
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

@servidor.get("/pessoas")
def pessoas(nome: str, idade: int):
    pessoas = [{"username": "joao",
               "email": "joao123@email.com",
               "password": "segredo123"
               },
               {"username": "ana",
                "email": "ana123@email.com",
                "password": "ana123"
                },
                {"username": "pedro",
                "email": "pedro123@email.com",
                "password": "pedro123"
                }]
    
    for pessoa in pessoas:
        if pessoa['username'] == nome:
            pessoa['idade'] = idade  # incluir idade no usuario encontrado
    return pessoas

# Subir servidor: atrela objeto da aplicação a um processo e disponibilia em um host/port
uvicorn.run(servidor, host='localhost', port=7777)