from fastapi import FastAPI
import uvicorn

# Instanciando aplicação
servidor = FastAPI()

# Definindo rotas
@servidor.get("/home")
def home():
    return {"mensagem": "Seja bem vindo!\nOlá Mundo",
            "lista": [1,2,3,4,5,6]}

@servidor.get("/pessoas")
def pessoas():
    pessoas = [{"username": "joao123",
               "email": "joao123@email.com",
               "password": "segredo123"
               },
               {
                "username": "ana123",
                "email": "ana123@email.com",
                "password": "ana123"
                },
                {
                "username": "pedro123",
                "email": "pedro123@email.com",
                "password": "pedro123"
                }]
    return pessoas

# Subir servidor: atrela objeto da aplicação a um processo e disponibilia em um host/port
uvicorn.run(servidor, host='localhost', port=7777)