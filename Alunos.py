class Alunos:
    def __init__(self,nome,ra):
        self.nome = nome
        self.ra = ra
class Universidade:
    def __init__(self,nome):
        self.nome = nome
        self.alunos = []

    def adicionar_alunos(self,aluno:object):
        self.alunos.append(aluno)

    def listar_alunos(self):
        for item in self.alunos:
            print(f'Nome: {item.nome}, RA: {item.ra}')    

a1 = Alunos("Jiban",123)
a2 = Alunos("Jiraya",456)
a3 = Alunos("Jaspion",789)
a4 = Alunos("Shurato",444)

faculdade = Universidade("SENAC MS")
print(len(faculdade.alunos))
faculdade.adicionar_alunos(a1)
faculdade.adicionar_alunos(a2)
faculdade.adicionar_alunos(a3)
faculdade.adicionar_alunos(a4)
print(len(faculdade.alunos))

faculdade.listar_alunos()