# Importa as bibliotecas Flask, jsonify e request para criar a aplicação web e manipular requisições e respostas JSON.
from flask import Flask, jsonify, request

# Importa a biblioteca Flask-CORS para permitir requisições de diferentes origens (cross-origin)
from flask_cors import CORS

# Importa a biblioteca mysql.connector para conectar e interagir com o banco de dados MySQL.
import mysql.connector
from mysql.connector import Error
import mysql.connector

# Cria uma instância da aplicação Flask.
app = Flask(__name__)
# Habilita o CORS na aplicação Flask.
CORS(app)

# Estabelece a conexão com o banco de dados MySQL.
DB_CONFIG = {
    'host':'localhost',  # Endereço do servidor do banco de dados.
    'user':'root',       # Nome de usuário do banco de dados.
    'password':'senai',  # Senha do banco de dados.
    'database':'Papelaria'  # Nome do banco de dados.
}

#FUNÇAÕ PARA CONECTAR COM BANCO DE DADOS
def conecta_bd():
    conexaoDB = mysql.connector.connect(**DB_CONFIG)
    cursorDB = conexaoDB.cursor()
    return conexaoDB, cursorDB

#função de fechar conexão DB
def close_db(conexaoDB, cursorDB):
    cursorDB.close()
    conexaoDB.close()


# Rota para cadastro de produtos no banco de dados.
@app.route('/produto', methods=['POST'])
def cadastro_produto():
    try:
        # Obtém os dados enviados na requisição JSON.
        dados = request.json
        nome = dados.get('nome')
        descricao = dados.get('descricao')
        preco = dados.get('preco')
        quantidade = dados.get('quantidade')
        img = dados.get('img')
        
        # Verifica se todos os campos obrigatórios estão preenchidos.
        if not all([nome,descricao,preco,quantidade]):
            return jsonify({'erro': 'Dados incompletos'}), 400
        
        # Comando SQL para inserir um novo produto no banco de dados.
        conexaoDB, cursorDB = conecta_bd()
        comandoSQL = 'INSERT INTO Produto (nome, descricao, preco, quantidade, img) VALUES (%s,%s,%s,%s,%s)'
        cursorDB.execute(comandoSQL, (nome, descricao, preco, quantidade, img))
        conexaoDB.commit()  # Confirma a inserção no banco de dados.
        
        return jsonify({'mensagem':'Cadastro realizado'}), 201  # Retorna mensagem de sucesso.
    except Error as erro:
        return jsonify({'erro': f'{erro}'}), 500  # Retorna erro do MySQL.
    except KeyError:
        return jsonify({'erro': 'Faltando informação'}), 400  # Retorna erro se faltar informação no JSON.
    finally:
            close_db(conexaoDB, cursorDB)
        
        
# Rota para listar todos os produtos do banco de dados.
@app.route('/produto', methods=['GET'])
def listar_produtos():
    try:
        # Comando SQL para selecionar todos os produtos.
        conexaoDB, cursorDB = conecta_bd()
        comandoSQL = "SELECT * FROM Produto"
        
        cursorDB.execute(comandoSQL)
        produtos = cursorDB.fetchall()  # Obtém todos os produtos.)
        
        if not produtos:
            return jsonify({'mensagem':'Não há produtos'}), 200  # Retorna mensagem se não houver produtos.
        
        return jsonify(produtos), 200  # Retorna a lista de produtos.
    except Error as erro:
        return jsonify({'erro': f'{erro}'}), 500  # Retorna erro do MySQL.
    except KeyError:
        return jsonify({'erro':'Faltando informação'}), 500
    finally:
        close_db(conexaoDB, cursorDB)  # Fecha a conexão com o banco de dados.
        

# Rota para retornar um produto específico pelo ID.
@app.route('/produto/<int:id_produto>', methods=['GET'])
def get_produto(id_produto):
    try:
        # Comando SQL para selecionar um produto específico pelo ID.
        conexaoDB, cursorDB = conecta_bd()
        comandoSQL = f'SELECT * FROM Produto WHERE idProduto = %s'
        cursorDB.execute(comandoSQL, (id_produto,))
        produto = cursorDB.fetchone()  # Obtém o produto.
        
        if not produto:
            return jsonify({'mensagem':'Produto não encontrado'}), 200  # Retorna mensagem se o produto não for encontrado.
        
        return jsonify(produto), 200  # Retorna o produto encontrado.
    except Error as erro:
        return jsonify({'erro': f'{erro}'}), 500  # Retorna erro do MySQL.
    except KeyError:
        return jsonify({'erro':'Faltando informação'}), 500
    finally:
        close_db(conexaoDB, cursorDB)

# Rota para atualizar um produto existente.
@app.route('/produto', methods=['PUT'])
def update_produto():
    try:
        # Obtém os dados enviados na requisição JSON.
        dados = request.json
        idproduto = dados.get('idproduto')
        nome = dados.get('nome')
        descricao = dados.get('descricao')
        preco = dados.get('preco')
        quantidade = dados.get('quantidade')
        img = dados.get('img')
        
        # Verifica se todos os campos obrigatórios estão preenchidos.
        if not idproduto or not nome or not descricao or not preco or not quantidade:
            return jsonify({'erro': 'Faltando informação'}), 400
        
        # Comando SQL para atualizar o produto no banco de dados.
        conexaoDB, cursorDB = conecta_bd()
        comandoSQL = f'UPDATE Produto SET nome = %s, descricao = %s, preco = %s, quantidade = %s, img = %s WHERE idproduto = %s'
        cursorDB.execute(comandoSQL, (nome, descricao, preco, quantidade, img, idproduto))
        conexaoDB.commit()  # Confirma a atualização no banco de dados.

        return jsonify({'mensagem':'Alteração realizada'}), 200  # Retorna mensagem de sucesso.
    except Error as erro:
        return jsonify({'erro': f'{erro}'}), 500  # Retorna erro do MySQL.
    except KeyError:
        return jsonify({'erro':'Faltando informação'}), 500
    finally:
        close_db(conexaoDB, cursorDB)  # Fecha a conexão com o banco de dados.

# Rota para excluir um produto pelo ID.
@app.route('/produto', methods=['DELETE'])
def delete_produto():
    try:
        # Obtém o ID do produto a ser excluído enviado na requisição JSON.
        dados = request.json
        id_produto = dados.get('idproduto')

        # Comando SQL para excluir o produto no banco de dados.
        conexaoDB, cursorDB = conecta_bd()
        comandoSQL = f'DELETE FROM Produto WHERE idProduto = %s'
        cursorDB.execute(comandoSQL, (id_produto,))
        conexaoDB.commit()  # Confirma a exclusão no banco de dados.

        return jsonify({'mensagem':'Produto excluido'}), 200  # Retorna mensagem de sucesso.
    except Error as erro:
        return jsonify({'erro': f'{erro}'}), 500  # Retorna erro do MySQL.
    except KeyError:
        return jsonify({'erro':'Faltando informação'}), 500
    finally:
        close_db(conexaoDB, cursorDB)  # Fecha a conexão com o banco de dados.


# ERRO 404
@app.errorhandler(404)
def pagina_nao_encontrada(erro):
    return jsonify({'erro':'Página não encontrada'}), 404

# ERRO 405
@app.errorhandler(405)
def metodo_invalido(erro):
    return jsonify({'erro':'Método HTTP inválido'}), 405

# ERRO 500
@app.errorhandler(500)
def erro_servidor(erro):
    return jsonify({'erro':'Erro interno no servidor'}), 500       
        
# Inicia a aplicação Flask no host 0.0.0.0 e na porta 80.
if __name__ == '__main__':
    app.run(debug=True)
