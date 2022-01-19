'''
Questão #11
Faça um programa que peça o peso e altura de uma pessoa e calcule seu IMC (Índice de Massa Corporal).
Obs: IMC = Peso/Altura**2
'''

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

IMC = peso / altura ** 2

print('O seu Índice de Massa Corporal é', IMC, 'kg/m2')