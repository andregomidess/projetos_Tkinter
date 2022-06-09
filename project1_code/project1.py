from cProfile import label
from tkinter import *
from tkinter import messagebox

def calcula_idade():
    pass    


if __name__ == '__main__':
   
   janela = Tk()
   janela.title('Calculadora de idade')
   data_niver = Label(janela, text='Data do aniversario', background='blue')
   data_niver.grid(column=1, row=0, padx=0, pady=3)
   
   dia_niver_label = Label(janela, text='Dia')
   dia_niver_label.grid(column=0, row=1)
   dia_niver = Entry(janela, text='Dia')
   dia_niver.grid(column=1, row=1)
   
   mes_niver_label = Label(janela, text='Mês').grid(column=0, row=2)
   mes_niver = Entry(janela)
   mes_niver.grid(column=1, row=2)
   
   ano_niver_label = Label(janela, text='Ano').grid(column=0, row=3)
   ano_niver = Entry(janela)
   ano_niver.grid(column=1, row=3)
   
   
   
   
   janela.mainloop() 