'''
Questão #6
Faça um programa que imprima o maior número de uma lista, sem usar a função max().
'''

lista = [78, 53, 83, 12, 21, 10, 93, 8]

maior_numero = lista[0]

for elemento in lista:
    if elemento > maior_numero:
        maior_numero = elemento

print('O maior número da lista', lista ,'é' ,maior_numero)
print(max(lista))