

# TIPO NUMERO EM PYTHON

num = 100
print(num)

num += 1
print(num)

num /= 2
print(num)

type(num)
# Informa a classe do número EX; INTEIRA, FLOAT ETC...

# TIPO FLOAT - TIPO REAL E DECIMAL / CASAS DECIMAIS

# sempre usar '.' para números decimais
valor = 1.44
print(valor)
print((type(valor)))
# Explicando tipo

# Dupla atribuição:
valor1, valor2 = 10, 44
print(valor1)
print((type(valor1)))
print(valor2)
print((type(valor2)))

# Conversão de FLOAT PARA INT ( PERDEMOS A PRECISÃO)
res = int(valor)
print(res)
print((type(res)))

# Para trabalhar com números Complexos usamos a letra (j)
variavel = 5j
print(variavel)
print((type(variavel)))

# ALGEBRA BOOLEANA
"""
2 constantes, Verdadeiro OU Falso
True -> Verdadeiro
Falso - Falso

OBS: SEMPRE COM A INICIAL MINÚSCULA

ERRADO:
true, false
CERTO
True, false

"""
ativo = False
print(ativo)

# NEGAÇÃO
print(not ativo)

logado = True

# OU (or):
"""
é uma operação binária, ou seja, depende de dois valores, Ou um ou outro devem ser verdadeiros.
"""

print(ativo or logado)

# E (and)
"""
Também é uma opção binária, depende de dois valores
e ambos devem ser verdadeiros
"""

# TIPO STRING

nome = 'Daniel Borba'
print(nome)
print(type(nome))

# Se possuir uma aspas na nossa "Palavra"
nome = "Bob's lanches"
print(nome)
print(type(nome))

# PULAR LINHA com \n
nome = 'Daniel\nBorba'
print(nome)
print(type(nome))
print(nome.split()) # .split transforma em uma lista


print('Digite seu nome')
nick = input()
print(nome.split()) # .split transforma em uma lista

print('Digite seu nome completo')
completo = input()
print(completo[0:30]) # SLICE DE STRING - Puxa desde o caractere inicial até o final que decidimos

print(nome[:: -1]) # invertendo caracteres

print(nome.replace('a', 'b'))
#onde tem letra A colocar Letra B

#ESCOPO DE VARIÁVEIS
"""
Dois casos de escopo:

1- Variaveis globais;
    São reconhecidas, ou seja, seu escopo compreende todo o programa!

2- Variaveis Locais;
    São reconhecidas apenas no bloco onde foram declaradas

como declarar variável em python:
nome da variável = valor da váriavel!
ao declararmos uma variável nós nao colocamos o tipo de dado dela 
pois python é uma linguagem de tipagem dinâmica;
Esse tipo é inferido ao atribuirmos o valor á mesma:
"""
numero = 42
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))


numero = 110
if numero > 10:
    novo = numero + 10 # A VARIÁVEL 'NOVO' ESTÁ DECLARADA LOCALMENTE NO BLOCO DO if.
    print(novo)
