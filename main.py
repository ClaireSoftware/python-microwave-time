from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import Text
from tkinter import Image
from tkinter import Canvas
from PIL import ImageTk, Image
from pyzbar.pyzbar import decode
def check():
    # use this to make sure a keyboardinterrupt quits the program
    root.after(50, check)


def displayQR(*args):
    try:
        timeMins, timeSecs = timeinput.get().split(":")
        totalSecs = (int(timeMins) * 60) + int(timeSecs)

        cookingTime = (1000/700) * totalSecs

        outputString = (f'Adjusted cooking time is {int(cookingTime // 60)}:{int(cookingTime % 60)}')
        outputLabel.config(text=outputString)
    except ValueError:
        pass

times = []

for i in range(1, 30):
    times.append(str(i) + ":00")
    times.append(str(i) + ":30")

root = Tk()
root.title("Claire's Microwave Wattage Prog")


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

filepicked = StringVar()

# Making another frame to make file name and output go together
doublegrid = ttk.Frame(mainframe, padding="0 0 0 0")
doublegrid.grid(column=1, row=1, sticky=W)

ttk.Label(doublegrid, text="Time for 1000W: ").grid(column=1, row=1, sticky=W)
timeinput = ttk.Combobox(doublegrid, values=times, width=5)
timeinput.grid(column=1, row=2, sticky=W)

ttk.Button(doublegrid, text="Compute value", command=displayQR).grid(column=1, row=3)
outputLabel = ttk.Label(doublegrid)
outputLabel.grid(column=1, row=4, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.after(50, check)
root.mainloop()
