import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.simpledialog import askstring
import aluno as alu
import curso
import disciplina as disc

class Curso:
    
    def __init__(self, nome, grade=None):
        self.__nome = nome
        self.__alunos = []
        self.__grade = grade
        
        
        
    def get_nome(self):
        return self.__nome
    
    def get_alunos(self):
        return self.__alunos
    
    def get_grade(self):
        return self.__grade
    
    def add_alunos(self, aluno):
        self.__alunos.append(aluno)
        
    def cria_grade(self, ano):
        self.__grade = grade(ano, self)   
    
class grade:
    
    def __init__(self, ano, curso):
        self.__ano = ano
        self.__curso = curso
        self.__disciplinas = []
    
    def get_ano(self):
        return self.__ano
    
    def get_curso(self):
        return self.__curso
    
    def get_disciplinas(self):
        return self.__disciplinas
    
    def add_disciplinas(self, disciplina):
        self.__disciplinas.append(disciplina)
        
        
class LimiteCadastrarCurso(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Cadsatrar curso")
        self.controle = controle

        self.frameCurso = tk.Frame(self)
        self.frameAnoGrade = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCurso.pack()
        self.frameAnoGrade.pack()
        self.frameButton.pack()
      
        self.labelCurso = tk.Label(self.frameCurso, text="Curso: ")
        self.labelCurso.pack(side="left")
        
        self.labelAnoGrade = tk.Label(self.frameAnoGrade, text="Ano da grade: ")
        self.labelAnoGrade.pack(side="left")      

        self.inputCurso = tk.Entry(self.frameCurso, width=20)
        self.inputCurso.pack(side="left")
        
        self.inputAnoGrade = tk.Entry(self.frameAnoGrade, width=20)
        self.inputAnoGrade.pack(side="left")         
      
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
        
class LimiteConsultaCurso(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Consultar curso")
        self.controle = controle

        self.frameCursoNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCursoNome.pack()
        self.frameButton.pack()
      
        self.labelCursoNome = tk.Label(self.frameCursoNome, text="Curso: ")
        self.labelCursoNome.pack(side="left")     

        self.inputCursoNome = tk.Entry(self.frameCursoNome, width=20)
        self.inputCursoNome.pack(side="left")         
      
        self.buttonConsulta = tk.Button(self.frameButton ,text="Consultar")      
        self.buttonConsulta.pack(side="left")
        self.buttonConsulta.bind("<Button>", controle.enterHandlerConsulta)
      
        
class CtrlCurso():
    
    def __init__(self, controlePrincipal):
        self.ControlePrincipal = controlePrincipal
        self.listaCursos = []
    
    def cadastrarCurso(self):
        self.limiteIns = LimiteCadastrarCurso(self)
     
    def consultaCurso(self):
        self.LimiteCons = LimiteConsultaCurso(self)           
        
    def enterHandler(self, event):
        cursoNome = self.limiteIns.inputCurso.get()
        AnoGrade = self.limiteIns.inputAnoGrade.get()
        self.curso = Curso(cursoNome)
        self.curso.cria_grade(AnoGrade)
        self.listaCursos.append(self.curso)
        self.limiteIns.mostraJanela('Sucesso', 'Curso cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputCurso.delete(0, len(self.limiteIns.inputCurso.get()))
        self.limiteIns.inputAnoGrade.delete(0, len(self.limiteIns.inputAnoGrade.get()))
    

    def fechaHandler(self, event):
        self.limiteIns.destroy()
        
    def enterHandlerConsulta(self, event):
        curso = self.LimiteCons.inputCursoNome.get()
        string = ''
        for cursos in self.listaCursos:
            if cursos.get_nome() == curso:
                for i in cursos.get_grade().get_disciplinas():
                    string += i.get_codigo() + i.get_nome() + i.get_carga_hr() + '\n'
                               
        self.limiteIns.mostraJanela('Grade Curso', string)        
        
                            