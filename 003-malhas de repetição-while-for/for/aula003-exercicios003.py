'''
Questão #3
Peça ao usuário para digitar um número N e some todos os números de 1 a N utilizando o laço de repetição while.
'''

numero = int(input("Digite o número: "))
numero_somado = numero + 1

soma = 0

for contador in range(numero_somado):
    soma += contador

print(f'A soma de 1 a {numero} é {soma}')