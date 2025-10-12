class Carro:
    def __init__(self,marca,modelo,cor,ano,valor,consumo,nivel=0):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.consumo = consumo
        self.nivel = nivel

    def abastecer(self,litros):
        self.nivel += litros
        print(f'O carro tem agora: {self.nivel:.1f} litros')
    
    def andar(self,kilometros):
        combustivel_necessario = kilometros/self.consumo
        if combustivel_necessario <= self.nivel:
            self.nivel -= combustivel_necessario
            print(f'O carro andou {kilometros} kilometros e consumiu {combustivel_necessario:.2f} litros')
        else:
            print('Combustivel Insuficiente')    
    def verificar_nivel(self):
        print(f'O nivel de combustivel é: {self.nivel} litros')

    def calcular_imposto(self):
        ipva = self.valor * 0.035
        print(f'O valor do IPVA: {ipva}')
        return ipva
    
carro1 = Carro("Honda","Civic","Prata",2022,300000,15)

carro1.abastecer(30)
carro1.andar(100)
carro1.verificar_nivel()
carro1.calcular_imposto()
    