'''
Questão #7
Faça um programa que peça para o usuário digitar a idade, o salário e o sexo de uma 
pessoa até que as entradas digitadas sejam válidas.
a. Idade: entre 0 e 150;
b. Salário: maior que 0;
c. Sexo: M, F ou Outro.
'''

idade = int(input('Digite a sua idade: '))

while idade < 0 or idade > 150:
    print('ERRO! A idade digitada está fora do intervalo entre 0 e 150. Digite outro valor.')
    idade = int(input('Digite a sua idade: '))
print('Informações de idade Ok!')


salario = float(input('Digite o seu salário: '))

while salario < 0:
    salario = float(input('Digite o seu salário: '))
    print('ERRO! O salário digitado é menor que 0. Digite outro valor.')
print('Informações de salário Ok!')


sexo = input('Qual é o seu sexo? Digite: M para Masculino, F para Feminino ou O para Outro ')

while sexo != 'M' and sexo != 'F' and sexo != 'O':
    print('ERRO! O sexo digitado está errado.')
    sexo = input('Qual é o seu sexo? Digite: M para Masculino, F para Feminino ou O para Outro ')

print('Informações de sexo Ok!')
