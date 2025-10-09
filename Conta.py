class Conta:
    def __init__(self,nome,cpf,numero,saldo = 0):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def depositar(self,valor):
        if valor >0:
            self.saldo += valor
            print(f'O valor depositado é: {valor}')
        else:
            print("Valor de Deposito Invalido") 

    def sacar(self,valor):
        if self.saldo > 0 and valor <= self.saldo:
            self.saldo -= valor
            print("Voce esta com saldo positivo")
            print(f'Saque de Valor: {valor}')

        elif self.saldo <= 0:
            print('Saldo Insuficiente')

        else:
            print('Valor não permitido de saque')

    def imprimir_saldo(self):
        print(f'Saldo Atual: {self.saldo:.2f}')        

conta1 = Conta("Ulrich VonLiencheinstein","046578945",1001,500) 

conta1.imprimir_saldo()
conta1.depositar(200)
conta1.sacar(100)
conta1.imprimir_saldo()
      