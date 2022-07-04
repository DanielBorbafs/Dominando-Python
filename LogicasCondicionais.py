"""
Estruturas condicionais
if (SE) ,   else(SENAO),  elif(SENAO FAÇA ISSO)
"""

idade = 18
if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('tem 18 anos')
else:
    print('Maior de idade')


"""
Estruturas lógicas AND (e), OR(ou), NOT(não), is(é)

operadores unários
- NOT 

operadores binários
- AND - OR - IS

Para o 'and' ambos os valores precisam ser TRUE
para o 'or' um ou outro valor precisa ser  TRUE
para o 'not', o valor do booleando é invertido, ou seja, se for TRUE, vira False. Vice-Versa

"""
ativo = False
logado = False

if not logado:
    print('Bem vindo Usuário')
else:
    print('Você precisa ativar sua conta, Por favor, cheque seu e-mail')

# no python se torna mais limpa a programação. Mais limpo e simples de ler!
