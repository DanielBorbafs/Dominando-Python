"""
Funções de maior grandeza!

oque significa?

- indica que podemos ter funções que retornam outras funções como resultado ou mesmo
que podemos passas funções como argumentos para outras funções, e até mesmo
criar variáveis do tipo de funções nos nossos programas.

em python, funções são Cidadoes de primeira classe, first Class citizes

"""


def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Testando as funções


print(calcular(4, 3, somar))


print(calcular(4, 3, diminuir))


print(calcular(4, 3, multiplicar))


print(calcular(4, 3, dividir))

# Nested Functions - funções Aninhadas

# Em python podemos tambem ter funções dentro de funçoes que são cconhecidas por nested functions.
# ou também inner functions( funções internas)

# Exemplo


from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa


print(cumprimento('Angelina'))


print(cumprimento('Maria'))


print(cumprimento('Iara'))



def faz_me_rir():
    def rir():
        return choice(('hahahaha', 'kkkkkkk', 'sahudhasudhasu'))
    return rir


rindo = faz_me_rir()
print(rindo())

# Inner Functions podem acessar escopo de funções mais externas

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahaha', 'kkkkkkk', 'sahudhasudhasu'))
        return f'{risada} {pessoa}'
    return dando_risada


rindo = faz_me_rir_novamente('Fernanda')

print(rindo())
print(rindo())
print(rindo())
