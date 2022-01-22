'''
Questão #1
Faça um programa que peça ao usuário um número e imprima todos os números de um até o número dado.
Exemplo:
digite: 5
imprime: 1 2 3 4 5
'''

numero = int(input('Digite um número: '))
numero_impresso = numero + 1

for contador in range(1, numero_impresso):
    print(contador)