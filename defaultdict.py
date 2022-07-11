""" Default dict


Default Dict => ao criar um dicionário utilizando-o, nós informamos um valor default;
podendo utilizar um lambda para isso. este valor será utilizado semrpe que não houver
um valor definido. caso tentamos acessar uma chave que não existe, essa chave será
criado e o valor default será atribuido
"""

# Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)
# Lambda são funções sem nome que podem ou não receber parâmetros de entradas.

print(dicionario)

dicionario['curso'] = 'Programação em Python: Essencial'


"""
Ordered dict

'GARANTE A ORDEM DE INSERÇÃO'
"""

from collections import OrderedDict
dicionario = OrderedDict({'a': 1, 'b':2, 'c': 3 })

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

# diferença entre DICT e Ordered Dict
odict1 = OrderedDict({'a': 1, 'b': 2, 'c': 3})
odcit2 = OrderedDict({'a': 1, 'c': 3, 'b': 2})

# A ordem importa logo, apesar das letras receberem  o mesmo valor. no final o dicionário é diferente.