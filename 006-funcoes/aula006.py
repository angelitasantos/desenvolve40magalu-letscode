def primeira_funcao():  
    print('Olá mundo')

print('Começo do programa')
primeira_funcao()
print('Meio do programa')
primeira_funcao()
print('Fim do programa')



##################################
# essa funcao soma 2 numeros inputados pelo usuario
def soma():
    numero1 = int(input('digite um numero: '))
    numero2 = int(input('digite outro numero: '))
    resultado = numero1 + numero2
    media = (resultado / 2)
    print(media)

soma()



##################################
def soma(numero1, numero2):
    resultado = numero1 + numero2
    media = (resultado / 2)
    print(resultado)
    print(media)

soma(14, 7)

x = 14
y = 20

soma(x, y)

numero1 = int(input('digite um numero: '))
numero2 = int(input('digite outro numero: '))

soma(numero1, numero2)



##################################
def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

soma1 = soma(14, 7)

media = (soma1 / 2)
print(media)



##################################
def saudação (nome, horario):
    if horario < 12:
        print ('Bom dia, ',nome,'!',sep="")
    elif horario <= 18 and horario >= 12:
        print ('Boa tarde, ',nome,'!',sep="")
    elif horario > 18:
        print ('Boa noite, ',nome,'!', sep="")

#teste
dia = saudação ('Daniel',10)
tarde = saudação ('Daniel',14)
noite = saudação ('Daniel',21)
saudação ('Daniel',8)



##################################
def par_ou_impar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# forma mais enxuta
def par_ou_impar2(numero):
    return numero % 2 == 0
