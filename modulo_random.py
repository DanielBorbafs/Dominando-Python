"""
Módulo random e oque são módulos?

- Em python, módulos nada mais são doque outros arquivos python.

módulo random -> Possui várias funções para geração de números pseudo-aleatórios

"""
# OBS: existem duas fromas de se utilizar um módulo ou função deste

# Forma 1 - importando todo módulo ( não recomendado)

import random

# ao realizar o import de todo o módulo, todas as funções atributos, classes e propriedades dentro do módulo
# ficarão disponíveis. (ficarão em memória). o ideal é puxar só as funções que precisa.
print(random.random())
# Nome do pacote depois o nome da função, separados por ponto .. RANDOM.RANDOM

# Forma 2 - IMportando uma função especifica do módulo


from random import random #forma recomendada


# No import acima, estamos falando: do Módulo random, importe a função random

for i in range(10):
    print(random())


'Gerar valores maiores'
# uniform() -> Gerar um número aleatório entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7)) # o 7 não é incluido

'Gerar valores inteiros'
# randint() -> gera valores pseudo-aleatórios entre os valores estabelecidos.
from random import randint
# Gerador de apostas para mega-sena

for i in range(6):
    print(randint(1, 61))

# choice() -> mostra um valor aleatório entre um iterável

from random import choice
jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))

# shuffle() -> tem a função embaralhar dados
from random import shuffle

cartas = ['K', 'Q', 'J', '5', '4']

print(cartas)

shuffle(cartas)

print(cartas)
