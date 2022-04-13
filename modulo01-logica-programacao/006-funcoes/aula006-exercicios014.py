'''
Questão #14
Faça uma função que recebe uma lista de números e retorna a média aritmética dos elementos dessa lista.
'''

def media_lista(lista):
    media = sum(lista) / len(lista)
    return media

lista = [5, 4, 9]
print(f'A média dos elementos da lista {lista} é {media_lista(lista)}')