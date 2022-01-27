'''
Questão #8
Faça uma função que recebe um número n de entrada, sorteia n números aleatórios entre 0 e 100 
e retorna a média deles.
'''


from random import randint

def media(qtde_numeros):
    valores_sorteados = []
    for elemento in range((qtde_numeros)):
        sorteio = randint(0, 101)
        valores_sorteados.append(sorteio)
    media = sum(valores_sorteados) / qtde_numeros
    print(valores_sorteados)
    return media

qtde_numeros = int(input('Digite quantos números devem ser sorteados: '))
print(f'O média dos valores sorteados é: {media(qtde_numeros)}')