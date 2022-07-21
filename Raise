
para simplificar, pense no raise como sendo útil para que possamos criar nossas
próprias exceções e mensagens de erro

a forma geral de utilização é:

raise TIPOERRO('MENSAGEM DE ERRO')

"""

# EXEMPLO REAL

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa de uma string')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Geek', 'branca')
