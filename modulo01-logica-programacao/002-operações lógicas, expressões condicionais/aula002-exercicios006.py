'''
Questão #6
Vamos fazer um programa para verificar quem é o assassino de um crime. 
Para descobrir o assassino, a polícia faz um pequeno questionário com 
5 perguntas onde a resposta só pode ser sim ou não:
a. Mora perto da vítima?
b. Já trabalhou com a vítima?
c. Telefonou para a vítima?
d. Esteve no local do crime?
e. Devia para a vítima?
Cada resposta sim dá um ponto para o suspeito. A polícia considera que 
os suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices 
e 2 pontos são apenas suspeitos, necessitando outras investigações. 
Valores iguais ou abaixo de 1 são liberados.
'''
print('\nPara responder as perguntas abaixo, digite S para sim e N para não\n')
pergunta1 = input('Mora perto da vítima?').lower()
pergunta2 = input('Já trabalhou com a vítima?').lower()
pergunta3 = input('Telefonou para a vítima?').lower()
pergunta4 = input('Esteve no local do crime?').lower()
pergunta5 = input('Devia para a vítima?').lower()

resposta_positiva = 0

if pergunta1 == "S" or pergunta1 == "s":
    resposta_positiva = resposta_positiva + 1
if pergunta2 == "S" or pergunta2 == "s":
    resposta_positiva = resposta_positiva + 1
if pergunta3 == "S" or pergunta3 == "s":
    resposta_positiva = resposta_positiva + 1
if pergunta4 == "S" or pergunta4 == "s":
    resposta_positiva = resposta_positiva + 1
if pergunta5 == "S" or pergunta5 == "s":
    resposta_positiva = resposta_positiva + 1

print(resposta_positiva)

if resposta_positiva == 5:
    print("Suspeito é assassino.")
elif resposta_positiva == 3 or resposta_positiva == 4:
    print("Suspeito é cumplice")
elif resposta_positiva == 2:
    print("Suspeito é apenas um suspeito")
else:
    print("Suspeito liberado")





