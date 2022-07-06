"""
tuplas(tuple)

tuplas é parecido com listas. existem duas diferença:
-tuplas são representadas por parenteses
-As tuplas são imutáveis, ela não sofre alterações
"""
print(type(()))

#ATENÇÃO - TUPLA SÃO REPRESENTADAS POR (), MAS ATENÇÃO:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))
'è a mesma coisa'


# Tuplas com 1 elemento
tupla3 = (4)
'Não EXISTE'

tupla4 = (4,) # ISSO È UMA TUPLA
print(type(tupla4))
" Podemos concluir que as tuplas são formadas por vírgulas e nao parenteses"

# TUPLA COM RANGE
tupla5 = tuple(range(11))
print(tupla5)
print(type(tupla5))

# TRABALHAR COM TUPLA TRÀS MAIS SEGURANÇA PARA O CÒDIGO POIS SÂO IMÙTAVEIS
