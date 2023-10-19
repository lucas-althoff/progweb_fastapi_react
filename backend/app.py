from datetime import datetime
from fastapi import FastAPI
from rotas.rotas_api import rotas
import uvicorn

app = FastAPI(title="Pokedex API",
                description="Aplicação para curso básico de FastAPI",
                summary="Permite o armazenamento de uma pokedex em uma base de dados SQL",
                version="0.0.1",
                terms_of_service="http://example.com/terms/",
                contact={
                    "name": "Prof. Lucas Althoff",
                    "url": "https://github.com/lucas-althoff",
                    "email": "lucas.althoff@ceub.edu.br",
                },
                license_info={
                    "name": "Apache 2.0",
                    "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
                })

@app.on_event('startup')
def __startup():
    """
    Inicialização da API
    """
    print(f'[SERVIDOR POKEMON] [{datetime.now()}] Iniciando - {"API de Teste HTTP"}')


@app.on_event('shutdown')
def __shutdown():
    """
    O que fazer quando a API é encerrada
    """
    print(f'[SERVIDOR POKEMON] [{datetime.now()}] Encerrando - {"A API de HTTP"}')

app.include_router(rotas)
    
if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=7777)