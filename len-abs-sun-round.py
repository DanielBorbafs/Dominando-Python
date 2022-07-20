"""
Len, Abs, Sun, Round

# LEN > Retorna o tamanho (ou seja, o número de itens)  de um iterável.

# ABS > Retorna o valor absoluto de um número, seu valor real.. sem o sinal

# SUN > Recebe como parâmetro um iterável, podendo receber um valor inicial e retorna a soma dos elementos junto com
o valor inicial

# ROUND > Retorna um número arredondado para N digito de precisão após a casa decimal
se a precisão não for informada, retorna o inteiro mais próximo da entrada


"""
print(len('Geek University'))
# Quantas letras tem!

# Por debaixo dos panos, quando utilizamos a função len, o python faz o seguinte:

print('Geek University'.__len__())
# DUNDER LEN

# EXEMPLO ABS ( APENAS NÙMEROS INTEIROS OU REAIS)
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14)) #'3.14'


# EXEMPLOS SUN

print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))


# Exemplos Round

print(round(10.2))
print(round(5.252154, 2)) # Para duas casas decimais após a vírgula
print(round(100.5))
print(round(25.8))
