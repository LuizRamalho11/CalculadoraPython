# Importando a biblioteca Tkinter

from tkinter import * 
from tkinter import ttk

# Cores

cor1 = "#938e9e"
cor2 = "#cc6606"
cor3 = "#E2E2E2"
cor4 = "#4D6080"
cor5 = "#ffffff"
cor6 = "#000000"
cor7 = "#33549c"

# Criando a janela principal

janela =Tk() 
janela.title('Calculadora Simples') 
janela.geometry("235x310")
janela.config(bg=cor6)

# Criando os frames

tela = Frame(janela, width=239, height=50, bg=cor4, relief=RAISED)
tela.grid(row=0, column=0)

corpo = Frame(janela)
corpo.grid(row=1, column=0)

# Configurando a tela

all_valores = ''  # Variável para armazenar todos os valores digitados
valor = StringVar()  # Variável para armazenar o valor do visor
valor.set(all_valores)  # Inicializando a variável StringVar com o valor vazio/vai passar o valor para o visor

# Funções para calcular e limpar os valores

def calcular():
    global all_valores
    resultado = eval(all_valores)  # Avalia a expressão matemática
    valor.set(resultado)  # Atualiza o visor com o resultado

def limpar():
    global all_valores
    all_valores = ''  # Limpa a variável que armazena os valores
    valor.set(all_valores)  # Atualiza o visor para refletir a limpeza

# Função para adicionar valores ao visor

def valores(processo):
    global all_valores 
    all_valores = all_valores + str(processo) # Adiciona o valor digitado à variável que armazena os valores
    valor.set(all_valores)  # Atualiza o visor com os valores digitados

# Criando Visor
visor = Label(tela, textvariable=valor, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font="Ivy 18", bg=cor4, fg=cor5)
visor.place(x=0, y=0)

# Criando os Botões
b1 = Button(corpo, command = limpar, text="C", width=11, height=2, bg=cor3, fg=cor6,font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b1.grid(row=0, column=0, columnspan=2)

b2 = Button(corpo, command= lambda: valores('%'), text="%", width=5, height=2, bg=cor3, fg=cor6,font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b2.grid(row=0, column=2)

b3 = Button(corpo, command= lambda: valores('/'), text="/", width=5, height=2, bg=cor2, fg=cor5, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b3.grid(row=0, column=3)

b4 = Button(corpo, command= lambda: valores('7'), text="7", width=5, height=2, bg=cor3, fg=cor6,font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b4.grid(row=1, column=0)

b5 = Button(corpo, command= lambda: valores('8'), text="8", width=5, height=2, bg=cor3, fg=cor6, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b5.grid(row=1, column=1)

b6 = Button(corpo, command= lambda: valores('9'), text="9", width=5, height=2, bg=cor3, fg=cor6, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b6.grid(row=1, column=2)

b7 = Button(corpo, command= lambda: valores('*'), text="*", width=5, height=2, bg=cor2, fg=cor5, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b7.grid(row=1, column=3)

b8 = Button(corpo, command= lambda: valores('4'), text="4", width=5, height=2, bg=cor3, fg=cor6,font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b8.grid(row=2, column=0)

b9 = Button(corpo, command= lambda: valores('5'), text="5", width=5, height=2, bg=cor3, fg=cor6, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b9.grid(row=2, column=1)

b10 = Button(corpo, command= lambda: valores('6'), text="6", width=5, height=2, bg=cor3, fg=cor6, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b10.grid(row=2, column=2)

b11 = Button(corpo, command= lambda: valores('-'), text="-", width=5, height=2, bg=cor2, fg=cor5, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b11.grid(row=2, column=3)

b12 = Button(corpo, command= lambda: valores('1'), text="1", width=5, height=2, bg=cor3, fg=cor6,font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b12.grid(row=3, column=0)

b13 = Button(corpo, command= lambda: valores('2'), text="2", width=5, height=2, bg=cor3, fg=cor6,font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b13.grid(row=3, column=1)

b14 = Button(corpo, command= lambda: valores('3'), text="3", width=5, height=2, bg=cor3, fg=cor6, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b14.grid(row=3, column=2)

b15 = Button(corpo, command= lambda: valores('+'), text="+", width=5, height=2, bg=cor2, fg=cor5, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b15.grid(row=3, column=3)

b16 = Button(corpo, command= lambda: valores('0'), text="0", width=11, height=2, bg=cor3, fg=cor6,font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b16.grid(row=4, column=0, columnspan=2)

b17 = Button(corpo, command= lambda: valores('.'), text=".", width=5, height=2, bg=cor3, fg=cor6,font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b17.grid(row=4, column=2)

b18 = Button(corpo, command= calcular, text="=", width=5, height=2, bg=cor2, fg=cor5, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b18.grid(row=4, column=3)

janela.mainloop()