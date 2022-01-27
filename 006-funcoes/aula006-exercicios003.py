'''
Questão #3
Faça uma função para cada operação matemática básica (soma, subtração, multiplicação e 
divisão). As funções devem receber dois números e retornar o resultado da operação.
'''


def soma(numero1, numero2):
    resultado = numero1 + numero2 
    return resultado

def subtracao(numero1, numero2):
    resultado = numero1 - numero2     
    return resultado

def multiplicacao(numero1, numero2):
    resultado = numero1 * numero2     
    return resultado

def divisao(numero1, numero2):
    resultado = numero1 / numero2     
    return resultado


numero1 = 5
numero2 = 3

print('soma = ', soma(numero1, numero2))
print('subtração = ', subtracao(numero1, numero2))
print('multiplicação = ', multiplicacao(numero1, numero2))
print('divisão = ', divisao(numero1, numero2))