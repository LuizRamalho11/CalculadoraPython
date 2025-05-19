from tkinter import *
from tkinter import ttk

cor1 = "#938e9e"
cor2 = "#cc6606"
cor3 = "#444444"
cor4 = "#393a3d"
cor5 = "#ffffff"
cor6 = "#1f1736"
cor7 = "#33549c"

j = Tk()
j.title("Calculadora Simples")
j.geometry("230x266")
j.config(bg=cor1)

divisao1 = Frame(j, width=230, height=58, bg=cor3)
divisao1.grid(row=0, column=0)

divisao2 = Frame(j, width=230, height=208, bg=cor1)
divisao2.grid(row=1, column=0)

visor = Label(divisao1, text="0", width=16, height=2, bg=cor3, fg=cor5, anchor="e", relief=FLAT, padx=10, justify=RIGHT, font=(" Ivy 17"))
visor.place(x=0, y=0)

b1 = Button(divisao2, text="C", width=15, height=3, bg=cor4, fg=cor5, relief=RAISED, overrelief=RIDGE, )
b1.place(x=0, y=0)

b2 = Button(divisao2, text="%", width=7, height=3, bg=cor4, fg=cor5, relief=RAISED, overrelief=RIDGE)
b2.place(x=115, y=0)

b3 = Button(divisao2, text="/", width=7, height=3, bg=cor2, fg=cor5, relief=RAISED, overrelief=RIDGE)
b3.place(x=172.5, y=0)

j.mainloop()