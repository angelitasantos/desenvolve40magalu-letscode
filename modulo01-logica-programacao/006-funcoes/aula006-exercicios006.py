'''
Questão #6
Faça uma função que recebe um número e retorna True se ele é par ou False, se ele é ímpar.
'''

def funcao(numero):
    if numero % 2 == 0:
        resultado = True
    else:
        resultado = False
    return resultado

numero = 4
print(f'O número {numero} é PAR? {funcao(numero)}')

numero = 9
print(f'O número {numero} é PAR? {funcao(numero)}')