'''
Questão #8
Faça um programa que peça a temperatura em graus Fahrenheit (F), 
transforme e mostre a temperatura em graus Celsius (°C).

°C = (5 * (F-32) / 9)
°F = C * 1.8 + 32

Obs: Tente também fazer um programa que faça o inverso: peça a 
temperatura em graus Celsius e a transforme em graus Fahrenheit.
'''

# Transformar Fahrenheit em Celsius
fahrenheit = float(input('Digite a temperatura em graus Fahrenheit: '))
celsius = (5 * (fahrenheit - 32) / 9)

print(fahrenheit, 'graus Fahrenheit equivale a', celsius, 'graus Celsius')



# Transformar Celsius em Fahrenheit
celsius = float(input('Digite a temperatura em graus Celsius: '))
fahrenheit = celsius * 1.8 + 32

print(celsius, 'graus Celsius equivale a', fahrenheit, 'graus Fahrenheit')

