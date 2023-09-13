from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Ola Mundo'}

@app.get('/dados')
def dados():
    return {'conteudo': 'Um tomate pequeno.'}

@app.get('/pokemon')
def pokemon():
    p = "pikachu"
    s = str([p,p])
    return {'conteudo': s}
    
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=7778)
