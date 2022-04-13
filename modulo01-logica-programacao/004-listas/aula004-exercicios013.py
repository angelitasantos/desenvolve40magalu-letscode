'''
Questão #13
Faça um programa que sorteie 10 números entre 0 e 100 e imprima:
a. o maior número sorteado;
b. o menor número sorteado;
c. a média dos números sorteados;
d. a soma dos números sorteados.
Obs.: Precisa usar a biblioteca random
'''

import random

qtde_numeros = 10

numeros = list(range(0,101))
numeros_sorteados = random.sample(range(101), qtde_numeros)

print(f'Os números sorteados são: {numeros_sorteados}')
print(f'O maior número sorteado é: {max(numeros_sorteados)}')
print(f'O menor número sorteado é: {min(numeros_sorteados)}')
print(f'A média dos números sorteados é: {sum(numeros_sorteados) / qtde_numeros}')
print(f'A soma dos números sorteados é: {sum(numeros_sorteados)}')

