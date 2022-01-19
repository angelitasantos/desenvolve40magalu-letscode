'''
Desafio #1
Peça para o usuário digitar uma velocidade inicial (em m/s), uma posição 
inicial (em m) e um instante de tempo (em s) e imprima a posição de um 
projétil nesse instante de tempo.

Use a fórmula matemática:
y(t) = y(0) + v(0)*t + (g*(t**2)/2)

Onde, g é a aceleração da gravidade (-10m/s²), y(t) é a posição final, y(0) é a 
posição inicial, v(0) é a velocidade inicial e t é o instante de tempo.
'''

velocidade_inicial = int(input('Digite a velocidade inicial (em m/s): '))
posicao_inicial = int(input('Digite a posição inicial (em m): '))
tempo = int(input('Digite o instante de tempo (em s): '))
aceleracao_gravidade = -10 # m/s²

posicao_final = posicao_inicial + velocidade_inicial * tempo + (aceleracao_gravidade * (tempo ** 2) / 2)

print(posicao_final, 'm')
