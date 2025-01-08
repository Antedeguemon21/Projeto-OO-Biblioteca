# Projeto-OO-Biblioteca

# Sistema de Biblioteca - Alexandria Python

## Descrição

Este é um sistema simples de biblioteca desenvolvido em Python utilizando a biblioteca Tkinter para a interface gráfica. O sistema permite registrar usuários, cadastrar livros, realizar empréstimos e devoluções, além de visualizar os livros e usuários cadastrados. As informações são salvas em um arquivo JSON, garantindo persistência de dados entre as execuções.

## Funcionalidades

- **Cadastro de Livros**: Permite adicionar livros à biblioteca, incluindo o título e o autor.
- **Cadastro de Usuários**: Permite registrar usuários com seus respectivos nomes.
- **Empréstimo de Livros**: Usuários podem emprestar livros disponíveis na biblioteca.
- **Devolução de Livros**: Permite que os usuários devolvam livros que foram emprestados.
- **Listar Livros Disponíveis**: Exibe todos os livros disponíveis para empréstimo.
- **Listar Usuários Cadastrados**: Exibe todos os usuários cadastrados na biblioteca.

## Requisitos

Para executar este projeto, você precisa ter o Python 3 instalado em seu sistema.

Além disso, a biblioteca Tkinter vem pré-instalada com o Python, então você não precisa instalar nada adicional.

## Como Usar

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu-usuario/sistema-biblioteca-python.git
   cd sistema-biblioteca-python
   ```

2. **Execute o código**:

   No terminal, navegue até a pasta onde o código foi clonado e execute o arquivo Python:

   ```bash
   python biblioteca.py
   ```

3. **Utilização**:

   - Na interface gráfica, você pode realizar as seguintes ações:
     - **Cadastrar Livros**: Digite o título e o autor, e clique em "Adicionar Livro".
     - **Cadastrar Usuários**: Digite o nome do usuário e clique em "Registrar Usuário".
     - **Emprestar Livro**: Escolha um usuário e um livro para emprestar.
     - **Devolver Livro**: Escolha um usuário e um livro para devolver.
     - **Listar Livros Disponíveis**: Exibe todos os livros disponíveis para empréstimo.
     - **Listar Usuários Cadastrados**: Exibe todos os usuários cadastrados na biblioteca.

4. **Persistência de Dados**: 

   As informações sobre livros, usuários, empréstimos e devoluções são salvas em um arquivo JSON chamado `biblioteca.json`. Isso garante que os dados persistam entre as execuções do programa.

## Estrutura de Arquivos

```
/sistema-biblioteca-python
│
├── biblioteca.py           # Código principal do sistema
├── biblioteca.json         # Arquivo JSON para persistência de dados
└── README.md               # Este arquivo
```

## Como Funciona o Código

### Estrutura do Sistema:

- **Item**: Representa um item genérico, com atributos como `id_item`, `titulo`, e `disponivel`. A classe `Livro` herda dessa classe e adiciona o atributo `autor` e o controle de empréstimos.
- **Livro**: Herda de `Item` e possui o atributo adicional `autor`. Ele também gerencia quem está emprestando o livro.
- **Usuario**: Representa um usuário da biblioteca, com `id_usuario` e `nome`. Um usuário pode registrar seus empréstimos.
- **Emprestimo**: Controla o processo de empréstimo de um livro a um usuário.
- **Biblioteca**: Gerencia todos os itens (livros e outros itens) e usuários. Permite o registro de novos livros e usuários, além de listar itens disponíveis para empréstimo.

### Funcionalidade JSON

- **Salvamento**: As informações sobre livros e usuários são salvas em um arquivo JSON (`biblioteca.json`).
- **Carregamento**: Ao iniciar o programa, as informações são carregadas do arquivo JSON, garantindo que os dados persistam entre as execuções.

## Dependências

Este projeto não possui dependências externas além do Tkinter, que já vem com o Python. Portanto, você não precisa instalar pacotes adicionais para executar o sistema.
