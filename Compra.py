class Compra:
    def __init__(self,numero,produto,valor):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        self.valor_total=0
        
    def calcular_valor_total(self):
        icms = self.valor * 0.17
        frete = self.valor * 0.05
        self.valor_total = self.valor + icms + frete
        print(f'O valor total é de: {self.valor_total:.2f}')

class CompraAvista(Compra):
    def __init__(self, numero, produto, valor, desconto):
        super().__init__(numero, produto, valor)
        self.desconto = desconto 

    # Sobrescreve o método de cálculo
    def calcular_valor_total(self):
        icms = self.valor * 0.17
        frete = self.valor * 0.05
        desconto_valor = self.valor * self.desconto
        self.valor_total = self.valor + icms + frete - desconto_valor
        print(f'O valor total da compra à vista com desconto é: R${self.valor_total:.2f}')

    # Getters e Setters
    def get_desconto(self):
        return self.desconto

    def set_desconto(self, novo_desconto):
        self.desconto = novo_desconto

class CompraParcelada(Compra):
    def __init__(self, numero, produto, valor):
        super().__init__(numero, produto, valor)

    def simular_numero_de_parcelas(self, parcelas):
        icms = self.valor * 0.17
        frete = self.valor * 0.05
        self.valor_total = self.valor + icms + frete
        valor_parcela = self.valor_total / parcelas
        print(f'Compra parcelada em {parcelas}x de R${valor_parcela:.2f} (Total: R${self.valor_total:.2f})')

    # Getters e Setters
    def get_valor_total(self):
        return self.valor_total

    def set_valor_total(self, novo_valor):
        self.valor_total = novo_valor

compra1 = CompraAvista(1, "Notebook", 3000, 0.10)
compra1.calcular_valor_total()

compra2 = CompraParcelada(2, "TV 50''", 2500)
compra2.simular_numero_de_parcelas(5)
