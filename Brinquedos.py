class Brinquedos:
    def __init__(self,nome,cor,tamanho,preco):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco

    def brincar(self):
        print(f'Estou brincando com: {self.nome}')    

class Boneco(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco,lancar_laser):
        super().__init__(nome, cor, tamanho, preco)    
        self.lancar_laser = lancar_laser

    def desintegrar(self):
        print(f'O Boneco {self.nome} esta {self.lancar_laser}...')

class Carro(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco,velocidade_max):
        super().__init__(nome, cor, tamanho, preco)        
        self.velocidade_max = velocidade_max

    def acelerar(self):
        print(f'O carrinho {self.nome} esta acelerando á {self.velocidade_max} km/h')    

class Urso_Pelucia(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco,fazer_som):
        super().__init__(nome, cor, tamanho, preco)
        self.fazer_som = fazer_som

    def apertar(self):
        print(f'O Ursinho {self.nome} foi apertado e dice {self.fazer_som}')

class Buzz_Lightwear(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco,lutar):
        super().__init__(nome, cor, tamanho, preco)   
        self.lutar = lutar

    def encorajar(self):
        print(f'O BOneco {self.nome} esta dizendo {self.lutar}!!!')

class Video_Game(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco,play):
        super().__init__(nome, cor, tamanho, preco)     
        self.play = play   

    def jogar(self):
        print(f'O {self.nome} esta jogando {self.play}!!')

boneco1 = Boneco("Super-Homem","azul","medio",20,"lançando laser")
boneco1.desintegrar()

carro1 = Carro("Ferrari","vermelho","medio",50,150)
carro1.acelerar()

ursinho1 = Urso_Pelucia("Poof","marrom","pequeno",45,"Oi vamos brincar?")
ursinho1.apertar()

boneco2 = Buzz_Lightwear("Buzz Lightwear","cinza e roxo","medio",70,"Ao Infinito e Além")
boneco2.encorajar()

jogo1 = Video_Game("Super Nintendo","cinza escuro","normal",200,"Top Gear")
jogo1.jogar()

