import json
from tkinter import *


class Item:
    def __init__(self, id_item, titulo, disponivel=True):
        self.id_item = id_item
        self.titulo = titulo
        self.disponivel = disponivel
    
    def emprestar(self, usuario):
        if self.disponivel:
            self.disponivel = False
            return True
        return False
    
    def devolver(self):
        self.disponivel = True
    
    def to_dict(self):
        return {
            'id_item': self.id_item,
            'titulo': self.titulo,
            'disponivel': self.disponivel
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['id_item'], data['titulo'], data['disponivel'])


class Livro(Item):
    def __init__(self, id_livro, titulo, autor, disponivel=True):
        super().__init__(id_livro, titulo, disponivel)
        self.autor = autor
        self.usuario_emprestado = None
    
    def emprestar(self, usuario):
        if self.disponivel:
            self.disponivel = False
            self.usuario_emprestado = usuario
            return True
        return False
    
    def devolver(self):
        self.disponivel = True
        self.usuario_emprestado = None
    
    def to_dict(self):
        data = super().to_dict()
        data['autor'] = self.autor
        return data

    @classmethod
    def from_dict(cls, data):
        livro = super().from_dict(data)
        livro.autor = data['autor']
        return livro


class Usuario:
    def __init__(self, id_usuario, nome):
        self.id_usuario = id_usuario
        self.nome = nome
        self.historico_emprestimos = []
    
    def registrar_emprestimo(self, item):
        self.historico_emprestimos.append(item)

    def to_dict(self):
        return {
            'id_usuario': self.id_usuario,
            'nome': self.nome,
            'historico_emprestimos': [item.id_item for item in self.historico_emprestimos]
        }

    @classmethod
    def from_dict(cls, data):
        usuario = cls(data['id_usuario'], data['nome'])
        return usuario


class Emprestimo:
    def __init__(self, usuario, item):
        self.usuario = usuario
        self.item = item
    
    def realizar_emprestimo(self):
        if self.item.emprestar(self.usuario):
            self.usuario.registrar_emprestimo(self.item)
            return True
        return False
    
    def realizar_devolucao(self):
        self.item.devolver()
        return True


class Biblioteca:
    def __init__(self):
        self.itens = [] 
        self.usuarios = []
    
    def adicionar_item(self, item):
        self.itens.append(item)
    
    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
    
    def listar_itens_disponiveis(self):
        return [f"Título: {item.titulo}, Autor: {getattr(item, 'autor', 'N/A')}" for item in self.itens if item.disponivel]

    def to_dict(self):
        return {
            'itens': [item.to_dict() for item in self.itens],
            'usuarios': [usuario.to_dict() for usuario in self.usuarios]
        }

    @classmethod
    def from_dict(cls, data):
        biblioteca = cls()
        biblioteca.itens = [Livro.from_dict(item_data) for item_data in data['itens']]
        biblioteca.usuarios = [Usuario.from_dict(usuario_data) for usuario_data in data['usuarios']]
        return biblioteca


def salvar_biblioteca_em_json(biblioteca, filename="biblioteca.json"):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(biblioteca.to_dict(), f, ensure_ascii=False, indent=4)

def carregar_biblioteca_de_json(filename="biblioteca.json"):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return Biblioteca.from_dict(data)
    except FileNotFoundError:
        return Biblioteca()


class Application:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Sistema de Biblioteca")
        self.biblioteca = carregar_biblioteca_de_json()


        self.widget1 = Frame(self.master)
        self.widget1.pack()


        self.msg = Label(self.widget1, text="Sistema de Biblioteca - Alexandria Python")
        self.msg.pack()

        self.lbl_titulo = Label(self.widget1, text="Título do Livro:")
        self.lbl_titulo.pack()
        self.entry_titulo = Entry(self.widget1)
        self.entry_titulo.pack()

        self.lbl_autor = Label(self.widget1, text="Autor do Livro:")
        self.lbl_autor.pack()
        self.entry_autor = Entry(self.widget1)
        self.entry_autor.pack()

        self.btn_adicionar_livro = Button(self.widget1, text="Adicionar Livro", command=self.adicionar_livro)
        self.btn_adicionar_livro.pack()


        self.lbl_nome_usuario = Label(self.widget1, text="Nome do Usuário:")
        self.lbl_nome_usuario.pack()
        self.entry_nome_usuario = Entry(self.widget1)
        self.entry_nome_usuario.pack()

        self.btn_registrar_usuario = Button(self.widget1, text="Registrar Usuário", command=self.registrar_usuario)
        self.btn_registrar_usuario.pack()

        self.lbl_usuario_emprestimo = Label(self.widget1, text="Nome do Usuário para Emprestar Livro:")
        self.lbl_usuario_emprestimo.pack()
        self.entry_usuario_emprestimo = Entry(self.widget1)
        self.entry_usuario_emprestimo.pack()

        self.lbl_livro_emprestimo = Label(self.widget1, text="Título do Livro para Emprestar:")
        self.lbl_livro_emprestimo.pack()
        self.entry_livro_emprestimo = Entry(self.widget1)
        self.entry_livro_emprestimo.pack()

        self.btn_emprestar_livro = Button(self.widget1, text="Emprestar Livro", command=self.emprestar_livro)
        self.btn_emprestar_livro.pack()

        
        self.lbl_usuario_devolucao = Label(self.widget1, text="Nome do Usuário para Devolver Livro:")
        self.lbl_usuario_devolucao.pack()
        self.entry_usuario_devolucao = Entry(self.widget1)
        self.entry_usuario_devolucao.pack()

        self.lbl_livro_devolucao = Label(self.widget1, text="Título do Livro para Devolver:")
        self.lbl_livro_devolucao.pack()
        self.entry_livro_devolucao = Entry(self.widget1)
        self.entry_livro_devolucao.pack()

        self.btn_devolver_livro = Button(self.widget1, text="Devolver Livro", command=self.devolver_livro)
        self.btn_devolver_livro.pack()

        
        self.btn_listar_livros = Button(self.widget1, text="Listar Livros Disponíveis", command=self.listar_livros)
        self.btn_listar_livros.pack()

        
        self.btn_listar_usuarios = Button(self.widget1, text="Listar Usuários Cadastrados", command=self.listar_usuarios)
        self.btn_listar_usuarios.pack()

        self.resultados = Label(self.widget1, text="")
        self.resultados.pack()

    def adicionar_livro(self):
        titulo = self.entry_titulo.get()
        autor = self.entry_autor.get()
        if titulo and autor:
            livro_id = len(self.biblioteca.itens) + 1
            livro = Livro(livro_id, titulo, autor)
            self.biblioteca.adicionar_item(livro)
            salvar_biblioteca_em_json(self.biblioteca)
            self.resultados.config(text=f"Livro '{titulo}' adicionado com sucesso!")
            
            self.entry_titulo.delete(0, END)
            self.entry_autor.delete(0, END)
        else:
            self.resultados.config(text="Erro: Preencha todos os campos.")

    def registrar_usuario(self):
        nome_usuario = self.entry_nome_usuario.get()
        if nome_usuario:
            usuario_id = len(self.biblioteca.usuarios) + 1
            usuario = Usuario(usuario_id, nome_usuario)
            self.biblioteca.registrar_usuario(usuario)
            salvar_biblioteca_em_json(self.biblioteca)
            self.resultados.config(text=f"Usuário '{nome_usuario}' registrado com sucesso!")
            
            self.entry_nome_usuario.delete(0, END)
        else:
            self.resultados.config(text="Erro: Preencha o nome do usuário.")

    def emprestar_livro(self):
        nome_usuario = self.entry_usuario_emprestimo.get()
        titulo_livro = self.entry_livro_emprestimo.get()
        
        
        usuario = next((u for u in self.biblioteca.usuarios if u.nome == nome_usuario), None)
        
        item = next((i for i in self.biblioteca.itens if i.titulo == titulo_livro), None)
        
        if usuario and item:
            emprestimo = Emprestimo(usuario, item)
            if emprestimo.realizar_emprestimo():
                salvar_biblioteca_em_json(self.biblioteca)
                self.resultados.config(text=f"Item '{titulo_livro}' emprestado para '{nome_usuario}'.")
            else:
                self.resultados.config(text=f"O item '{titulo_livro}' não está disponível para empréstimo.")
        else:
            self.resultados.config(text="Erro: Usuário ou Item não encontrados.")

    def devolver_livro(self):
        nome_usuario = self.entry_usuario_devolucao.get()
        titulo_livro = self.entry_livro_devolucao.get()

       
        usuario = next((u for u in self.biblioteca.usuarios if u.nome == nome_usuario), None)
       
        item = next((i for i in self.biblioteca.itens if i.titulo == titulo_livro), None)
        
        if usuario and item:
            emprestimo = Emprestimo(usuario, item)
            if emprestimo.realizar_devolucao():
                salvar_biblioteca_em_json(self.biblioteca)
                self.resultados.config(text=f"Item '{titulo_livro}' devolvido por '{nome_usuario}'.")
            else:
                self.resultados.config(text=f"O item '{titulo_livro}' não foi emprestado para '{nome_usuario}'.")
        else:
            self.resultados.config(text="Erro: Usuário ou Item não encontrados.")

    def listar_livros(self):
        
        lista_itens = Toplevel(self.master)
        lista_itens.title("Itens Cadastrados")

        itens_disponiveis = self.biblioteca.listar_itens_disponiveis()
        if itens_disponiveis:
            lista_texto = "\n".join(itens_disponiveis)
        else:
            lista_texto = "Não há itens disponíveis no momento."
        
        lbl_lista_itens = Label(lista_itens, text=lista_texto, justify=LEFT)
        lbl_lista_itens.pack()

    def listar_usuarios(self):
       
        lista_usuarios = Toplevel(self.master)
        lista_usuarios.title("Usuários Cadastrados")

        usuarios_cadastrados = [f"ID: {u.id_usuario}, Nome: {u.nome}" for u in self.biblioteca.usuarios]
        if usuarios_cadastrados:
            lista_texto = "\n".join(usuarios_cadastrados)
        else:
            lista_texto = "Não há usuários cadastrados."
        
        lbl_lista_usuarios = Label(lista_usuarios, text=lista_texto, justify=LEFT)
        lbl_lista_usuarios.pack()


root = Tk()
app = Application(master=root)
root.mainloop()
