'''
Questão #9
Implemente um sistema de busca para o programa do exercício anterior. Isto é, se o 
usuário digitar 4, procure um determinado usuário pelo seu CPF.
'''

escolha = 1
dicionario = {}

while escolha != 3:

    print('-' * 30)
    print('MENU')
    print('1: Cadastrar novo usuário')
    print('2: Listar usuários cadastrados')
    print('3: Fechar o programa')
    print('4: Buscar CPF')

    escolha = int(input('Digite uma opcão: ' ))

    if escolha == 1:
        cpf = input('Digite o CPF sem pontos ou traço:')
        nome = input('Digite o nome:')
        idade = input('Digite a idade:')
        email = input('Digite o email:')
        dicionario[cpf] = {'nome': nome, 'idade': idade, 'email': email}

    elif escolha == 2:
        print(dicionario)
    
    elif escolha == 4:
        buscar_cpf = input("Digite o CPF que deseja encontrar: ") 
        if buscar_cpf in dicionario:
            print(dicionario[buscar_cpf])
        else:
            print("Esse CPF não está cadastrado!")
        
    elif escolha <= 0 or escolha > 4: 
        print('Opção inválida! Digite uma opção válida.')

print('Obrigado por usar o programa, volte sempre!')   