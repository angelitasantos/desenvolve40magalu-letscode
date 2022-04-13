'''
Desafio #3
Um hospital quer fazer o diagnóstico de gripe ou dengue a partir de um questionário de sintomas, tendo as perguntas abaixo, faça um programa que faça o diagnóstico deste hospital:
a. Sente dor no corpo?
b. Você tem febre?
c. Você tem tosse?
d. Está com congestão nasal?
e. Tem manchas pelo corpo?
Para o diagnóstico ele tem a seguinte tabela:
A 	B 	C 	D 	E 	Resultado
Sim 	Sim 	Não 	Não 	Sim 	Dengue
Sim 	Sim 	Sim 	Sim 	Não 	Gripe
Não 	Sim 	Sim 	Sim 	Não 	Gripe
Sim 	Não 	Não 	Não 	Não 	Sem doenças
Não 	Não 	Não 	Não 	Não 	Sem doenças
'''

print('\nPara responder as perguntas abaixo, digite S para sim e N para não\n')
pergunta1 = input('Sente dor no corpo? ')
pergunta2 = input('Você tem febre? ')
pergunta3 = input('Você tem tosse? ')
pergunta4 = input('Está com congestão nasal? ')
pergunta5 = input('Tem manchas pelo corpo? ')

if pergunta1 == "S" and pergunta2 == "S" and pergunta3 == "N" and pergunta4 == "N" and pergunta5 == "S":
    print('Você está com Dengue.')
elif pergunta1 == "S" and pergunta2 == "S" and pergunta3 == "S" and pergunta4 == "S" and pergunta5 == "N":
    print('Você está com Gripe.')
elif pergunta1 == "N" and pergunta2 == "S" and pergunta3 == "S" and pergunta4 == "S" and pergunta5 == "N":
    print('Você está com Gripe.')
elif pergunta1 == "S" and pergunta2 == "N" and pergunta3 == "N" and pergunta4 == "N" and pergunta5 == "N":
    print('Você não está doente.')
elif pergunta1 == "N" and pergunta2 == "N" and pergunta3 == "N" and pergunta4 == "N" and pergunta5 == "N":
    print('Você não está doente.')
else:
    print('Você não está com Dengue ou Gripe. Você tem outra doença.')