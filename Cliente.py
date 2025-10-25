from datetime import datetime,date,time

class Cliente:
    def __init__(self,nome,cpf,telefone,email,endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.agendamentos = []

    def cadastrar(self):
        print(f"O cliente {self.nome} foi cadastrado com sucesso.")

    def atualizar_dados(self,novo_endereco,novo_telefone,novo_email):
        if novo_endereco:
            self.endereco = novo_endereco
        elif novo_telefone:
            self.telefone = novo_telefone
        elif novo_email:
            self.email = novo_email
        print(f"Os dados do cliente {self.nome} foram atualizados.")  

    def visualizarAgenda(self):
        if not self.agendamentos:
            print("Não há agendamentos.")
        else:
           print(f"Agendamento de {self.nome}:")
           for agenda in self.agendamentos: 
                print(f"{agenda.data} ás {agenda.hora}, com {agenda.profissional.nome} ({agenda.status}) ")

class Profissional:
    def __init__(self,nome,especialidade,registro,telefone):
        self.nome = nome
        self.especilidade = especialidade
        self.registro = registro
        self.telefone = telefone
        self.disponibilidade = True
        self.horarios = []

    def disponibilidade_horarios(self,horario):
        return horario in self.horarios
    def add_horarios(self,horario):
        if horario not in self.horarios:
            self.horarios.append(horario)
            print(f"O horario {horario} adicionando para {self.nome}.")
        else:
            print("Horario já existente.")
    def remover_horario(self,horario):
        if horario in self.horarios:
            self.horarios.remove(horario)
            print(f"Horario {horario} foi removido para {self.nome}.")
        else:
            print("Horario não encontrado.")

class Servico:
    def __init__(self,codigo,nome,descricao,duracao,preco):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.duracao = duracao
        self.preco = preco

    def calcular_preco(self,desconto=0):
        valor_final = self.preco - (self.preco/desconto*100)
        return valor_final
    def atualizar_Descr(self,nova_descricao):
        self.descricao = nova_descricao
        print(f"Descrição de Serviço {self.nome} atualizada.")
    def listar_servicos(self):
        print(f"Codigo: {self.codigo} | Nome: {self.nome} | Preço: {self.preco:.2f}")    

class Pagamento:
    def __init__(self, idPagamento, valor, formaPagamento):
        self.idPagamento = idPagamento
        self.valor = valor
        self.formaPagamento = formaPagamento
        self.data = date.today()
        self.status = "Pendente"

    def processarPagamento(self):
        self.status = "Pago"
        print(f"Pagamento de R${self.valor:.2f} processado com sucesso.")

    def verificarStatus(self):
        print(f"Status do pagamento: {self.status}")

    def emitirRecibo(self):
        if self.status == "Pago":
            print(f"Recibo: Pagamento {self.idPagamento} no valor de R${self.valor:.2f} realizado em {self.data}.")
        else:
            print("Pagamento ainda não realizado.")

class Agedamento:
    def __init__(self, codigo, data, hora, cliente, profissional, servico):
        self.codigo = codigo
        self.data = data
        self.hora = hora
        self.cliente = cliente
        self.profissional = profissional
        self.servico = servico
        self.status = "Pendente"
        self.pagamento = None

    def criarAgenda(self):
        if self.hora not in self.profissional.horarios:
            print(f"O horário {self.hora} não está disponível para {self.profissional.nome}.")
        else:
            self.status = "Agendado"
            self.cliente.agendamentos.append(self)
            print(f"Agendamento criado para {self.cliente.nome} com {self.profissional.nome} em {self.data} às {self.hora}.")

    def cancelar(self):
        self.status = "Cancelado"
        print(f"Agendamento {self.codigo} cancelado.")

    def confirmar(self):
        self.status = "Confirmado"
        print(f"Agendamento {self.codigo} confirmado.")

    def adicionarPagamento(self, pagamento):
        self.pagamento = pagamento
        print(f"Pagamento vinculado ao agendamento {self.codigo}.") 


    if __name__ == "__main__":
        # Criar cliente
        cliente1 = Cliente("Ana Silva", "12345678900", "99999-9999", "ana@email.com", "Rua A, 100")
        cliente1.cadastrar()
    
        # Criar profissional
        prof1 = Profissional("Marcos Oliveira", "Esteticista", "CRP1234", "98888-8888")
        prof1.add_horario("14:00")
        prof1.add_horario("15:00")
    
        # Criar serviço
        serv1 = Servico(1, "Limpeza de Pele", "Limpeza profunda da pele", 60, 120.0)
    
        # Criar agendamento
        ag1 = Agendamento(101, "2025-10-25", "14:00", cliente1, prof1, serv1)
        ag1.criarAgenda()
        ag1.confirmar()
    
        # Criar pagamento
        pag1 = Pagamento(1, serv1.preco, "Cartão de Crédito")
        pag1.processarPagamento()
        ag1.adicionarPagamento(pag1)
    
        # Visualizar agenda do cliente
        cliente1.visualizar_agenda()

    