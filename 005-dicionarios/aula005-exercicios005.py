'''
Questão #5
Crie uma função que receba os valores do nome, idade e e-mail de uma pessoa e 
guarde-os em um dicionário com as chaves ‘nome’, ‘idade’ e ‘email’, respectivamente. 
Sua função deve retornar esse dicionário.
'''

dados = {   'nome': '',
            'idade': 0,
            'email': ''
        }

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
email = input('Digite o seu email: ')

if dados == {}:
    dados['nome'] = nome
    dados['idade'] = idade
    dados['email'] = email
    print('Cadastro Efetuado com Sucesso.')
else:
    dados.update({'nome': nome})
    dados.update({'idade': idade})
    dados.update({'email': email})
    print('Cadastro Atualizado com Sucesso')
    
print(dados)



