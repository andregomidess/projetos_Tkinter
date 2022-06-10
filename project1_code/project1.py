from cProfile import label
from tkinter import *
from tkinter import messagebox

def calcula_idade():
    diaNiver = int(dia_niver.get())
    mesNiver = int(mes_niver.get())
    anoNiver = int(ano_niver.get())
    
    diaDesejado = int(dia_desejado.get())
    mesDesejado = int(mes_desejado.get())
    anoDesejado = int(ano_desejado.get())
    
    anos = anoDesejado - anoNiver
    meses = mesDesejado - mesNiver
    dias = diaDesejado - diaNiver
    if meses < 0:
        anos -= 1
        meses += 12
    if dias < 0:
        dias += 30
        meses -= 1  
            
      


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
   # label data desejada azul
   data_desejada = Label(janela, text='Data desejada', background='blue')
   data_desejada.grid(column=4, row=0, padx=0, pady=3)
   
   dia_desejado_label = Label(janela, text='Dia desejado')
   dia_desejado_label.grid(column=3, row=1)
   dia_desejado = Entry(janela, text='Dia')
   dia_desejado.grid(column=4, row=1)
   # mes do niver
   mes_desejado_label = Label(janela, text='Mês desejado').grid(column=3, row=2)
   mes_desejado = Entry(janela)
   mes_desejado.grid(column=4, row=2)
   # ano do niver
   ano_desejado_label = Label(janela, text='Ano desejado').grid(column=3, row=3)
   ano_desejado = Entry(janela)
   ano_desejado.grid(column=4, row=3)
   
   
   janela.mainloop() 