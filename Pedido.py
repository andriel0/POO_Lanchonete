from Pizza import Pizza
from Lanche import Lanche
from Salgadinho import Salgadinho

class Pedido:
    def __init__(self, nome_cliente):
        self.__nome_cliente = nome_cliente
        self.__taxa_servico = 0.0
        self.__itens_consumidos = []

    @property
    def nome_cliente(self):
        return self.__nome_cliente

    @nome_cliente.setter
    def nome_cliente(self, nome_cliente):
        self.__nome_cliente = nome_cliente

    @property
    def taxa_servico(self):
        return self.__taxa_servico

    def calcularTaxa(self):
        valorTotal = 0
        for i in self.__itens_consumidos:
            valorTotal += (i.preco*i.peso)/1000
        return valorTotal * 0.1

    @property
    def itens_consumidos(self):
        return self.__itens_consumidos

    def inserir_item(self, item):
        self.__itens_consumidos.append(item)

    def gerar_nota(self):
        valorPagar = 0
        print(f'\n\nLANCHONETE QUASE TRÊS LANCHES\n\n'
              f'======================================\n\n'
              f'Ficha do cliente {self.__nome_cliente}\n\n'
              f'======================================\n')
        for n in self.__itens_consumidos:
            valorPagar += (n.preco*n.peso)/1000
            print(f'{n.nome}\nValidade {n.data_val}\nPeso {n.peso}g....Preço por kg: {n.preco:.2f} \n'
                  f'Preço: {(n.preco*n.peso)/1000:.2f}\n\n'
                  f'===================================\n')
        print(f'Valor de todos os produtos.....R$ {valorPagar:.2f}\n'
              f'Taxa de serviço................R$ {self.calcularTaxa():.2f}\n'
              f'Valor total a pagar............R$ {(valorPagar+self.calcularTaxa()):.2f}')

    def gerarTroco(self):
        valor = 0
        for j in self.__itens_consumidos:
            valor += (j.preco*j.peso)/1000
        valor = valor + self.calcularTaxa()
        pagamento = float(input('\nQuanto você vai dar? '))
        troco = pagamento - valor
        print(f'\n===================================\n'
              f'\nValor pago...............R$ {pagamento:.2f}\n'
              f'Valor total..............R$ {valor:.2f}\n'
              f'Troco....................R$ {troco:.2f}\n'
              f'===================================\n'
              f'Obrigado pela preferência, volte sempre.')

def main():
    nome_cliente = input('Boa noite, qual seu nome? ')
    cliente = Pedido(nome_cliente)

    while True:
        pedido = input('\nO que você vai querer hoje? Temos pizza, lanche e salgadinho. ')
        if pedido.lower() == 'pizza':
            qtd = int(input('Quantas pizzas você vai querer? '))
            for pi in range(qtd):
                molho = input('\nQual o molho você vai querer? ')
                recheio = input('Qual o recheio você vai querer? ')
                borda = input('Qual a borda você vai querer? ')
                pizza = Pizza('Pizza', 55, '29/07/2022', 600, molho, recheio, borda)
                cliente.inserir_item(pizza)

        elif pedido.lower() == 'lanche':
            qtd = int(input('Quantos lanches você vai querer? '))
            for lan in range(qtd):
                pao = input('\nQual o pão você vai querer? ')
                molho = input('Qual o molho você vai querer? ')
                recheio = input('Qual o recheio você vai querer? ')
                lanche = Lanche('Lanche', 44.75, '28/07/2022', 400, pao, molho, recheio)
                cliente.inserir_item(lanche)

        elif pedido.lower() == 'salgadinho':
            qtd = int(input('Quantos salgadinhos você vai querer? '))
            for sal in range(qtd):
                tipo = input('\nComo você vai querer seu salgadinho, assado ou frito? ')
                massa = input('Qual a massa você vai querer? ')
                recheio = input('Qual o recheio você vai querer? ')
                salgadinho = Salgadinho('Salgadinho', 23, '28/07/2022', 300, tipo, recheio, massa)
                cliente.inserir_item(salgadinho)

        mais = input('\nVocê quer algo mais? ')
        if mais.lower() == 'nao' or mais.lower() == 'não':
            cliente.calcularTaxa()
            cliente.gerar_nota()
            cliente.gerarTroco()
            break

if __name__ == '__main__':
    main()



