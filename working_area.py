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
    Label(choose_window, text='Długość przerwy:', justify=LEFT, padx=20).pack()
    for option, value in enumerate(brakes_values):
        Radiobutton(choose_window,
                    text=value+' minut',
                    padx=20,
                    variable=v,
                    command=show_choice,
                    value=option).pack(anchor=W)
    # One option with indicator set to 0 (default is 1)
    Radiobutton(choose_window,
                text='test value XX minut',
                padx=20,
                variable=v,
                command=show_choice,
                value=111, indicator=0).pack(anchor=W)


def check_option():
    def check():
        print('Opcja 1: {}\nOpcja 2: {}\nOpcja 3: {}'.format(var_1.get(), var_2.get(), var_3.get()))
    check_window = Tk()
    check_window.title('Check box test')
    Label(check_window, text='Kiedy mają nastąpić przerwy?', padx=50).grid(row=0, sticky=W)
    var_1 = IntVar(check_window)
    Checkbutton(check_window, text='Po pierwszej sesji', variable=var_1).grid(row=1, sticky=W)
    var_2 = IntVar(check_window)
    Checkbutton(check_window, text='Po drugiej sesji', variable=var_2).grid(row=2, sticky=W)
    var_3 = IntVar(check_window)
    Checkbutton(check_window, text='Po trzeciej sesji', variable=var_3).grid(row=3, sticky=W)
    Button(check_window, text='Show', command=check).grid(row=4, sticky=S, pady=5)


def info_input_option():

    def show_entry():
        print('Imie: {}\nNazwisko: {}'.format(name.get(), last_name.get()))
    info_window = Tk()
    info_window.title('Wprowadź dane')
    Label(info_window, text='Imię:').grid(row=0)
    Label(info_window, text='Naziwsko:').grid(row=1)
    name = Entry(info_window)
    name.grid(row=0, column=1)
    last_name = Entry(info_window)
    last_name.grid(row=1, column=1)
    Button(info_window, text='Show', command=show_entry).grid(row=2, column=1, sticky=E, padx=60)
    Button(info_window, text='Quit', command=info_window.destroy).grid(row=2, column=1, sticky=E, pady=4)


def fetch(entries):
    for entry in entries:
        field = entry[0]
        text = entry[1]
        print('{} {}'.format(field, text))


def make_form(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=15, text=field, anchor=W)
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((field, ent))
    return entries

def daily_goals_option():
    fields = 'Imię:', 'Nazwisko:', 'Dzisiejsze założenie:', 'Ogólny postęp:'
    daily_goals_window = Tk()
    daily_goals_window.title('Cele')
    ents = make_form(daily_goals_window, fields)
    def show_entries(entries=ents):
        for entry in entries:
            print(entry[0], entry[1].get())
    show_button = Button(daily_goals_window, text='Show', command=show_entries)
    show_button.pack(side=LEFT, padx=5, pady=5)
    quit_button = Button(daily_goals_window, text='Quit', command=daily_goals_window.destroy)
    quit_button.pack(side=LEFT, padx=5, pady=5)


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


# Creating label for counting seconds and buttons inside root window
seconds_label = Label(root, fg='red')
exit_button = Button(root, text='Quit', width=25, command=quit)
quote_button = Button(root, text='Quote', width=35, command=quote_display)
choose_button = Button(root, text='Choose', width=20, command=choose_option)
check_button = Button(root, text='Check button', width=30, command=check_option)
info_input = Button(root, text='Dodaj dane', width=30, command=info_input_option)
daily_goals_input = Button(root, text='Cele', command=daily_goals_option)
exit_button.pack(side='bottom')
quote_button.pack(side='bottom')
choose_button.pack(side='bottom')
check_button.pack(side='bottom')
info_input.pack(side='bottom')
daily_goals_input.pack(side='bottom')
seconds_label.pack(side='bottom')
counter_label(seconds_label)


# Running the tkinter event loop which works until we close the window.
root.mainloop()
