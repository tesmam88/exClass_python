class Aluno_academia:
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        

    def calcular_IMC(self):
        imc = self.peso / (self.altura**2)
        return imc
    
    def Obter_valor_Mensalidade(self):
        base = 120
        if self.idade < 18:
            return base * 0.95
        else:
            return base
aluno1 = Aluno_academia('Maximus',16,50,1.65)
print(aluno1.calcular_IMC())
print(aluno1.Obter_valor_Mensalidade())
