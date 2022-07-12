"""
Entendendo o "Args

- O "args é um parâmetro como outro qualquer, isso significa que você poderá chamar de qualquer coisa

exemplo:
*xis

mas por convenção decidiram adotar o nome ARGS para defíni-lo

o parametro 'args utilizado em uma função coloca os valores extras informados como entrada em uma tupla.
"""


# Exemplos


def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_todos_numeros(4, 6, 9))


# ENTENDENDO O ARGS

def definindo_args(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total

print(definindo_args())
print(definindo_args(2))
print(definindo_args(3, 5, 6))
print(definindo_args(1, 2, 5))

print(definindo_args(23, 4, 12.5))

# Outro exemplo de utilização do *args


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem vindo Geek'
    return ' Eu não tenho certeza quem é você '


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'university', 3.145))


def soma_numeros(*args):
    return sum(args)

numero = [1, 2, 3, 4, 5, 6, 7]

print(soma_numeros(*numero))
'Desempacotando'


# O * serve para informarmos que estamos passando uma coleção de dados, entao ele precisará desempacotar antes.
