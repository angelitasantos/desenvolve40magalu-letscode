import datetime

data_hora_atuais = datetime.datetime.now()
data_hora_pt_BR = data_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')

class Loja:

    def __init__(self, nome, estoque=[]):
        self.nome = nome
        self.estoque = estoque
        self.valor_hora = 5
        self.valor_dia = 25
        self.valor_semana = 100
        self.qtde_min_promocao = 3
        self.perc_promocao = 30
        self.conta_total = []

    def __repr__(self):
        return f'\nLoja: {self.nome}'

    def mostrar_estoque(self):

        total_estoque = len(self.estoque)

        total_disponivel = 0
        for bicicleta in self.estoque:
            if bicicleta[3] == 'Não':
                total_disponivel += 1
        
        print(f'\nLoja: {self.nome}')
        print(f'\nEstoque total =', total_estoque, 'bicicletas \nDisponíveis =', total_disponivel, 'bicicletas')
        print('-' *100)
        print(f" KEY | ID    | MODELO   | COR        | ALUGADA | TIPO ALUGUEL | QTDE | CLIENTE ")
        print('-' *100)

        for chave, valor in enumerate(self.estoque):
            print(  f" {chave:03d} | "+
                    f"{self.estoque[chave][0]} | "+
                    f"{self.estoque[chave][1]:<8s} | "+
                    f"{self.estoque[chave][2]:<10s} | "+
                    f"{self.estoque[chave][3]:<7s} | "+
                    f"{self.estoque[chave][4]:<12s} | "+
                    f"{self.estoque[chave][5]:04d} | "+
                    f"{self.estoque[chave][6]:<30s}")

        print('-' *100, '\n')

    def devolver_aluguel(self, loja, cliente, modelo, qtde):
        for bicicleta in self.estoque:
            if bicicleta[0] == modelo and bicicleta[3] == 'Sim':
                bicicleta[5] = qtde

    def calcular_conta(self, loja, cliente):

        print('~' * 100)
        print('\nDevolução de Aluguel de Bicicletas')
        print(loja)
        print(cliente)

        self.conta_total = []

        for bicicleta in self.estoque:
            if bicicleta[6] == cliente.email and bicicleta[5] > 0:
                
                if bicicleta[4] == 'hora':
                    conta_hora = bicicleta[5] * self.valor_hora
                    self.conta_total.append(conta_hora)
                    print(f'\nAluguel devolvido com sucesso.')
                    print(f'Identificador: {bicicleta[0]}, Modelo: {bicicleta[1]}, Cor: {bicicleta[2]}')
                    print(f'Valor total do aluguel para {bicicleta[5]} horas: R$ {conta_hora:.02f}')

                elif bicicleta[4] == 'dia':
                    conta_dia = bicicleta[5] * self.valor_dia
                    self.conta_total.append(conta_dia)
                    print(f'\nAluguel devolvido com sucesso.')
                    print(f'Identificador: {bicicleta[0]}, Modelo: {bicicleta[1]}, Cor: {bicicleta[2]}')
                    print(f'Valor total do aluguel para {bicicleta[5]} dias: R$ {conta_dia:.02f}')

                elif bicicleta[4] == 'semana':
                    conta_semana = bicicleta[5] * self.valor_semana
                    self.conta_total.append(conta_semana)
                    print(f'\nAluguel devolvido com sucesso.')
                    print(f'Identificador: {bicicleta[0]}, Modelo: {bicicleta[1]}, Cor: {bicicleta[2]}')
                    print(f'Valor total do aluguel para {bicicleta[5]} semanas: R$ {conta_semana:.02f}')

                bicicleta[3] = 'Não'
                bicicleta[4] = ''
                bicicleta[5] = 0
                bicicleta[6] = ''

        if len(self.conta_total) >= self.qtde_min_promocao:
            desconto = sum(self.conta_total) * (self.perc_promocao / 100)
            valor_liquido = sum(self.conta_total) - desconto

            print(f'\nValor total da conta: R$ {sum(self.conta_total):.02f}')
            print(f'Valor total do desconto: R$ {desconto:.02f}')
            print(f'Valor a pagar: R$ {valor_liquido:.02f}')  
            print(f'PARABENS! Você ganhou {self.perc_promocao}% de desconto referente a Promoção de {self.qtde_min_promocao} locações ou mais.\n')  
        else:
            print(f'\nValor total da conta: R$ {sum(self.conta_total):.02f}')
            print(f'QUE PENA!. Você NÃO tem direito ao desconto de {self.perc_promocao}% referente a Promoção de {self.qtde_min_promocao} locações ou mais.\n')

        print('~' * 100)

class Cliente:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __repr__(self):
        return f'Cliente: {self.nome} | e-mail: {self.email}' 

    def visualizar_bicicletas(self, loja):

        total_disponivel = 0
        for bicicleta in loja.estoque:
            if bicicleta[3] == 'Não':
                total_disponivel += 1
        
        print(f'\nTemos', total_disponivel, 'bicicletas disponíveis')
        print('-' *40)
        print(f" KEY | ID    | MODELO   | COR        ")
        print('-' *40)

        for chave, valor in enumerate(loja.estoque):
            if loja.estoque[chave][3] == 'Não':
                print(  f" {chave:03d} | "+
                        f"{loja.estoque[chave][0]} | "+
                        f"{loja.estoque[chave][1]:<8s} | "+
                        f"{loja.estoque[chave][2]:<10s}"
                        )

        print('-' *40, '\n')

    def alugar_bicicleta_por_hora(self, loja, modelo):
        print('~' * 70)
        print(f'Cliente: {self.nome} | e-mail: {self.email}' )
        self.visualizar_bicicletas(loja)

        for bicicleta in loja.estoque:
            if bicicleta[0] == modelo and bicicleta[3] == 'Não':
                bicicleta[3] = 'Sim'
                bicicleta[4] = 'hora'
                bicicleta[6] = self.email
                print(f'{self.nome}, \nAluguel realizado com sucesso.')
                print(f'Identificador: {bicicleta[0]}, Modelo: {bicicleta[1]}, Cor: {bicicleta[2]}\n')
            elif bicicleta[0] == modelo and bicicleta[3] == 'Sim':
                print(f'{self.nome}, \nBicicleta indisponível. Escolha outro modelo.\n')

    def alugar_bicicleta_por_dia(self, loja, modelo):
        print('~' * 70)
        print(f'Cliente: {self.nome} | e-mail: {self.email}' )
        self.visualizar_bicicletas(loja)

        for bicicleta in loja.estoque:
            if bicicleta[0] == modelo and bicicleta[3] == 'Não':
                bicicleta[3] = 'Sim'
                bicicleta[4] = 'dia'
                bicicleta[6] = self.email
                print(f'{self.nome}, \nAluguel realizado com sucesso.')
                print(f'Identificador: {bicicleta[0]}, Modelo: {bicicleta[1]}, Cor: {bicicleta[2]}\n')
            elif bicicleta[0] == modelo and bicicleta[3] == 'Sim':
                print(f'{self.nome}, \nBicicleta indisponível. Escolha outro modelo.\n')

    def alugar_bicicleta_por_semana(self, loja, modelo):
        print('~' * 70)
        print(f'Cliente: {self.nome} | e-mail: {self.email}' )
        self.visualizar_bicicletas(loja)

        for bicicleta in loja.estoque:
            if bicicleta[0] == modelo and bicicleta[3] == 'Não':
                bicicleta[3] = 'Sim'
                bicicleta[4] = 'semana'
                bicicleta[6] = self.email
                print(f'{self.nome}, \nAluguel realizado com sucesso.')
                print(f'Identificador: {bicicleta[0]}, Modelo: {bicicleta[1]}, Cor: {bicicleta[2]}\n')
            elif bicicleta[0] == modelo and bicicleta[3] == 'Sim':
                print(f'{self.nome}, \nBicicleta indisponível. Escolha outro modelo.\n')

    def alugar_bicicleta_promocao(self, loja, cliente):
        qtde_aluguel = 0
        for bicicleta in loja.estoque:
            if bicicleta[6] == cliente.email:
                qtde_aluguel += 1
        return f'[{cliente.email}, {qtde_aluguel}]'





print('=' * 100)
print("MAGAZINE LUIZA - LET'S CODE")
print('PROJETO - PROGRAMACAO ORIENTADA A OBJETO')
print(data_hora_pt_BR)
print('=' * 100)


nome_loja1 = 'Bike ABC Locação de Bicicletas'
estoque_loja1 = [
                ['00001', 'Aro 26', 'Azul', 'Não', '', 0, ''],
                ['00002', 'Aro 26', 'Verde', 'Não', '', 0, ''],
                ['00003', 'Aro 26', 'Vermelha', 'Não', '', 0, ''],
                ['00004', 'Aro 29', 'Branca', 'Não', '', 0, ''],
                ['00005', 'Aro 29', 'Preta', 'Não', '', 0, ''],
                ]
loja1 = Loja(nome_loja1, estoque_loja1)
loja1.mostrar_estoque()


cliente1 = Cliente('Maria José', 'maria@email.com')
cliente1.alugar_bicicleta_por_hora(loja1, '00001')
cliente1.alugar_bicicleta_por_dia(loja1, '00003')
cliente1.alugar_bicicleta_por_semana(loja1, '00005')
loja1.mostrar_estoque()


cliente2 = Cliente('José Maria', 'jose@email.com')
cliente2.alugar_bicicleta_por_semana(loja1, '00001')
cliente2.alugar_bicicleta_por_semana(loja1, '00002')
cliente2.alugar_bicicleta_por_semana(loja1, '00004')
loja1.mostrar_estoque()


loja1.devolver_aluguel(loja1, cliente2, '00002', 2)
loja1.devolver_aluguel(loja1, cliente2, '00004', 5)
loja1.calcular_conta(loja1, cliente2)
loja1.mostrar_estoque()


loja1.devolver_aluguel(loja1, cliente1, '00001', 7)
loja1.devolver_aluguel(loja1, cliente1, '00003', 4)
loja1.devolver_aluguel(loja1, cliente1, '00005', 2)
loja1.calcular_conta(loja1, cliente1)
loja1.mostrar_estoque()