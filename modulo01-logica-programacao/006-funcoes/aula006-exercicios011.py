'''
Questão #11
Faça uma função que recebe um número x e uma lista numérica e retorna uma lista cujos 
elementos são os itens da lista de entrada multiplicado por x.
Exemplo:
Se a função receber o número 5 e a lista [3,5,1], então a função deve retornar 
[5x3, 5x5, 5x1] = [15, 25, 5].
'''

def produto_lista(numero, lista1):
    lista2 = []
    lista3 = []
    for elemento in range(len(lista1)):
        produto = lista1[elemento] * numero
        lista2.append(f'{lista1[elemento]} x {numero}')
        lista3.append(produto)
    retornar = print(f'{lista2} = {lista3}')
    return retornar

numero = 5
lista1 = [3, 5, 1]
produto_lista(numero, lista1)