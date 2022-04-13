'''
Questão #1
Faça um programa que peça ao usuário um número e imprima todos os números de um até o número dado.
Exemplo:
digite: 5
imprime: 1 2 3 4 5
'''

contador = 1
numero = int(input('Digite um número: '))

while contador <= numero:
    print(contador)
    contador = contador + 1