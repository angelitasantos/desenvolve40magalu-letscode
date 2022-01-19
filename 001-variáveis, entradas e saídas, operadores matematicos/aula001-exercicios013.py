'''
Questão #13
Faça um programa que peça um valor monetário e diminua-o em 15%. 
Seu programa deve imprimir a mensagem “O novo valor é [valor]”.
'''

valor = float(input('Digite um valor monetário: '))
desconto = 15 / 100

valor_liquido = valor * (1 - desconto)

print('O novo valor é R$', valor_liquido)