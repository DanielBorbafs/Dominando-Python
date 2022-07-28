"""
*** Orientação a Objetos ***
PRODUTO
nome                    notebook
preço   > Classe        R$ 2.300,00 > Objetos
desconto                15%

- Classe -> modelo de objeto do mundo r eal sendo representado computacionalmente
- Atributo -> Característica do Objeto
- Método -> Comportamento do objeto(funções)
- Construtor -> Método especial utilizado para criar os objetos:
- Objeto -> Instância de classe.

"""

numero = 10

print(numero)
print(type(numero))


nome = 'Geek'
print(nome)
print(type(nome))


class Produto:
    pass


ps4 = Produto()
print(ps4)
print(type(ps4))



"""

CLASSES

EM POO Classes são modelos dos objetos do mundo real sendo representados computacionalmente

imagine que você queira fazer um sistema para automatizar 
o controle das lâmpadas da sua casa

Classes podem conter:
    - Atributos > Repesentam as características do objeto, ou seja, pelos atributos
    conseguimos representar computacionalmente os estados de um objeto. No caso da Lâmpada
    iriamos querer saber se a lâmpada é 110 ou 220 volts, se ela é branca, rosa ou outra cor
    Luminosidade ETC.
    
    - Métodos (funções) > Representam os comportamentos do objeto, ou seja, o objeto pode realizar no seu sistema,
    no caso da lâmpada por exemplo, um comportamento comum que muito provavelmente iriamos querer
    representar no nosso sistema é o de ligar e desligar a mesma.
    


Em Python, para definir uma classe utilizamos a palavra reservada class.



OBS: utilizamos a palavra 'Pass' em Python quando temos um bloco de código que ainda não está implementado.

OBS: quando nomeamos nossas classes em Python, utilizamos por convenção o nome com inicial em Maiúsculo,
se o nome for composto, utiliza-se as iniciais de ambas as palavras em maíusculo, todas juntas

Obs: quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos estes objetos 
que serão mapeados para classes de entidade.

"""

idade = 32 # INT


preco = 2200.20 #FLOAT


nome = 'Daniel' #STRING


class Lampada:
    pass


class Contacorrente:
    pass


class Usuario:
    pass


valor = int('42')


lamp = Lampada()


print(type(lamp))
