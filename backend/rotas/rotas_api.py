from fastapi import APIRouter

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

@rotas.get('/')
def home():
    return {'message': 'Ola Mundo'}

@rotas.get('/dados')
def dados():
    return {'conteudo': 'Um tomate pequeno.'}

@rotas.get('/pokemon')
def pokemon():
    p = "pikachu"
    s = str([p,p])
    return {'conteudo': s}

@rotas.get('/pokemon/arquivo')
def leitura_pokemon():
    caminho_arq_json = coletar_caminho()
    resultado = manipulacao_arq_json(fpath=caminho_arq_json, acao='leitura')
    print("RESULTADO: ", resultado, type(resultado))
    return resultado

@rotas.post('/pokemon')
def atualizacao_pokemon():
    # Receber novo pokemon
    # Abrir arquivo
    # Incluir pokemon
    # Salvar novo arquivo
    # Devolver lista de pokemons atualizada
    ...