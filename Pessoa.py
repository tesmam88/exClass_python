## Classe Pessoa: Crie uma classe que modele uma pessoa. Esta classe deve possuir os seguintes atributos:
##Nome
##Idade
##Endereço

class Pessoa:
    def __init__(self,nome,idade,endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    
    def imprimir(self,nome,idade,endereco):
        print(f'Nome:{nome}, Idade:{idade}, Endereço:{endereco}')

pessoa = Pessoa("Mario","35","rua alameda dos anjos,45")       
print(pessoa.nome,pessoa.idade,pessoa.endereco) 
