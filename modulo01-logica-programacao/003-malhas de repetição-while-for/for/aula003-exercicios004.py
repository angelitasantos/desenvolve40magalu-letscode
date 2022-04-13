'''
Questão #4
Faça um programa que imprima a tabuada do 9 (de 9*1 a 9*10) usando loops.
'''

tabuada = int(input('Digite qual a tabuada você deseja que seja impressa: '))
ultimo_numero = 10 + 1

print(f'\nTabuada do {tabuada}')
for contador in range(ultimo_numero):
    resultado = tabuada * contador
    print(f'{tabuada} x {contador} = {resultado}')