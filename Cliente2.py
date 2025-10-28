class Cliente2:
    def __init__(self,id,nome,cpf,email,tel):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.tel = tel
        self.pedidos = []

    def cadastro(self):
        print(f"Cliente {self.nome} id: {self.id} cadastrado")

    def atualizar(self,nome,email,tel):
        self.email = email
        self.tel = tel

lista_clientes = []
cliente1 = Cliente2 (1,'alan','000000','alan@yahoo.com.br','67888888')
lista_clientes.append(cliente1)
print(lista_clientes[0])    
lista_clientes[0].cadastro()

class Produto:
    def __init__(self,cod,nome,desc,preco,qtd):
        self.cod = cod
        self.nome = nome
        self.desc = desc
        self.preco = preco
        self.qtd = qtd

    def atualizar(self,nova_qtd):    
        self.qtd = nova_qtd
        print(f"A nova quantidade de estoque é: {self.qtd}")

    def aplicar_desconto(self,percentual):
        preco_desc = self.preco - (self.preco *(percentual/100))
        return preco_desc
    def exibir_info(self):
        print(f'Nome: {self.nome} | Preço: {self.preco:.2f} | Quantidade: {self.qtd}')

lista_produtos = []
produto1 = Produto(1,'lata de tinta',0,15,5)
lista_produtos.append(produto1)
print(lista_produtos[0])      
lista_produtos[0].exibir_info()   