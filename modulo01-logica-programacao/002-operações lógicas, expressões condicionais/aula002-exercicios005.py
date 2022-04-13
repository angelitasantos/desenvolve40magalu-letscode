'''
Questão #5
Escreva um programa que peça a nota de 3 provas de um aluno e verifique se ele passou ou não de ano.
Obs.: O aluno irá passar de ano se sua média for maior que 6.
'''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

print('A media do aluno é', media)

if media > 6:
    print('Aprovado')
else:
    print('Reprovado')
