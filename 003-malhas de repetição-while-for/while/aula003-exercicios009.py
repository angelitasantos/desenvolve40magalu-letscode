'''
Desafio #2
Calcule a soma de mil termos dos inversos dos fatoriais: 
1/(1!) + 1/(2!) + 1/(3!) + 1/(4!) + ...
Dica: Assim como no exercício anterior use três variáveis: um contador; uma 
variável para a soma; e uma variável para os termos. Lembre-se de que 
4! = 4*3*2*1 que também é igual a 4*3!.
'''

'''
1/1! + 1/2! + 1/3! + ... = 1.718
'''

soma = 0
fatorial = 1
contador = 1

while contador <= 1000:
    # fatorial *= contador
    fatorial = fatorial * contador
    termo = 1 / fatorial
    soma = soma + termo
    contador =  contador + 1

print(soma)
