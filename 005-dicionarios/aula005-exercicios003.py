'''
Questão #3
Crie um dicionário para as seguintes relações:
‘Banana’: 3.0
‘Cebola’: 4.0
‘Maçã’: 5.7
‘Abacaxi’: 8.0
'''

frutas =    {   'Banana': 3.0, 
                'Cebola': 4.0,
                'Maçã': 5.7, 
                'Abacaxi': 8.0
            }

print(frutas)

for fruta in frutas:
    print(f'{fruta} - {frutas[fruta]}')