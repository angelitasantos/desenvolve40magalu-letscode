'''
Questão #7
Faça um programa que conte quantas vezes cada elemento aparece em uma lista 
(pode criar uma lista na mão). Esse programa deverá guardar os dados em um 
dicionário no qual as chaves são os elementos da lista e os valores são a 
contagem de quantas vezes esse elemento aparece.
'''


lista = [2, 3, 8, 9, 1, 2, 3, 5, 7, 9, 1, 3, 8, 2]
lista.sort()

dic_repeticao = []
repeticao = 0

for key in range(0, len(lista)-1):
    if (lista[key] == lista[key + 1]):
        repeticao += 1
        
        if key == len(lista)-2:
            print(lista[key], ' - ', repeticao + 1)
        
    else:
        print(lista[key], ' - ', repeticao + 1)
        repeticao = 0

print(dic_repeticao)


'''




lista = [2, 3, 8, 9, 1, 2, 3, 5, 7, 9, 1, 3, 8, 2]
valores = []
repetidos = set()

for elemento in lista:
    if elemento not in valores:
        valores.append(elemento)
        valores.sort()
    else:
        repetidos.add(elemento)


print(f'Valores = {valores}')
print(f'Repetidos = {repetidos}')

'''

'''
lista = [2, 3, 8, 9, 1, 2, 3, 5, 7, 9, 1, 3, 8, 2]
valores = []
quantidade = set()
repetidos = set()

for elemento in lista:
    if elemento not in valores:
        valores.append(elemento)
    else:
        repetidos.add(elemento)

print(f'Valores = {valores}')
print(f'Quantidade = {quantidade}')
print(f'Repetidos = {repetidos}')


for elemento in lista:
    quantidade = lista.count(elemento)
    print(f'{elemento} x {quantidade}')

'''