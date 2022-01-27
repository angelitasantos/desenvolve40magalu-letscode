'''
Questão #9
Pegue a lista gerada no exercício anterior e transforme cada um dos itens dessa lista em um float.
OBS: Não é para alterar o programa anterior, mas sim a lista gerada por ele.
'''

numero = 5
contador = numero + 1
lista = []

for elemento in range(1, contador):
    lista.append(input(f"Digite o {elemento}° numero: "))

lista_float = []

for elemento in lista:
    lista_float.append(float(elemento))
    
print(f"Sua lista é: {lista_float}")