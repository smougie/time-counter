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


def quote_display():
    quote_bill_gates = 'Software is a great combination between artistry and engineering.\n(Bill Gates)'
    msg_window = Tk()
    msg_window.title('Quote')
    msg = Message(msg_window, text=quote_bill_gates)
    msg.config(bg='pale green', fg='black', font='Times 24 italic', justify='right')
    msg.pack(fill=BOTH)


def choose_option():
    def show_choice():
        print(v.get())
    choose_window = Tk()
    choose_window.title('Choose')
    brakes_values = ['5', '10', '15', '20', '30']
    v = IntVar(master=choose_window)
    options_label = Label(choose_window, text='Długość przerwy:', justify=LEFT, padx=20).pack()
    for option, value in enumerate(brakes_values):
        Radiobutton(choose_window, text=value+' minut', padx=20, variable=v, command=show_choice, value=option).pack(anchor=W)




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


# Creating label for counting seconds and quote button
seconds_label = Label(root, fg='red')
exit_button = Button(root, text='Quit', width=25, command=quit)
quote_button = Button(root, text='Quote', width=35, command=quote_display)
choose_button = Button(root, text='Choose', width=20, command=choose_option)
exit_button.pack(side='bottom')
quote_button.pack(side='bottom')
choose_button.pack(side='bottom')
seconds_label.pack(side='bottom')
counter_label(seconds_label)

# Creating radio button



# Running the tkinter event loop which works until we close the window.
root.mainloop()
