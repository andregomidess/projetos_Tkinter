import tkinter as tk
from tkinter import messagebox

class aluno:
    def __init__(self, nro_matr, nome, curso, historico=None):
        self.__nro_matr = nro_matr
        self.__nome = nome
        self.__curso = curso
        self.__historico = historico
        
        curso.add_alunos(self)
        
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
        
class LimiteMostraAluno():
    def __init__(self, str):
        messagebox.showinfo('Lista de alunos', str)
        
class LimiteConsultaAluno():
    def __init__(self, str):
        messagebox.showinfo('Dados do aluno', str)
        
class LimiteCadastraDiscCursada(tk.toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Cadastrar disciplinas cursadas")
        self.controle = controle
        
        self.frameDisc = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frameSemestre = tk.Frame(self)
        self.frameNota = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNro.pack()
        self.frameNome.pack()
        self.frameCurso.pack()
        self.frameNota.pack()
        self.frameButton.pack()
        
        self.labelDIsc = tk.Label(self.frameDisc,text="Disciplina: ")
        self.labelAno = tk.Label(self.frameAno,text="Ano: ")
        self.labelSemestre = tk.Label(self.frameSemestre, text="Semestre: ")
        self.labelNota = tk.Label(self.frameNota, text="Nota: ")
        self.labelNro.pack(side="left")
        self.labelNome.pack(side="left")   

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
        
class CtrlEstudante():       
    def __init__(self):
        self.listaAlunos = []

    def insereAluno(self):
        self.limiteIns = LimiteInsereAluno(self) 

    def mostraEstudantes(self):
        str = 'Nro Matric. -- Nome\n'
        for est in self.listaEstudantes:
            str += est.getNroMatric() + ' -- ' + est.getNome() + '\n'       
        self.limiteLista = LimiteMostraAluno(str)
        
    def consulta_estudante(self):
        nro_mat = askstring("Consulta por n° matrícula", "Digite n° matrícula")
        for est in self.listaEstudantes:
            if nro_mat == est.getNroMatric():
                str = 'Nro Matric. -- Nome\n'
                str += est.getNroMatric() + ' -- ' + est.getNome() + '\n'
                self.limiteNroMat = LimiteConsultaAluno(str)
                break
            else:
                messagebox.showinfo('Alerta', 'N° de matrícula inexistente')
                break    

    def enterHandler(self, event):
        nroMatric = self.limiteIns.inputNro.get()
        nome = self.limiteIns.inputNome.get()
        curso = self.limiteIns.inputCurso.get()
        self.Aluno = aluno(nroMatric, nome, curso)
        self.Aluno.cria_historico()
        self.listaEstudantes.append(self.Aluno)
        self.limiteIns.mostraJanela('Sucesso', 'Estudante cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputNro.delete(0, len(self.limiteIns.inputNro.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputCurso.delete(0, len(self.limiteIns.inputCurso.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()                       