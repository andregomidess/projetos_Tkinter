from cProfile import label
from tkinter import *
from tkinter import messagebox

def calcula_idade():
    pass    


if __name__ == '__main__':
   
   janela = Tk()
   # label azul
   janela.title('Calculadora de idade')
   data_niver = Label(janela, text='Data do aniversario', background='blue')
   data_niver.grid(column=1, row=0, padx=0, pady=3)
   #dia do niver
   dia_niver_label = Label(janela, text='Dia')
   dia_niver_label.grid(column=0, row=1)
   dia_niver = Entry(janela, text='Dia')
   dia_niver.grid(column=1, row=1)
   # mes do niver
   mes_niver_label = Label(janela, text='Mês').grid(column=0, row=2)
   mes_niver = Entry(janela)
   mes_niver.grid(column=1, row=2)
   # ano do niver
   ano_niver_label = Label(janela, text='Ano').grid(column=0, row=3)
   ano_niver = Entry(janela)
   ano_niver.grid(column=1, row=3)
   # botão resultado
   botao_result = Button(janela, text='Calcular idade', background='red')
   botao_result.grid(column=2, row=4, padx =10, pady=10)
   # anos resultado
   anos_result_label = Label(janela, text='Anos')
   anos_result_label.grid(column=2, row=5)
   anos_result_entry = Entry(janela)
   anos_result_entry.grid(column=2, row=6)
   # resultado meses
   meses_result_label = Label(janela, text='meses')
   meses_result_label.grid(column=2, row=7)
   meses_result_entry = Entry(janela)
   meses_result_entry.grid(column=2, row=8)
   # resultado dias
   dias_result_label = Label(janela, text='Dias')
   dias_result_label.grid(column=2, row=9)
   dias_result_entry = Entry(janela)
   dias_result_entry.grid(column=2, row=10)
   
   data_niver = Label(janela, text='Data do aniversario', background='blue')
   data_niver.grid(column=1, row=0, padx=0, pady=3)
   
   
   janela.mainloop() 