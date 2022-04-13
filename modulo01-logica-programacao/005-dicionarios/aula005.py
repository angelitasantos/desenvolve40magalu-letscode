turma = {'Código':839, 'Linguagem':'Python', 'Matriculados':25, 
'Empresa':'Magazine Luiza', 'Professores':['Rafael', 'Matheus']}

print(turma['Linguagem'])
print(turma['Empresa'])


turma['Módulo'] = 1

print(turma)

for chave in turma:
    print(chave, '-', turma[chave])

if 'Empresa' in turma:
    print('A nossa empresa é:', turma['Empresa'])
else:
    turma['Empresa'] = 'Novíssima Empresa S/A'

print(turma)

# lista de todas as chaves:
chaves = list(turma.keys())
print(chaves)
valores = list(turma.values())
print(valores)

for professor in turma['Professores']:
    print('Prof.', professor)



#################
from dataclasses import dataclass
d = {}
dados = {}

for chave in range (len(d)):
    produto = d[chave]['id']
    categoria = d[chave]['categoria']
    produtos ={'produtos':produto,'categoria': categoria }
    dados.append(produtos)

print(d)
print(dados)



#################
pessoas = [{'nome': 'ana', 'cpf': '1000', 'endereco': 'rua xxxx'},
           {'nome': 'carlos', 'cpf': '8770', 'endereco': 'Rua aaaa'},
           {'nome': 'maria', 'cpf': '7770', 'endereco': 'Rua bbbb'}]

nome = 'maria'
cpf = '1000'

for elemento in pessoas:
    if nome == elemento['nome']:
        print(elemento)

frutas = {'pera': 10, 'uva': 2, 'maça': 55}

print(frutas.items())



#################
compras = []
frutas = {
            'pera': 50, 
            'uva': 2, 
            'maçã':55, 
            'abacaxi': 25
            }
compras.append(frutas)
legumes = {
            'cenoura': 3,
            'tomate': 5,
            'alface': 2
            }
compras.append(legumes)

for compra in compras:
    for k, v in compra.items():
        print(k +": " +str(v))

print(compras)

pera: 50
uva: 2
maçã: 55
abacaxi: 25
cenoura: 3
tomate: 5
alface: 2



frutas = {
            'pera': [50, 10, 20],
            'uva':  [2, 1], 
            'maçã': [55, 10, 15],
            'abacaxi': [25, 8],
            }

for fruta, qtds in frutas.items():
    print(fruta +": ")
    for qtd in qtds:
        print("= " + str(qtd))



compras = {
            'frutas_joao': {
            'pera': 50, 
            'uva': 2, 
            'maçã':55, 
            'abacaxi': 25,
            },
           'frutas_maria': {
            'pera': 40, 
            'uva': 3, 
            'maçã':35, 
            'abacaxi': 15,
            },}
for tipo, tipo2 in compras.items():
    print('\nTipo do item: '+ tipo)
    tudo_qtd = 'pera: '+str(tipo2['pera']) + " "
    tudo_qtd += 'uva: '+str(tipo2['uva']) + " "
    tudo_qtd += 'maçã: '+str(tipo2['maçã']) + " "
    tudo_qtd += 'abacaxi: '+str(tipo2['abacaxi'])
    
    print('Quantidade de itens comprados: '+tudo_qtd.title())
'''
Tipo do item: frutas_joao
Quantidade de itens comprados: Pera: 50 Uva: 2 Maçã: 55 Abacaxi: 25

Tipo do item: frutas_maria
Quantidade de itens comprados: Pera: 40 Uva: 3 Maçã: 35 Abacaxi: 15
'''