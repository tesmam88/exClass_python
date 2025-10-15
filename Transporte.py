class Transporte:
    def __init__(self,capacidade):
        self.capacidade = capacidade

    def exibir_info(self):
        print(f'A capacidade do Transporte é: {self.capacidade}')

class Terrestre(Transporte):
    def __init__(self, capacidade,numero_rodas):
        super().__init__(capacidade)          
        self.numero_rodas = numero_rodas
    def exibir_info(self):
        super().exibir_info()      
        print(f'O numero de rodas do transporte terrestre é de: {self.numero_rodas}')

class Aquatico(Transporte):
    def __init__(self, capacidade,tipo_embarcacao):
        super().__init__(capacidade)        
        self.tipo_embarcacao = tipo_embarcacao
    def exibir_info(self):
        super().exibir_info()
        print(f'Tipo de embarcação: {self.tipo_embarcacao}')

class Aereo(Transporte):
    def __init__(self, capacidade,tipo_aeronave):
        super().__init__(capacidade)           
        self.tipo_aeronave = tipo_aeronave
       
    def exibir_info(self):
        super().exibir_info()
        print(f'Tipo de Aeronave: {self.tipo_aeronave}')     

class Automovel(Terrestre):
    def __init__(self, capacidade, numero_rodas,cor,placa,numero_portas):
        super().__init__(capacidade, numero_rodas)
        self.cor = cor
        self.placa = placa
        self.numero_portas = numero_portas

    def exibir_info(self):
        super().exibir_info()
        print(f'Cor do carro: {self.cor}')
        print(f'Placa: {self.placa}')
        print(f'Numero de portas: {self.numero_portas}')   

class Lancha(Aquatico):
    def __init__(self, capacidade, tipo_embarcacao,motor,velocidade,tamanho):
        super().__init__(capacidade, tipo_embarcacao)        
        self.motor = motor
        self.velocidae = velocidade
        self.tamanho = tamanho
    def exibir_info(self):
        super().exibir_info()
        print(f'O motor da lancha: {self.motor}')
        print(f'Velocidade maxima: {self.velocidae}')
        print(f'Tamanho: {self.tamanho}')    

barco = Aquatico(10, "Veleiro")
carro = Automovel(5, 4, "Prata", 4, "ABC-1234")
aviao = Aereo(150, "Comercial")


print("=== Barco ===")
barco.exibir_info()

print("\n=== Automóvel ===")
carro.exibir_info()

print("\n=== Avião ===")
aviao.exibir_info()    



