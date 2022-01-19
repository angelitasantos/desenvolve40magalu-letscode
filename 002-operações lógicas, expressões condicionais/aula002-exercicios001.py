'''
Questão #1
Faça um programa que peça a idade do usuário e imprima se ele é maior ou menor de 18 anos.
'''

idade = int(input('Digite a sua idade: '))

if idade > 18:
    print('Você é maior de 18 anos')
elif idade < 18:
    print('Você é menor de 18 anos')
else:
    print('Você tem 18 anos')
