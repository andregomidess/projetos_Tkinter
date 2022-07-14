import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import aluno as alu
import curso
import disciplina as disc

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.alunoMenu = tk.Menu(self.menubar)
        self.cursoMenu = tk.Menu(self.menubar)
        self.disciplinaMenu = tk.Menu(self.menubar)     

        self.alunoMenu.add_command(label="Cadastrar aluno", \
                    command=self.controle.insereAluno)
        self.alunoMenu.add_command(label="Cadastrar disciplina cursada", \
                    command=self.controle.cadastraDiscAluno)
        self.alunoMenu.add_command(label="Consultar", command=self.controle.consultaAluno)
        self.menubar.add_cascade(label="Aluno", \
                    menu=self.alunoMenu)

        self.cursoMenu.add_command(label="Cadastrar Curso", \
                    command=self.controle.cadastrarCurso)
        self.cursoMenu.add_command(label="Consultar", command=self.controle.consultaCurso)        
        self.menubar.add_cascade(label="Curso", \
                    menu=self.cursoMenu)

        self.disciplinaMenu.add_command(label="Cadastrar", command=self.controle.consultaDisciplina)                     
        self.menubar.add_cascade(label="Disciplina", \
                    menu=self.disciplinaMenu)        

        self.root.config(menu=self.menubar)
        
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlAluno = alu.CtrlAluno(self)
        self.ctrlCurso = curso.CtrlCurso(self)
        self.ctrlDisciplina = disc.CtrlDisciplina(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Trabalho 12")
        # Inicia o mainloop
        self.root.mainloop()
        
    def insereAluno(self):
        self.ctrlAluno.insereAluno()
        
    def cadastraDiscAluno(self):
        self.ctrlAluno.cadastraDiscAluno()
        
    def consultaAluno(self):
        self.ctrlAluno.consultaAluno()
        
    def cadastrarCurso(self):
        self.ctrlCurso.cadastrarCurso()
        
    def consultaCurso(self):
        self.ctrlCurso.consultaCurso()
        
    def consultaDisciplina(self):
        self.ctrlDisciplina.consultaDisciplina()                    
            
        
        
if __name__ == '__main__':
    c = ControlePrincipal()                