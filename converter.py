from tkinter import *
from tkinter import ttk
from conv_lekcia import USD, EUR, GBP, CNY, JPY, PKR


converter = Tk()
converter.title("Unit Converter")
converter.geometry("600x400")

OPTIONS = {
    "British Pound":GBP,
    "Chinese Yuan":CNY,
    "Euro":EUR,
    "Japanese Yen":JPY,
    "Pakistani Rupee":PKR,
    "Us Dollar":USD
        }

def ok():
    price = rubles.get()
    answer = variable1.get()
    DICT = OPTIONS.get(answer,None)
    converted = float(DICT)*float(price)
    result.delete(1.0,END)
    result.insert(INSERT,"Цена в ",INSERT,answer,INSERT," = ",INSERT,converted)
appName = Label(converter,text="Конвертер валют",font=("arial",25,"bold"),fg="green")
appName.place(x=170, y=10)

result = Text(converter,height=5,width=50,font=("arial",12,"bold"),bd=5)
result.place(x=125, y=230)

russia = Label(converter,text="Напишите рубли:",font=("arial",12,"bold"),fg="red")
russia.place(x=30, y=83)

rubles = Entry(converter,font=("arial",12))
rubles.place(x=150, y=80)

choice = Label(converter,text="Выберите валюту:",font=("arial",12,"bold"),fg="red")
choice.place(x=30, y=130)

variable1 = StringVar(converter)
variable1.set(None)
option = OptionMenu(converter,variable1,*OPTIONS)
option.place(x=150, y=120,width=150, height=40)

button = Button(converter,text="Конвертировать",fg="green",font=("arial",20),bg="powder blue",command=ok)
button.place(x=220, y=180,height=40,width=200)

converter.mainloop()