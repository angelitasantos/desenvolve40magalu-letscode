'''
Questão #13
Faça uma função que recebe uma lista de números e retorna a soma dos elementos dessa lista.
'''

def soma_lista(lista):
    soma = sum(lista)
    return soma

lista = [1, 4, 3]
print(f'A soma dos elementos da lista {lista} é {soma_lista(lista)}')