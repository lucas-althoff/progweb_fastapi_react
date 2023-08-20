from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
async def home():
    return {'message': 'Ola Mundo'}

@app.get('/dados')
async def dados():
    return {'conteudo': 'Um tomate pequeno.'}
    
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=7777)
