from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        root.mainloop()
        
    def tela(self):
        self.root.title("Cadastro de Clientes") # Declarando o título da janela
        self.root.configure(background= '#1e3743') # Configurando a cor de fundo
        self.root.geometry('780x500') # Configurando as dimensões da janela (Horizontal X Vertical)
        self.root.resizable(True, True) # Permitir que as dimensões horizontal e vertical sejam responsivas
        self.root.maxsize(width=980, height=700) # Delimitando a largura e altura máxima
        self.root.minsize(width=400, height=300) # Delimitando a largura e altura mínima
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee', 
                             highlightbackground='#759fe6', highlightthickness=2)
        self.frame_1.place(relx= 0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        
        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=2)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
        
Application()