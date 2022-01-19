'''
Questão #3
Faça um programa que peça um número para o usuário (string), 
converta-o para float e depois imprima-o na tela. 
Você consegue fazer a mesma coisa, porém convertendo para int?
'''

numero_string = input('Digite um numero: ')
print('O tipo inicial do número', numero_string ,'é', type(numero_string))

numero_float = float(numero_string)
print('Agora o tipo do número', numero_float ,'mudou para', type(numero_float))

numero_int = int(numero_float)
print('Agora o tipo do número', numero_int ,'mudou para', type(numero_int))
