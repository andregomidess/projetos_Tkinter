import imp
from operator import le
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import produto
import cupom
import os.path
import pickle


class CupomFiscal():
    def __init__(self, nroCupom, itensCupom):
        self.__nroCupom = nroCupom
        self.__itensCupom = itensCupom

    def getNroCupom(self):
        return self.__nroCupom

    def getItensCupom(self):
        return self.__itensCupom
    

class LimiteCriaCupom(tk.Toplevel):
    def __init__(self, controle, listaProd):

        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Cria Cupom")
        self.controle = controle 

        self.frameNroCupom = tk.Frame(self)
        self.frameItens = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNroCupom.pack()
        self.frameItens.pack()
        self.frameButton.pack()

        self.labelNroCupom = tk.Label(self.frameNroCupom, text='Digite o N° do cupom: ')  
        self.labelNroCupom.pack(side='left')  
        self.inputNroCupom = tk.Entry(self.frameNroCupom, width=20)
        self.inputNroCupom.pack(side='left')

        self.labelItens = tk.Label(self.frameItens,text="Escolha o item: ")
        self.labelItens.pack(side="left") 
        self.listbox = tk.Listbox(self.frameItens)
        self.listbox.pack(side="left")
        for prod in listaProd:
            self.listbox.insert(tk.END, prod.getCodigo())

        self.buttonInsere = tk.Button(self.frameButton ,text="Insere produto")      
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereProduto)
      
        self.buttonCria = tk.Button(self.frameButton ,text="Cria cupom")      
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criarCupom)  

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
        
class LimiteConsultaCupom(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('400x300')
        self.title("Consulta Cupom")
        self.controle = controle 
        
        self.frameNroCupom = tk.Frame(self)
        self.frameDados = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNroCupom.pack()
        self.frameDados.pack()
        self.frameButton.pack()

        self.labelNroCupom = tk.Label(self.frameNroCupom, text='Digite o N° do cupom: ')  
        self.labelNroCupom.pack(side='left')  
        self.inputNroCupom = tk.Entry(self.frameNroCupom, width=20)
        self.inputNroCupom.pack(side='left')
        self.labelDados = tk.Label(self.frameDados, text='')
        self.labelDados.pack(side="top")
        
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandlerCons)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandlerCons)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandlerCons)
        
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)                   

class CtrlCupom():
    def __init__(self, controlePrincipal):
        self.controlePrincipal = controlePrincipal
        self.itensCupom = []
        if not os.path.isfile("cupom.pickle"):
            self.listaCupom =  []
        else:
            with open("cupom.pickle", "rb") as f:
                self.listaCupom = pickle.load(f)
    
    def salvaCupom(self):
        if len(self.listaCupom) != 0:
            with open("cupom.pickle","wb") as f:
                pickle.dump(self.listaCupom, f)            

    def criaCupom(self):
        listaProd = self.controlePrincipal.ctrlProduto.listaProdutos
        self.limiteIns = LimiteCriaCupom(self, listaProd)
        
    def consultaCupom(self):
        self.limiteCons = LimiteConsultaCupom(self)    

    def insereProduto(self, event):
        itemSel = self.limiteIns.listbox.get(tk.ACTIVE)
        item = self.controlePrincipal.ctrlProduto.getProduto(itemSel)
        self.itensCupom.append(item)
        self.limiteIns.mostraJanela('Sucesso', 'Item Cadastrado')
        

    def criarCupom(self, event):
        n = self.limiteIns.inputNroCupom.get()
        listaI = self.itensCupom.copy()
        cupom = CupomFiscal(n, listaI)
        self.listaCupom.append(cupom)
        self.limiteIns.mostraJanela('Sucesso', 'Cupom Cadastrado')
        self.itensCupom.clear()
        self.limiteIns.destroy()   
        
    def enterHandlerCons(self, event):
        nro = self.limiteCons.inputNroCupom.get()
        self.limiteCons.labelDados.config(text=' ')
        string = ''
        precoTotal = 0.0
        for cup in self.listaCupom:
            if cup.getNroCupom() == nro:
                string += 'N° do cupom: ' + cup.getNroCupom() + '\n\n'
                for itens in cup.getItensCupom():
                    string += 'Código: ' + itens.getCodigo() + '\nDescrição: ' + itens.getDescricao() + '\nValor unitário: ' + itens.getValorUnitario() + '\n\n'
                    precoTotal += float(itens.getValorUnitario())
        if string == '':
            self.limiteCons.mostraJanela('Falha', 'Nro do cupom inexistente')
        else:        
            string += 'Preço total: ' + str(precoTotal)            
            self.limiteCons.labelDados.config(text=string)            
            self.clearHandlerCons(event)

    def clearHandlerCons(self, event):
        self.limiteCons.inputNroCupom.delete(0, len(self.limiteCons.inputNroCupom.get()))

    def fechaHandlerCons(self, event):
        self.limiteCons.destroy()                                