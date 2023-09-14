from datetime import datetime
from fastapi import FastAPI
from rotas.rotas_api import rotas
import uvicorn

app = FastAPI()

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
    uvicorn.run(app, host='0.0.0.0', port=7777)