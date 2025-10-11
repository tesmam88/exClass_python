class Triangulo:
    def __init__(self,ladoA,ladoB,ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
        
    def calcular_Perimetro(self):
        perimetro = self.ladoA + self.ladoB + self.ladoC
        return perimetro
    def get_maiorLado(self):
        if self.ladoA > self.ladoB and self.ladoA > self.ladoC:
            print(f'O maior lado é: {self.ladoA}')
            return self.ladoA
        elif self.ladoB > self.ladoA and self.ladoB > self.ladoC:
            print(f'O maior lado é: {self.ladoB}')
            return self.ladoB
        else:
            print(f'O maior lado é: {self.ladoC}')
            return self.ladoC

triangulo1 = Triangulo(5,5,7)
print(triangulo1.calcular_Perimetro(),triangulo1.get_maiorLado())                    