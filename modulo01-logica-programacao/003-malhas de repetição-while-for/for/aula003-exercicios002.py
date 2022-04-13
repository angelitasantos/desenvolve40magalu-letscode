'''
Questão #2
Peça ao usuário para digitar um número e imprima o fatorial de n.
'''

# n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1


numero = int(input("Digite o número que você deseja saber o seu fatorial: ") )
numero_fatorial = numero + 1
fatorial = 1

for contador in range(1, numero_fatorial):
    fatorial *= contador
    
print(f'Fatorial de {numero} é {fatorial}')