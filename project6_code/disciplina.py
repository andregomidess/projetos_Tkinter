import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import aluno as alu
import curso
import disciplina as disc


class disciplina:
    
    def __init__(self, codigo, nome, carga_hr, grade):
        self.__codigo = codigo
        self.__nome = nome
        self.__carga_hr = carga_hr
        self.__grade = grade
        
    def get_codigo(self):
        return self.__codigo
    
    def get_nome(self):
        return self.__nome
    
    def get_carga_hr(self):
        return self.__carga_hr
    
    def get_grade(self):
        return self.__grade
    
class LimiteConsultaDisciplina(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('300x150')
        self.title("disciplina")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameCargaHr = tk.Frame(self)
        self.frameGrade = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameNome.pack()
        self.frameCargaHr.pack()
        self.frameGrade.pack()
        self.frameButton.pack()
      
        self.labelCodigo = tk.Label(self.frameCodigo,text="Codigo: ")
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelCargaHr = tk.Label(self.frameCargaHr, text="Carga Horária: ")
        self.labelGrade = tk.Label(self.frameGrade, text='Curso')
        self.labelCodigo.pack(side="left")
        self.labelNome.pack(side="left")
        self.labelCargaHr.pack(side="left")
        self.labelGrade.pack(side="left")     

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")
        self.inputCargaHr = tk.Entry(self.frameCargaHr, width=20)
        self.inputCargaHr.pack(side="left")
        self.inputGrade = tk.Entry(self.frameGrade, width=20)
        self.inputGrade.pack(side="left")        
      
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
        
class CtrlDisciplina():
    def __init__(self, controlePrincipal):
        self.ControlePrincipal = controlePrincipal
        self.listaDisciplinas = []
        
    def consultaDisciplina(self):
        self.limiteIns = LimiteConsultaDisciplina(self)    
        
    def enterHandler(self, event):
        cod = self.limiteIns.inputCodigo.get()
        nome = self.limiteIns.inputNome.get()
        carga_hr = self.limiteIns.inputCargaHr.get()
        curso = self.limiteIns.inputGrade.get()
        listaCurso = self.ControlePrincipal.ctrlCurso.listaCursos
        for cursos in listaCurso:
            if cursos.get_nome() == curso:
                self.disc = disciplina(cod, nome, carga_hr, cursos.get_grade())
                cursos.get_grade().add_disciplinas(self.disc)
                self.listaDisciplinas.append(self.disc)
                self.limiteIns.mostraJanela('Sucesso', 'Disciplina cadastrada com sucesso')
                self.clearHandler(event)
            else:
                self.limiteIns.mostraJanela('Falha', 'Disciplina inexistente')
                self.clearHandler(event)    

    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputCargaHr.delete(0, len(self.limiteIns.inputCargaHr.get()))
        self.limiteIns.inputGrade.delete(0, len(self.limiteIns.inputGrade.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()            
        