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

numero = range(20)

meu_for(numero)

print('\n')


# Escrevendo um iterador Customizado

for n in range(2, 11):
    print(n)
print('\n')


# SELF SEMPRE APARECE QUANDO UMA FUNÇÃO ESTÁ DENTRO DE UMA CLASSE
class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration


con = Contador(2, 10)

it = iter(con)

print(next(it))
print(next(it))
print(next(it))
print(next(it))

# Refatorar
for n in Contador(2, 10):
    print(f'{n}')
