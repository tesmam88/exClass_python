class Agenda:
    def __init__(self,dia,mes,ano,anotacao=''):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao
    def validar_data(self):
        if self.mes < 1 or self.mes >12:
            return False
        ##define os dias maximos de cada mes
        dias_por_mes = [31,28,31,30,31,30,31,31,30,31,30,31]

        ##Verifica se o ano é bissexto e ajusta fevereiro
        if(self.ano %4 == 0 and self.ano % 100 != 0) or (self.ano %400 ==0):
            dias_por_mes[1] = 29

        ## Verifica se o dia é valido para o mes
        if 1 <= self.dia <= dias_por_mes[self.mes - 1]:
            return True
        else:
            return False

    def anotar_tarefa(self,nova_anotacao):
        self.anotacao = nova_anotacao
        print(f'Tarefa anotaada para{self.dia},{self.mes},{self.ano}')

    def mostrar_anotacao(self):
        if self.validar_data():
            print(f'Data: {self.dia}/{self.mes}/{self.ano}')
            print(f'Anotação: {self.anotacao}')
        else:
            print("Comando Invalido")

agenda1 = Agenda(10,7,1988,'Dia de Gloria e muita Alegria')
print(agenda1.validar_data())
                    
        
        