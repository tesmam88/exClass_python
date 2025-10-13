class Imovel:
    def __init__(self,inscricaoMunicipal,valor_Aluguel,iptu):
        self.inscricaoMunicipal = inscricaoMunicipal
        self.valor_Aluguel = valor_Aluguel
        self.iptu = iptu

    def obter_parcela_IPTU(self):
        print(f'A parcela do IPTU é de: {self.iptu}')

    def set_valor_Aluguel(self):
        print(f'O valor do aluguel é de: {self.valor_Aluguel}')

class Casa(Imovel):
    def __init__(self, inscricaoMunicipal, valor_Aluguel, iptu,piscina,saladeestar,banheiro,suite,churrasqueira,quartos):
        super().__init__(inscricaoMunicipal, valor_Aluguel, iptu)            
        self.piscina = piscina
        self.saladeestar = saladeestar
        self.banheiro = banheiro
        self.suite = suite
        self.churrasqueira = churrasqueira
        self.quartos = quartos

    def exibir_dados_casa(self):
        print(f'A casa tem {self.piscina} piscina')
        print(f'A casa tem {self.saladeestar} sala de estar')
        print(f'A casa tem {self.banheiro} banheiros')     
        print(f'A casa tem {self.suite} suites')
        print(f'A casa tem {self.churrasqueira} charrasqueiras')
        print(f'A casa tem {self.quartos} quartos')

class Apartamento(Imovel):
    def __init__(self, inscricaoMunicipal, valor_Aluguel, iptu,saladeestar,cozinha,banheiro,suite,quartos,varanda):
        super().__init__(inscricaoMunicipal, valor_Aluguel, iptu)
        self.saladeestar = saladeestar
        self.cozinha = cozinha
        self.banheiro = banheiro
        self.suite = suite
        self.quartos = quartos
        self.varanda = varanda

    def exibir_dados_ap(self):
        print(f'O apartamento tem {self.saladeestar} sala de estar')
        print(f'O apartamento tem {self.cozinha} cozinha')
        print(f'O apartamento tem {self.banheiro} banheiros')
        print(f'O apartamento tem {self.suite} suites')
        print(f'O apartamento tem {self.quartos} quartos')
        print(f'O apartamento tem {self.varanda} varanda')

class Terreno(Imovel):
    def __init__(self, inscricaoMunicipal, valor_Aluguel, iptu,metros_quadrados):
        super().__init__(inscricaoMunicipal, valor_Aluguel, iptu)        
        self.metros_quadrados = metros_quadrados

    def exibir_terreno(self):
        print(f'O terreno tem: {self.metros_quadrados} metros quadrados')

class Chacara(Imovel):
    def __init__(self, inscricaoMunicipal, valor_Aluguel, iptu,saladeestar,quartos,banheiro,cabana,cozinha,pocodagua,riacho):
        super().__init__(inscricaoMunicipal, valor_Aluguel, iptu)            
        self.saladeestar = saladeestar
        self.quartos = quartos
        self.banheiro = banheiro
        self.cabana = cabana
        self.cozinha = cozinha
        self.pocodagua = pocodagua
        self.riacho = riacho

    def exibir_dados_chacara(self):
        print(f'A chacara tem {self.saladeestar} sala de estar')
        print(f'A chacara tem {self.quartos} quartos')
        print(f'A chacara tem {self.banheiro} banheiros')
        print(f'A chacara tem {self.cabana} cabana')
        print(f'A chacara tem {self.cozinha} cozinha')
        print(f'A chacara tem {self.pocodagua} poço dagua')
        print(f'A chacara tem {self.riacho} riacho')

casa1 = Casa(123,500,2000,1,1,2,1,1,3)
casa1.exibir_dados_casa()

ap1 = Apartamento(12,800,2500,1,1,3,2,3,1)
ap1.exibir_dados_ap()

terreno1 = Terreno(45,0,500,300)
terreno1.exibir_terreno()

chacara1 = Chacara(789,0,2000,1,5,3,1,2,1,1)
chacara1.exibir_dados_chacara()


