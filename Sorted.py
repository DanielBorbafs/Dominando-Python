"""
SORTED

obs: Não confunda, apesar do nome, com a função sort() que já estudamos em listas. 0 sort()
só funciona em listas.

podemos utilizar o sorted() com qualquer iterável.

 O sorted sempre retorna uma lista com os elementos do iterável ordenados

"""

# EXEMPLO

numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros)) # Ordernar do menor para o maior

print(numeros)

# ADICIONANDO  parametros ao sorted()

print(sorted(numeros, reverse=True))  # ordena do maior para o menor

# podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "daniielborba", "tweets": [" Eu amo jogar videogame", " Eu amo escutar musica"]},
    {"username": "caroline", "tweets": [" ", " Eu amo escutar musica"]},
    {"username": "viviane", "tweets": []},
    {"username": "joana", "tweets": ["Gosto de ir na praia ", "Preciso pentear o cabelo "]},
    {"username": "naiane", "tweets": []},
    {"username": "livia", "tweets": ["Não gosto de ir na praia", " "]},

]

print(usuarios)

print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# OUTRO EXEMPLO

musicas = [
    {"titulo": "Thunterstruck", "tocou": 30},
    {"titulo": "Corte americano", "tocou": 352},
    {"titulo": "Mitsubishi", "tocou": 85},
]

# Ordena da menos tocaeda para a mais tocada
print(sorted(musicas, key=lambda musica:musica['tocou']))


# Ordena da mais tocada para menos tocada
print(sorted(musicas, key=lambda musica:musica['tocou'], reverse=True))