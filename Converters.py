from tkinter import *

ms = Tk()
ms.geometry('400x300')
ms.title('Converters')
ms['bg'] = '#5d8a82'
ms.resizable(False, False)

f = ("Times bold", 14)

def temperature():
    ms.destroy()
    import temperature_converter


def distance():
    ms.destroy()
    import Distance_Converter


def weight():
    ms.destroy()
    import weight_Converter


def number_system():
    ms.destroy()
    import number


Label(
    ms,
    text="Converters",
    padx=20,
    pady=20,
    bg='#5d8a82',
    font=f
).place(relx=0.5, rely=0.1, anchor=CENTER)

Button(
    ms,
    text="Temperature Converter",
    font=f,
    bg='#8ed2c7',
    command=temperature
).place(relx=0.5, rely=0.3, anchor=CENTER)

Button(
    ms,
    text="Weight Converter",
    font=f,
    bg='#8ed2c7',
    command=weight
).place(relx=0.5, rely=0.5, anchor=CENTER)

Button(
    ms,
    text="Distance Converter",
    font=f,
    bg='#8ed2c7',
    command=distance
).place(relx=0.5, rely=0.7, anchor=CENTER)

Button(
    ms,
    text="Number system Converter",
    font=f,
    bg='#8ed2c7',
    command=number_system
).place(relx=0.5, rely=0.9, anchor=CENTER)



ms.mainloop()