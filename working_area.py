from tkinter import *
# Function section
counter = 3600000


def counter_label(label):
    def count():
        global counter
        counter -= 1
        label.config(text=str(counter))
        label.after(1000, count)

    count()


# Initializing Tkinter by creating TK root widget - window with title bar.
root = Tk()
root.title('Time Counter')

# Loading and resizing a label with logo
logo = PhotoImage(file='timer_logo.gif')
logo = logo.zoom(17)
logo = logo.subsample(70)
logo_label = Label(root, image=logo).pack(side='right')

# Creating description header
header_txt = 'Opis:'
description_header_label = Label(root,
                                 text=header_txt,
                                 fg='white',
                                 bg='black',
                                 font='Helvetica 16 bold').pack(side='top')

# Creating a label with short api description
explanatation = '''
Tutaj znajdzie się krótki opis działania programu.
Może to być również wielolinijkowy opis.
Test testowanego testu testów.'''
description_label = Label(root, justify=LEFT, padx=10, text=explanatation).pack(side='left')


# Creating label for counting seconds
seconds_label = Label(root, fg='red')
exit_button = Button(root, text='Quit', width=25, command=root.destroy)
exit_button.pack(side='bottom')
seconds_label.pack(side='bottom')
counter_label(seconds_label)

# Running the tkinter event loop which works until we close the window.
root.mainloop()
