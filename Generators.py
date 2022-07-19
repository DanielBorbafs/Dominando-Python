"""
Generators
em aulas anteriores nós estudamos:
- list comprehension
- Dictionary comprehension
-set comprehension

Não vimos:
- Tuple comprehension...porque elas se chamam Generators

nomes = ['Carlos', 'Camila', 'Carla','Cassiano']
print(any(nome[0] == 'C' for nome in nomes]))

"""
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano']

print(any ([nome[0] == 'C' for nome in nomes]))

# List comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)



# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)
# Generator ocupa menos espaço em memória.



# Qual é a utilidade de getsizeof() -> retorna a quantidade em bytes de memória
from sys import getsizeof

print(getsizeof('Geek'))

# Mostra quantos bytes a string está ocupando

print(getsizeof('Geek'))
print(getsizeof('University'))
print(getsizeof('9999999'))
print(getsizeof('22'))


# GERANDO UMA LISTA DE números com list comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando lista com dictionary
dic_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando lista com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('para fazer a mesma tarefa gastamos em memória`:')
print(f'List comprehension:{list_comp} bytes')
print(f'Dictionary:{dic_comp} bytes')
print(f'List Generator:{gen}bytes')

# ITERANDO

gen = (x * 10 for x in range (100))
print(gen)
print(type(gen))

for num in gen:
    print(num)