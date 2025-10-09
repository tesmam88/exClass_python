class Funcionario:
    def __init__(self,nome,sobrenome,Horas_trabalhadas,Valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.Horas_trabalhadas = Horas_trabalhadas
        self.Valor_hora = Valor_hora

    def nomeCompleto(self):
            print(f'Nome Completo: {self.nome} {self.sobrenome}')

    def calcularSalario(self):
            salario = self.Horas_trabalhadas * self.Valor_hora
            print(f'O salario é: {salario:.2f}') 
            return salario 

    def incrementarHora(self,horas):
            if horas > 0:
                self.Horas_trabalhadas += horas
                print(f'{horas} Horas adicionais. Total de HOras: {self.Horas_trabalhadas}')
            else:
                print("Valor Invalido. Horas deven ser positivas")

func1 = Funcionario("Ulrich","VonLincheinstein",150,25)

func1.nomeCompleto()
func1.calcularSalario()
func1.incrementarHora(20)
func1.calcularSalario()
