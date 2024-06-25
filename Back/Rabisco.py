import mysql.connector #drive bd MySQL
import os

# CONEXÃO COM O BANCO DE DADOS
conexaoDB = mysql.connector.connect(
    host="localhost",
    user="root",
    password="senai",
    database="papelaria"
)

# FUNÇÃO PARA CADASTRAR PRODUTO
def cadastro_prod():
    imprimir_header()
    print("*** CADASTRO DE PRODUTOS ***")
    nome = input("Informe o nome do produto: ")
    descricao = input("Digite a descrição do produto: ")
    
    try:
        preco = float(input("Preço: "))
        quantidade = float(input("Quantidade: "))
        imagem = input("Informe o caminho da imagem do produto: ")
    except ValueError:
        print("ERRO! Preço e quantidade devem ser valores numéricos.")
        return # VOLTAR PARA O MENU
    
    # VALIDAÇÃO
    if (not nome) or (not descricao) or (not preco) or (not quantidade) or (not imagem):
        print("ERRO! TODOS OS CAMPOS DEVEM SER PREENCHIDOS!.")
        return
    if (preco < 0) or (quantidade < 0):
        print("ERRO! Preço e quantidade devem ser maior que zero.")
        return
    if len(nome) > 50:
        print("ERRO! O nome do produto é maior que 50 caracteres!.")
        return

    comandoSQL = f'INSERT INTO Produto VALUES(NULL, "{nome}", "{descricao}", {preco}, {quantidade}, "{imagem}")'

    try:
        cursorDB = conexaoDB.cursor()
        cursorDB.execute(comandoSQL)
        conexaoDB.commit()
    except mysql.connector.Error as erro:
        print(f"ERRO! Falha ao cadastrar: {erro}")
        return
    
    print("*** OK! Cadastro realizado com sucesso! ")
    cursorDB.close()

# BUSCAR O ID
def get_prod(id_produto):
    cursorDB = conexaoDB.cursor()
    comandoSQL = f'SELECT * FROM produto WHERE idProduto = {id_produto}'
    cursorDB.execute(comandoSQL)
    resultado = cursorDB.fetchone()
    cursorDB.close()
    return resultado

# FUNÇÃO PARA MOSTRAR OS PRODUTOS
def mostrar_prod():
    imprimir_header()
    print("*** LISTA DE PRODUTOS ***")

    try:
        cursorDB = conexaoDB.cursor()
        cursorDB.execute('SELECT * FROM Produto')
        resultados = cursorDB.fetchall()
        
        if not resultados:
            print("Não há produtos cadastrados!")
        else:
            for produto in resultados:
                print(f"ID: {produto[0]} - NOME: {produto[1]} - DESCRIÇÃO: {produto[2]} - PREÇO: {produto[3]} - QUANTIDADE: {produto[4]}")
                print(f"IMAGEM: {produto[5]}")
                print("- " * 40)

    except mysql.connector.Error as erro:
        print(f"ERRO! Falha ao cadastrar: {erro}")
        return

# FUNÇÃO PARA ALTERAR AS QUANTIDADES
def altera_quant():
    imprimir_header()
    print("*** ALTERAÇÃO DA QUANTIDADE ***")
    try:
        id_produto = int(input("Informe o ID do produto: "))
    except ValueError:
        print("ERRO! ID deve ser numérico!")
        return

    produto = get_prod(id_produto)
    
    if not produto:
        print(f"Produto com o ID {id_produto} não encontrado!")
        return

    print("Produto encontrado!")
    print(f"ID: {produto[0]} - NOME: {produto[1]} - QUANTIDADE ATUAL: {produto[4]}")

    try:
        nova_quant = int(input("Informe a nova quantidade: "))
    except ValueError:
        print("Erro! Valor da quantidade deve ser número inteiro!")
        return
    
    if nova_quant == produto[4]:
        print("Erro: A quantidade informada é igual a quantidade anterior!")
        return

    if nova_quant < 0 or nova_quant > 10000:
        print("Erro: A quantidade é INVÁLIDA!")
        return
    
    try:
        comandoSQL = f'UPDATE produto SET quantidade = {nova_quant} WHERE idProduto = {id_produto}'
        cursorDB = conexaoDB.cursor()
        cursorDB.execute(comandoSQL)
        conexaoDB.commit()
    except mysql.connector.Error as erro:
        print(f'Erro: Falha na atualização: {erro}')

    print("OK! Atualização realizada com sucesso!")
    cursorDB.close()

# FUNÇÃO PARA ALTERAR O PREÇO
def muda_preco():
    imprimir_header()
    print("*** ALTERAÇÃO DO PREÇO ***")
    try:
        id_produto = int(input("Informe o ID do produto: "))
    except ValueError:
        print("ERRO! ID deve ser numérico!")
        return

    produto = get_prod(id_produto)
    
    if not produto:
        print(f"Produto com o ID {id_produto} não encontrado!")
        return

    print("Produto encontrado!")
    print(f"ID: {produto[0]} - NOME: {produto[1]} - PREÇO: {produto[3]}")

    try:
        nova_preco = float(input("Informe o novo Preço: "))
    except ValueError:
        print("Erro! Valor do preço está inválido!")
        return
    
    if nova_preco == produto[3]:
        print("Erro: Este preço é igual ao preço anterior!")
        return

    if nova_preco < 0 or nova_preco > 1000000:
        print("Erro: Este preço é INVÁLIDO!")
        return
    
    try:
        comandoSQL = f'UPDATE produto SET preco = {nova_preco} WHERE idProduto = {id_produto}'
        cursorDB = conexaoDB.cursor()
        cursorDB.execute(comandoSQL)
        conexaoDB.commit()
    except mysql.connector.Error as erro:
        print(f'Erro: Falha na atualização: {erro}')

    print("OK! Atualização realizada com sucesso!")
    cursorDB.close()

# EXCLUIR PRODUTOS
def excluir_prod():
    imprimir_header()
    print("*** EXCLUIR PRODUTOS ***")
    try:
        id_produto = int(input("Informe o ID do produto: "))
    except ValueError:
        print("ERRO! ID deve ser numérico!")
        return

    produto = get_prod(id_produto)
    
    if not produto:
        print(f"Produto com o ID {id_produto} não encontrado!")
        return

    print("Produto encontrado!")
    print(f"ID: {produto[0]} - NOME: {produto[1]}")

    confirma = input("Digite S para confirmar a exclusão: ")
    if confirma != 'S' and confirma != "s":
        print("Exclusão cancelada!")
        return # VOLTAR AO MENU
    
    try:
        cursorDB = conexaoDB.cursor()
        comandoSQL = f'DELETE FROM Produto WHERE idProduto = {id_produto}'
        cursorDB.execute(comandoSQL)
        conexaoDB.commit()
    except mysql.connector.Error as erro:
        print(f'Erro: Falha na exclusão: {erro}')
        return
    
    print("OK! Exclusão realizada com sucesso!")

# HEADER PADRÃO
def imprimir_header():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("- " * 20)
    print("*** SISTEM PAPELARIA ***")
    print("- " * 20)
    return

# PROGRAMA PRINCIPAL
while True:
    imprimir_header()
    print("Informe a opção desejada")
    print("1 - Cadastrar produto")
    print("2 - Alterar a quantidade do produto")
    print("3 - Alterar o preço")
    print("4 - Mostrar todos os produtos")
    print("5 - Excluir um produto")
    print("6 - SAIR")
    
    opcao = input("Informe a opção desejada:")
    
    if opcao == '1':
        cadastro_prod()
    elif opcao == '2':
        altera_quant()
    elif opcao == '3':
        muda_preco()
    elif opcao == '4':
        mostrar_prod()
    elif opcao == '5':
        excluir_prod()
    elif opcao == '6':
        break
    else:
        print("Opção inválida")

    os.system('pause')

print("SISTEMA ENCERRADO!")