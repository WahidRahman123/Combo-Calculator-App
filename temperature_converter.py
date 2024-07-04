
#Best temperature Converter:

from tkinter import *

def convert_fahr():
    words = fbtext.get()
    ftemp = float(words)
    celbox.delete(0, END)
    celbox.insert(0, '%.2f' % (tocel(ftemp)))
    kelbox.delete(0, END)
    kelbox.insert(0, '%.2f' % (tokel(tocel(ftemp))))
    return

def convert_cel():
    words = cbtext.get()
    ctemp = float(words)
    fahrbox.delete(0, END)
    fahrbox.insert(0, '%.2f' % (tofahr(ctemp)))
    kelbox.delete(0, END)
    kelbox.insert(0, '%.2f' % (tokel(ctemp)))

def convert_kel():
    words = kbtext.get()
    ktemp = float(words)
    fahrbox.delete(0, END)
    fahrbox.insert(0, '%.2f' % (tofahr(ktoc(ktemp))))
    celbox.delete(0, END)
    celbox.insert(0, '%.2f' % (ktoc(ktemp)))

def tocel(fahr):
    return (fahr-32) * 5.0 / 9.0

def tofahr(cel):
    return cel * 9.0 / 5.0 + 32

def ktoc(kel):
    return kel - 273.15

def tokel(cel):
    return cel + 273.15

app = Tk()
app.title('Temperature')
app.geometry("252x140")
app.resizable(False, False)
app['bg'] = '#5d8a82'

fahrlabel = Label(app, text = 'FAHRENHEIT', bg="#5d8a82")
fahrlabel.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = E)

cellabel = Label(app, text = 'CELSIUS', bg="#5d8a82")
cellabel.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = E)

kellabel = Label(app, text = 'KELVIN', bg="#5d8a82")
kellabel.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = E)

fbtext = StringVar()
fbtext.set('')
fahrbox = Entry(app, textvariable=fbtext, bg='#8ed2c7')
fahrbox.grid(row=0, column=1, padx=5, pady=5)

cbtext = StringVar()
cbtext.set('')
celbox = Entry(app, textvariable=cbtext, bg='#8ed2c7')
celbox.grid(row=1, column=1, padx=5, pady=5)

kbtext = StringVar()
kbtext.set('')
kelbox = Entry(app, textvariable=kbtext, bg='#8ed2c7')
kelbox.grid(row=2, column=1, padx=5, pady = 5)

fgobutton = Button(app, text='Go', bg='#8ed2c7', command=convert_fahr)
fgobutton.grid(row=0, column=2, padx=5, pady=5, sticky=N+S+E+W)

cgobutton = Button(app, text='Go', bg='#8ed2c7', command=convert_cel)
cgobutton.grid(row=1, column=2, padx=5, pady=5, sticky=N+S+E+W)

kgobutton = Button(app, text='Go', bg='#8ed2c7', command=convert_kel)
kgobutton.grid(row=2, column=2, padx=5, pady=5, sticky=N+S+E+W)

exitbutton = Button(app, text='Exit', bg='#8ed2c7', command=quit)
exitbutton.grid(row=3, column=0, padx=5, pady=5, sticky=N+S+E+W, columnspan=3)

app.mainloop()