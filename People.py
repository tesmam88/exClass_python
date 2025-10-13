class People:
    def __init__(self,nome,telefone,email,endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def negociar(self):
        print(f'O cliente {self.nome} esta em negociação')

    def exibir_dados(self):
        print(f'Nome do Cliente: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print(f'Email: {self.email}')
        print(f'Endereço do Cliente: {self.endereco}')

class Pessoa_Fisica(People):
    def __init__(self, nome, telefone, email, endereco,cpf):
        super().__init__(nome, telefone, email, endereco) 
        self.cpf = cpf

    def comprar(self):
        print(f'A pessoa fisica {self.nome} com cpf: {self.cpf} está realizando uma compra')
         

class Pessoa_Juridica(People):
    def __init__(self, nome, telefone, email, endereco,cnpj):
        super().__init__(nome, telefone, email, endereco)  
        self.cnpj = cnpj

    def vender(self):
        print(f'A empresa de nome {self.nome} esta em venda com cnpj {self.cnpj}')

print("---Pessoa Fisica---") 
pf = Pessoa_Fisica('Olavo',67555555,'olavo@yahoo.com','Rua das Mangueiras,67',456753125)
pf.exibir_dados()
pf.negociar()
pf.comprar()

print("---Pessoa Juridica---")
pj = Pessoa_Juridica('Zé da Manga ltda',67888888,"zemanga@gmail.com","ruas das mangas,89",111222333444)
pj.exibir_dados()
pj.negociar()
pj.vender()
        