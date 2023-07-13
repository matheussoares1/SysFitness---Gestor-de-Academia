import sqlite3
from tkinter import messagebox

class SistemaDeRegistro:
    def __init__(self):
        self.conexao = sqlite3.connect("estudante.db")
        self.cursor = self.conexao.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS estudantes (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL,
                                email TEXT NOT NULL, 
                                tel TEXT NOT NULL,
                                sexo TEXT NOT NULL,
                                data_nascimento TEXT NOT NULL,
                                endereco TEXT NOT NULL,
                                curso TEXT NOT NULL,
                                picture TEXT NOT NULL)''')
        
    def Registro_Estudante(self, estudantes):
        self.cursor.execute(''' INSERT INTO estudantes(nome,email,tel,sexo,data_nascimento,endereco,curso,picture) VALUES (?,?,?,?,?,?,?,?) ''',
            (estudantes))
        self.conexao.commit()

        # mostrando mensagem de sucesso

        messagebox.showinfo("Sucesso", "Registro feito com sucesso!")

    def MostrarEstudantes(self):
        self.cursor.execute(''' SELECT * FROM estudantes ''')
        dados = self.cursor.fetchall()
        return dados
    def BuscaEstudante(self, id):
        self.cursor.execute(''' SELECT * FROM estudantes WHERE id=?''', (id,))
        dados = self.cursor.fetchone()
        return dados

    def AtualizarDados(self, novos_valores):
        query = "UPDATE estudantes SET nome = ?, email = ?, tel = ?, sexo = ?, data_nascimento = ?, endereco = ?, curso = ?, picture = ? WHERE id = ?"
        self.cursor.execute(query, novos_valores)
        self.conexao.commit()

        messagebox.showinfo("Sucesso", f"Estudante com id: {novos_valores[8]} foi atualizado!")

    def DeletarEstudante(self, id):
        self.cursor.execute(''' DELETE FROM estudantes WHERE id = ? ''', (id,))
        self.conexao.commit()

        messagebox.showinfo("Sucesso", f"Estudante com id: {id} foi deletado!")


sistema = SistemaDeRegistro()