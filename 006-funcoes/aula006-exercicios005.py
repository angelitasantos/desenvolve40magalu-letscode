'''
Questão #5
Faça uma função que recebe um nome e um horário e imprime “Bom dia, [nome]”, caso seja antes de 
12h, “Boa Tarde, [nome]”, caso seja entre 12h e 18h e “Boa noite, [nome]” se for após às 18h.
'''
from time import strftime, localtime

hoje = strftime('%d/%m/%Y')
horaAtual = strftime('%H:%M:%S', localtime())

print(f'Hoje é dia {hoje}')
print(f'Agora são {horaAtual}')

def saudacao(nome, horario):
    if horario >= '05:00' and horario <= '12:00':
        print(f'Bom dia, {nome}!')
    elif horario > '12:00' and horario <= '18:00':
        print(f'Boa tarde, {nome}!')
    else:
        print(f'Boa noite, {nome}!')

nome = 'Maria'
horario = horaAtual
saudacao(nome, horario)
