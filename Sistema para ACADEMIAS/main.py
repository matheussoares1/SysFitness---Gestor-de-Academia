
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


# IMportando VIew

from view import *

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

	# INPUT TIPO TEXTO

	l_nome = Label(frame_detalhes, text="Nome do Cliente: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_nome.place(x=7, y=10)
	enome_cliente = Entry(frame_detalhes, width=35, justify='left', relief='solid')
	enome_cliente.place(x=7, y=30)

	l_cpf = Label(frame_detalhes, text="Numero do CPF: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_cpf.place(x=7, y=100)
	ecpf = Entry(frame_detalhes, width=15, justify='left', relief='solid')
	ecpf.place(x=7, y=120)

	l_telefone = Label(frame_detalhes, text="Contato: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_telefone.place(x=150, y=100)
	etelefone = Entry(frame_detalhes, width=15, justify='left', relief='solid')
	etelefone.place(x=153, y=120)

	l_endereco = Label(frame_detalhes, text="Endereço: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_endereco.place(x=7, y=55)
	eendereco = Entry(frame_detalhes, width=35, justify='left', relief='solid')
	eendereco.place(x=7, y=75)


	# INPUT TIPO CALENDÁRIO
	l_datanasc = Label(frame_detalhes, text="Nascimento: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_datanasc.place(x=7, y=150)
	edata_nascimento = DateEntry(frame_detalhes, width=10, background='darkblue', foreground='white', borderwidht=2, year=2020)
	edata_nascimento.place(x=7, y=170)


	l_data_inicio = Label(frame_detalhes, text="Data de Início: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_data_inicio.place(x=150, y=150)
	edata_inicio_clienter = DateEntry(frame_detalhes, width=10, background='darkblue', foreground='white', borderwidht=2, year=2020)
	edata_inicio_clienter.place(x=150, y=170)

	# INPUT TIPO SELETOR

	l_personalnome = Label(frame_detalhes, text="Personal: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_personalnome.place(x=270, y=160)

	#PEGANDO OS PERSONAIS
	personais = ["Oscar", "Rafael"]
	personal = []

	for i in personais:
		personal.append(i)

	epersonal_nome = ttk.Combobox(frame_detalhes, width=15, font=('Ivy 8 bold'))
	epersonal_nome['values'] = (personal)
	epersonal_nome.place(x=270, y=180)


	l_turmasnome = Label(frame_detalhes, text="Turma: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_turmasnome.place(x=400, y=160)


	turmas = ["teste", "teste"]
	turmas = []

	for i in turmas:
		turma.append(i)

	eturmas_nome = ttk.Combobox(frame_detalhes, width=15, font=('Ivy 8 bold'))
	eturmas_nome['values'] = (personal)
	eturmas_nome.place(x=400, y=180)


	# INPUT TIPO NUMEROS REAIS


	# INPUT TIPO NUMEROS INTEIROS



	# Botões de Salvar, Editar e Deletar
	botao_salvarcliente = Button(frame_detalhes, anchor=CENTER, text="Salvar".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
	botao_salvarcliente.place(x=630, y=120)


	botao_atualizarcliente = Button(frame_detalhes, anchor=CENTER, text="Pesquisar".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1)
	botao_atualizarcliente.place(x=630, y=145)


	botao_deletarcliente = Button(frame_detalhes, anchor=CENTER, text="Deletar".upper(), width=20, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
	botao_deletarcliente.place(x=630, y=170)

	botao_vercliente = Button(frame_detalhes, anchor=CENTER, text="Ver".upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co8, fg=co1)
	botao_vercliente.place(x=600, y=70)

	#INPUT CARREGAR FOTO

	global imagem, Imagem_String, l_imagem

	def escolher_imagem():

		global imagem, Imagem_String, l_imagem

		imagem = fd.askopenfilename()
		Imagem_String = imagem

		# Abrindo Imagem
		imagem = Image.open(imagem)
		imagem = imagem.resize((120,120))
		imagem = ImageTk.PhotoImage(imagem)
		l_imagem = Label(frame_detalhes, image=imagem)
		l_imagem.place(x=325,y=5)

		app_upload['text'] = 'Trocar de foto'
	
	app_upload = Button(frame_detalhes, command=escolher_imagem, text="Enviar Imagem".upper(), width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7'), bg=co1, fg=co0)
	app_upload.place(x=318, y=130)

	
	# Linha Divisória
	l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
	l_linha.place(x=570, y=10)

	l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
	l_linha.place(x=569, y=10)

	l_nome = Label(frame_detalhes, text="Buscar Cliente: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_nome.place(x=600, y=10)
	enome_personal = Entry(frame_detalhes, width=25, justify='left', relief='solid')
	enome_personal.place(x=600, y=35)

	botao_ver = Button(frame_detalhes, anchor=CENTER, text="Pesquisar".upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co8, fg=co1)
	botao_ver.place(x=720, y=70)


	# Tabela Alunos
	def mostrar_clientes():
		app_nome = Label(frame_tabela, text="Tabela de estudantes", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
		app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

		# creating a treeview with dual scrollbars
		list_header = ['id','Nome','Endereço',  'CPF','Contato', 'Imagem', 'Dt Nasc', 'Dt Inicio','Personal', 'Turma']

		df_list = []

		global tree_personal

		tree_cliente = ttk.Treeview(frame_tabela, selectmode="extended",columns=list_header, show="headings")

		# vertical scrollbar
		vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_cliente.yview)
		# horizontal scrollbar
		hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_cliente.xview)

		tree_cliente.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
		tree_cliente.grid(column=0, row=1, sticky='nsew')
		vsb.grid(column=1, row=1, sticky='ns')
		hsb.grid(column=0, row=2, sticky='ew')
		frame_tabela.grid_rowconfigure(0, weight=12)
		
		hd=["nw","nw","nw","center","center","center","center","center","center","center"]
		h=[40,150,150,60,60,60,60,80,100,60]
		n=0
		
		for col in list_header:
   			tree_cliente.heading(col, text=col.title(), anchor=NW)
   			tree_cliente.column(col, width=h[n],anchor=hd[n])
   			n+=1

		for item in df_list:
			tree_cliente.insert('', 'end', values=item)
	
	mostrar_clientes()


#Funcao para adicionar Personais e Turmas
def adicionar():
	
	frame_tabela_personais = Frame(frame_tabela, width=400, height=200, bg=co1)
	frame_tabela_personais.grid(row=0, column=0, pady=0, padx=20, sticky=NSEW)

	frame_tabela_divisao = Frame(frame_tabela, width=15, height=200, bg=co1)
	frame_tabela_divisao.grid(row=0, column=1, pady=0, padx=10, sticky=NSEW)

	frame_tabela_turmas = Frame(frame_tabela, width=320, height=200, bg=co1)
	frame_tabela_turmas.grid(row=0, column=2, pady=0, padx=10, sticky=NSEW)

	#Detalhes dos Personais-----------------------------------------------------

	#Funçao novo personal

	def novo_personal():
		nome = enome_personal.get()
		descricao = esobrenome_personal.get()
		preco = epreco_personal.get()

		lista_personal = [nome, descricao, preco]

		# Caso esteja vazio haverá uma tela de insereçao de ddos obrigatórios
		for i in lista_personal:
			if i=="":
				messagebox.showerror('Erro', 'Preencha todos os campos.')
				return

		#Inserindo dados no banco de dados 
		inserir_personais(lista_personal)

		# Mostrando mensagem de sucesso
		messagebox.showinfo('Sucesso', 'Dados inseridos com sucesso!')

		enome_personal.delete(0,END)
		esobrenome_personal.delete(0,END)
		epreco_personal.delete(0,END)

		# Mostrando os valores na tabela
		mostrar_personais()

	#Atualizar Personal
	def update_personal():
		try:
			tree_itens = tree_personais.focus()
			tree_dicionario = tree_personais.item(tree_itens)
			tree_lista = tree_dicionario['values']

			valor_id = tree_lista[0]


			# Inserindo os valores nas entries
			enome_personal.insert(0, tree_lista[1])
			esobrenome_personal.insert(0, tree_lista[2])
			epreco_personal.insert(0, tree_lista[3])


			#função atualizar
			def update():


				nome = enome_personal.get()
				descricao = esobrenome_personal.get()
				preco = epreco_personal.get()

				lista_personal = [nome, descricao, preco, valor_id]

				# Caso esteja vazio haverá uma tela de insereçao de ddos obrigatórios
				for i in lista_personal:
					if i=="":
						messagebox.showerror('Erro', 'Preencha todos os campos.')
						return

				#Inserindo dados no banco de dados 
				atualizar_personais(lista_personal)

				# Mostrando mensagem de sucesso
				messagebox.showinfo('Sucesso', 'Dados inseridos com sucesso!')

				enome_personal.delete(0,END)
				esobrenome_personal.delete(0,END)
				epreco_personal.delete(0,END)

				# Mostrando os valores na tabela
				mostrar_personais()

				#Destruindo o Botão Salvar após Salvar os dados
				botao_salvar.destroy()


			botao_salvar = Button(frame_detalhes,command=update, anchor=CENTER, text="Salvar Atualização".upper(), overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
			botao_salvar.place(x=190, y=170)		

		except IndexError:
			messagebox.showerror('Erro', 'Selecione um dos personais na tabela')



	#Deletar Personal
	def delete_personal():
		try:
			tree_itens = tree_personais.focus()
			tree_dicionario = tree_personais.item(tree_itens)
			tree_lista = tree_dicionario['values']

			valor_id = tree_lista[0]

			#Deletando dados do banco de dados
			deletar_personais([valor_id])

			# Mostrando mensagem de sucesso
			messagebox.showinfo('Sucesso', 'Dados deletados com sucesso!')

			#mostrando os valores na tabela
			mostrar_personais()

		except IndexError:
			messagebox.showerror('Erro', 'Selecione um dos personais para deletar')


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
	botao_carregar = Button(frame_detalhes,command=novo_personal, anchor=CENTER, text="Inserir".upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
	botao_carregar.place(x=117, y=145)

	botao_atualizar = Button(frame_detalhes,command=update_personal, anchor=CENTER, text="Atualizar".upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1)
	botao_atualizar.place(x=217, y=145)

	botao_deletar = Button(frame_detalhes,command=delete_personal, anchor=CENTER, text="Deletar".upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
	botao_deletar.place(x=317, y=145)

	
	def mostrar_personais():


		app_nome = Label(frame_tabela_personais, text="Tabela de Personais", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
		app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)
		
		# creating a treeview with dual scrollbars
		list_header = ['ID','Nome','Descrição','Preço']

		df_list = ver_personais()

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

	def inserindo_turma():

		nome = enome_turma.get()
		personal = epersonal_nome.get()
		data = edata_inicio.get()

		lista_personal = [nome, personal, data]

		# Caso esteja vazio haverá uma tela de insereçao de ddos obrigatórios
		for i in lista_personal:
			if i=="":
				messagebox.showerror('Erro', 'Preencha todos os campos.')
				return

		#Inserindo dados no banco de dados 
		criar_turmas(lista_personal)

		# Mostrando mensagem de sucesso
		messagebox.showinfo('Sucesso', 'Dados inseridos com sucesso!')

		enome_turma.delete(0,END)
		epersonal_nome.delete(0,END)
		edata_inicio.delete(0,END)

		# Mostrando os valores na tabela
		mostrar_turmas()



	


	#Atualizar Turma
	def update_turma():
		try:
			tree_itens = tree_turmas.focus()
			tree_dicionario = tree_turmas.item(tree_itens)
			tree_lista = tree_dicionario['values']

			valor_id = tree_lista[0]


			# Inserindo os valores nas entries
			enome_turma.insert(0, tree_lista[1])
			epersonal_nome.insert(0, tree_lista[2])
			edata_inicio.insert(0, tree_lista[3])


			#função atualizar
			def update():


				nome = enome_turma.get()
				personal = epersonal_nome.get()
				data = edata_inicio.get()

				lista_personal = [nome, personal, data, valor_id]

				# Caso esteja vazio haverá uma tela de insereçao de ddos obrigatórios
				for i in lista_personal:
					if i=="":
						messagebox.showerror('Erro', 'Preencha todos os campos.')
						return

				#Inserindo dados no banco de dados 
				atualizar_turmas(lista_personal)

				# Mostrando mensagem de sucesso
				messagebox.showinfo('Sucesso', 'Dados inseridos com sucesso!')

				enome_turma.delete(0,END)
				epersonal_nome.delete(0,END)
				edata_inicio.delete(0,END)

				# Mostrando os valores na tabela
				mostrar_turmas()

				#Destruindo o Botão Salvar após Salvar os dados
				botao_salvar_turma.destroy()


			botao_salvar_turma = Button(frame_detalhes,command=update, anchor=CENTER, text="Salvar Atualização".upper(), overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
			botao_salvar_turma.place(x=650, y=95)		

		except IndexError:
			messagebox.showerror('Erro', 'Selecione um dos personais na tabela')



	#Deletar Personal
	def delete_turma():
		try:
			tree_itens = tree_turmas.focus()
			tree_dicionario = tree_turmas.item(tree_itens)
			tree_lista = tree_dicionario['values']

			valor_id = tree_lista[0]

			#Deletando dados do banco de dados
			deletar_turmas([valor_id])

			# Mostrando mensagem de sucesso
			messagebox.showinfo('Sucesso', 'Dados deletados com sucesso!')

			#mostrando os valores na tabela
			mostrar_turmas()

		except IndexError:
			messagebox.showerror('Erro', 'Selecione um dos personais para deletar')





	l_nome_turma = Label(frame_detalhes, text="Nome da Turma: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_nome_turma.place(x=480, y=10)
	enome_turma = Entry(frame_detalhes, width=35, justify='left', relief='solid')
	enome_turma.place(x=480, y=35)


	l_personalnome = Label(frame_detalhes, text="Personal Responsavel: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_personalnome.place(x=480, y=65)

	#PEGANDO OS PERSONAIS
	personais = ver_personais()
	personal = []

	for i in personais:
		personal.append(i[1])

	epersonal_nome = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 8 bold'))
	epersonal_nome['values'] = (personal)
	epersonal_nome.place(x=480, y=90)

	l_datainicio = Label(frame_detalhes, text="Data de Início: ", height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
	l_datainicio.place(x=480, y=120)
	edata_inicio = DateEntry(frame_detalhes, width=10, background='darkblue', foreground='white', borderwidht=2, year=2020)
	edata_inicio.place(x=480, y=145)


	# Botões
	botao_carregar_turmas = Button(frame_detalhes, command=inserindo_turma, anchor=CENTER, text="Salvar".upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
	botao_carregar_turmas.place(x=610, y=125)

	botao_atualizar_turmas = Button(frame_detalhes,command=update_turma, anchor=CENTER, text="Atualizar".upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1)
	botao_atualizar_turmas.place(x=720, y=125)

	botao_deletar_turmas = Button(frame_detalhes,command=delete_turma, anchor=CENTER, text="Deletar".upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
	botao_deletar_turmas.place(x=665, y=160)


	def mostrar_turmas():
		app_nome = Label(frame_tabela_turmas, text="Tabela de Turmas", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
		app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)
		
		# creating a treeview with dual scrollbars
		list_header = ['ID','Nome','Personal','Início']

		df_list = ver_turmas()

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

cadastrar()
# Executando a janela
janela.mainloop()
 
