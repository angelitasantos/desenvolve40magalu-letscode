'''
Questão #8
Faça um programa que pede para o usuário digitar 5 números e, ao final, imprime uma lista com os 5 
números digitados pelo usuário (sem converter os números para int ou float).
Exemplo: Se o usuário digitar 1, 5, 2, 3, 6, o programa deve imprimir a lista ['1','5','2','3','6']
'''

numero = 5
contador = numero + 1
lista = []

for elemento in range(1, contador):
    lista.append(input(f"Digite o {elemento}° numero: "))

print(f"Sua lista é: {lista}")