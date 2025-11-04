class Alumni:
    def __init__(self,matricula,nome,nota1,nota2,nota3):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def exibir_nome(self):
        return self.nome
    
    def calcular_media(self):        
        media = (self.nota1 + self.nota2 + self.nota3)/3
        return media
   
    def situacao(self):
        media = self.calcular_media()
        if media >= 6:
            return "Aprovado"
        else:
            return "Reprovado"

class Gerenciar_alunos:   
    def __init__(self):
        self.alunos = []    

    def adicionar_alunos(self,aluno):
        self.alunos.append(aluno)  

    def listar_alunos(self):
        for aluno in self.alunos:
            print(f'Aluno: {aluno.exibir_nome()} | Matricula: {aluno.matricula} | Media: {aluno.calcular_media()} | Situação: {aluno.situacao()} ')

    def nota_max(self):
        maior_media = max(self.alunos, key = lambda a: a.calcular_media())   
        print(f'O aluno com maior media é: {maior_media.exibir_nome()} | Media: {maior_media.calcular_media(): .2f}')     

    def nota_min(self):
        menor_media = min(self.alunos, key = lambda a: a.calcular_media())
        print(f'O aluno com menor media é: {menor_media.exibir_nome()} | Media: {menor_media.calcular_media():.2f}')


def main():
    sistema = Gerenciar_alunos()

    # (a) Entrada de dados de 5 alunos
    for i in range(5):
        print(f"\nCadastro do {i+1}º aluno:")
        matricula = input("Matrícula: ")
        nome = input("Nome: ")
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))

        aluno = Alumni(matricula, nome, nota1, nota2, nota3)
        sistema.adicionar_alunos(aluno)

    print("\n=== Lista de Alunos ===")
    sistema.listar_alunos()

    print("\n=== Estatísticas ===")
    sistema.nota_max()
    sistema.nota_min()


# Executar programa
main()
