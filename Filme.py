class Filme:
    def __init__(self,nome,duracao):
        self.nome = nome
        self.duracao = duracao
    def play(self):
        print(f'Dando play no filme {self.nome} com duração de {self.duracao} minutos')

class Acao(Filme):
    def __init__(self, nome, duracao,explosoes):
        super().__init__(nome, duracao)
        self.explosoes = explosoes
    
    def explodir(self):
        print(f'O filme {self.nome} teve {self.explosoes} explosões!!')

class Drama(Filme):
    def __init__(self, nome, duracao,lagrimas):
        super().__init__(nome, duracao)      
        self.lagrimas = lagrimas

    def chorar(self):
        print(f'O filme {self.nome} teve {self.lagrimas} lagrimas')

filme1 = Acao("A VOLTA DOS QUE NÃO FORAM",120,20)
filme2 = Drama("HOMEM CHORÃO",150,1000)

filme1.play()
filme1.explodir()

filme2.play()
filme2.chorar()
        