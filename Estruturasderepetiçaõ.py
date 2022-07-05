"""
Loop for

Loop - > Estrutura de repetição
For - > Uma dessas estruturas

UTILIZAMOS LOOPS PARA ITERAR SOBRE SEQUENCIAS OU SOBRE VALORES ITERAVEIS:

EXEMPLOS DE ITERÁVEIS:
- STRING
    NOME = DANIEL BORBA
- lISTA
    LISTA = [ 1, 3, 5, 7, 9]
- RANGE
    NUMEROS = RANGE(1, 10)
"""

nome = 'Daniel Borba'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)


# exemplo de for 1 ( sobre string)
for letra in nome:
    print(letra)


# exemplo de for 2 (sobre lista)
for numero in lista:
    print(numero)


# exemplo de for 3 (iterando sobre um range)
for numero in range(1,10):
    print(numero)
'O VALOR VAI ATÈ O PENÚLTIMO DADO DA RANGE'


# Descobrindo o índice
for indice, letra in enumerate(nome):
    print(nome[indice])


'Mostra o indice e a letra, se quisermos só a letra faremos a operação abaixo:'
for  letra in enumerate(nome):
    print(letra)

nome1 = 'Iara teixeira'
for valor in enumerate(nome1):
    print(valor)


# COLETANDO DADOS E RODANDO LOOP 1
qtd = int(input('Quantas vezes esse loop deve rodar?'))
for n in range (1, qtd+1):
    print(f'imprimindo{n}')


# COLETANDO DADOS E RODANDO LOOP 2

qtd2 = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0
for n in range(1, qtd2+1):
    num = int(input(f'Infome o {n}/{qtd} valor:'))
    soma = soma + num
print(f'A soma é {soma}') # Somando os loops


# Como não pular linha
nome = 'Daniel Borba'
print(nome, end= '')


'EMOJI NO TERMINAL'
emoji = 'U0001F680'
for num in range(1,11):
    print('\U0001F680' * num)



