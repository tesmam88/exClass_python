class Person:
    def __init__(self,nome,matricula,idade):
        
        self.matricula = matricula
        self.nome = nome
        self.idade = idade

    def exibir_dados(self):
        print(f'A matricula é: {self.matricula}')
        print(f'Nome: {self.nome}')    
        (f'Idade: {self.idade}')

class Aluno(Person):
    def __init__(self,matricula, nome, idade,notas):
        super().__init__(nome, idade,matricula)
        self.notas = notas
        self.media = 0.0

    def calcular_media(self):
        if len(self.notas) > 0:
            self.media = sum(self.notas) / len(self.notas)
            print(f'O aluno {self.nome} teve media: {self.media}')
        else:
            print("Nenhuma nota informada")    

    def estudar(self):
        print(f'O aluno {self.nome} esta estudando...')

class Professor(Person):
    def __init__(self, matricula, nome, idade,formacao,disciplina,carga_horaria,salario):
        super().__init__(nome, matricula, idade)        
        self.formacao = formacao
        self.disciplina = disciplina
        self.carga_horaria = carga_horaria
        self.salario = salario

    def lesionar(self):
        print(f'O {self.nome} esta ensinando {self.disciplina}')

    def exibir_informacoes(self):
        self.exibir_dados()
        print(f'Formação: {self.formacao}')
        print(f'Disciplina: {self.disciplina}')
        print(f'Carga Horaria: {self.carga_horaria:.2f}')
        print(f'Salario: {self.salario}')

aluno1 = Aluno(123,"Hugh",12,[8.5,9,7.5])
aluno1.exibir_dados() 
aluno1.estudar()
aluno1.calcular_media()

print("\n")

prof1 = Professor(234,"Lucrecio",55,"Matematico","Matematica",40,5500)
prof1.exibir_informacoes()
prof1.lesionar()