'''
Questão #5
Agora usando a função max() faça um programa que imprima os três maiores números de uma lista.
Dica: Use o método próprio de listas .remove().
'''

lista = [8, 83, 12, 57, 21, 95, 10, 78]
lista_inicial = [8, 83, 12, 57, 21, 95, 10, 78]
maiores_numeros = []

for elemento in range(3):
    maiores_numeros.append(max(lista))
    lista.remove(max(lista))

print('Os três maiores números da lista', lista_inicial , 'são:' ,maiores_numeros)

