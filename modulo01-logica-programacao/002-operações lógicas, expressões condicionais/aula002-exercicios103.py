'''
Desafio #2
Faça o mesmo programa do exercício anterior, porém com 4 números.
'''

numero1 = float(input('Qual o primeiro número? '))
numero2 = float(input('Qual o segundo número? '))
numero3 = float(input('Qual o terceiro número? '))
numero4 = float(input('Qual o quarto número? '))

if numero1 > numero2 and numero1 > numero3 and numero1 > numero4:
    print(numero1, 'é o maior número entre os números digitados')
elif numero2 > numero3 and numero2 > numero4:
    print(numero2, 'é o maior número entre os números digitados')
elif numero3 > numero4:
    print(numero3, 'é o maior número entre os números digitados')
else:
    print(numero4, 'é o maior número entre os números digitados')