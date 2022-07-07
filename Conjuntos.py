"""
Conjuntos

- Conjuntos = Referência a teoria dos conjuntos da matemática
- aqui no python chamamos de sets
Regras:
- sets (conjuntos) não possuem valores duplicados:
- sets (conjuntos) não possuem valores ordenados:
- Elementos não são acessados via índice, ou  seja, conjuntos não são indexados;

Os conjuntos são referenciados com chaves {}

Diferença de conjuntos e mapas:
- Um dicionário tem chave/valor;
- Conjunto possui apenas valor;
"""
# EXEMPLO DE CONJUNTO
# Forma 1

s = set({1, 2, 3, 4, 5, 6, 7, 2}) # Não vai printar o 2 pois está repetido.
print(s)
print(type(s))
# Quando criar um conjunto. caso seja adicionado um valor ja existente, o mesmo será ignorado sem gerar erro

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# Também não temos ordem...
lista = [99, 1, 2, 5, 4, 8, 9, 100, 9, 5]
print(f'Lista {lista}com {len(lista)} elementos')

tupla = (99, 1, 2, 5, 4, 8, 9, 100, 9, 5)
print(f'tupla {tupla}com {len(tupla)} elementos')

dicionario = (lista, 'dict')
print(f'Dicionário:{dicionario}com {len(dicionario)} elementos')

conjunto = {99, 1, 2, 5, 4, 8, 9, 100, 9, 5}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')
# Contando elementos do conjunto


s = {1, 'b', True, 34.22, 44}
# Podemos misturar todos os valores dentro dos conjuntos

# usos interessantes com sets
"Formulário de cadastro de visitantes, e os visitantes informam manualmente a cidade de onde vieram"
# Nós adicionamos cada cidade em uma lista python.

cidades = ['Belo horizonte', 'Rio de Janeiro', 'São Paulo', 'Rio de Janeiro', 'São Paulo']
print(cidades)
print(len(cidades))

# quantas cidades únicas temos? oque fazer?
print(len(set(cidades)))

# Adicionando elementos em um conjunto

adicionando = {1, 2, 3}
adicionando.add(4)
adicionando.add(4)
print(adicionando)
# ADICIONAR ITEM DUPLICADO, NÃO DA ERRO.. SÒ IGNORA

adicionando.remove(3)
print(adicionando)
# Removendo item forma 1

adicionando.discard(2)
print(adicionando) # FORMA 2

# Copiando um conjunto para outro
adicionando = s.copy()
print(adicionando)
adicionando.add(4)
print(adicionando)
print(s)

# Removendo todos os itens de um conjunto
s.clear()
print(s)

# Método matemático

estudantejava = { 'julia', 'lais', 'laila', 'iara'}
estudantepython = {'julia', 'laila', 'joyce', 'bia'}
# Veja que alguns alunos  que estudam python também estudam java

# Como gerar um conjunto com nome de estudante únicos

# Forma1 - Utilizando union

unicos1 = estudantepython.union(estudantejava)
print(unicos1)

# Utilizando o Caractere pipe '|'
unicos2 = estudantepython | estudantejava
print(unicos2),


# Gerando quem estuda em ambos cursos

#  Utilizando intersection
ambos1 = estudantepython.intersection(estudantejava)
print(ambos1)


# Em cursos separados

python = estudantepython.difference(estudantejava)
print(python)