'''
Questão #9
Faça um programa que peça o dia, o mês e o ano para o usuário 
e imprima a data completa no formato dd/mm/aaaa.
'''

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

data_completa = str(dia) + '/' + str(mes)  + '/' + str(ano)

print('Data completa:',data_completa)