"""
try / except / else  / finally

dica de quando e onde tratar o código:

TODA ENTRADA DO USUÁRIO DEVE SER TRATADA!

OBS: a função do usuário é destruir seu sistema.
"""
# ELSE > é executado somente se não ocorrer o erro.

try:
    num = int(input('Informe um número:'))
except ValueError:
    print('Valor incorreto, digite um NÚMERO')
else:
    print(f'Você digitou {num}')

# Finally
try:
    num = int(input('informe um número: '))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executando o finally')

# OBS:  O bloco finally é SEMPRE executado, independente da função.

# O finally, é usado para fechar ou desalocar recursos.

# Exemplo mais complexo ERRADO

def dividir(a, b):
    return a / b

num1 = int(input('Informe o primeiro número: '))

try:
    num2 = int(input('informe o segundo número:'))
except ValueError:
    print(' O valor precisa ser numérico')
try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')

print(dividir(num1, num2))

# Exemplo mais complexo CERTO

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:# Except (ValueError, ZeroDivisionError) as err:
        print('Valor incorreto')
    except ZeroDivisionError:
        return 'Não é possivel dividir por zero'


num1= input('informe o primeiro número:')
num2= input('informe o segundo número:')