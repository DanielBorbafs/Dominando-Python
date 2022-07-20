"""
Zip > cria um iterável (zip object) que agrega elementos de cada um dos iteráveis passados como entradas em pares

"""

# Exemplos

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))

# Sempre podemos gerar uma lista, tupla, set ou dicionário

print(list(zip1))

print(tuple(zip1))

print(set(zip1))

print(dict(zip1))

# Se estiver trabalhando com iteráveis de tamanhos diferentes irá parar quando os elementos do menor iterável acabar


# Exemplo

list3 = ['Daniielborba', 'Enailaborba', 'SofiaBorba']
list4 = ['db1578', 'naila1578', 'sofi1578'] # se colocar mais um elemento aqui, será ignorado pois na lista anterior possui só 3


zip2 = zip(list3, list4)

print(zip2)

print(list(zip2))

# Podemos utilizar diferentes iteráveis com zip

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 13, 'c': 15, 'd': 25, 'e': 30}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

dados = [(0, 1), (1, 2), (2, 3), (3, 4)]
print(list(zip(*dados)))
# Lista de tuplas

# Exemplo mais complexo
prova1 = [80, 91, 70]
prova2 = [98, 89, 50]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]:max(dado[1], dado[2]) for dado in zip(alunos,prova1,prova2)}

print(final)

# utilizando o map()

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))