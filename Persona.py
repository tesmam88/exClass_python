class Persona:
    def __init__(self,nome,idade,endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def mostrar_endereco(self):
        print(f'O endereço de {self.nome} é {self.endereco}')    

    def alterar_endereco(self,novo_endereco):
        self.endereco = novo_endereco
        return novo_endereco
    
persona1 = Persona("Durval",20,"rua das araras 45")
persona1.mostrar_endereco()
new_endereco = persona1.alterar_endereco("rua das aguas 54")
persona1.mostrar_endereco()    