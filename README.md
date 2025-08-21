
# Trabalho Primeiro Semestre - Capacitação Python 🐍

Sistema simples de controle de estoque para uma biblioteca, onde basicamente o usuário pode gerenciar entrada e saída de livros (empréstimos), visualizar livros disponíveis, visualizar os empréstimos e fazer devolução de livros.

## ✅ Execução do programa

Para rodar o programa é necessário apenas ter o Python instalado, para isso basta rodar o comando abaixo: 

```bash
sudo apt install python3
```
Se você estiver no Windows, basta clicar [nesse link!](https://www.python.org/downloads/)

Para rodar o programa é recomendado ter alguma IDE, recomendo o [Visual Studio Code](https://code.visualstudio.com/Download)

Caso preferir, é possível rodar via CLI também com os comandos abaixo: 
- Linux
```bash
python3 main.py
```
- Windows
```bash
python ./main.py
```

## 💻 Funções principais

As principais funções dentro do sistema são: 

- **gerar_id()** - Responsável por gerar os ID´s auto incrementais para os registros de livros, usuários e empréstimos realizados.
- **excluir_registros()** - Responsável por excluir os arquivos .csv em cada execução caso já existam, dessa forma sempre que o programa rodar esses arquivos serão criados de forma automática.
- **criar_cabecalho()** - Responsável por criar os cabeçalhos dos arquivos .csv, sempre que abrir os arquivos .csv ele já adiciona por padrão o cabeçalho que por sua vez corresponde aos nomes das colunas de uma tabela no banco de dados.
- **carregar_dados()** - Responsável por alimentar o array de informações dos usuários, dos livros e dos empréstimos com as informações inseridas.
- **cadastrar_livros()** - Responsável por inserir informações relacionadas aos livro que são inseridas pelo usuário dentro do array de livros.
- **cadastrar_usuarios()** - Responsável por inserir informações relacionadas aos usuários que são inseridas pelo usuário dentro do array de usuários.
- **registrar_devolucao()** - Responsável por mudar o status de um livro, tornando ele disponível para outro usuário fazer um empréstimo.
- **cadastrar_emprestimo()** - Responsável por inserir informações relacionadas aos empréstimos que são inseridas pelo usuário dentro do array de empréstimos.
- **listar_emprestimos()** - Responsável por listar todos os empréstimos registrados no tempo de execução do programa.
- **listar_livros_disponiveis()** - Responsável por listar todos os livros que possuem o status de disponíveis dentro do tempo de execução.
- **limpar_console()** - Responsável por limpar o console e facilitar a visualização da execução do programa.
- **exportar_relatorio()** - Responsável por exportar um relatório sobre os livros disponíveis, os usuários presentes no sistema e todos os empréstimos feitos durante o tempo de execução.
- **menu()** - Responsável por exibir o menu de opções no console para o usuário.
