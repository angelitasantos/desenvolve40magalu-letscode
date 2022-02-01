'''
Questão #8
Faça um programa que fique pedindo uma resposta do usuário, entre 1, 2 e 3. Se o 
usuário digitar 1, o programa deve cadastrar um novo usuário e guardar esse cadastro 
num dicionário cuja chave será o CPF da pessoa. Quando o usuário digitar 2, o programa 
deve imprimir os usuários cadastrados; e se o usuário digitar 3, o programa deve fechar.
Exemplo do dicionário:
‘987.654.321-00’: {‘nome’: Maria, ‘idade’: 20, ‘email’ :             maria@mail.com}
'''

escolha = 1
dicionario = {}

while escolha != 3:

    print('-' * 30)
    print('MENU')
    print('1: Cadastrar novo usuário')
    print('2: Listar usuários cadastrados')
    print('3: Fechar o programa')

    escolha = int(input('Digite uma opcão: ' ))

    if escolha == 1:
        cpf = input('Digite o CPF sem pontos ou traço:')
        nome = input('Digite o nome:')
        idade = input('Digite a idade:')
        email = input('Digite o email:')
        dicionario[cpf] = {'nome': nome, 'idade': idade, 'email': email}

    elif escolha == 2:
        print(dicionario)
        
    elif escolha <= 0 or escolha > 3: 
        print('Opção inválida! Digite uma opção válida.')

print('Obrigado por usar o programa, volte sempre!')   