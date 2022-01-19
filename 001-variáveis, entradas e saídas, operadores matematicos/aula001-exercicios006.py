'''
Questão #6
Faça um programa que peça o raio de um círculo, calcule e mostre sua área.
Obs: Fórmula da área de um círculo: A = 3,14*(r**2), onde r é o raio.
'''

raio = float(input('Digite o raio do círculo: '))
pi = 3.14

area_circulo = pi * (raio ** 2)

print('A área do círculo é', area_circulo)