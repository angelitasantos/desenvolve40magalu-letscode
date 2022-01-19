'''
Questão #3
Faça um programa que peça dois números e mostre o maior deles.
'''

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))

if numero1 > numero2:
    print(numero1, 'é o maior número entre os dois números digitados')
else:
    print(numero2, 'é o maior número entre os dois números digitados')