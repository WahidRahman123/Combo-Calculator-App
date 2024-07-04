from tkinter import *

ws = Tk()
ws.geometry('400x300')
ws.title('Main Page')
ws['bg'] = '#5d8a82'
ws.resizable(False, False)


f = ("Times bold", 14)


def cal():
    ws.destroy()
    import calculators


def con():
    ws.destroy()
    import Converters


Label(
    ws,
    text="Select your desired choice",
    padx=20,
    pady=20,
    bg='#5d8a82',
    font=f
).place(relx=0.5, rely=0.1, anchor=CENTER)

Button(
    ws,
    text="Calculator",
    font=f,
    bg='#8ed2c7',
    command=cal
).place(relx=0.5, rely=0.4, anchor=CENTER)

Button(
    ws,
    text="Converters",
    font=f,
    bg='#8ed2c7',
    command=con
).place(relx=0.5, rely=0.6, anchor=CENTER)

ws.mainloop()