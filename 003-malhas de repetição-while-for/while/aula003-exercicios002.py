'''
Questão #2
Peça ao usuário para digitar um número e imprima o fatorial de n.
'''

# n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1

numero = int(input("Digite o número que você deseja saber o seu fatorial: ") )

fatorial = 1
contador = 1

while contador <= numero:
    fatorial *= contador
    contador += 1

print(f'Fatorial de {numero} é {fatorial}')