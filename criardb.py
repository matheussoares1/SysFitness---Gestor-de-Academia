""" Crindo Banco de Dados """
import sqlite3

""" Criando Conexão """
try:
    conn = sqlite3.connect('cadastro_clientes.db') #nome do banco de dados
    print("Conexão realizada com sucesso! ")
except sqlite3.Error as e:
    print("Erro ao conectar com banco de dados: ", e)

#Criando tabela de personais

try:
    with conn:
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS personais(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    sobrenome TEXT,
                    preco REAL
        ) """)

        print("TABELA PERSONAIS CRIADA COM SUCESSO")

except sqlite3.Error as e:
    print("Erro ao criar a tabela PERSONAIS ", e)

""" Criando Tabela de turmas"""

try:
    with conn:
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS turmas(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    personal_nome TEXT,
                    data_inicio DATE,
                    FOREIGN KEY (personal_nome) REFERENCES personais (nome) ON UPDATE CASCADE ON DELETE CASCADE
        ) """)

        print("TABELA TURMAS CRIADA COM SUCESSO")

except sqlite3.Error as e:
    print("Erro ao criar a tabela turmas", e )

try:
    with conn:
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS clientes(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    cpf TEXT,
                    telefone TEXT,
                    endereco TEXT,
                    imagem TEXT,
                    data_nasc DATE,
                    meses_pagos INT,
                    turma_nome TEXT,
                    
                    FOREIGN KEY (turma_nome) REFERENCES turmas (nome) ON DELETE CASCADE
        ) """)

        print("TABELA CLIENTES CRIADA COM SUCESSO")

except sqlite3.Error as e:
    print("Erro ao criar a tabela CLIENTES", e )



