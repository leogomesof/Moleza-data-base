##############################
#       MolezaDB v1.0        #
# Autor: Leonardo Gomes      #
# Função: Classes para criar #
# a apliação CRUD.           #
# Matrícula: 2022101335      #
# Útlima revisão: 27/11/2022 #
##############################

class MyCrud:
    #Essa classe foi criada para facilitar e organizar o código entre
    #Aplicação e movimentações do banco de dados

    def __init__(self,moleza):
        import sqlite3 #Biblioteca do SQLite3
        self.conexao=sqlite3.connect(moleza) #Conexão com o banco de dados (Moleza)
        self.cursor=self.conexao.cursor()

    def fecharDB(self):
        self.conexao.close() #Fechar o banco de dados quando a aplicação terminar
        print("\n!!! BANCO DE DADOS FECHADO !!!\n")

    def criarTabela(self): #Criação da tabela e ela verifica se a mesma já foi criada
        sql='''CREATE TABLE IF NOT EXISTS pessoas (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL, cpf TEXT NOT NULL);'''
        self.cursor.execute(sql)

    def selecionar(self): #Campo de visualização de dados inseridos
        sql='''SELECT * FROM pessoas;'''
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()
        for i in resultado:
            print(i)

    def inserir(self, nome, cpf): #Campo para inserir dados
        sql='''INSERT INTO pessoas (nome, cpf) VALUES (?,?);'''
        self.cursor.execute(sql,(nome,cpf))
        self.conexao.commit()

    def alterar(self, id, nome, cpf): #Campo de alteração de dados de acordo com a ID, nome e CPF
        sql='''UPDATE pessoas SET nome = ?, cpf = ? WHERE id = ?;'''
        self.cursor.execute(sql,(nome, cpf, id))
        self.conexao.commit()

    def deletar(self, id): #Campo para apagar os dados de acordo com a ID, nome e CPF
        sql='''DELETE FROM pessoas WHERE id = ?;'''
        self.cursor.execute(sql,(id,))
        self.conexao.commit()