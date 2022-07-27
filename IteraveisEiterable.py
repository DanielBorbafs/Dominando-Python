"""
ENTENDENDO ITERATORS E ITERABLES

iterator ->

    - objeto que pode ser iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada.

iterable ->
    - Um objeto que irá retornar um iterator quando a função iter() for chamada.

"""

nome = 'Geek'
numeros = [1, 2, 3, 4, 5, 6]
# Transformando em iterable
it1 = iter(nome)
it2 = iter(numeros)
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

# REFATORANDO

nome = 'Geek'

for letra in nome:
    print(f'{letra}')

# Criando versão de LOOP

for num in [1, 2, 3, 4, 5]:
    print(num)

print('\n')

for letra in 'Daniel Borba':
    print(letra)

def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


numero = range(20)

meu_for(numero)
