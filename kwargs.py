"""
*Kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras
em uma tupla, o *kwargs exige que utilizemos parâmetros nomeados, e  transforma esses
parâmetros extras em um dicionário.
"""

# Exemplo


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'a cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul')


# Os parametros * args e **kwargs não são obrigatórios

# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Voce recebeu um cumprimento pythoico geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!'"
    return 'Não tenho certeza quem você é..'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='oi'))
print(cumprimento_especial(geek='especial'))


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'julia')
minha_funcao(18, 'felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='não', voce='vai')
minha_funcao(19, 'carla', 9, 4, 3, java=False, python=True)


def mostra_indo( a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_indo(1, 2, 3, sobrenome='university', cargo='instrutor'))


def soma_multiplos_numeros(a, b, c):
    print( a + b + c)


lista = [1, 2, 3]
tupla = [1, 2, 3]
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)


