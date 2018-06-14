from tkinter import *

# Initializing Tkinter by creating TK root widget - window with title bar.
root = Tk()

# Loading and resizing a label with logo
logo = PhotoImage(file='timer_logo.gif')
logo = logo.zoom(17)
logo = logo.subsample(70)
logo_label = Label(root, image=logo).pack(side='right')

# Creating a label with short api description
explanatation = '''
Tutaj znajdzie się krótki opis działania programu.
Może to być również wielolinijkowy opis.
Test testowanego testu testów.'''
description_label = Label(root, justify=LEFT, padx=10, text=explanatation).pack(side='left')


# Running the tkinter event loop which works until we close the window.
root.mainloop()