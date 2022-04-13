'''
Questão #4
Faça um programa que leia a validade das informações:
a. Idade: entre 0 e 150;
b. Salário: maior que 0;
c. Sexo: M, F ou Outro;
O programa deve imprimir uma mensagem de erro para cada informação inválida.
'''

idade = int(input('Digite a sua idade: '))
salario = float(input('Digite o seu salário: '))
sexo = input('Qual é o seu sexo? Digite: M para Masculino, F para Feminino ou O para Outro ')

if idade < 0 or idade > 150:
    print('ERRO! A idade digitada está fora do intervalo entre 0 e 150. Digite outro valor.')

if salario < 0:
    print('ERRO! O salário digitado é menor que 0. Digite outro valor.')

if sexo != 'M' and sexo != 'F' and sexo != 'O':
    print('ERRO! O sexo digitado está errado. Digite: M para Masculino, F para Feminino ou O para Outro')