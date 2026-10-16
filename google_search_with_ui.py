import pywhatkit
from tkinter import *

def SHOW_RESULTS():
    FETCH_STRING = str(ENTRYBOX.get())
    pywhatkit.search(FETCH_STRING)


Sparsh_Root = Tk()
Sparsh_Root.geometry("853x480")

LABEL1 = Label(Sparsh_Root, text = 'Search something', font = ('Bahnschrift 20 bold'))
LABEL1.pack()

ENTRYBOX = Entry(Sparsh_Root)
ENTRYBOX.pack()

SEARCH_BUTTON = Button(Sparsh_Root, text = 'SEARCH',  bg = 'red', fg = 'blue', activebackground = 'yellow', font = ('Bahnschrift'), command = SHOW_RESULTS)
SEARCH_BUTTON.pack()

PLEASE_NOTE = Label(Sparsh_Root, text = "Please Note!\nWhen you click on the search button, you will be directed to the\n google on your default browser", font = ('Bahnschrift 15 italic'))
PLEASE_NOTE.pack()

# FETCH_STRING = str(ENTRYBOX.get())
# print(pywhatkit.search(FETCH_STRING))

Sparsh_Root.mainloop()
