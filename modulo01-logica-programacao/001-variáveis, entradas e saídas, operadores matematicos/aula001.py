# variáveis, entradas e saídas, operadores matemáticos
'''
comentário com mais
de uma linha
'''

####### VARIAVEIS #######

# String
nome = "Angelita Santos"
string = 'essa frase tem "olá mundo" no meio da frase'
# int
idade = 15
# boolean
menor_idade = True
# float
altura = 1.69
peso = 74.5



####################################################################################
####### ENTRADAS #######

# input()
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
menor_idade = True
altura = float(input("Digite a sua altura: "))
peso = float(input("Digite a sua peso: "))



####################################################################################
####### SAIDAS #######

# print()

print(f"O seu nome é: {nome}")
print("A sua idade é:", idade)
print(type(menor_idade))
print(altura)
print(peso)
print(string)



####################################################################################
####### OPERADORES MATEMATICOS #######

numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite outro numero: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao_real = numero1 / numero2
divisao_inteira = numero1 // numero2
resto = numero1 % numero2
potencia = numero1 ** numero2

print('Soma: ', soma)
print('Subtração: ', subtracao)
print('Multiplicação: ', multiplicacao)
print('Divisão Real: ', divisao_real)
print('Divisão Inteira: ', divisao_inteira)
print('Resto da Divisão: ', resto)
print('Potência: ', potencia)



####################################################################################