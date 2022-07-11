""" Named tuple"""
"""
#tupla
tupla = (1, 2, 3)

print(tupla[1])
# Named tuple -> são tupla, diferenciadas onde especificamos um nome para mesma e também parametros
"""
#import

from collections import namedtuple

# precisamos definir o nome e parâmetros.

# forma 1 - declaração named tupla

cachorro = namedtuple('cachorro', 'idade raca nome')

# forma 2 = Declaração Named tuple

cachorro = namedtuple('Cachorro', 'idade, raca, nome')

# forma 3 = namedtuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

ray = cachorro(idade=2, raca='Chow-Chow', nome='ray')

print(ray)

print(ray[2])
# ACESSANDO PELO INDICE
print(ray.nome)
# ACESSANDO PELO INDICE

print(ray.index('ray'))
# demonstrando onde está o índice
