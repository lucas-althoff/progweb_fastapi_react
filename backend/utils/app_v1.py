from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

# Instanciando aplicação
servidor = FastAPI()

@servidor.get("/")
def raiz():
    return HTMLResponse("""<html>
                Olá Mundo <br>
                Programação para Web
                </html>""")

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