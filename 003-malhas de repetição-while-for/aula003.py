# Malhas de repetição

####### WHILE #######

# Pergunte ao usuário a quantidade de provas que ele fez.
# Calcule e exiba sua média aritmética (pode "perder" valores já digitados).

quantidade = int(input('Digite a quantidade de provas: '))
soma = 0

contador = 1
while contador <= quantidade:
    nota = float(input('Digite a sua nota: '))
    soma = soma + nota
    contador = contador + 1
media = soma/quantidade
print(media)



####### FOR #######
'''
Calcule a soma de mil termos dos inversos dos fatoriais: 
1/(1!) + 1/(2!) + 1/(3!) + 1/(4!) + ...
Dica: Assim como no exercício anterior use três variáveis: um contador; uma 
variável para a soma; e uma variável para os termos. Lembre-se de que 
4! = 4*3*2*1 que também é igual a 4*3!.

1/1! + 1/2! + 1/3! + ... = 1.718
'''

soma = 0
fatorial = 1

for i in range(1, 1001):
    fatorial *= i
    soma = soma + (1 / fatorial)

print(soma)