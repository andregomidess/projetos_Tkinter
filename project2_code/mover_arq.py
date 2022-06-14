import os, shutil
from tkinter import *
from tkinter import filedialog, messagebox


def pergunta_dir_origem():
    global origem
    origem = filedialog.askdirectory()
    pasta_origem_entry.insert(0, origem)
    

def pergunta_dir_dest():
    global destino
    destino = filedialog.askdirectory()
    pasta_destino_entry.insert(0, destino)    
    
    
def copia_seletiva():
    pasta_origem = os.path.abspath(str(pasta_origem_entry.get()))
    print(pasta_origem )
    pasta_destino = os.path.abspath(str(pasta_destino_entry.get()))
    for foldername, subfolders, filenames in os.walk(pasta_origem):
        for filename in filenames:
            if filename.endswith('.py'):
                shutil.copy(os.path.join(foldername, filename), pasta_destino)

if __name__ == '__main__':
    janela = Tk()
    janela.title('Copiador de .py')
    pasta_origem = Label(janela, text='Pasta origem', background='red')
    pasta_origem.grid(column = 0, row = 0, padx=3, pady=10)
    pasta_origem_entry = Entry(janela)
    pasta_origem_entry.grid(column=2, row=0, padx=3, pady=10)
    button_pasta_origem = Button(janela, text='Procurar', background='white', command = pergunta_dir_origem)
    button_pasta_origem.grid(column =3, row=0)
    
    pasta_destino = Label(janela, text='Pasta destino', background='red')
    pasta_destino.grid(column = 0, row = 1, padx=3, pady=10)
    pasta_destino_entry = Entry(janela)
    pasta_destino_entry.grid(column=2, row=1, padx=3, pady=10)
    button_pasta_dest = Button(janela, text='Procurar', background='white', command = pergunta_dir_dest)
    button_pasta_dest.grid(column =3, row=1)
    
    button_confirm = Button(janela, text='Confirmar copia .py', background='green', command=copia_seletiva).grid(column=2, row=2)
    
    
    janela.mainloop()   