from tkinter import *

win = Tk()
win.title('계산기')
display = Entry(win, width=33, bg='yellow')
display.grid(row=0, column=0, columnspan=5)

button_list = ['7', '8', '9', '/', 'C',
               '4', '5', '6', '*', ' ',
               '1', '2', '3', '-', ' ',
               '0', '.', '=', '+', ' ']


def click(key):
    if key == '=':
        result = eval(display.get())
        s = str(result)
        display.insert(END, '=' + s)
    else:
        display.insert(END, key)


row_index = 1
column_index = 0
for button in button_list:
    def process(t=button):
        click(t)


    b = Button(win, text=button, width=5, command=process)
    b.grid(row=row_index, column=column_index)
    column_index += 1
    if column_index > 4:
        row_index += 1
        column_index = 0
