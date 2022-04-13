'''
Questão #7
Faça um programa que pergunte quanto você ganha por hora e o número de 
horas trabalhadas no mês e depois, calcule e mostre o total do seu 
salário no referido mês.
'''

valor_hora = float(input('Quanto você ganha por hora? '))
horas_trabalhadas = int(input('Quantas horas você trabalhou no mês? '))

salario_mensal = valor_hora * horas_trabalhadas

print('O seu salário desse mês é de: R$', salario_mensal)