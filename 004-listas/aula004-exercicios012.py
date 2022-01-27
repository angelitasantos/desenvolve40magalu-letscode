'''
Questão #12
Faça um programa que sorteia 10 números entre 0 e 100 e conte quantos números sorteados são maiores que 50.
Obs.: Precisa usar a biblioteca random
'''

import random 

numeros = list(range(0,101))
numeros_sorteados = random.sample(range(101), 10)

qtde_maior = 50

print(f'Os números sorteados são: {numeros_sorteados}')

# filtro_lista = [elemento for elemento in numeros_sorteados if elemento > qtde_maior]
filtro_lista = [elemento for elemento in numeros_sorteados if elemento > qtde_maior]

print(f'A quantidade de números maiores que {qtde_maior} = ', len(filtro_lista))
print(f'Os números maiores que 50 da lista são: {filtro_lista}')
