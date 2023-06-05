from tkinter import *
from tkinter import ttk

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        root.mainloop()
        
    def tela(self):
        self.root.title("Cadastro de Clientes") # Declarando o título da janela
        self.root.configure(background= '#1e3743') # Configurando a cor de fundo
        self.root.geometry('780x500') # Configurando as dimensões da janela (Horizontal X Vertical)
        self.root.resizable(True, True) # Permitir que as dimensões horizontal e vertical sejam responsivas
        self.root.maxsize(width=980, height=700) # Delimitando a largura e altura máxima
        self.root.minsize(width=500, height=400) # Delimitando a largura e altura mínima
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee', 
                             highlightbackground='#759fe6', highlightthickness=2)
        self.frame_1.place(relx= 0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        
        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=2)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    
    def widgets_frame1(self):
        ### Criação do botão limpar
        self.bt_limpar = Button(self.frame_1, text='Limpar', bd=4, bg='#107db2', fg='white',
                                 font=('verdana',8,'bold'))
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)   
             
        ### Criação do botão buscar
        self.bt_buscar = Button(self.frame_1, text='Buscar', bd=4, bg='#107db2', fg='white',
                                 font=('verdana',8,'bold'))
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        
        ### Criação do botão novo
        self.bt_buscar = Button(self.frame_1, text='Novo', bd=4, bg='#107db2', fg='white',
                                 font=('verdana',8,'bold'))
        self.bt_buscar.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        
        ### Criação do botão alterar
        self.bt_buscar = Button(self.frame_1, text='Alterar', bd=4, bg='#107db2', fg='white',
                                 font=('verdana',8,'bold'))
        self.bt_buscar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15) 
               
        ### Criação do botão apagar
        self.bt_buscar = Button(self.frame_1, text='Apagar', bd=4, bg='#107db2', fg='white',
                                 font=('verdana',8,'bold'))
        self.bt_buscar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)
        
        
        ### Criação da label e entrada do código
        self.lb_codigo = Label(self.frame_1, text='Código', bg='#dfe3ee', fg='#107db2')
        self.lb_codigo.place(relx=0.05, rely=0.05)
        
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)
        
        ### Criação da label e entrada do nome
        self.lb_nome = Label(self.frame_1, text='Nome', bg='#dfe3ee', fg='#107db2')
        self.lb_nome.place(relx=0.05, rely=0.35)
        
        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)
        
        ### Criação da label e entrada do telefone
        self.lb_telefone = Label(self.frame_1, text='Telefone', bg='#dfe3ee', fg='#107db2')
        self.lb_telefone.place(relx=0.05, rely=0.6)
        
        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)
        
        ### Criação da label e entrada da cidade
        self.lb_cidade = Label(self.frame_1, text='Cidade', bg='#dfe3ee', fg='#107db2')
        self.lb_cidade.place(relx=0.5, rely=0.6)
        
        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)
        
        
    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, column=('col1', 'col2', 'col3', 'col4'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='Código')
        self.listaCli.heading('#2', text='Nome')
        self.listaCli.heading('#3', text='Telefone')
        self.listaCli.heading('#4', text='Cidade')
        
        self.listaCli.column('#0', width=1)
        self.listaCli.column('#1', width=50)
        self.listaCli.column('#2', width=200)
        self.listaCli.column('#3', width=125)
        self.listaCli.column('#4', width=125)
        
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
        
        
        self.scrollLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)                
        
        
        
        
             
Application()