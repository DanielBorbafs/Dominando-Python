"""
Leitura de arquivos

para ler o conteúdo de um arquivo em python, utilizamos a função integradad open()
que literalmente significa 'abrir'

open() -> na forma mais simples, passamos apenas um parâmetro de entrada
que nesse caso é o nome do arquivo a ser lido. Essa função retorna um
_io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions_html/open

# Por padrão a função open() abre o arquivo para leitura. este arquivo deve existir
ou então teremos o erro FileNotFoundError


mode r - > Modo de leitora .r -> read() -> ler

"""

# exemplo

arquivo = open('texto.txt', 'r', encoding='utf-8')

# print(arquivo)

# print(type(arquivo))

# Para ler um conteúdo de um arquivo, após sua abertura, devemos utilizar a função read()
ret = arquivo.read()
print(type(ret))
print(ret)

print(arquivo.read())

# OBS: a função read() lê todo conteúdo do arquivo.

