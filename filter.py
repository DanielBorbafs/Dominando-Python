"""
Filter
filter() -> Serve para filtrar dados de uma coleção
"""
#Biblioteca para trabalhar com dados estatísticos

import statistics

# Dados ecoletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.3, 4.1, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

print(f'Média: {media}')

# OBS: assim como a função map(), a filter () recebe dois parãmeros, sendo
# Uma função e um iterável

res = filter (lambda valor: valor > media, dados)
print(list(res))

# OBS: assim como na função map(), após serem utilizados os dados de filter() eles são excluidos da memória.

paises = [' ', 'Argentina', ' ', ' Brasil', 'Chile', ' ', 'Colombia', ' ', 'Equador', ' ', ' ', 'Venezuela']

res = filter(None, paises)

print(list(res))

# Diferença entre map e filter é :

# Map recebe dois parâmetros uma função e um iterável
# Filter() => recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de acordo com a função

# EXEMPLO MAIS COMPLEXO

usuarios = [
    {"username": "daniielborba", "tweets": [" Eu amo jogar videogame", " Eu amo escutar musica"]},
    {"username": "caroline", "tweets": [" ", " Eu amo escutar musica"]},
    {"username": "viviane", "tweets": []},
    {"username": "joana", "tweets": ["Gosto de ir na praia ", "Preciso pentear o cabelo "]},
    {"username": "naiane", "tweets": []},
    {"username": "livia", "tweets": ["Não gosto de ir na praia", " "]},

]

print(usuarios)
# Filtrar os usuários que estão inativos no twitter

# FORMA 1
inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
print(inativos)

# FORMA 2
inativos = list(filter(lambda usuario: not usuario ['tweets'], usuarios ))
print(inativos)
