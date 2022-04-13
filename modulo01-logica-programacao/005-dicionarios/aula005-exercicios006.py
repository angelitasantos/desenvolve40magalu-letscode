'''
Questão #6
Como você armazenaria a seguinte tabela usando apenas dicionários? Tente imprimir o valor 
correspondente da linha Pedro x Coluna B.
	Coluna A 	Coluna B
Maria 	1 		5
Pedro 	0.5 	3
João 	3.2 	1
'''

dicionarios = 	{	'Maria': [1, 5],
					'Pedro': [0.5, 3],
					'João': [3.2, 1],
				}

print('Pedro x Coluna B = ',dicionarios['Pedro'][1])
