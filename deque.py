"""
O deque é uma lista de alta performance
"""
# import

from collections import deque

# Criando deques

deq = deque('geek')

print(deq)

# adicionando elementos no deque

deq.append('y')
print(deq)

deq.appendleft('k') #adiciona no começo da lista
print(deq)

# removendo elementos

print(deq.pop())
print(deq)

# removendo primeiro elemento

print(deq.popleft())
print(deq)