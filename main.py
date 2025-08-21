# ------------------------------------------------------------------#
# Sistema de Biblioteca – Modelo                                    #
# Autor: Gustavo Pereira Goncalves de Campos                        #
# Data Criação: 10/08/2025                                          #
# Data Última Atualização: 10/08/2025                               #       
# Atualização Feita por: Gustavo Pereira Goncalves de Campos        #
# Versão: 1.0                                                       #
# Principais Funções: gerar_id(), excluir_registros(),              #     
# criar_cabecalho(), carregar_dados(), cadastrar_livro(),           #
# registrar_devolucao(), cadastrar_emprestimo(),                    #
# listar_emprestimos(), listar_livros_disponiveis(),                # 
# limpar_console(), exportar_relatorio(), menu()                    #
# ------------------------------------------------------------------#

# Importações necessárias
import csv
import os
import datetime
from datetime import date, timedelta

# Estruturas de dados (Listas/Dicionários)
livros = []
usuarios = []
emprestimos = []

#----------------------------
#   Funções Principais  
#----------------------------

def gerar_id (nome_arquivo):
    if not os.path.exists(nome_arquivo) or os.path.getsize(nome_arquivo) == 0:
        return 1
    with open (nome_arquivo, "r", encoding="utf-8") as arquivo:
        reader = csv.reader(arquivo)
        next(reader, None)
        
        ids = []
        
        for row in reader:
            if row and row[0].strip().isdigit():
                ids.append(int(row[0]))
        return (max(ids) + 1) if ids else 1

def excluir_registros():
    livros = "livros.csv"
    usuarios = "usuarios.csv"
    emprestimos = "emprestimos.csv"

    if os.path.exists(livros):
        os.remove(livros)
    if os.path.exists(usuarios):
        os.remove(usuarios)
    if os.path.exists(emprestimos):
        os.remove(emprestimos)
    pass

def criar_cabecalho():
    with open ("livros.csv", "w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["id", "titulo", "autor", "ano de lancamento", "isbn", "status"])

    with open ("usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["id", "nome", "matricula", "email"])

    with open ("emprestimos.csv", "w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["id", "usuario_fk", "livro_fk", "data_retirada", "data_devolucao"])
    pass

def carregar_dados ():    
    if os.path.exists("livros.csv"):
            with open ("livros.csv", "r", encoding="utf-8") as arquivo:
                reader = csv.DictReader(arquivo)
                for linhas in arquivo:
                    livros.append(linhas)

    if os.path.exists("usuarios.csv"):
            with open ("usuarios.csv", "r", encoding="utf-8") as arquivo:
                reader = csv.DictReader(arquivo)
                for linhas in arquivo:
                    usuarios.append(linhas)

    if os.path.exists("emprestimos.csv"):
            with open ("emprestimos.csv", "r", encoding="utf-8") as arquivo:
                reader = csv.DictReader(arquivo)
                for linhas in arquivo:
                    emprestimos.append(linhas)
    pass

def cadastrar_livro ():
    id_livro = gerar_id("livros.csv")
    titulo = input("digite aqui o titulo do livro:")
    autor = input("digite aqui o autor do livro:")
    ano = input("digite aqui o ano do lançamento do livro:")
    isbn = input("digite aqui o ISBN do livro:")
    status = True

    informations = [id_livro, titulo, autor, ano, isbn, status]

    with open ("livros.csv", "a", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(informations)
        carregar_dados()

def cadastrar_usuario ():
    id_usuario = gerar_id("usuarios.csv")
    nome = input("digite aqui seu nome:")
    matricula = input("digite aqui sua matrícula:")
    email = input("digite aqui o seu e-mail:")

    informations = [id_usuario, nome, matricula, email]

    with open ("usuarios.csv", "a", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(informations)
        carregar_dados()

def registrar_devolucao (): 
    livro_fk = int(input("digite aqui o ID do livro que você deseja devolver:"))

    livros = []
    find = False

    with open ("livros.csv", "r", newline="", encoding="utf-8") as arquivo: 
        reader = csv.reader(arquivo)
        for line in reader: 
            if line[0] == str(livro_fk):
                if line[-1] == "False":
                    line[-1] = "True"
                    find = True
                else:
                    print("livro já disponível")
            livros.append(line)
    
    if not find:
        print("livro não está registrado ou já está disponivel!")
        return 

    with open("livros.csv", "w", newline="", encoding="utf-8") as arquivo: 
        writer = csv.writer(arquivo)
        writer.writerows(livros)

    print("livro devolvido!")

def cadastrar_emprestimo():
    id_emprestimo = gerar_id("emprestimos.csv")
    usuario_fk = int(input("digite o ID do usuário que será emprestado:"))
    livro_fk = int(input("digite o ID do livro que será emprestado:"))
    data_atual = date.today()
    data_futura = data_atual + timedelta(days=7)

    livros = []
    disponivel = False

    with open("livros.csv", "r", newline="", encoding="utf-8") as arquivo:
        reader = csv.reader(arquivo)
        for linha in reader:
            if linha[0] == str(livro_fk):
                if linha[-1] == "True":
                    disponivel = True
                    linha[-1] = "False"
            livros.append(linha)

    if not disponivel:
        print("este livro já está emprestado ou não existe dentro do registro de livros!")
        return

    with open("livros.csv", "w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerows(livros)

    informations = [id_emprestimo, usuario_fk, livro_fk, data_atual, data_futura]

    with open("emprestimos.csv", "a", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(informations)
        carregar_dados()

    print("empréstimo salvo com sucesso!")
    print(f"data do emprestimo: {data_atual} | data da devolucao: {data_futura}")

def listar_emprestimos():
    with open ("emprestimos.csv", "r", encoding="utf-8") as arquivo:
        reader = csv.reader(arquivo)
        # next(arquivo, None)

        for lines in reader:
            print(", ".join(lines))

def listar_livros_disponiveis(): 
    livros_disponiveis = []

    with open ("livros.csv", "r", newline="", encoding="utf-8") as arquivo: 
        reader = csv.reader(arquivo)
        for line in reader: 
            if line[-1] == "True":
                livros_disponiveis.append(line)
            
    if not livros_disponiveis:
        print("nenhum livro disponível")
        return

    print("livros disponíveis para empréstimos:")     
    for livro in livros_disponiveis:
        print(f"ID: {livro[0]} | Título: {livro[1]} | Autor: {livro[2]} | Ano: {livro[3]} | ISBN: {livro[4]}")   

def limpar_console () :
    os.system("cls")

def exportar_relatorio ():
    # livros_string = ""
    # for livro in livros:
    #     livros_string += f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}\n"

    # print(livros_string)
    pass

#----------------------------
#   Menu principal
#----------------------------

def menu():
    while True:
        print("\n=== Sistema de Biblioteca ===")
        print("1 - Cadastrar Livro")
        print("2 - Cadastrar Usuário")
        print("3 - Registrar Empréstimo")
        print("4 - Registrar Devolução")
        print("5 - Listar Livros Disponíveis")
        print("6 - Listar Empréstimos")
        print("7 - Limpar Console")
        print("8 - Exportar relatório")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            cadastrar_usuario()
        elif opcao == "3":
            cadastrar_emprestimo()
        elif opcao == "4":
            registrar_devolucao()
        elif opcao == "5":
            listar_livros_disponiveis()
        elif opcao == "6":
            listar_emprestimos()
        elif opcao == "7": 
            limpar_console()
        elif opcao == "8": 
            exportar_relatorio()
        elif opcao == "0":
            print("salva os dados e sai do sistema")
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

#----------------------------
#   Execução Principal
#----------------------------

excluir_registros()
criar_cabecalho()
menu()