
# Coletando dados do USUÁRIO

# ESTÀGIO 1 - COLETANDO DADOS
### EXEMPLO ANTIGO DO PYTHON####
print("QUAL É O SEU NOME?")


nome = input() #ENTRADA DE DADOS


# ESTÀGIO 2 - RESPOSTA DO ESTAGIO1


print('Seja bem vindo (a) %s' %nome)


# OUTRO EXEMPLO
print("QUAL SUA IDADE?")
idade = input()


print('O %s tem %s anos' % (nome, idade))

##### MODO 3.X ####

print('Qual seu nome?')
nome = input()

print('Seja bem vindo(a) {0}'.format(nome))

print('Qual sua idade?')
idade = input()

print('O {0} Tem {1} anos'.format(nome, idade))


#### MODO MAIS ATUAL ####


print('Qual seu nome?')
nome = input()

print(f'Seja bem vindo(a){nome}')

print('Qual sua idade?')
idade = input()
print(f'{nome} tem {idade} anos')

print(f'O {nome},nasceu em { 2022 - int (idade) }!')


# TODO DADO RECEBIDO VIA INPUT É DO TIPO STRING - ' ' / " " / '''  '''/ """ """/

