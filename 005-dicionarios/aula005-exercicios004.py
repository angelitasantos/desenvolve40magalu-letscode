'''
Questão #4
Altere o valor da chave ‘Maçã’ no dicionário do exercício anterior para 8.6.
'''

frutas =    {   'Banana': 3.0, 
                'Cebola': 4.0,
                'Maça': 5.7, 
                'Abacaxi': 8.0
            }

print(frutas)

if 'Maçã' in frutas:
    frutas['Maçã'] = 8.3
else:
    frutas.update({'Maçã':8.6})

print(frutas)