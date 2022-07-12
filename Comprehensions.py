""" LIST COMPREHENSION
# Sintaxe da list comprehension

[ dado for dado in iterável ]
"""

# exemplo

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

"""
para entender melhor oque ta acontecendo:

- a primeira parte: for numero in numeros
- a segunda parte: numero * 10

"""
res = [numero / 2 for numero in numeros]
print(res)


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]
print(res)

#Loop

numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

# LIST COMPREHENSION
print((numero * 2 for numero in [1, 2, 3, 4, 5]))
# REFATORAÇÂO PERFEITA PYTHON AVANÇADO

# OUTROS EXEMPLOS

nome = 'Geek university'
print([letra.upper() for letra in nome])

# 2

amigos = ['maria', 'julia', 'pedro', 'guilherme']
print([amigo[0].upper() for amigo in amigos])


# 3
print([numero * 3 for numero in range(1, 10)])

# 5

print([str(numero) for numero in [1, 2, 3, 4, 5]])

# Qualquer número par módulo de 2 é 0 em python é False.
pares = [numero for numero in numeros if not numero % 2]
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# 2
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)