# operações lógicas e expressões condicionais

####### OPERAÇÕES LOGICAS #######

'''
Maior que: >
Maior ou igual: >=
Menor que: <
Menor ou igual: <=
Igual: ==
Diferente: !=
'''

maior_que = 5 > 2
print(maior_que)

maior_ou_igual = 5 >= 4
print(maior_ou_igual)

menor_que = 2 < 5
print(menor_que)

menor_ou_igual = 4 <= 5
print(menor_ou_igual)

igual = 5 == 5
print(igual)

diferente = 5 != 3
print(diferente)



# Conjunções lógicas

## exemplo 1
media_nota = float(input('Digite a média do aluno: '))
presenca = int(input('Digite as presenças do aluno: '))

aprovado = media_nota >= 6.0 and presenca >= 9
print(aprovado)


## exemplo 2
dia_final = int(input('Digite o dia do mês para encerrar a promoção: '))
dia_atual = int(input('Digite o dia do mês atual: '))
estoque = int(input('Digite a quantidade de itens no estoque: '))

acabou = dia_atual > dia_final or estoque == 0
print(acabou)



####################################################################################
####### EXPRESSÕES CONDICIONAIS #######

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

media = (nota1 + nota2) / 2



# if
if media >= 6.0:
    print('Aprovado')
print('Média: ', media)



# else
if media >= 6.0:
    print('Aprovado')
else:
    print('Reprovado')

print('Média: ', media)



# Aninhando condições
if media >= 6.0:
    print('Aprovado')
else:
    if media >= 3.0:
        print('Recuperação')
    else:
        print('Reprovado')

print('Média: ', media)



## elif
if media >= 6.0:
    print('Aprovado')
elif media >= 3.0:
    print('Recuperação')
else:
    print('Reprovado')

print('Média: ', media)