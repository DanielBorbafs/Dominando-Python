"""
Min e max retorna o menor ou o maior valor de um iterável


"""

# Exemplos
lista = [1, 2, 8, 12, 55, 100, 129]
print(max(lista))

conjunto = [1, 2, 8, 12, 55, 100, 129]
print(max(conjunto))

tupla = [1, 2, 8, 12, 55, 100, 129]
print(max(tupla))

dicionario = {'a': 1, 'b' : 2,'c': 8,'d': 12,'e': 55,'f': 100, 'g': 129}
print(max(dicionario.values()))

# RECEBER DOIS VALORES DO USUÀRIO E MOSTRAR O MAIOR

val1 = int(input('Informe o primeiro valor:'))
val2 = int(input('Informe o primeiro valor:'))

print(max(val1, val2))

print(max('a', 'b', 'abc', 'abcdef'))


"""
Min() > retorna o menor valor em um iterável  ou o menor de dois ou mais elementos
"""

lista = [1, 2, 8, 12, 55, 100, 129]
print(min(lista))

conjunto = [1, 2, 8, 12, 55, 100, 129]
print(min(conjunto))

tupla = [1, 2, 8, 12, 55, 100, 129]
print(min(tupla))

dicionario = {'a': 1, 'b' : 2,'c': 8,'d': 12,'e': 55,'f': 100, 'g': 129}
print(min(dicionario.values()))

print(min('DanielBorba'))

# OUTROS EXEMPLOS

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(max(nomes)) # TIM

print(min(nomes))   # ARYA

# USANDO A LAMBDA PARA ORDENAR POR TAMANHO DE NOME.
print(max(nomes, key=lambda nome: len(nome))) # OLLIVANDER
print(min(nomes, key=lambda nome: len(nome))) # TIM



musicas = [
    {"título": "Corte americano", "tocou": 3},
    {"título": "Mitsubishi", "tocou": 25},
    {"título": "Iphone Branco", "tocou": 50}

]

# Imprimindo qual música mais tocou

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# IMPRIMINDO SOMENTE O Título da música
print(min(musicas, key=lambda musica: musica['tocou'])['título'])
print(max(musicas, key=lambda musica: musica['tocou'])['título'])

# Desafio! como encontrar a musica mais tocada sem usar lambda

max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']
for musica in musicas:
    if musica['tocou'] == max:
        print(musica['título'])


min = 9999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']
for musica in musicas:
    if musica['tocou'] == min:
        print(musica['título'])


