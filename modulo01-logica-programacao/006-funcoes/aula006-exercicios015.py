'''
Questão #15
Desafio 1 - Faça uma função que receba um número e calcule seu fatorial.
'''

def fatorial(numero):
    fatorial = 1
    contador = 1
    while contador <= numero:
        fatorial *= contador
        contador += 1
    return fatorial

numero = 5
print(f'Fatorial de {numero} é {fatorial(numero)}')
