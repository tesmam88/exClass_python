class Student:
    def __init__(self,nome,matricula,curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def mostrar_curso(self):
        print(f"O curso do aluno {self.nome} é {self.curso}")

    def alterar_curso(self,novo_curso):
        self.curso = novo_curso
        return novo_curso

aluno1 = Student("ROmeu Capuleto",123,"3ano B")
aluno1.mostrar_curso()
new_curso = aluno1.alterar_curso("3ano A")
aluno1.mostrar_curso()            