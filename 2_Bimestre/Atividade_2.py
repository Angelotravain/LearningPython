class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado.")
        else:
            print(f"O livro '{self.titulo}' não está disponível para empréstimo.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro '{self.titulo}' foi devolvido.")
        else:
            print(f"O livro '{self.titulo}' já está disponível.")

    def apresentar(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano de Publicação: {self.ano_publicacao}")
        print(f"Status: {status}")
        print()


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"O livro '{livro.titulo}' foi adicionado à biblioteca.")

    def listar_livros(self):
        if len(self.livros) == 0:
            print("A biblioteca não possui livros.")
        else:
            print("Livros disponíveis na biblioteca:")
            for livro in self.livros:
                livro.apresentar()


# Testando o sistema de biblioteca
livro1 = Livro("A Guerra dos Tronos", "George R.R. Martin", 1996)
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
livro3 = Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997)

biblioteca = Biblioteca()

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

livro2.emprestar()
livro1.emprestar()

biblioteca.listar_livros()

livro2.devolver()
livro1.devolver()

biblioteca.listar_livros()
