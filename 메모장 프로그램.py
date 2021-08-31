from tkinter import messagebox
from tkinter import filedialog
from tkinter import *


def open():
    file = filedialog.askopenfile(parent=window, mode='r')
    if file != None:
        line = file.read()
        text.insert('1.0', line)
        file.close()


def save():
    file = filedialog.asksaveasfile(parent=window, mode='w')
    if file != None:
        line = get.text('1.0', END + '-1c')
        file.write(line)
        file.close()


def exit():
    if messagebox.askokcancel('quit', 'quit?'):
        window.destroy()


def about():
    label = messagebox.showinfo('about', 'memo')


window = Tk()
text = Text(window, height=30, width=80)
text.pack()
menubar = Menu(window)
window.config(menu=menubar)
filemenu = Menu(menubar)
menubar.add_cascade(label='파일', menu=filemenu)
filemenu.add_command(label='열기', command=open)
filemenu.add_command(label='저장하기', command=save)
filemenu.add_command(label='종료', command=exit)
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='도움말', menu=helpmenu)
helpmenu.add_command(label='프로그램 정보', command=about)
window.mainloop()
