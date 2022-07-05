"""
Ranges são utilizados para gerar sequências numéricas, não de forma aleatória
mas sim de maneira especificada.
"""
# FORMA 1
for num in range(11):
    print(num)

# FORMA 2
for num in range(4, 11):
    print(num)
'Valor de inicio, valor de parada'


# FORMA 3
for num in range(5, 55, 5):  # de 5 a 55 de 5 em 5
    print(num)
'Valor de inicio, valor de parada, passo'

# FORMA 4
for num in range(10,0,-1):'contagem progressiva'

"""
Loop while

forma geral
while expressão_booleana:
    //execução do loop
    
Expressão boleana é toda expressão onde o resultado é verdadeiro ou falso
"""
numero = 1

while numero < 100:
    print(numero)
    numero = numero + 1

# OBS: Em um loop, é importante que cuidamos do criterio de parada.

# Exemplo 2
resposta = ''
while resposta != 'sim':
    resposta = input('Quer namorar comigo?')
# Se nao aceitar o programa vai rodar eternamente até falar sim KKKK

# Saindo de LOOP com Break

" Utiliza-se o break para sair de loops de maneira projetada"

# EXEMPLO1
for numero in range(1, 11):
    if numero == 7:
        break
    else:
        print(numero)

print('Saindo do loop')

# EXEMPLO2
while True:
    comando = input('Digit "sair"" para sair:')
    if comando == 'sair':
        break