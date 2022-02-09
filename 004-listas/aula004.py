lista = ["abacaxi", "laranja", "banana", "abacate", "maça", "uva"]

for elemento in lista:
    print(elemento)


lista = [1,2,3,4,5,6]

for indice in range(6):
    print(lista[indice])


# Notas
notas = []
qtde = int(input())

for contador in range(qtde):
    nota = float(input())
    notas.append(nota)

soma = 0
for nota in notas:
    soma = soma + nota

media = soma/len/(notas)

maior = max(notas)
menor = min(notas)

print(media)
print(maior)
print(menor)


# estruturas de dados
lista = [3.14, 2.7, 10, 'olá', True, 'mundo']
#indices: 0,    1,   2,   3,    4,     5

print(2.7 in lista)
print('abacate' in lista)


print(lista[4])


for indice in range(6):
    print(lista[indice])
    lista[indice] = 10

print(lista)

for elemento in lista:
    print(elemento)
    elemento = 10


# Sobre loop para percorre listas
notas = []
quantidade = int(input('Digite a quantidade de provas: '))

# esse loop NÃO É para percorrer lista!
# esse loop é para repetir operações (leitura de nota)
for contador in range(quantidade):
    nota = float(input('Digite a sua nota: '))
    notas.append(nota)

# o próximo loop VAI percorrer a lista:
soma = 0
for n in notas:
    soma = soma + n
media = soma/len(notas)
# media = soma/quantidade

maior = max(notas)
menor = min(notas)

print('Sua média foi:', media)
print('Maior nota:', maior)
print('Menor nota:', menor)

#################################
# outras observações:

notas.append(10) # insere o valor 10 no final da lista
notas.remove(5)  # remove o valor 5 da lista

notas.insert(7, 10) # insere o valor 10 na posição 7
notas.pop(5)        # remove o elemento que estiver na posição 5

if 10 in notas:
    print('existe nota 10')