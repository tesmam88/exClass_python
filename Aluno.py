class Aluno:
    def __init__(self,nome,ra,nota1,nota2,nota3,nota4):
        self.nome = nome
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    def imprimir_notas(self,nota1,nota2,nota3,nota4):
        print(f'NOta 1: {nota1}\n ,Nota 2: {nota2}\n ,Nota3: {nota3}\n ,Nota4: {nota4}')

    def calcular_media(self):
        media = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4 
        print(f'A Media Aritmetica é: {media:.2f}')
        return media 
    def mostrar_situacao(self):
        media = self.calcular_media()
        if media >= 7:
            print("O Aluno esta Aprovado")
        elif media  >= 5:
            print("O aluno esta de Exame")
        else:
            print("O aluno esta Reprovado")


aluno1 = Aluno("Ulrich",123456,8,5,6,8)

print(f'Aluno:{aluno1.nome}')
print(f'RA: {aluno1.ra}')

aluno1.calcular_media()
aluno1.mostrar_situacao()