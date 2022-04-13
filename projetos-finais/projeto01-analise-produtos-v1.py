import json
import os.path
import sys

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    Cuidado para não retornar categorias repetidas.    
    '''
    lista_categorias = []
    for categoria in dados:
        if not (categoria['categoria']) in lista_categorias:
            lista_categorias.append(categoria['categoria'])
    lista_categorias.sort()
    return lista_categorias

def listar_por_categoria(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    produto_por_categoria = []
    for produto in dados:
        if produto['categoria'] == categoria:
            produto_por_categoria.append({'id': produto['id'], 'preco': produto['preco']})
    return produto_por_categoria

def produto_mais_caro(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    lista_mais_caro = []
    produto_mais_caro = {}
    for produto in dados:
        if produto['categoria'] == categoria:
            lista_mais_caro.append(float(produto['preco']))
            produto_mais_caro[categoria] = lista_mais_caro[0]
        lista_mais_caro.sort(reverse=True)

    mais_caro = str(lista_mais_caro[0])
    for produto in dados:
        if produto['preco'] == mais_caro:
            print({'categoria': produto['categoria'], 'id': produto['id'], 'preco': produto['preco']})
    resultado = ''
    return resultado

def produto_mais_barato(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais barato da categoria dada.
    '''
    lista_mais_barato = []
    produto_mais_barato = {}
    for produto in dados:
        if produto['categoria'] == categoria:
            lista_mais_barato.append(float(produto['preco']))
            produto_mais_barato[categoria] = lista_mais_barato[0]
        lista_mais_barato.sort()

    mais_barato = str(lista_mais_barato[0])
    for produto in dados:
        if produto['preco'] == mais_barato:
            print({'categoria': produto['categoria'], 'id': produto['id'], 'preco': produto['preco']})
    resultado = ''
    return resultado

def top_10_caros(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    # pegar os 10 maiores preços
    lista_ordem_mais_caro = []
    for produto in dados:
        lista_ordem_mais_caro.append(float(produto['preco']))
    lista_ordem_mais_caro.sort(reverse=True)

    # transformar os itens da lista de float para string
    ordem_mais_caro = lista_ordem_mais_caro[:10]
    ordem_mais_caro_str = []
    for elemento in ordem_mais_caro:
        ordem_mais_caro_str.append(str(elemento))

    # criar um dicionario com a chave preco
    por_preco = {}
    for dado in dados:
        if not (dado['preco']) in por_preco:
            por_preco[dado['preco']] = []
        id = dado['id']
        preco = dado['preco']
        categoria = dado['categoria']
        por_preco[dado['preco']].append({'id': id, 'preco': preco, 'categoria': categoria})

    # comparar a lista com os 10 maiores valores com o dicionario com a chave preco
    lista_10_mais_caros = []
    for elemento in ordem_mais_caro_str:
        if elemento in por_preco:
            lista_10_mais_caros.append(por_preco[elemento])
    return lista_10_mais_caros

def top_10_baratos(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais baratos.
    '''
    # pegar os 10 menores preços
    lista_ordem_mais_barato = []
    for produto in dados:
        lista_ordem_mais_barato.append(float(produto['preco']))
    lista_ordem_mais_barato.sort()

    # transformar os itens da lista de float para string
    ordem_mais_barato = lista_ordem_mais_barato[:10]
    ordem_mais_barato_str = []
    for elemento in ordem_mais_barato:
        ordem_mais_barato_str.append(str(elemento))

    # criar um dicionario com a chave preco
    por_preco = {}
    for dado in dados:
        if not (dado['preco']) in por_preco:
            por_preco[dado['preco']] = []
        id = dado['id']
        preco = dado['preco']
        categoria = dado['categoria']
        por_preco[dado['preco']].append({'id': id, 'preco': preco, 'categoria': categoria})

    # comparar a lista com os 10 maiores valores com o dicionario com a chave preco
    lista_10_mais_baratos = []
    for elemento in ordem_mais_barato_str:
        if elemento in por_preco:
            lista_10_mais_baratos.append(por_preco[elemento])
    return lista_10_mais_baratos

def menu(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo. 
    O loop encerra quando a opção do usuário for 0.
    '''

    # variáveis para os inputs e prints do MENU
    categoria_inexistente = 'Categoria inexistente. Digite uma categoria que existe.'
    escolher_categoria = 'Digite a categoria que deseja consultar: '
    continuar_consulta = 'Digite "S" para fazer outra consulta desta opção: '
    opcao_invalida = 'Por favor, digite uma opção válida.'
    multiplicador = 150

    opcao = 999

    while opcao != 0:
        print('=' * multiplicador)
        print('MAGAZINE LUIZA\nAPI BLACK FRIDAY')
        print('=' * multiplicador)
        print('MENU')
        print('   1. Listar categorias')
        print('   2. Listar produtos de uma categoria')
        print('   3. Produto mais caro por categoria')
        print('   4. Produto mais barato por categoria')
        print('   5. Top 10 produtos mais caros')
        print('   6. Top 10 produtos mais baratos')
        print('   0. Sair')
        print('-' * multiplicador)

        # validar a entrada da opção para outros tipos de variáveis diferente de valor inteiro
        o = str(input('Escolha uma das seguintes opções acima: '))
        while o.isnumeric() != True:
            print(opcao_invalida)
            o = str(input('Escolha uma das seguintes opções acima: '))
        opcao = int(o)
        print('-' * multiplicador)
        
        ########################################################################################
        if opcao == 1:
            print('\n>>> Lista de Categorias por Ordem Alfabética <<<\n')
            listar_categorias(dados)
            for elemento in listar_categorias(dados):
                print(elemento)
            print(f'\nExistem {len(listar_categorias(dados))} categorias ativas no sistema.\n')            
        
        ########################################################################################
        if opcao == 2:
            categoria = input(escolher_categoria).strip().lower()

            while categoria not in listar_categorias(dados):
                print(categoria_inexistente)
                categoria = input(escolher_categoria).strip().lower()
            
            print(f'\n>>> Lista de Produtos da Categoria: {categoria} <<<\n')
            for elemento in listar_por_categoria(dados, categoria):
                print(elemento)
            print(f'\nExistem {len(listar_por_categoria(dados, categoria))} produtos para esta categoria.\n')  
            
        ########################################################################################
        if opcao == 3:
            categoria = input(escolher_categoria).strip().lower()

            while categoria not in listar_categorias(dados):
                print(categoria_inexistente)
                categoria = input(escolher_categoria).strip().lower()

            print(f'\nProduto Mais Caro da Categoria:')
            print(f'{produto_mais_caro(dados, categoria)}\n')

            continuar = input(continuar_consulta).strip().upper()
            while continuar == 'S':
                categoria = input(escolher_categoria).strip().lower()

                while categoria not in listar_categorias(dados):
                    print(categoria_inexistente)
                    categoria = input(escolher_categoria).strip().lower()

                print(f'\nProduto Mais Caro da Categoria:')
                print(f'{produto_mais_caro(dados, categoria)}\n')

                continuar = input(continuar_consulta).strip().upper()

        ########################################################################################
        if opcao == 4:
            categoria = input(escolher_categoria).strip().lower()

            while categoria not in listar_categorias(dados):
                print(categoria_inexistente)
                categoria = input(escolher_categoria).strip().lower()

            print(f'\nProduto Mais Barato da Categoria:')
            print(f'{produto_mais_barato(dados, categoria)}\n')

            continuar = input(continuar_consulta).strip().upper()
            while continuar == 'S':
                categoria = input(escolher_categoria).strip().lower()

                while categoria not in listar_categorias(dados):
                    print(categoria_inexistente)
                    categoria = input(escolher_categoria).strip().lower()

                print(f'\nProduto Mais Barato da Categoria:')
                print(f'{produto_mais_barato(dados, categoria)}\n')

                continuar = input(continuar_consulta).strip().upper()

        ########################################################################################
        if opcao == 5:
            print('\n>>> Lista dos 10 produtos mais caros <<<\n')
            for elemento in top_10_caros(dados):
                print(elemento)
            print('')

        ########################################################################################
        if opcao == 6:
            print('\n>>> Lista dos 10 produtos mais baratos <<<\n')
            for elemento in top_10_baratos(dados):
                print(elemento)
            print('')
        
        ########################################################################################
        if opcao >= 7:
            print(opcao_invalida)

        ########################################################################################
        if opcao == 0:
            print('~' * multiplicador)
            print('MAGAZINE LUIZA\nAPI BLACK FRIDAY --- FIM')
            print('\nCurso: Desenvolve 40+ Magalu')
            print('Projeto: Lógica de Programação')
            print('~' * multiplicador)

        # algumas falhas de validação não consegui entender porque acontece, por exemplo, depois que escolheu uma opcao 
        # e a proxima escolha não é valida da erro de sintax
    
# Programa Principal - não modificar!
d = obter_dados()
menu(d)
