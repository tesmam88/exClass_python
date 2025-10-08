class Livro:
    def __init__(self,nome,autor,editor,paginas):
        self.nome = nome
        self.autor = autor
        self.editor = editor
        self.paginas = paginas

    def Alterar_editora(self,nova_editora):
        self.editor = nova_editora
        return True

    def Listar_qntas_paginas(self,listar_pgs):
        self.paginas = listar_pgs
        return True

livro = Livro("It","Stephen King","Suma","300")
print(livro.nome , livro.autor, livro.editor, livro.paginas)

livro.Alterar_editora("Cia das Letras")
livro.Listar_qntas_paginas("450")

print(livro.nome , livro.autor, livro.editor, livro.paginas)
