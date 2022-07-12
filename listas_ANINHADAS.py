"""
       Listas aninhadas

 Listas =+- Arrays
Em Python nós temos as listas

numeros = [1, 'b', 3.234, True, 5]

"""

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3

print(listas)

print(type(listas))

print(listas[0][1]) # 2
print(listas[2][1]) # 8

for lista in listas:
    for num in lista:
        print(num)


# exemplos
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

print([['*' for i in range(1, 4) for j in range (1, 4)]])