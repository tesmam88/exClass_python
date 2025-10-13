class Funcionarios:
    def __init__(self,nome,matricula,salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario
        self.pontos = []

    def bater_ponto(self,ponto):
        if ponto in (0,1):
            self.pontos.append(ponto)
            print(f'Ponto Registrado para {self.nome} : {ponto} ')
        else:
            print("Valor INvalido. Use 0 ou 1")

    def __str__(self):
        return f'Funcionario: {self.nome}, Matricula: {self.matricula}, Salario: {self.salario}'

class Vendedor(Funcionarios):
    def __init__(self, nome, matricula, salario,comissao):
        super().__init__(nome, matricula, salario)   
        self.comissao = comissao

    def bater_meta(self,vendas):
        if vendas >= 1000:
            bonus = vendas * self.comissao
            print(f"O vendedor {self.nome} bateu a meta com: R${bonus:.2f} de bonus")
        else:
            print(f'O vendedor {self.nome} não bateu a meta de vendas')

class Gerente(Funcionarios):
    def __init__(self, nome, matricula, salario,senha):
        super().__init__(nome, matricula, salario)   
        self.senha = senha

    def acessar_senha(self,senha_digitada):
        if senha_digitada == self.senha:
            print(f"Acesso permitido para gerente {self.nome}")
        else:
            print("Senha Incorreta")

v1 = Vendedor("Eustaquio",123,2500,0.05) 
v1.bater_ponto(1)
v1.bater_meta(15000)   
print(v1)

func1 = Gerente("Braulio",465,5000,555222)
func1.acessar_senha(555222)
            
