"""
Preservando metadatas com wraps

metadatas -> são dados intrisecos em arquivos

wraps -> funções que envolvem elementos com diversadas finalidades

"""

# Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        """ i am one function (loguin) """
        print(f' Voce esta chamando{funcao.__name__}')
        print(f'aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma dois numeros"""
    return a + b

print(soma(10, 30))

print(soma.__name__)
print(soma.__doc__)



# Resolução do problema


from functools import wraps


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """ i am one function (loguin) """
        print(f' Voce esta chamando{funcao.__name__}')
        print(f'aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois numeros"""
    return a + b


print(soma(10, 30))


print(soma.__name__)
print(soma.__doc__)

print(help(soma))
