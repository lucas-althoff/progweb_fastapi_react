# progweb_fastapi_react
Um projeto de servidor fullstack minimalista, para ser utilizado em cursos básicos de Programação WEB em Python.

## Tecnologias 
Servidor Back-end: Python com o Framework FastAPI
Servidor Front-end: Javascript com os frameworks Reactjs e Bootstrap

## Configurando ambiente
`conda create -n progweb python=3.11 pip git`
## Configurando o servidor Back-end

Após instalar o Python em versão acima da 3.7 executar:

`pip install fastapi`
`pip install uvicorn`
`pip install SQLite` ou `pip install tinydb`
`pip install 'pydantic[email]'`


Para subir o servidor base você tem duas opções, rodando o interpretador no arquivo python:
- `python backend/app_v1_uvicorn.py`

Chamando o servidor uvicorn para implantar o objeto app:
-  `cd backend` 
- `uvicorn app_v1:app --reload`

O backend em sua versão de treinamento será incluido na pasta app_v1.

## Configurando o servidor Front-end