"""
MAP

"""

import math


def area(r):
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]


areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

areas = map(area, raios)

print(areas)
print(type(areas))

print(list(areas))

print(list(map(lambda r: math.pi * (r ** 2), raios)))


# obs: após utilizar a função map() depois da primeira utilização, ele zera.

# Para fixar -  map

# temos dados iteráveis

# dados: a1, a2, ...., an

# temos um função:

# Função: f(x)

cidades = [('Berlim', 29), ('Cairo', 36), ('londres', 22)]

print(cidades)


# f = 9/5 * c + 32

# Lambda


c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)


print(list(map(c_para_f, cidades)))
