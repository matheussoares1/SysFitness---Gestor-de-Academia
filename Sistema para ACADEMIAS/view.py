import sqlite3 as lite

""" Criando Conexão """
try:
    conn = lite.connect('cadastro_clientes.db') #nome do banco de dados
    print("Conexão realizada com sucesso! ")
except lite.Error as e:
    print("Erro ao conectar com banco de dados: ", e)

"""Tabela de Personais--------------------------------------------"""
#Inserir Personais

def inserir_personais(i):
	with conn:
		cur = conn.cursor()
		query = "INSERT INTO personais (nome, sobrenome, preco) VALUES (?,?,?)"

		cur.execute(query, i)

#inserir_personais(['Oscar', 'Paulino', 50])

#VER todos os ppersonais (SELECIONAR) R
def ver_personais():
	lista = []
	with conn:
		cur = conn.cursor()
		cur.execute('SELECT * FROM personais')
		linha = cur.fetchall()

		for i in linha:
			lista.append(i)
	return lista

#print(ver_personais())

def atualizar_personais(i):
	with conn:
		cur = conn.cursor()
		query = "UPDATE personais SET nome=?, sobrenome=?, preco=? WHERE id=?"

		cur.execute(query, i)


#atualizar_personais(l)

#print(ver_personais())


def deletar_personais(i):
	with conn:
		cur = conn.cursor()
		query = "DELETE FROM personais WHERE id=?"

		cur.execute(query, i)


#deletar_personais([1])
#print(ver_personais())


#TURMAS---------------------------------------

def criar_turmas(i):
	with conn:
		cur = conn.cursor()
		query = "INSERT INTO personais (nome, personal_nome, data_inicio) VALUES (?,?,?)"

		cur.execute(query, i)


#VER todas as turmas
def ver_turmas():
	lista = []
	with conn:
		cur = conn.cursor()
		cur.execute('SELECT * FROM turmas')
		linha = cur.fetchall()

		for i in linha:
			lista.append(i)
	return lista


#Atualizar as turmas
def atualizar_turmas(i):
	with conn:
		cur = conn.cursor()
		query = "UPDATE turmas SET nome=?, personal_nome=?, data_inicio=? WHERE id=?"

		cur.execute(query, i)


#Deletar Turma
def deletar_turmas(i):
	with conn:
		cur = conn.cursor()
		query = "DELETE FROM turmas WHERE id=?"

		cur.execute(query, i)


#Tabela de Clientes ------------------------------------------------------------------------------

def criar_clientes(i):
	with conn:
		cur = conn.cursor()
		query = "INSERT INTO clientes (nome, cpf, telefone, endereco, imagem, data_nasc, meses_pagos, turma_nome) VALUES (?,?,?,?,?,?,?,?)"

		cur.execute(query, i)


#VER todas as turmas
def ver_clientes():
	lista = []
	with conn:
		cur = conn.cursor()
		cur.execute('SELECT * FROM clientes')
		linha = cur.fetchall()

		for i in linha:
			lista.append(i)
	return lista


#Atualizar as turmas
def atualizar_clientes(i):
	with conn:
		cur = conn.cursor()
		query = "UPDATE turmas SET nome=?, cpf=?, telefone=?, endereco=?, imagem=?, data_nasc=?, meses_pagos=?, turma_nome=? WHERE id=?"

		cur.execute(query, i)


#Deletar Turma
def deletar_turmas(i):
	with conn:
		cur = conn.cursor()
		query = "DELETE FROM turmas WHERE id=?"

		cur.execute(query, i)

