import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.simpledialog import askstring
import aluno as alu
import curso
import disciplina as disc

class aluno:
    def __init__(self, nro_matr, nome, curso, historico=None):
        self.__nro_matr = nro_matr
        self.__nome = nome
        self.__curso = curso
        self.__historico = historico
    
        
    def get_nro_matr(self):
        return self.__nro_matr
    
    def get_nome(self):
        return self.__nome
    
    def get_curso(self):
        return self.__curso
    
    def get_historico(self):
        return self.__historico
    
    def cria_historico(self):
        self.__historico = historico(self)
    
    def inserir_disciplina_hist(self, disciplina):
        self.__historico.add_disciplina(disciplina)
        
class historico:

    def __init__(self, aluno):
        self.__aluno = aluno
        self.__disciplinas = []
        
    def get_aluno(self):
        return self.__aluno
    
    def get_disciplinas(self):
        return self.__disciplinas
    
    def add_disciplina(self, disciplina):
        self.__disciplinas.append(disciplina)
        
        
class LimiteInsereAluno(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Aluno")
        self.controle = controle

        self.frameNro = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameCurso = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNro.pack()
        self.frameNome.pack()
        self.frameCurso.pack()
        self.frameButton.pack()
      
        self.labelNro = tk.Label(self.frameNro,text="Nro Matrícula: ")
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelCurso = tk.Label(self.frameCurso, text="Curso: ")
        self.labelNro.pack(side="left")
        self.labelNome.pack(side="left")
        self.labelCurso.pack(side="left")   

        self.inputNro = tk.Entry(self.frameNro, width=20)
        self.inputNro.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")
        self.inputCurso = tk.Entry(self.frameCurso, width=20)
        self.inputCurso.pack(side="left")        
      
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
        
class LimiteConsultaAluno():
    def __init__(self, str):
        messagebox.showinfo('Historico do aluno', str)
        
class LimiteCadastraDiscCursada(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('300x150')
        self.title("Cadastrar disciplinas cursadas")
        self.controle = controle
        
        self.frameNroMat = tk.Frame(self)
        self.frameDisc = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frameSemestre = tk.Frame(self)
        self.frameNota = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNroMat.pack()
        self.frameDisc.pack()
        self.frameAno.pack()
        self.frameSemestre.pack()
        self.frameNota.pack()
        self.frameButton.pack()
        
        self.labelNroMat = tk.Label(self.frameNroMat, text="N° matricula do aluno: ")
        self.labelDisc = tk.Label(self.frameDisc,text="Disciplina cursada: ")
        self.labelAno = tk.Label(self.frameAno,text="Ano: ")
        self.labelSemestre = tk.Label(self.frameSemestre, text="Semestre: ")
        self.labelNota = tk.Label(self.frameNota, text="Nota: ")
        self.labelNroMat.pack(side="left")
        self.labelDisc.pack(side="left")
        self.labelAno.pack(side="left")
        self.labelSemestre.pack(side="left")
        self.labelNota.pack(side="left")   

        self.inputNroMat = tk.Entry(self.frameNroMat, width=20)
        self.inputNroMat.pack(side="left")
        self.inputDisc = tk.Entry(self.frameDisc, width=20)
        self.inputDisc.pack(side="left")
        self.inputAno = tk.Entry(self.frameAno, width=20)
        self.inputAno.pack(side="left")
        self.inputSemestre = tk.Entry(self.frameSemestre, width=20)
        self.inputSemestre.pack(side="left")
        self.inputNota = tk.Entry(self.frameNota, width=20) 
        self.inputNota.pack(side="left")       
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandlerDisc)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandlerDisc)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandlerDisc)
        
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
        
class CtrlAluno():       
    def __init__(self, controlePrincipal):
        self.ControlePrincipal = controlePrincipal
        self.listaAlunos = []
        self.listaAprovReprov = []

    def insereAluno(self):
        self.limiteIns = LimiteInsereAluno(self)
        
    def cadastraDiscAluno(self):
        self.limiteDiscAl = LimiteCadastraDiscCursada(self)        
        
    def consultaAluno(self):
        nro_mat = askstring("Consulta por n° matrícula", "Digite n° matrícula")
        tam = 0
        string = 'Disciplina -- Ano -- Semestre -- Nota -- Situação \n'
        for al in self.listaAlunos:
            if nro_mat == al.get_nro_matr():
                for disc_al in al.get_historico().get_disciplinas():
                    string += disc_al.get_nome() + ': ' +  self.listaAprovReprov[tam] + '\n'
                    tam += 1
            else:
                messagebox.showinfo('Alerta', 'N° de matrícula inexistente')
                break
        self.LimiteMostra = LimiteConsultaAluno(string)        

    def enterHandler(self, event):
        nroMatric = self.limiteIns.inputNro.get()
        nome = self.limiteIns.inputNome.get()
        curso = self.limiteIns.inputCurso.get()
        Aluno = aluno(nroMatric, nome, curso)
        Aluno.cria_historico()
        listaCursos = self.ControlePrincipal.ctrlCurso.listaCursos
        for c in listaCursos:
            if c.get_nome() == curso:
                c.add_alunos(Aluno)
                self.listaAlunos.append(Aluno)
                self.limiteIns.mostraJanela('Sucesso', 'Estudante cadastrado com sucesso')
                self.clearHandler(event)
            #else:
                #self.limiteIns.mostraJanela('Falha', 'Este curso não existe')
                #self.clearHandler(event)    

    def clearHandler(self, event):
        self.limiteIns.inputNro.delete(0, len(self.limiteIns.inputNro.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputCurso.delete(0, len(self.limiteIns.inputCurso.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()
        
        
    def enterHandlerDisc(self, event):
        nMat = self.limiteDiscAl.inputNroMat.get()
        disc = self.limiteDiscAl.inputDisc.get()
        ano = self.limiteDiscAl.inputAno.get()
        semestre = self.limiteDiscAl.inputSemestre.get()
        nota = self.limiteDiscAl.inputNota.get()
        str = ''
        for alunos in self.listaAlunos:
            if alunos.get_nro_matr() == nMat:
                for discip in self.ControlePrincipal.ctrlDisciplina.listaDisciplinas:
                    if disc == discip.get_nome():
                        alunos.inserir_disciplina_hist(discip)
                        if float(nota) >= 6.0:
                            str = ano + ' ' + semestre + ' ' + nota + ' APROVADO'
                        else:
                            str = ano + semestre + nota + 'REPROVADO'
                        self.listaAprovReprov.append(str)       
                        self.limiteIns.mostraJanela('Sucesso', 'Disciplina cadastrada com sucesso')
                    #else:
                        #self.limiteIns.mostraJanela('Falha', 'Disciplina inexistente!')
                            
            else:
                self.limiteIns.mostraJanela('Falha', 'N° informado não existe')
                break    
                        
        self.clearHandlerDisc(event)

    def clearHandlerDisc(self, event):
        self.limiteDiscAl.inputNroMat.delete(0, len(self.limiteDiscAl.inputNroMat.get()))
        self.limiteDiscAl.inputDisc.delete(0, len(self.limiteDiscAl.inputDisc.get()))
        self.limiteDiscAl.inputAno.delete(0, len(self.limiteDiscAl.inputAno.get()))
        self.limiteDiscAl.inputSemestre.delete(0, len(self.limiteDiscAl.inputSemestre.get()))
        self.limiteDiscAl.inputNota.delete(0, len(self.limiteDiscAl.inputNota.get()))

    def fechaHandlerDisc(self, event):
        self.limiteDiscAl.destroy()                           