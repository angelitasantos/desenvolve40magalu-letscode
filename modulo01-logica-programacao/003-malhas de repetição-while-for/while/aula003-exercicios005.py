'''
Questão #5
Faça um programa, usando loops, que peça para um usuário digitar um número e 
que só finaliza quando o usuário digitar 0. Ao final imprima a soma de todos os números digitados.
'''


numero = int(input('Digite um número ou digite "0" para finalizar: '))
soma = 0

while numero != 0:
    print('Número armazenado. Digite outro número')
    soma = soma + numero
    numero = int(input("Digite um inteiro ou 0 para terminar: "))

print(f'A soma dos números digitados é {soma}')