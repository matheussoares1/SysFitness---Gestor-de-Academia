from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry
from datetime import date
from main import SistemaDeRegistro


co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#146C94"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde




# Criando a janela
janela = Tk()
janela.title("Cadastro de Alunos")
janela.geometry("810x535")
janela.configure(background="#feffff")
janela.resizable(width=FALSE, height=FALSE)

# Criando frames
# Header
frame_logo = Frame(janela, width = 810, height = 52, bg=co6)
frame_logo.grid(row = 0, column = 0, pady = 0, padx = 0, sticky = NSEW, columnspan = 5)

# Seções
frame_botoes = Frame(janela, width = 100, height = 200, bg=co1, relief = RAISED)
frame_botoes.grid(row = 1, column = 0, pady = 1, padx = 0, sticky = NSEW,)

frame_details = Frame(janela, width = 800, height = 100, bg=co1, relief = SOLID)
frame_details.grid(row = 1, column = 1, pady = 1, padx = 10, sticky = NSEW,)

# Tabela

frame_tabela = Frame(janela, width = 800, height = 100, bg=co1, relief = SOLID)
frame_tabela.grid(row = 3, column = 0, pady = 0, padx = 10, sticky = NSEW, columnspan = 5)

# frame logo
global imagem, imagem_string, l_imagem

imagem = Image.open("logo.png")
imagem = imagem.resize((50,50))
imagem = ImageTk.PhotoImage(imagem)
app_logo = Label(frame_logo, image = imagem, text = "  Sistema de Registro de Aluno", width = 850, compound = LEFT, anchor = NW, font = ("Verdana 15"), bg = co6, fg = co1)
app_logo.place(x = 5, y = 0)


imagem = Image.open("logo.png")
imagem = imagem.resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)
l_imagem = Label(frame_details, image = imagem, bg = co1, fg = co4)
l_imagem.place(x = 390, y = 10)

# Criando objeto do sistema de registro
sistema = SistemaDeRegistro()


    # creating a treeview with dual scrollbars
list_header = ['id','Nome','email',  'Telefone','sexo','Data', 'Endereço','Curso']

    # view all students
df_list = sistema.MostrarEstudantes()

tree_aluno = ttk.Treeview(frame_tabela, selectmode="extended",columns=list_header, show="headings")

    # vertical scrollbar
vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_aluno.yview)
    # horizontal scrollbar
hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_aluno.xview)

tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
tree_aluno.grid(column=0, row=1, sticky='nsew')
vsb.grid(column=1, row=1, sticky='ns')
hsb.grid(column=0, row=2, sticky='ew')
frame_tabela.grid_rowconfigure(0, weight=12)

hd=["nw","nw","nw","center","center","center","center","center","center"]
h=[40,150,150,70,70,70,120,100,100]
n=0

for col in list_header:
    tree_aluno.heading(col, text=col.title(), anchor=NW)
        # adjust the column's width to the header string
    tree_aluno.column(col, width=h[n],anchor=hd[n])

    n+=1

for item in df_list:
    tree_aluno.insert('', 'end', values=item)



# Funções de CRUD
def adicionar_aluno():
    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    sexo = c_sexo.get()
    data_nascimento = dataNascimento.get_date().strftime('%Y-%m-%d')
    endereco = e_endereco.get()
    curso = c_curso.get()
    img = ''  # Implemente a lógica para salvar a imagem no banco de dados

    aluno = (nome, email, tel, sexo, data_nascimento, endereco, curso, img)
    sistema.Registro_Estudante(aluno)
    mostrar_alunos()

def mostrar_alunos():
    # Limpar tabela existente
    for child in tree_aluno.get_children():
        tree_aluno.delete(child)

    # Obter lista de alunos do banco de dados
    alunos = sistema.MostrarEstudantes()

    # Preencher tabela com os dados dos alunos
    for aluno in alunos:
        tree_aluno.insert("", END, values=aluno)

def atualizar_aluno():
    # Obter o ID do aluno selecionado na tabela
    selection = tree_aluno.selection()
    if len(selection) == 0:
        messagebox.showwarning("Aviso", "Selecione um aluno para atualizar.")
        return
    aluno_id = tree_aluno.item(selection[0])["values"][0]

    # Obter os novos valores dos campos de entrada
    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    sexo = c_sexo.get()
    data_nascimento = dataNascimento.get_date().strftime('%Y-%m-%d')
    endereco = e_endereco.get()
    curso = c_curso.get()
    img = ''  # Implemente a lógica para salvar a nova imagem no banco de dados

    aluno = (nome, email, tel, sexo, data_nascimento, endereco, curso, img, aluno_id)
    sistema.AtualizarDados(aluno)
    mostrar_alunos()

def deletar_aluno():
    # Obter o ID do aluno selecionado na tabela
    selection = tree_aluno.selection()
    if len(selection) == 0:
        messagebox.showwarning("Aviso", "Selecione um aluno para deletar.")
        return
    aluno_id = tree_aluno.item(selection[0])["values"][0]

    # Confirmar a deleção com uma caixa de diálogo
    confirm = messagebox.askyesno("Confirmação", "Tem certeza que deseja deletar este aluno?")
    if confirm:
        sistema.DeletarEstudante(aluno_id)
        mostrar_alunos()

l_nome = Label(frame_details, text = "Nome *", anchor = NW, font = ("Ivy 10"), bg = co1, fg = co4)
l_nome.place(x = 4, y = 10)
e_nome = Entry(frame_details, width = 30, justify = "left", relief = "solid")
e_nome.place(x = 7, y = 40)

l_email = Label(frame_details, text = "Email *", anchor = NW, font = ("Ivy 10"), bg = co1, fg = co4)
l_email.place(x = 4, y = 70)
e_email = Entry(frame_details, width = 30, justify = "left", relief = "solid")
e_email.place(x = 7, y = 100)

l_tel = Label(frame_details, text = "Telefone *", anchor = NW, font = ("Ivy 10"), bg = co1, fg = co4)
l_tel.place(x = 4, y = 130)
e_tel = Entry(frame_details, width = 15, justify = "left", relief = "solid")
e_tel.place(x = 7, y = 160)

l_sexo = Label(frame_details, text = "Sexo *", anchor = NW, font = ("Ivy 10"), bg = co1, fg = co4)
l_sexo.place(x = 127, y = 130)
c_sexo = ttk.Combobox(frame_details, width = 7, font = ("Ivy 8 bold"), justify = "center")
c_sexo["values"] = ("M", "F")
c_sexo.place(x = 130, y = 160)


l_dataNascimento = Label(frame_details, text = "Data de nascimento *", anchor = NW, font = ("Ivy 10"), bg = co1, fg = co4)
l_dataNascimento.place(x = 220, y = 10)
dataNascimento = DateEntry(frame_details, width = 18, justify = "center", background = "darkblue", foregound = "white", borderwidth = 2, year = 2023)
dataNascimento.place(x = 224, y = 40)

l_endereco = Label(frame_details, text = "Endereço *", anchor = NW, font = ("Ivy 10"), bg = co1, fg = co4)
l_endereco.place(x = 220, y = 70)
e_endereco = Entry(frame_details, width = 20, justify = "left", relief = "solid")
e_endereco.place(x = 224, y = 100)

cursos = ["Engenharia", "Medicina", "Sociais"]

l_curso = Label(frame_details, text = "Curso *", anchor = NW, font = ("Ivy 10"), bg = co1, fg = co4)
l_curso.place(x = 220, y = 130)
c_curso = ttk.Combobox(frame_details, width = 20, font = ("Ivy 8 bold"), justify = "center")
c_curso["values"] = (cursos)
c_curso.place(x = 224, y = 160)


# Escolher imagem

def EscolherImagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    image_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_details, image = imagem, bg = co1, fg = co4)
    l_imagem.place(x = 390, y = 10)
    botao_carregar["text"] = "Trocar de foto"

botao_carregar = Button(frame_details, command = EscolherImagem, text = "Carregar Foto".upper(), width = 20, compound = CENTER, anchor = CENTER, overrelief = RIDGE, font=("Ivy 7 bold"), bg = co1, fg = co0)
botao_carregar.place(x = 390, y = 160)


# Botoes
app_img_adicionar = Image.open("add.png")
app_img_adicionar = app_img_adicionar.resize((25, 25))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)

botao_add = Button(frame_botoes, image = app_img_adicionar, relief = GROOVE, text = "Adicionar", width = 100, compound = "left", overrelief = RIDGE, font=("Ivy 11"), bg = co1, fg = co0)
botao_add.grid(row = 1, column = 0, pady = 5, padx = 10, sticky = NSEW)


app_img_deletar = Image.open("delete.png")
app_img_deletar = app_img_deletar.resize((25, 25))
app_img_deletar = ImageTk.PhotoImage(app_img_deletar)

botao_delete = Button(frame_botoes, image = app_img_deletar, relief = GROOVE, text = "Deletar", width = 100, compound = "left", overrelief = RIDGE, font=("Ivy 11"), bg = co1, fg = co0)
botao_delete.grid(row = 3, column = 0, pady = 5, padx = 10, sticky = NSEW)

app_img_atualizar = Image.open("update.png")
app_img_atualizar = app_img_atualizar.resize((25, 25))
app_img_atualizar = ImageTk.PhotoImage(app_img_atualizar)

botao_atualizar = Button(frame_botoes, image = app_img_atualizar, relief = GROOVE, text = "Atualizar", width = 100, compound = "left", overrelief = RIDGE, font=("Ivy 11"), bg = co1, fg = co0)
botao_atualizar.grid(row = 2, column = 0, pady = 5, padx = 10, sticky = NSEW)


# Chamar função para exibir alunos na tabela
mostrar_alunos()

# Executar janela
janela.mainloop()
