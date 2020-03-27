from tkinter import *

janela = Tk()
janela.geometry("450x450+300+300")

def bt_click1():
    import Aula01e02.py

def bt_click2():
    import Aula3.py

def bt_click3():
    import Aula4.py

def bt_click4():
    import Aula5.py

def bt_click5():
    import Aula6.py

def bt_click6():
    import Aula7.py

def bt_click7():
    import Aula8.py

def bt_click8():
    import Aula9.py

def bt_click9():
    import Aula10.py

def bt_click10():
    import MenuAulasProntas.py


bt1 = Button(janela, width=90, text="Aula01e02", bg="red", height="7")
bt1["command"] = (bt_click1)
bt1.place(x=10, y=60)

bt2 = Button(janela, width=90, text="Aula03", bg="blue", height="7")
bt2["command"] = (bt_click2)
bt2.place(x=10, y=180)

bt3 = Button(janela, width=90, text="Aula04", bg="yellow", height="7")
bt3["command"] = (bt_click3)
bt3.place(x=10, y=300)

bt4 = Button(janela, width=90, text="Aula05", bg="darkblue", height="7")
bt4["command"] = (bt_click4)
bt4.place(x=10, y=420)

bt5 = Button(janela, width=90, text="Aula06", bg="gray", height="7")
bt5["command"] = (bt_click5)
bt5.place(x=710, y=60)

bt6 = Button(janela, width=90, text="Aula07", bg="pink", height="7")
bt6["command"] = (bt_click6)
bt6.place(x=710, y=180)

bt7 = Button(janela, width=90, text="Aula08", bg="orange", height="7")
bt7["command"] = (bt_click7)
bt7.place(x=710, y=300)

bt8 = Button(janela, width=90, text="Aula09", bg="green", height="7")
bt8["command"] = (bt_click8)
bt8.place(x=710, y=420)

bt9 = Button(janela, width=90, text="Aula10", bg="beige", height="7")
bt9["command"] = (bt_click9)
bt9.place(x=710, y=540)

bt10 = Button(janela, width=90, text="Ver todas as Aulas Juntas", bg="darkgreen", height="7")
bt10["command"] = (bt_click10)
bt10.place(x=10, y=540)

lb = Label(janela, text="Testando Projeto de Linguagem de Programação Final - Python - Teste Concluido com Sucesso",
font=('Times', '25'))
lb.place(x=100, y=5)

janela.geometry("1400x700+00+00")
janela.mainloop()