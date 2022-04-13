'''
Questão #2
Faça uma função que recebe o valor do raio de um círculo e retorna o valor do 
comprimento de sua circunferência: C = 2*pi*r. 
'''


def comprimento(raio):
    pi = 3.1415
    circunferência = 2 * pi * raio
    return circunferência

raio = 2
print(comprimento(raio))
