import random

class Motor:
    def __init__(self,pot,comb):
        self.chassis = random.randrange(0,1000)
        self.potencia = pot
        self.combustivel = comb

    def get_combustivel(self):
        return self.combustivel
class Carro:
    def __init__(self,modelo,potercia_motor,combustivel):
        self.modelo = modelo
        self.motor = Motor(potercia_motor,combustivel) #composição

        
        