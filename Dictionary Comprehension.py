"""DICTIONARY COMPREHENSION

pense no seguinte:

se quisermos criar uma lista fazemos:

lista = [1, 2, 3, 4]

se quisermos criar uma tupla:

tupla = (1, 2, 3, 4)

se quisermos criar um Conjunto

conjunto = {1, 2, 3, 4}

Se quisermos criar um dicionário

dicionario = {'a':1, 'b':2, 'c':3}

# Sintaxe

{chave:valor for valor in iterável}

{valor for valor in iterável}
"""
# Exemplos

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)


numeros = [1, 2, 3, 4, 5]

quadrados = {valor: valor ** 2 for valor in numeros}

print(quadrados)

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range (0, len(chaves))}
print(mistura)

numeros = [1, 2, 3, 4, 5]
res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)

"Set comprehension"

# Exemplos

numeros = {num for num in range(1, 7)}
print(numeros)

# outro exemplo

numeros = { x ** 2 for x in range(10)}
print(numeros)

# Desafio! Faça uma alteração na estrutura acima para gerar um dicionário ao invés de set

numeros = {x ** 2 for x in range(10)}
print(numeros)

# NAO TEM ORDENAÇÃO NEM REPETIÇÃO DE VALORES

letras = {letra for letra in 'Geek University'}
print(letras)