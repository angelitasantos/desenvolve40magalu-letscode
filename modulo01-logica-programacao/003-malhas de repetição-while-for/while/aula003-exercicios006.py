'''
Questão #6
Faça um programa que sorteia um número N e peça para o usuário adivinhar o número sorteado. 
A cada resposta errada, o seu programa deve imprimir um aviso dizendo que a resposta está 
errada e pedir novamente uma resposta ao usuário.
Para a realização desse exercício, utilize alguma função da biblioteca random (e.g. randint()).
'''

import random 

numero_sorteado = random.randint(1,10)

palpite = 0 
tentativas = 0

while palpite != numero_sorteado:
    tentativas = tentativas + 1
    palpite = int(input('Digite um número de 1 a 10 ou digite "99" para desistir: '))
    if palpite == numero_sorteado:
        print('Parabéns! O número sorteado foi:', numero_sorteado)
        print('O número de tentativas foi: ', tentativas)
    elif palpite == 99: 
        desistencia = tentativas - 1
        print(f'Você desistiu após {desistencia} tentativas. Que pena!')
        break
    else:
        print('Você errou! Tente novamente!')


