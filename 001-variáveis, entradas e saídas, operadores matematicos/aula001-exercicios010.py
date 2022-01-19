'''
Questão #10
Faça um programa que peça 2 números inteiros e um número real, calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo.
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.
'''

numero_inteiro_1 = int(input('Digite um numero inteiro: '))
numero_inteiro_2 = int(input('Digite outro numero inteiro: '))
numero_real = float(input('Digite um numero real: '))
     
# o produto do dobro do primeiro com metade do segundo.
resultado_a = (numero_inteiro_1 * 2) * (numero_inteiro_2 / 2)
print('O produto do dobro de', numero_inteiro_1, 'com metade de', numero_inteiro_2, 'é', resultado_a)

# a soma do triplo do primeiro com o terceiro.
resultado_b = (numero_inteiro_1 * 3) + numero_real
print('A soma do triplo de', numero_inteiro_1, '+', numero_real, 'é', resultado_b)

# o terceiro elevado ao cubo.
resultado_c = numero_real ** 3
print(numero_real, 'elevado ao cubo é', resultado_c)