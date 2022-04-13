'''
Questão #4
Faça um programa que imprima a tabuada do 9 (de 9*1 a 9*10) usando loops.
'''

tabuada = int(input('Digite qual a tabuada você deseja que seja impressa: '))
contador = 1

print(f'\nTabuada do {tabuada}')
while contador <= 10:
    resultado = tabuada * contador
    print(f'{tabuada} x {contador} = {resultado}')
    contador = contador + 1

