import imp
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import produto
import cupom
import os.path
import pickle

class Produto:
    def __init__(self, codigo, descricao, valorUnitario):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valorUnitario = valorUnitario

    def getCodigo(self):
        return self.__codigo
    def getDescricao(self):
        return self.__descricao
    def getValorUnitario(self):
        return self.__valorUnitario

class LimiteCadastraProduto(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Produto")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameDescricao = tk.Frame(self)
        self.frameValorUnitario = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameDescricao.pack()
        self.frameValorUnitario.pack()
        self.frameButton.pack()
      
        self.labelCodigo = tk.Label(self.frameCodigo,text="Código: ")
        self.labelDescricao = tk.Label(self.frameDescricao,text="Descrição: ")
        self.labelValorUnitario = tk.Label(self.frameValorUnitario, text='Valor Unitário: ')
        self.labelCodigo.pack(side="left")
        self.labelDescricao.pack(side="left")
        self.labelValorUnitario.pack(side="left")  

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")
        self.inputDescricao = tk.Entry(self.frameDescricao, width=20)
        self.inputDescricao.pack(side="left") 
        self.inputValorUnitario = tk.Entry(self.frameValorUnitario, width=20)
        self.inputValorUnitario.pack(side="left")            
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaProduto(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Consulta Produto")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text='Digite o código')
        self.labelCodigo.pack(side="left")
        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")

        self.buttonConsulta = tk.Button(self.frameButton ,text="Consulta")      
        self.buttonConsulta.pack(side="left")
        self.buttonConsulta.bind("<Button>", controle.enterHandlerCons)

        self.buttonFecha = tk.Button(self.frameButton ,text="Fechar")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandlerCons)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)    



class CtrlProduto():
    def __init__(self, controlePrincipal):
        self.controlePrincipal = controlePrincipal
        
        if not os.path.isfile("produtos.pickle"):
            self.listaProdutos =  []
        else:
            with open("produtos.pickle", "rb") as f:
                self.listaProdutos = pickle.load(f)
    
    def salvaProdutos(self):
        if len(self.listaProdutos) != 0:
            with open("produtos.pickle","wb") as f:
                pickle.dump(self.listaProdutos, f)            

    def cadastraProduto(self):
        self.limiteIns = LimiteCadastraProduto(self)

    def consultaProduto(self):
        self.limiteCons = LimiteConsultaProduto(self)
        
    def getProduto(self, codigo):
        codRet = None
        for prod in self.listaProdutos:
            if prod.getCodigo() == codigo:
                codRet = prod
        return codRet                                    

    def enterHandler(self, event):
        codigo = self.limiteIns.inputCodigo.get()
        descricao = self.limiteIns.inputDescricao.get()
        valorU = self.limiteIns.inputValorUnitario.get()
        prod = Produto(codigo, descricao, valorU)
        self.listaProdutos.append(prod)
        self.limiteIns.mostraJanela('Sucesso', 'Produto cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputDescricao.delete(0, len(self.limiteIns.inputDescricao.get()))
        self.limiteIns.inputValorUnitario.delete(0, len(self.limiteIns.inputValorUnitario.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()          

    def enterHandlerCons(self, event):
        codigo = self.limiteCons.inputCodigo.get()
        for prod in self.listaProdutos:
            if prod.getCodigo() == codigo:
                self.limiteCons.mostraJanela('Sucesso', prod.getDescricao())
                self.limiteCons.destroy()
                break
            else:    
                self.limiteCons.mostraJanela('Falha', 'Codigo Inexistente')
            

    def fechaHandlerCons(self, event):
        self.limiteCons.destroy()            