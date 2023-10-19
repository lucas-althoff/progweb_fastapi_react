from fastapi import FastAPI
import uvicorn
from rotas_pizza import rotas

pizza = FastAPI()
pizza.include_router(rotas)
uvicorn.run(pizza, host='0.0.0.0', port=7778)
