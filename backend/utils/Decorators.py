# Decorators

def ola():
    return 'ola!'


def olazao(f):
    def wrapper():
        texto = f()
        textao = texto.upper()
        return textao
    return wrapper

ola()

def cronometro(f):
     def encapsulador():
             ini = datetime.now()
             f()
             fim = datetime.now()
             print("Tempo decorrido na execução da função \n",fim-ini)
     return encapsulador