'''
Questão #9
Faça uma função que recebe uma lista de palavras e retorna uma lista contendo as mesmas 
palavras da lista anterior, porém escritas em caixa alta.
'''


def palavras(lista):
    lista_upper = []
    for itens in lista:
        lista_upper.append(itens.upper())
    return lista_upper

lista = ['abacaxi', 'maça', 'laranja', 'uva', 'banana']
print(palavras(lista))

