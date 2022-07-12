"""
- Funções são pequenos trechos de códigos que realizam tarefas especificas
- pode ou não receber entrada de dados e retornar saida de dados.
- Muito uteis para executar procedimentos similares por repetidas vezes
OBS: Se escrevermos uma função que realiza várias tarefas dentro dela:
é bom fazer uma verificação para que a função seja simplificada
"""

# Exemplo de utilização de funções:

cores = ['verde', 'amarelo', 'azul', 'branco']  # lista

# Utilizando a função integrada (bult-in) do python print()

print(cores)

curso = 'programação em python'  # string

print(curso)

cores.append('roxo')

print(cores)

# alguns parametros tipo append só podem ser chamados se estivermos trabalhando com dados do tipo lista

"""Em python a forma geral de definir uma função é 
def nome_da_funcao(parametros_de_entrada):
    bloco_da_função
    
onde:

nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome completo, separado por underlline(snake case):
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula. Podendo ser opcionais ou não:
bloco da funcao_ -> também chamado de corpo da função ou implementação, é onde o processamento da função acontece.

OBS: para definir uma função, utilizamos a palavra reservada 'def' informando ao python
que estamos definindo uma função, também abrimos o bloco de código com o já conhecido dois pontos:


"""


# Definindo a primeira função

def diz_oi():
    print('Olá!')


# UTILIZANDO ELA / chamando ela
diz_oi()
# Sempre colocar os parenteses sem espaço

def cantar_parabens():
    print('parabens para voce')
    print('nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')

cantar_parabens()

# for n in range(2):
 #   cantar_parabens()

 # em python, podemos inclusive criar variáveis do tipo função e executar esta função através da variável

canta = cantar_parabens
canta()


" FUNÇÕES DE RETORNO "

# EXEMPLO

def quadrado_de_7():
   return 7 * 7

quadrado_de_7()

ret = quadrado_de_7()


print(f'retorno{ret}')

print(f'retorno:{quadrado_de_7() + 1}')

" FUNÇÕES EM PYTHON QUE RETORNAM VALORES, DEVEM RETORNAR ESSES VALORES COM A PALAVRA RETURN "

# Refatorando novamente:

def diz_oii():
    return 'OI!'

print(diz_oi())

alguem = 'Pedro'

print(diz_oii() + alguem)

# Torna o código mais eficaz buscando o return na função e traz mais flexibilidade

'OBS: SOBRE RETURN'
' Ela finaliza a função'
' Podemos ter em uma função diferentes returns:'
' Podemos em uma função, retornar qualquer tipo de dados e ate mesmo multiplos valores'

# EXEMPLO 1:

def diz_olá():
    return 'Olá'
    print('AQUI NUNCA VAI EXECUTAR PORQUE O RETURN FINALIZA O BLOCO')

print(diz_olá())

# EXEMPLO 2:

def nova_funcao():
    variavel = None
    if variavel:
      return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())

# Exemplo 3:

def outra_funcao():
    return 2, 3, 4, 5

print(outra_funcao())
print(type(outra_funcao))

# VAMOS CRIAR UMA FUNÇÂO PARA JOGAR A MOEDA

from random import random

def joga_moeda():
    # Gera um numero pseudo randomico entre 0 e 1
    if random() > 0.5:
        return 'cara'
    return 'coroa'

print(joga_moeda())

def quadrado(numero):
    return numero * numero

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)


# REFATORANDO PARABENS PARA VOCÊ

def cantar_parabens(aniversariante):
    print('Parabens para você')
    print('Nesta data querida')
    print('muitas felicidades')
    print('Muitos anos de vida')

cantar_parabens('PATRICIAAAAAAAAAAAAA')

def soma(a, b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outa(num1, b, msg):
    return (num1 + b) * msg
print(soma(2, 5))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outa(3, 2, 'Geek '))

# Se a gente informar um numero errado de parametro ou argumento, teremos typerrors


def nome_completo(string1, string2):
    return f' Seu nome completo é {string1} {string2}'

print(nome_completo('Angelina','Jolie'))

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
           total = total + num
        return total

lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

"""
Funções com parâmetro ( DEFAULT PARAMETER)

- funçoes onde a passagem de parametro seja opcional:

#Exemplo de função onde a passagem de parametro seja opcional
print('Geek University')
print()
"""

def exponencial(numero, potencia):
    return numero ** potencia

print(exponencial(2, 3))
print (exponencial(3, 2))

# OS PARAMETROS COM VALORES DEFAULT DEVEM ESTAR SEMPRE NO FINAL


def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek'
    elif nome == 'Geek':
        return ' Eu pensei que você era o instrutor'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor = True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stephany'))


# Exemplos

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtraco(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtraco))

# Escopo - evitar problemas e confusoes

# variaveis globais
# variaveis locais

total = 0

def incrementa():
   #total = total + 1 # A VARIAVEL LOCAL ESTA SENDO UTILIZADA PARA PROCESSAMENTO SEM TER SIDO INICIALIZADA
    return total

print(incrementa())

total = 0

def incrementa():
    global total

    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())

def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

