"""
Utilizando Lambdas

conhecidas por expressoes lambddas, são funções sem nome, ou seja funções anônimas:

# Função Python

def soma(a, b):
    return a + b


"""


def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))


# Expressão lambda ( começa com a palava lambda no inicio)
lambda x: 3 * x + 1



# Como usar essa expressão


calc = lambda x: 3 * x + 1
print(calc(4))
print(calc(7))

# Podemos ter expressões lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome

print(nome_completo('angelina', 'JOLIE'))

# EM FUNÇÃO PYTHON PODEMOS TER NENHUM OU VÀRIAS ENTRADAS. EM LAMBDAS TAMBÈM


amar = lambda: 'Como não amar python'

uma = lambda x: 3 * x +1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z )

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

#OBS: se passarmos mais argumentos do que parametros esperados teremos TYPE ERROR


# OUTRO EXEMPLO

nomes = ['caua' , 'daniel', 'joao', 'wanner', 'dyeni', 'iara']

print(nomes)

nomes.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(nomes)


#  Função quadratica
#f(x) = a * x ** 2 + b * x + c

def geradora_funcao_quadratiica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratiica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratiica(3, 0, 1)(2))
