import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from click import command

class Vinho:
    def __init__(self, codigo, nome, tipo, variedade, origem, preco):
        self.codigo = codigo
        self.nome = nome
        self.tipo = tipo
        self.variedade = variedade
        self.origem = origem
        self.preco = preco
    
    def getCodigo(self):
        return self.codigo

    def getNome(self):
        return self.nome

    def getTipo(self):
        return self.tipo

    def getVariedade(self):
        return self.variedade

    def getOrigem(self):
        return self.origem

    def getPreco(self):
        return self.preco

    def getVinho(self):
        return "Nome: " + str(self.getNome())\
        + "\nCodigo: " + str(self.getCodigo())\
        + "\nTipo: " + str(self.getTipo())\
        + "\nVariedade: " + str(self.getVariedade())\
        + "\nOrigem: " + str(self.getOrigem())\
        + "\nPreço: " + str(self.getPreco())


class tipoInv(Exception):
    pass

class variedadeInv(Exception):
    pass

class origemInv(Exception):
    pass

class campoVazio(Exception):
    pass
    

class LimiteInsereVinho(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Vinho")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameTipo = tk.Frame(self)
        self.frameVariedade = tk.Frame(self)
        self.frameOrigem = tk.Frame(self)
        self.framePreco = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        
        self.frameCodigo.pack()
        self.frameNome.pack()
        self.frameTipo.pack()
        self.frameVariedade.pack()
        self.frameOrigem.pack()
        self.framePreco.pack()
        self.frameButton.pack()
      
        self.labelCodigo = tk.Label(self.frameCodigo, text="Codigo: ")
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelTipo = tk.Label(self.frameTipo, text="Tipo: ")
        self.labelVariedade = tk.Label(self.frameVariedade, text="Variedade: ")
        self.labelOrigem = tk.Label(self.frameOrigem, text="Origem: ")
        self.labelPreco = tk.Label(self.framePreco, text="Preco: ")
        self.labelCodigo.pack(side="left")
        self.labelNome.pack(side="left")
        self.labelTipo.pack(side="left")
        self.labelVariedade.pack(side="left")
        self.labelOrigem.pack(side="left")
        self.labelPreco.pack(side="left")

        self.inputCodigo = tk.Entry(self.frameCodigo, width=10)
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputTipo = tk.Entry(self.frameTipo, width=15)
        self.inputVariedade = tk.Entry(self.frameVariedade, width=20)
        self.inputOrigem = tk.Entry(self.frameOrigem, width=15)
        self.inputPreco = tk.Entry(self.framePreco, width=10)
        self.inputCodigo.pack(side="left")
        self.inputNome.pack(side="left")
        self.inputTipo.pack(side="left")
        self.inputVariedade.pack(side="left")
        self.inputOrigem.pack(side="left")
        self.inputPreco.pack(side="left")
      
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

#Escrever código
class LimiteConsultaVinho(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('400x300')
        self.title("Consulta Vinho")
        self.controle = controle
        
        self.frameCombobox = tk.Frame(self)
        self.frameDados = tk.Frame(self)
        self.frameCombobox.pack()
        self.frameDados.pack(side="left", pady=20)
        
        self.labelDados = tk.Label(self.frameDados, text='')
        self.labelDados.pack(side="top")
        
        self.labelcombobox = tk.Label(self.frameCombobox, text='Tipo: ')
        self.labelcombobox.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameCombobox, width = 15, textvariable=self.escolhaCombo)
        self.combobox.pack(side="left")
        self.lista_tipos_sel = []
        for tipo in self.controle.listaVinhos:
            if tipo.getTipo() in self.lista_tipos_sel:
                continue
            else:
                self.lista_tipos_sel.append(tipo.getTipo())
        self.combobox['values'] = self.lista_tipos_sel    
        self.escolha = self.combobox.bind("<<ComboboxSelected>>", self.controle.exibeTipo)
        
        self.labelcombobox2 = tk.Label(self.frameCombobox, text='Variedade: ')
        self.labelcombobox2.pack(side="left")
        self.escolhaCombo2 = tk.StringVar()
        self.combobox2 = ttk.Combobox(self.frameCombobox, width = 15, textvariable=self.escolhaCombo2)
        self.combobox2.pack(side="left")
        self.lista_var_sel = []
        for var in self.controle.listaVinhos:
            if tipo.getVariedade() in self.lista_var_sel:
                continue
            else:
                self.lista_var_sel.append(var.getVariedade())
        self.combobox2['values'] = self.lista_var_sel 
        self.combobox2.bind("<<ComboboxSelected>>", self.controle.exibeVariedade)
        

class CtrlVinho():
    def __init__(self, controlador):
        self.controlador = controlador
        self.listaTipos = ["Branco", "Tinto", "Rose", "Espumante"]
        self.listaVar = ["Cabernet Sauvignon", "Carmenere", "Merlot", "Malbec", "Sauvignon Blanc", "Pinot Grigio"]
        self.listaPaises = ["Brasil", "Argentina", "Chile", "Itália", "França", "Portugal", "África do Sul"]

        self.listaVinhos =  []
    
    def cadastraVinho(self):
        self.limiteIns = LimiteInsereVinho(self)

    def consultaVinho(self):
        self.limiteCons = LimiteConsultaVinho(self)
    
    def enterHandler(self, event):
        codigo = self.limiteIns.inputCodigo.get()
        nome = self.limiteIns.inputNome.get()
        tipo = self.limiteIns.inputTipo.get()
        variedade = self.limiteIns.inputVariedade.get()
        origem = self.limiteIns.inputOrigem.get()
        preco = self.limiteIns.inputPreco.get()
        try:
            if codigo == '' or nome == '' or tipo == '' or variedade == '' or origem == '' or preco == '':
                raise campoVazio
            if tipo not in self.listaTipos:
                raise tipoInv
            if variedade not in self.listaVar:
                raise variedadeInv
            if origem not in  self.listaPaises:
                raise origemInv
        except tipoInv:
                messagebox.showinfo('Alerta', 'Tipo inválido!')
        except variedadeInv:
                messagebox.showinfo('Alerta', 'Variedade inválida!')
        except origemInv:
            messagebox.showinfo('Alerta', 'Origem inválida!')
        except campoVazio:
            messagebox.showinfo('Alerta', 'Campo vazio!')                                
        else:  
            vinho = Vinho(codigo, nome, tipo, variedade, origem, preco)
            self.listaVinhos.append(vinho)            
            self.limiteIns.mostraJanela('Sucesso', 'Vinho cadastrado com sucesso')
            self.clearHandler(event)
    
    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputTipo.delete(0, len(self.limiteIns.inputTipo.get()))
        self.limiteIns.inputVariedade.delete(0, len(self.limiteIns.inputVariedade.get()))
        self.limiteIns.inputOrigem.delete(0, len(self.limiteIns.inputOrigem.get()))
        self.limiteIns.inputPreco.delete(0, len(self.limiteIns.inputPreco.get()))
    
    def fechaHandler(self, event):
        self.limiteIns.destroy()

    def exibeTipo(self, event):
        self.limiteCons.labelDados.config(text='')
        self.string = ''
        for dados in self.listaVinhos:
            if dados.getTipo() == self.limiteCons.combobox.get():
                self.string += dados.getVinho() + '\n\n'
        self.limiteCons.labelDados.config(text=self.string)                                 
    
    def exibeVariedade(self, event):
        self.limiteCons.labelDados.config(text='')
        self.string = ''
        for var in self.listaVinhos:
            if var.getTipo() == self.limiteCons.combobox.get() and var.getVariedade() == self.limiteCons.combobox2.get():    
                self.string += var.getVinho() + '\n\n'
        self.limiteCons.labelDados.config(text=self.string)        