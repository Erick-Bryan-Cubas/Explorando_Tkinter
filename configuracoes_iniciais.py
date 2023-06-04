from tkinter import * # Importamos todas as chamadas da biblioteca Tkinter

root = Tk() # Variável com o nome da janela

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()
        
    def tela(self):
        self.root.title("Cadastro de Clientes") # Declarando o título da janela
        self.root.configure(background= '#1e3743') # Configurando a cor de fundo
        self.root.geometry("780x500") # Configurando as dimensões da janela (Horizontal X Vertical)
        self.root.resizable(True, True) # Permitir que as dimensões horizontal e vertical sejam responsivas
        self.root.maxsize(width=980, height=700) # Delimitando a largura e altura máxima
        self.root.minsize(width=400, height=300) # Delimitando a largura e altura mínima
        
Application()