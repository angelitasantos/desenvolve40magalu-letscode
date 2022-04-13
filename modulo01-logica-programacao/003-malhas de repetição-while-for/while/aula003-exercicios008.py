'''
Desafio #1
Calcule a soma de até mil termos da série 1 + 1/2 + 1/4 + 1/8 + 1/16 + ...
Dica: Use três variáveis:
• um contador, que começa em zero;
• uma variável para a soma de todos os termos, que também começa em zero;
• uma variável para cada termo, que começa em 1 e a cada loop é dividida por 2.
A repetição da soma de mil termos pode ser feita com a função while contador < 1000.
'''

'''
1 + 1/2 + 1/4 + ... = 2.0
'''

contador = 0
soma = 0
termo = 1

while contador <= 1000:
    soma = soma + termo
    termo = termo / 2
    contador = contador + 1

print(soma)
