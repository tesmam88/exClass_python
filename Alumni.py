class Alumni:
    def __init__(self,matricula,nome,nota1,nota2,nota3):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def exibir_nome(self,nome):
        self.nome = nome 
        self.alunos = []

    def adicionar_aluno(self,aluno):    
        self.alunos.append = aluno

    def listar_aluno(self):
        for item in self.alunos:
            print(f"Aluno: {item.nome} | Matricula: {item.matricula}")
    
    def notas(self,nota1,nota2,nota3):
          print(f'Notas do aluno {self.nome}: 1ra nota - {nota1} |  2da nota - {nota2} |  3ra nota - {nota3}')

    def calcular_media(self):        
        media = (self.nota1 + self.nota2 + self.nota3)/3
        print(f'A média do aluno {self.nome} é: {media:.2f}')
        return media
    
    