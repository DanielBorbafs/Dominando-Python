""" DICIONÀRIOS PODEM SER CONHECIDOS COMO 'MAPAS'

São Coleções de tipo chave/Valor
Dicionários são representados por chaves {}

OBS: Sobre dicionários
    'CHAVE E VALOR SÃO SEPARADOS POR DOIS PONTOS 'CHAVE':'VALOR'
 tanto chave quanto valor podem ser de qualquer tipo e valor
 podemos misturar tipos de dados;


"""
paises = {'br': 'Brasil', 'eua': 'Estados Unidos'}
print(paises)
print(type(paises))

# acessando elementos
# Forma 1 - Acessando via/chave
'Dicionarios nao são indexados'

print(paises['br'])
print(paises['eua'])
# CASO UTILIZAMOS UM ACESSO A CHAVE QUE NÃO EXISTE TEREMOS UM ERRO


# Forma 2 - acessando via GET - RECOMENDADO

print(paises.get('br'))
print(paises.get('py'))
# APARECE NONE
# PODEMOS USAR NONE QUANDO QUEREMOS UTILIZAR UMA VÀRIAVEL VAZIA, E DEPOIS USA-LA

russia = paises.get('eua','não encontrado') # Modelo 1
print(f'Encontrei o pais {russia}')
if russia:
    print('Encontrei o pais') #Modelo 2 Desconsiderar no contexto atual
else:
    print('Não encontrei o pais')

localidades = {
    (35.6895, 39.6917): 'Escritório em londres',
    (38.9875,  35.6578): 'Escritório em nova york',
}
print(localidades)

# adicionar elementos em um dicionário
receita = {'jan':100,'fev':500}

receita ['abr'] = 350

print(receita)

# Atualizando dados em um dicionário

# Forma 1
receita['abr'] = 400
print(receita)
# NÃAO podemos ter chaves repetidas!!

# REMOVER DADOS DE UM DICIONÀRIO

# forma 1 MAIS COMUM
ret = receita.pop('abr')
print(ret)
print(receita)
# RET - RETORNA O VALOR
# SEMPRE INFORMAR A CHAVE


# Forma 2
del receita['fev']
print(receita)
# Se a chave não existir será gerado um keyerror
# Nesse caso o valor removido não é retornado

carrinho = []
produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2000.00}
produto2 = {'nome': 'Playstatation 3', 'quantidade': 3, 'preco': 1000.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)


# Métodos de dicionários.
d = dict(a=1, b=2, c=3)
print(d)

# limpar dados
# d.clear()
# print(d)

# copiando dicionário para outro DEEP COPY
novo = d.copy()
print(d)
print(novo)
novo['d'] = 5
print(novo)


