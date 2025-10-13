class Passagem:
    def __init__(self,preco,assento):
        self.preco = preco
        self.assento = assento

    def alterar_preco(self,novo_preco):
        print(f'O preço da passagem de R$ {self.preco} foi alterado para R${novo_preco}')
        self.preco = novo_preco

    def escolher_assento(self):
        print(f'O assento escolhido foi: {self.assento}')

class Passagem_Bus(Passagem):
    def __init__(self, preco, assento,placa,leito):
        super().__init__(preco, assento)
        self.placa = placa
        self.leito = leito

    def placa(self):
        print(f'A placa do Onibus é: {self.placa}')
    def leito(self):
        if self.leito:
            print('Voce esta em leito. Aproveite a Viagem')
        else:
            print("Seu assento não é leito")
    def abastecer(self):
        print(f"O onibus de placa {self.placa} esta abastecendo")


class Passagem_Aviao(Passagem):
    def __init__(self, preco, assento,porta_embarque,checkin):
        super().__init__(preco, assento)   

        self.porta_embarque = porta_embarque
        self.checkin = checkin

    def mostar_porta_embarque(self):
        print(f'Seu portão de embarque é: {self.porta_embarque}')

    def verificar_checkin(self):
        if self.checkin:
            print("Voce esta com o checkin feito")
        else:
            print("Volte e faça o checkin antes da decolagem")

    def decolar(self):
        print("O avião esta decolando")

onibus1 = Passagem_Bus(120,"5B","TRE-785",leito=True)
onibus1.alterar_preco(200)
onibus1.escolher_assento()
onibus1.abastecer()

aviao1 = Passagem_Aviao(1000,"M2","G8",checkin=True)
aviao1.verificar_checkin()
aviao1.mostar_porta_embarque()
aviao1.decolar()


