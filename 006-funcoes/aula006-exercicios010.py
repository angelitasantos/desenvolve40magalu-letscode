'''
Questão #10
Faça uma função que recebe duas listas e retorna a soma item a item dessas listas.
Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve retornar 
[1+3, 4+5, 3+1] = [4, 9, 4].

'''

def soma_lista(lista1, lista2):
    lista3 = []
    lista4 = []
    if len(lista1) != len(lista2):
        print("As listas tem tamanhos diferentes! Não é possível fazer a soma entre elas.")
    for elemento in range(len(lista1)):
        soma = lista1[elemento] + lista2[elemento]
        lista3.append(f'{lista1[elemento]} + {lista2[elemento]}')
        lista4.append(soma)
    retornar = print(f'{lista3} = {lista4}')
    return retornar

lista1 = [1, 4, 3]
lista2 = [3, 5, 1]
soma_lista(lista1, lista2)
