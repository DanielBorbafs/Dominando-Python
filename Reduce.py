"""
Reduce

Temos que importar a função do módulo ' Functools '
99% das vezes usar o loop for é bem melhor doque o reduce.

A função Reduce(), cunciona da seguinte forma:
    passo 1: res1 = f(a1, a2) # APlica a função nos dois primeiros elementos da coleção e guarda o resultado
    passo2 = f(res1, a3) # Aplica a função passando o resultado do passo1 mais o terceiro elemento e guarda o res.

    isso é repetido até o final.
    Passo 3: res= f(res2, a 4)

ou seja em cada passo ele aplica uma função passando primeiro argumento  o resultado da aplicação  anterior,
no final reduce() iár retornar o resutado final.

alternativamente, poderiamos ver a função reduce()  como:

funcao(funcao(funcao(a1, a2, a3), a4), ...), an)
"""
# Como funciona na prática?

# Vamos utilizar a função reduce() para multiplicar todos os números de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar o reduce() nós precisamos de uma função em que receba dois parâmetros

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)


# Utilizando um loop normal
res = 1
for n in dados:
    res = res * n
print(res)
