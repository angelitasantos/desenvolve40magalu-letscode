'''
Questão #12
Faça uma função que receba duas listas e retorne o produto item a item dessas listas.
Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve retornar 
[1x3, 4x5, 3x1] = [3, 20, 3].
'''

def produto_lista(lista1, lista2):
    lista3 = []
    lista4 = []
    if len(lista1) != len(lista2):
        print("As listas tem tamanhos diferentes! Não é possível fazer a multiplicação entre seus valores.")
    for elemento in range(len(lista1)):
        produto = lista1[elemento] * lista2[elemento]
        lista3.append(f'{lista1[elemento]} x {lista2[elemento]}')
        lista4.append(produto)
    retornar = print(f'{lista3} = {lista4}')
    return retornar

lista1 = [1, 4, 3]
lista2 = [3, 5, 1]
produto_lista(lista1, lista2)