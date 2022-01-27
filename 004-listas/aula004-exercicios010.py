'''
Questão #10
Faça um programa que peça as 4 notas bimestrais e mostre a média aritmética delas, usando listas. 
'''

notas = 4
contador = notas + 1
lista = []

for elemento in range(1, contador):
    lista.append(float(input(f"Digite a {elemento}° nota: ")))

media = sum(lista) / notas

print(f"Suas notas são: {lista} e sua média é: {media}")