'''
Questão #12
Faça um programa que peça um valor monetário e aumente-o em 15%. 
Seu programa deve imprimir a mensagem “O novo valor é [valor]”.
'''

valor = float(input('Digite um valor monetário: '))
acrescimo = 15 / 100

valor_acrescido = valor * (1 + acrescimo)

print('O novo valor é R$', valor_acrescido)