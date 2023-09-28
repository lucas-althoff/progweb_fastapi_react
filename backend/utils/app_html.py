from fastapi import Request
from fastapi.templating import Jinja2Templates
import os

templates = Jinja2Templates(directory=os.path.norm('\templates'))

@rotas.get('/', include_in_schema=False)
def home(request: Request):
    return """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <title>Biblioteca de Pokemons</title>
</head>
<body>
    <div class="inner-header flex">
        <h1>Biblioteca de Pokemons API</h1>
    </div>
</body>
</html>
"""


@rotas.get('/', include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})