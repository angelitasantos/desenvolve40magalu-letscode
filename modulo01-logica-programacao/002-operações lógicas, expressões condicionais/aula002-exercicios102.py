'''
Desafio #1
Faça um programa que leia 3 números e informe o maior deles.
'''

numero1 = float(input('Qual o primeiro número? '))
numero2 = float(input('Qual o segundo número? '))
numero3 = float(input('Qual o terceiro número? '))

if numero1 > numero2 and numero1 > numero3:
    print(numero1, 'é o maior número entre os números digitados')
elif numero2 > numero3:
    print(numero2, 'é o maior número entre os números digitados')
else:
    print(numero3, 'é o maior número entre os números digitados')