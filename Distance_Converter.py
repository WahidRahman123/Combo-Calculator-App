from tkinter import Tk, Label, Entry, Button, DISABLED, StringVar


def convert_mile():
    """Takes miles entered, converts them to km, and displays the result"""
    miles = float(entryMiles.get())
    kilometers.set(str(miles * 1.60934))

def convert_km():
    kilo = float(entryKm.get())
    mi.set(str(kilo * 0.621371))

#def clear():
#    entryMiles.delete(0,END)
#    entryKm.delete(0,END)


# create the GUI

rootWindow = Tk()  # create main window
rootWindow.title("Miles to kilometers")
rootWindow.geometry('525x98+0+0')
rootWindow.grid_columnconfigure(1, weight=1)
rootWindow.resizable(False, False)
rootWindow['bg'] = '#5d8a82'

labelMiles = Label(rootWindow, text='Distance in miles:', bg='#5d8a82')  # create label for miles field
labelMiles.grid(row=0, column=0)

labelKm = Label(rootWindow, text='Distance in kilometers:', bg='#5d8a82')  # create label for km field
labelKm.grid(row=2, column=0)

mi = StringVar()
entryMiles = Entry(rootWindow, textvariable=mi, bg='#8ed2c7')  # create entry field for miles
entryMiles.grid(row=0, column=1, sticky='w,e')

kilometers = StringVar()  # create entry field for displaying km
entryKm = Entry(rootWindow, textvariable=kilometers, bg='#8ed2c7')
entryKm.grid(row=2, column=1, sticky='w,e')

convertButton = Button(rootWindow, text='Convert', command=convert_mile, bg='#8ed2c7')  # create button for running conversion
convertButton.grid(row=1, column=1)
convertButton = Button(rootWindow, text='Convert', command=convert_km, bg='#8ed2c7')  # create button for running conversion
convertButton.grid(row=3, column=1)
#ee = Label(rootWindow, text=" ", bg="#5d8a82").grid(row=4, column=0)
#convertButton = Button(rootWindow, text='Clear', command=clear, bg='#8ed2c7')  # create button for running conversion
#convertButton.grid(row=5, column=1)
# run the event processing loop  

rootWindow.mainloop()