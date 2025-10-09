class Circulo:
    def __init__(self,raio,pi):
        self.raio = raio
        self.pi = 3.14159

    def imprimir_raio(self):
        print(f"O raio do circulo é: {self.raio}")
    def calcular_area(self):
        area = self.pi * (self.raio ** 2)
        print(f"A area do circulo é: {area:.2f}")
        return area
    def calcular_circunferencia(self):
        circunferencia = 2 * self.pi * self.raio
        print(f'A circunferencia do circulo é: {circunferencia:.2f}')    
        return circunferencia

circulo1 = Circulo(5)
circulo1.imprimir_raio()
circulo1.calcular_area()
circulo1.calcular_circunferencia()        