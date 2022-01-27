'''
Questão #7
Faça uma função que sorteia 10 números aleatórios entre 0 e 100 e retorna o maior entre eles.
'''

from random import randint

def maior_valor():
    valores_sorteados = []
    for elemento in range(10):
        sorteio = randint(0, 101)
        valores_sorteados.append(sorteio)
    maior = max(valores_sorteados)
    print(valores_sorteados)
    return maior

print(f'O maior valor sorteado foi: {maior_valor()}')