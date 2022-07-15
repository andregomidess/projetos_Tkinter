import imp
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import produto
import cupom
import os.path
import pickle

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.produtoMenu = tk.Menu(self.menubar)
        self.cupomMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)    

        self.produtoMenu.add_command(label="Cadastrar", \
                    command=self.controle.cadastraProduto)
        self.produtoMenu.add_command(label="Consultar", \
                    command=self.controle.consultaProduto)
        self.menubar.add_cascade(label="Produto", \
                    menu=self.produtoMenu)

        self.cupomMenu.add_command(label="Criar", \
                    command=self.controle.criaCupom)
        self.cupomMenu.add_command(label="Consultar", \
                    command=self.controle.consultaCupom)        
        self.menubar.add_cascade(label="Cupom fiscal", \
                    menu=self.cupomMenu) 
        
        self.sairMenu.add_command(label="Salva", \
                    command=self.controle.salvaDados)
        self.menubar.add_cascade(label="Sair", \
                    menu=self.sairMenu)       

        self.root.config(menu=self.menubar)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlProduto = produto.CtrlProduto(self)
        self.ctrlCupom = cupom.CtrlCupom(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Trabalho 15")
        # Inicia o mainloop
        self.root.mainloop()
       
    def cadastraProduto(self):
        self.ctrlProduto.cadastraProduto()

    def consultaProduto(self):
        self.ctrlProduto.consultaProduto()

    def criaCupom(self):
        self.ctrlCupom.criaCupom()

    def consultaCupom(self):
        self.ctrlCupom.consultaCupom()
        
    def salvaDados(self):
        self.ctrlProduto.salvaProdutos()
        self.ctrlCupom.salvaCupom()
        self.root.destroy()    

if __name__ == '__main__':
    c = ControlePrincipal()