"""
LISTAS
Listas em Python são dinamicas podendo armazenar qualquer tipo de dado.

Dinâmico : Não possui tamanho fixo: ou seja, podemos criar a lista
e simplesmente ir adicionando elementos.

As listas são representadas por COLCHETES: []
"""

# MEGA IMPORTANTE

lista1 = [1, 5, 9, 7, 8, 5, 8, 10]

lista2 = ['G', 'g', 'p', 's', 'e', 'i', 'l', 'g', 'e']

lista3 = []

lista4 = list(range(11))

lista5 = list('GgApseil')

# Checagem de dados na lista
num = 18
if num in lista4:
   print(f'Encontrei o numero {num}')
else:
   print(f'Não encontrei o número {num}')

# Ordenagem da lista
lista1.sort()
print(lista1)

lista5.sort()
print(lista5)

# Contar o número de ocorrencias de um valor em uma lista
print(lista1.count(1))
print(lista2.count('e'))


# Adicionar elementos em listas
'''Para adicionar elementos em listas utilizamos a função append'''

print(lista1)
lista1.append(42) # com append conseguimos adicionar apenas 1 elemento por vez
print(lista1)

lista1.append([8, 5, 2])
print(lista1)

if [8, 5, 2] in lista1:
    print('encontrei a lista')
else:
    print('não encontrei a lista')

# forma para colocar mais de um item sem os '[]'

lista1.extend([123, 44, 67])
print(lista1)

# Inserido um elemento na posição que queremos na lista
# O Valor anterior da posição, é deslocado para direita
lista1.insert(2, 'Aqui')
print(lista1)

# juntando duas listas
lista6 = lista1 + lista2
print(lista6)

# inversão de listas
lista1.reverse()
lista6.reverse()

# Copiar uma lista
lista7 = lista2.copy()

# Contagem de elementos na lista
print(len(lista2))

# Removendo o ultimo elemento de uma lista
print(lista6)
lista6.pop()
print(lista6)

# Removendo elemento por indice
print(lista6)
lista6.pop(2)
print(lista6)

# Removendo todos elementos
print(lista6)
lista6.clear()
print(lista6)

# Repetindo elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Converter string para lista(separa por espaço)

nome = 'Daniel dos santos Borba'
print(nome)
nome = nome.split()
print(nome)

#  OUTRO EXEMPLO
nome = 'Daniel,dos,santos,Borba'
print(nome)
nome = nome.split(',')
print(nome)

# convertendo lista em string
nome = ' '.join(nome) # pega o nome e coloca um espaço e transforma em string
print(nome)

# Iterando sobre listas
# exemplo 1
soma = 0
for elemento in lista6:
    print(elemento)
    soma = soma + elemento
print(soma)

# Utilizando WHILE - Exemplo 2

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair'para sair")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
for produto in carrinho:
    print(produto)

# fazemos acesso aos elementos de forma indexada

#            0      1              2         3
cores = ['verde', 'amarelo', 'vermelho', 'branco']
print(cores[1])
print(cores[-1]) # BRANCO - reverte como se fosse um círculo

indice = 0
while indice < len(cores): # len = tamanho - nesse caso 4
    print(cores[indice])
    indice = indice + 1

# Gerando indices em for
for indice,cor in enumerate(cores):
    print(indice, cor)

# Buscando indice de um elemento em uma lista
lista20 = [5, 6, 7, 8, 9, 10, 15, 8, 20]
lista20.reverse()
print(lista20)
# em qual indice está o número 8
print(lista20.index(8))

"Caso tenha dois números iguais ele irá puxar o primeiro da lista"

# Fazendo buscas dentro de um range
print(lista20.index(5, 1)) #  Busca a partir do indice 1

# invertendo valores em uma lista

# Soma, valor máximo e valor minimo = somente se forem valores inteiros

lista50 = [ 1, 2, 3, 4, 5, 6]
print(sum(lista50)) # Soma
print(max(lista50)) # valor máximo
print(min(lista50)) # Valor minimo
print(len(lista50)) # Tamanho da lista