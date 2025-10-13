class Ingresso:
    def __init__(self,preco,setor):
        self.preco = preco
        self.setor = setor

    def alterar_preco(self,novo_preco):    
        print(f'Preço do Ingresso {self.preco} alterado para {novo_preco}')
        self.preco = novo_preco

    def mostrar_setor(self):
        print(f'Voce selecionou o setor {self.setor} para função')  

class Ingresso_VIP(Ingresso):
    def __init__(self, preco, setor,camarote,open_bar,open_food,estacionamento):
        super().__init__(preco, setor)          
        self.camarote = camarote
        self.open_bar = open_bar
        self.open_food = open_food
        self.estacionamento = estacionamento

    def pegar_bebida(self):
        if self.open_bar:
            print('Voce pegou uma bebida no open bar')
        else:
            print('Uso indisponivel para open bar')

    def pegar_comida(self):
        if self.open_food:
            print('Voce pegou comida no open food')
        else:
            print("Não há acesso ao open food")        

    def acessar_camarote(self):
        if self.acessar_camarote:
            print('Voce tem acesso ao camarote')
        else:
            print('Não há ingresso para o camarote')

    def mostrar_beneficios(self):
        print("----Ingresso VIP----")
        print(f'Setor: {self.setor}')
        print(f"Camarote: {'Sim' if self.camarote else 'Não'}")   
        print(f"Open-Bar: {'Sim' if self.open_bar else 'Não'}")
        print(f"Open-Food: {'Sim' if self.open_food else 'Não'}")
        print(f"Esacionamento: {'Sim' if self.estacionamento else 'Não'}")
        print(f'Preço: {self.preco:.2f}')

print("---Ingresso Normal---")
ingresso1 = Ingresso(40,"Arquibancada")
ingresso1.mostrar_setor()
ingresso1.alterar_preco(50)


ingresso2 = Ingresso_VIP(100,'VIP',camarote=True,open_bar=True,open_food=False,estacionamento=True)
ingresso2.mostrar_beneficios()
ingresso2.pegar_bebida()
ingresso2.acessar_camarote()