"""
ANY E ALL

all() -> retorna true se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio

"""

# Exemplo all()

print(all([ 1, 2, 3, 4])) #  Todos os números são verdadeiros ? TRUE
print(all([0, 1, 2, 3, 4])) #  Todos os números são verdadeiros ? FALSE


nomes = ['Carlos', 'Camila', 'Carla']
print(all([nome[0] == 'C' for nome in nomes ])) # TRUE


nomes = ['Carlos', 'Camila', 'Carla', 'Daniel']
print(all([nome[0] == 'C' for nome in nomes ])) # FALSE



# OBS: um iterável vazio convertido em boolean é False, mas o ALL() entende como true
print(all([letra for letra in 'eio' if letra in 'aeiou']))

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))


"""
 ANY() = RETORNA TRUE SE  QUALQUER ELEMENTO DO ITERÀVEL FOR VERDADEIRO, se o iterável estiver vazio, retorna False
"""

print(any([0, 1, 2, 3, 4])) # TRUE

print(any([0, False, {}, (), []])) # FALSE