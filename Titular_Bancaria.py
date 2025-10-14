class Titular_Bancaria:
    def __init__(self,nome,cpf,endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

    def exibir_dados(self):
        print (f'Nome do Cliente: {self.nome}, CPF: {self.cpf}, Endereço: {self.endereco}')

class ContaBancaria:
    def __init__(self,numero,titular,saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self,valor):
        if valor > 0:
            self.saldo += valor
            print(f'O valor depositado {valor:.2f} esta na conta')
        else:
            print('O valor não foi depositado') 

    def sacar(self,valor):                       
        if valor < 0 and valor <=self.saldo:
            self.saldo += valor
            print(f'Saque de {valor:.2f} realizado com sucesso')
        else:
            print("Saque Indisponivel")

    def exibir_saldo(self):
        print(f'O seu saldo na conra é {self.saldo}')

class Conta_Corrente(ContaBancaria):
    def __init__(self, numero, titular, saldo=0,limite=500):
        super().__init__(numero, titular, saldo)        
        self.limite = limite

    def sacar(self, valor):
        if 0 <= valor <= (self.saldo + self.limite):
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso')
        else:
            print('Saldo Insuficiente')

class Poupanca(ContaBancaria):
    def __init__(self, numero, titular, saldo=0,taxa_rendimento=0.005):
        super().__init__(numero, titular, saldo)                 
        self.taxa_rendimento = taxa_rendimento

    def render_juros(self):
        ganho = self.saldo * self.taxa_rendimento
        self.saldo += ganho
        print(f'O seu rendimento é de: {ganho}, Novo Saldo: R${self.saldo:.2f}')

class AplicacaoFundo(ContaBancaria):
    def __init__(self, numero, titular, saldo=0,taxa_rendimento = 0.020):
        super().__init__(numero, titular, saldo)
        self.taxa_rendimento = taxa_rendimento

    def aplicar_rendimento(self):
        ganho = self.saldo * self.taxa_rendimento
        self.saldo += ganho
        print(f'O seu rendimento é de: {ganho:.2f}. Novo Saldo: R${self.saldo:.2f}')

titular1 = Titular_Bancaria("Ana Silva", "123.456.789-00", "Rua das Flores, 123")

conta_corrente = Conta_Corrente(1001, titular1, saldo=1000, limite=300)
conta_poupanca = Poupanca(2001, titular1, saldo=2000)
fundo = AplicacaoFundo(3001, titular1, saldo=5000)

conta_corrente.sacar(1200)
conta_corrente.exibir_saldo()

conta_poupanca.render_juros()

fundo.aplicar_rendimento()        


