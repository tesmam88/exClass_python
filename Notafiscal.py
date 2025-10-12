class Notafiscal:
    def __init__(self,numero,serie,cnpj,razao_social,data,icms,frete,ipi,valor_produto):
        self.numero = numero
        self.serie = serie
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data = data
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valor_produto = valor_produto
        self.valor_total = 0

    def obterNumero(self):
        print(f'O numero de Nota Fiscal é: {self.numero}')
        return self.numero
    
    def obterDataEmissao(self):
        print(f'A data de emissão é: {self.data}')
        return self.data
    
    def alterarRazaoSocial(self,nova_razao):
        print(f'Razão Socil alterada de {self.razao_social} para {nova_razao}')
        self.razao_social = nova_razao

    def calcularValorTotal(self):
        self.valor_total = self.valor_produto + self.icms + self.ipi + self.frete
        print(f'O valor Total é de: {self.valor_total:.2f}')
        return self.valor_total
    
notaFiscal1 = Notafiscal(1234,1,4651233,"HighTech ltda","15/10/2025",500,200,300,5000)
notaFiscal1.obterNumero()
notaFiscal1.obterDataEmissao()
notaFiscal1.alterarRazaoSocial("GloboDyne ltda")
notaFiscal1.calcularValorTotal()   
    

    

