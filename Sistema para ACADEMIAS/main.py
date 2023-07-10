# importando dependencias do Tkinter
from tkinter.ttk import *
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# importando pillow
from PIL import ImageTk, Image

# tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date


# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha
co6 = "#038cfc"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

# Criando janela
janela = Tk()
janela.title("")
janela.geometry('850x620')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Criando Frames
frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_dados = Frame(janela, width=850, height=65, bg=co1)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_detalhes = Frame(janela, width=850, height=200, bg=co1)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=850, height=200, bg=co1)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)



#FRAME LOGO ------------------------------------------------------------------------
app_lg = Image.open('logo.png')
app_lg = app_lg.resize((70,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="  Academia OscaFitness", width=850, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=co6, fg=co1)
app_logo.place(x=10, y=0)


#Funcao para cadastrar Clientes
def cadastrar():
	print('Clientes')

#Funcao para adicionar Personais e Turmas
def adicionar():
	
	frame_tabela_personais = Frame(frame_tabela, width=400, height=200, bg=co1)
	frame_tabela_personais.grid(row=0, column=0, pady=0, padx=20, sticky=NSEW)

	frame_tabela_divisao = Frame(frame_tabela, width=15, height=200, bg=co1)
	frame_tabela_divisao.grid(row=0, column=1, pady=0, padx=10, sticky=NSEW)

	frame_tabela_turmas = Frame(frame_tabela, width=320, height=200, bg=co1)
	frame_tabela_turmas.grid(row=0, column=2, pady=0, padx=10, sticky=NSEW)

	#Detalhes dos Personais inputs

	l_nome = Label(frame_detalhes, text="Nome do(a) Personal: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_nome.place(x=7, y=10)
	enome_personal = Entry(frame_detalhes, width=35, justify='left', relief='solid')
	enome_personal.place(x=7, y=35)


	l_sobrenome = Label(frame_detalhes, text="Descriçao do(a) Personal(Informações Extras): ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_sobrenome.place(x=7, y=65)
	esobrenome_personal = Entry(frame_detalhes, width=35, justify='left', relief='solid')
	esobrenome_personal.place(x=7, y=90)

	l_preco = Label(frame_detalhes, text="Preço do(a) Personal: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_preco.place(x=7, y=120)
	epreco_personal = Entry(frame_detalhes, width=10, justify='left', relief='solid')
	epreco_personal.place(x=7, y=145)

	#BOTÕES

	botao_carregar = Button(frame_detalhes, anchor=CENTER, text="Salvar".upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
	botao_carregar.place(x=117, y=145)

	botao_atualizar = Button(frame_detalhes, anchor=CENTER, text="Atualizar".upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1)
	botao_atualizar.place(x=217, y=145)

	botao_deletar = Button(frame_detalhes, anchor=CENTER, text="Deletar".upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
	botao_deletar.place(x=327, y=145)

	
	def mostrar_personais():
		app_nome = Label(frame_tabela_personais, text="Tabela de Personais", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
		app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)
		
		# creating a treeview with dual scrollbars
		list_header = ['ID','Nome','Descrição','Preço']

		df_list = []

		global tree_personais

		tree_personais = ttk.Treeview(frame_tabela_personais, selectmode="extended", columns=list_header, show="headings")

 		# vertical scrollbar
		vsb = ttk.Scrollbar(frame_tabela_personais, orient="vertical", command=tree_personais.yview)
		# horizontal scrollbar
		hsb = ttk.Scrollbar(frame_tabela_personais, orient="horizontal", command=tree_personais.xview)

		tree_personais.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
		tree_personais.grid(column=0, row=1, sticky='nsew')
		vsb.grid(column=1, row=1, sticky='ns')
		hsb.grid(column=0, row=2, sticky='ew')
		frame_tabela_personais.grid_rowconfigure(0, weight=12)

		hd = ["nw","nw","e","e"]
		h = [30,150,150,60]
		n = 0
 
		for col in list_header:
			tree_personais.heading(col, text=col.title(), anchor=NW)
			# adjust the column's width to the header string
			tree_personais.column(col, width=h[n], anchor=hd[n])
			n+=1

		for item in df_list:
			tree_personais.insert('', 'end', values=item)
			
	mostrar_personais()

	#Linha divisória-------------------

	l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
	l_linha.place(x=459, y=10)

	l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
	l_linha.place(x=458, y=10)


	#Linha divisória tabela-------------------

	l_linha = Label(frame_tabela_divisao, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
	l_linha.place(x=1, y=10)

	l_linha = Label(frame_tabela_divisao, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
	l_linha.place(x=0, y=10)


	#Detalhes das Turmas INPUTS


	l_nome_turma = Label(frame_detalhes, text="Nome da Turma: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_nome_turma.place(x=480, y=10)
	enome_turma = Entry(frame_detalhes, width=35, justify='left', relief='solid')
	enome_turma.place(x=480, y=35)


	l_personalnome = Label(frame_detalhes, text="Personal Responsavel: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_personalnome.place(x=480, y=65)

	#PEGANDO OS PERSONAIS
	personais = ["Oscar", "Rafael"]
	personal = []

	for i in personais:
		personal.append(i)

	epersonal_nome = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 8 bold'))
	epersonal_nome['values'] = (personal)
	epersonal_nome.place(x=480, y=90)


	l_datainicio = Label(frame_detalhes, text="Data de Início: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_datainicio.place(x=480, y=120)
	edata_inicio = DateEntry(frame_detalhes, width=10, background='darkblue', foreground='white', borderwidht=2, year=2020)
	edata_inicio.place(x=480, y=145)


	# Botões

	botao_carregar_turmas = Button(frame_detalhes, anchor=CENTER, text="Salvar".upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
	botao_carregar_turmas.place(x=610, y=125)

	botao_atualizar_turmas = Button(frame_detalhes, anchor=CENTER, text="Atualizar".upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1)
	botao_atualizar_turmas.place(x=720, y=125)

	botao_deletar_turmas = Button(frame_detalhes, anchor=CENTER, text="Deletar".upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
	botao_deletar_turmas.place(x=665, y=160)




	def mostrar_turmas():
		app_nome = Label(frame_tabela_turmas, text="Tabela de Turmas", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
		app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)
		
		# creating a treeview with dual scrollbars
		list_header = ['ID','Nome','Personal','Início']

		df_list = []

		global tree_turmas

		tree_turmas = ttk.Treeview(frame_tabela_turmas, selectmode="extended", columns=list_header, show="headings")

 		# vertical scrollbar
		vsb = ttk.Scrollbar(frame_tabela_turmas, orient="vertical", command=tree_turmas.yview)
		# horizontal scrollbar
		hsb = ttk.Scrollbar(frame_tabela_turmas, orient="horizontal", command=tree_turmas.xview)

		tree_turmas.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
		tree_turmas.grid(column=0, row=1, sticky='nsew')
		vsb.grid(column=1, row=1, sticky='ns')
		hsb.grid(column=0, row=2, sticky='ew')
		frame_tabela_turmas.grid_rowconfigure(0, weight=12)

		hd = ["nw","nw","e","e"]
		h = [30,120,90,60]
		n = 0
 
		for col in list_header:
			tree_turmas.heading(col, text=col.title(), anchor=NW)
			# adjust the column's width to the header string
			tree_turmas.column(col, width=h[n], anchor=hd[n])
			n+=1

		for item in df_list:
			tree_turmas.insert('', 'end', values=item)
			
	mostrar_turmas()


#Funcao para Salvar
def salvar():
	print('Salvar')


#Funcao de controle

def control(i):
	#CADASTRO DE CLIENTE
	if i == 'cadastro':

		for widget in frame_detalhes.winfo_children():
			widget.destroy()

		for widget in frame_tabela.winfo_children():
			widget.destroy()

		#Chamando Função Clientes
		cadastrar()

	if i == 'adicionar':

		for widget in frame_detalhes.winfo_children():
			widget.destroy()

		for widget in frame_tabela.winfo_children():
			widget.destroy()

		#Chamando Função Clientes
		adicionar()

	if i == 'salvar':

		for widget in frame_detalhes.winfo_children():
			widget.destroy()

		for widget in frame_tabela.winfo_children():
			widget.destroy()

		#Chamando Função Clientes
		salvar()


#Criando Botoes ------------------------------------------------------------------------
#Cadastro
app_img_cadastro = Image.open('add.png')
app_img_cadastro = app_img_cadastro.resize((18,18))
app_img_cadastro = ImageTk.PhotoImage(app_img_cadastro)
app_cadastro = Button(frame_dados, command=lambda:control('cadastro'), image=app_img_cadastro, text=" Cadastro", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_cadastro.place(x=10, y=30)

#Adicionar
app_img_adicionar = Image.open('add.png')
app_img_adicionar = app_img_adicionar.resize((18,18))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_dados, command=lambda:control('adicionar'), image=app_img_adicionar, text=" Adicionar", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_adicionar.place(x=140, y=30)

#Salvar
app_img_salvar = Image.open('save.png')
app_img_salvar = app_img_salvar.resize((18,18))
app_img_salvar = ImageTk.PhotoImage(app_img_salvar)
app_salvar = Button(frame_dados, command=lambda:control('salvar'), image=app_img_salvar, text=" Salvar", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_salvar.place(x=270, y=30)


# Executando a janela
janela.mainloop()
 
