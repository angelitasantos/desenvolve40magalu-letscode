'''
Questão #11
Crie uma lista de 10 números e imprima:
a. uma lista com os 4 primeiros números;
b. uma lista com os 5 últimos números;
c. uma lista contendo apenas os elementos das posições pares;
d. uma lista contendo apenas os elementos das posições ímpares;
e. a lista inversa da lista sorteada (isto é, uma lista que começa com o último elemento 
da lista sorteada e termina com o primeiro);
f. uma lista inversa dos 5 primeiros números;
g. uma lista inversa dos 5 últimos números.
'''

lista = [21, 12, 78, 8, 2, 93, 13, 9, 53, 72]
print(f'A lista é: {lista}')

print(f'Os 4 primeiros números da lista são: {lista[:4]}')
print(f'Os 5 últimos números da lista são: {lista[5:]}')

# posições pares e ímpares da lista
posicao_par = []
posicao_impar = []

for elemento in range(len(lista)):
    if elemento % 2 == 0:
        posicao_par.append(lista[elemento])
    else:
        posicao_impar.append(lista[elemento])
    
print(f'As posições pares da lista são: {posicao_par}')
print(f'As posições ímpares da lista são: {posicao_impar}')

print(f'A lista inversa da lista sorteada é: {sorted(lista, reverse=True)}')

print(f'A lista inversa dos 5 primeiros números é: {sorted(lista[:5], reverse=True)}')
print(f'A lista inversa dos 5 últimos números é: {sorted(lista[5:], reverse=True)}')

