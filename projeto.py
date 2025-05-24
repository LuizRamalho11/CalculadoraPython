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

janela =Tk()
janela.title('Calculadora Simples')
janela.geometry("235x318")
janela.config(bg=cor6)

# Criando os frames
tela = Frame(janela, width=235, height=50, bg=cor4, )
tela.grid(row=0, column=0)

corpo = Frame(janela, width=235, height=268)
corpo.grid(row=1, column=0)

# Criando Visor
visor = Label(tela, text="123456789", width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font="Ivy 18", bg=cor4, fg=cor5)
visor.place(x=0, y=0)


# Criando os Botões
b1 = Button(corpo, text="C", width=11, height=2, bg=cor3, fg=cor6,font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)
b2 = Button(corpo, text="%", width=5, height=2, bg=cor3, fg=cor6,font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b2.place(x=118, y=0)
b3 = Button(corpo, text="/", width=5, height=2, bg=cor2, fg=cor5, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b3.place(x=177, y=0)

b4 = Button(corpo, text="7", width=5, height=2, bg=cor3, fg=cor6,font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=52)
b5 = Button(corpo, text="8", width=5, height=2, bg=cor3, fg=cor6, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b5.place(x=59, y=52)
b6 = Button(corpo, text="9", width=5, height=2, bg=cor3, fg=cor6, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b6.place(x=118, y=52)
b7 = Button(corpo, text="*", width=5, height=2, bg=cor2, fg=cor5, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b7.place(x=177, y=52)

b8 = Button(corpo, text="4", width=5, height=2, bg=cor3, fg=cor6,font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b8.place(x=0, y=104)
b9 = Button(corpo, text="5", width=5, height=2, bg=cor3, fg=cor6, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b9.place(x=59, y=104)
b10 = Button(corpo, text="6", width=5, height=2, bg=cor3, fg=cor6, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b10.place(x=118, y=104)
b11 = Button(corpo, text="-", width=5, height=2, bg=cor2, fg=cor5, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b11.place(x=177, y=104)

b12 = Button(corpo, text="1", width=5, height=2, bg=cor3, fg=cor6,font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b12.place(x=0, y=156)
b13 = Button(corpo, text="2", width=5, height=2, bg=cor3, fg=cor6,font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b13.place(x=59, y=156)
b14 = Button(corpo, text="3", width=5, height=2, bg=cor3, fg=cor6, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b14.place(x=118, y=156)
b15 = Button(corpo, text="+", width=5, height=2, bg=cor2, fg=cor5, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b15.place(x=177, y=156)

b16 = Button(corpo, text="0", width=11, height=2, bg=cor3, fg=cor6,font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b16.place(x=0, y=208)
b17 = Button(corpo, text=".", width=5, height=2, bg=cor3, fg=cor6,font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b17.place(x=118, y=208)
b18 = Button(corpo, text="=", width=5, height=2, bg=cor2, fg=cor5, font="Ivy 13 bold", relief=RAISED, overrelief=RIDGE)
b18.place(x=177, y=208)

janela.mainloop()