from tkinter import *
from datetime import datetime

# Function section
counter = 3600000


def counter_label(label):
    """This function will count down 2 hours and 40 minutes lesson. TO DO - parse seconds for H:M:S format."""
    def count():
        global counter
        counter -= 1
        label.config(text=str(counter))
        label.after(1000, count)

    count()


def quote_display():
    """Message pop up window with message - TO DO add sound and change text value."""
    quote_bill_gates = 'Software is a great combination between artistry and engineering.\n(Bill Gates)'
    msg_window = Tk()
    msg_window.title('Quote')
    msg = Message(msg_window, text=quote_bill_gates)
    msg.config(bg='pale green', fg='black', font='Times 24 italic', justify='right')
    msg.pack(fill=BOTH)


def choose_option():
    """Window with break time radio choose."""
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
    """Window with multi select where user choose when he want to make breaks."""
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
    """Window with User name and last name input. I'm not sure if it will be used."""
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


def make_form(root, fields):
    """This function creates form with data from daily_goals_option function."""
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
    """Window with daily goals provided by the user."""
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


def basic_operation_option():
    """Simply calculator option which calculate user expression"""
    def evaluate(event):
        result.configure(text='Wynik: ' + str(eval(operation_entry.get())))

    operation_window = Tk()
    operation_window.title('Licz')
    Label(operation_window, text='Wprowadź działanie matematyczne:').grid(row=0)
    operation_entry = Entry(operation_window, width=30)
    operation_entry.bind('<Return>', evaluate)
    operation_entry.grid(row=1)
    result = Label(operation_window, text='Wynik:')
    result.grid(row=2)


def canvas_option():
    """In this function I'm preparing some graphic using tkinter tool - canvas"""
    canvas_window = Tk()
    canvas_window.title('Canvas Graphic')
    rectangle_area = Canvas(canvas_window, width=200, height=200)
    rectangle_area.pack()
    rectangle_area.create_rectangle(50, 50, 150, 150, width=3, fill='light sky blue')
    rectangle_area.create_rectangle(75, 75, 125, 125, fill='beige')
    rectangle_area.create_line(0, 0, 50, 50, width=3)
    rectangle_area.create_line(0, 200, 50, 150, width=3)
    rectangle_area.create_line(150, 50, 200, 0, width=3)
    rectangle_area.create_line(150, 150, 200, 200, width=3)
    rectangle_area.create_text(100, 100, text='Rafon')


def canvas_flex_option():
    """Another function which create graphic, but this one will be more flexible."""
    canvas_width = 200
    canvas_height = 100
    colours = ['light slate grey', 'pale green']
    box = []

    for ratio in (0.2, 0.35):
        box.append((canvas_width * ratio,
                    canvas_height * ratio,
                    canvas_width * (1 - ratio),
                    canvas_height * (1 - ratio)))
    print(box)

    canvas_2_window = Tk()
    canvas_2_window.title('Canvas FLEX')
    flexible_rects = Canvas(canvas_2_window, width=canvas_width, height=canvas_height)
    flexible_rects.pack()

    # Two rectangles
    for i in range(2):
        flexible_rects.create_rectangle(box[i][0], box[i][1], box[i][2], box[i][3], fill=colours[i])

    # Lines
    flexible_rects.create_line(0, 0, box[0][0], box[0][1], fill=colours[0], width=2)
    flexible_rects.create_line(canvas_width, 0, box[0][2], box[0][1], fill=colours[0], width=2)
    flexible_rects.create_line(0, canvas_height, box[0][0], box[0][3], fill=colours[0], width=2)
    flexible_rects.create_line(canvas_width, canvas_height, box[0][2], box[0][3], fill=colours[0], width=2)
    flexible_rects.create_text(canvas_width / 2, canvas_height / 2, text='TEXT', fill='red')

    # Polygons
    flexible_rects.create_polygon([0, 0, (canvas_width / 2), box[0][1], canvas_width, 0],
                                  outline='green', fill='yellow', width=1)
    flexible_rects.create_polygon([0, 0, box[0][0], (canvas_height / 2), 0, canvas_height],
                                  outline='green', fill='yellow', width=1)
    flexible_rects.create_polygon([canvas_width, 0, box[0][2], (canvas_height / 2), canvas_width, canvas_height],
                                  outline='green', fill='yellow', width=1)
    flexible_rects.create_polygon([0, canvas_height, (canvas_width / 2), box[0][3], canvas_width, canvas_height],
                                  outline='green', fill='yellow', width=1)


def oval_canvas():
    """Function which will display current time in some canvas ovals."""
    circle_width = 500
    circle_height = 250
    colours = ['spring green', 'yellow green']
    box = []

    for ratio in (0.2, 0.3):
        box.append((circle_width * ratio,
                    circle_height * ratio,
                    circle_width * (1 - ratio),
                    circle_height * (1 - ratio)))

    oval_window = Tk()
    oval_window.title('Oval')
    circle_area = Canvas(oval_window, width=circle_width, height=circle_height)
    circle_area.pack()

    for i in range(2):
        circle_area.create_oval(box[i][0], box[i][1], box[i][2], box[i][3], width=2, fill=colours[i])

    # Clock for circle_area
    circle_time = circle_area.create_text(circle_width / 2, circle_height / 2, font='Times 24')

    def update_time():
        time_now = datetime.now().time().strftime('%X')
        circle_area.itemconfigure(circle_time, text=time_now)
        oval_window.after(1000, update_time)

    update_time()


def paint():
    """This function allows to draw in app using left mouse button."""
    canvas_width = 500
    canvas_height = 200

    def drawing(event):
        color = 'red'
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        draw.create_oval(x1, y1, x2, y2, fill=color)

    paint_window = Tk()
    paint_window.title('Rysuj')
    draw = Canvas(paint_window, width=canvas_width, height=canvas_height)
    draw.pack(expand=YES, fill=BOTH)
    draw.bind('<B1-Motion>', drawing)

    message = Label(paint_window, text='Naciśnij lewy przycisk myszy aby rysować')
    message.pack(side='bottom')


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


# Buttons and Labels section
# Labels and button
seconds_label = Label(root, fg='red')
exit_button = Button(root, text='Quit', width=25, command=quit)
quote_button = Button(root, text='Quote', width=35, command=quote_display)
choose_button = Button(root, text='Choose', width=20, command=choose_option)
check_button = Button(root, text='Check button', width=30, command=check_option)
info_input = Button(root, text='Dodaj dane', width=30, command=info_input_option)
daily_goals_input = Button(root, text='Cele', command=daily_goals_option)
basic_operation = Button(root, text='Licz', command=basic_operation_option)
canvas_button = Button(root, text='Grafika', command=canvas_option)
flexible_canvas_button = Button(root, text='Flex Grafika', command=canvas_flex_option)
oval_canvas_button = Button(root, text='Owalna Grafika', command=oval_canvas)
paint_button = Button(root, text='Rysuj', command=paint)

# Section responsible for putting button and labels inside root window
exit_button.pack(side='bottom')
quote_button.pack(side='bottom')
choose_button.pack(side='bottom')
check_button.pack(side='bottom')
info_input.pack(side='bottom')
daily_goals_input.pack(side='bottom')
basic_operation.pack(side='bottom')
canvas_button.pack(side='bottom')
flexible_canvas_button.pack(side='bottom')
oval_canvas_button.pack(side='bottom')
paint_button.pack(side='bottom')
seconds_label.pack(side='bottom')
counter_label(seconds_label)


# Running the tkinter event loop which works until we close the window.
root.mainloop()
