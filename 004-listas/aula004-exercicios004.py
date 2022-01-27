'''
Questão #4
Faça um programa que olhe todos os itens de uma lista e diga quantos deles são pares.
'''

lista = [11, 22, 33, 44, 55, 66, 77, 88, 99]
soma = 0

for elemento in range(len(lista)):
    if lista[elemento] % 2 == 0:
        soma += 1

print('A lista', lista , 'possui', soma ,'numeros pares.')
