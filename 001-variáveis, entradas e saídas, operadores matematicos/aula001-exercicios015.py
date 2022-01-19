'''
Desafio #2
Faça um programa que informe a data e a hora para o usuário. 
Para isso use a função datetime.now() do módulo datetime.
'''

import datetime

data_e_hora_atuais = datetime.datetime.now()
data_e_hora_pt_BR = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')

print(data_e_hora_atuais)
print(data_e_hora_pt_BR)