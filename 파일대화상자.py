from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
def open():
    file=filedialog.askopenfile(parent=win, mode='r')
    if file!=None:
        lines=file.read()
        text.insert('1.0', lines)
        file.close()
def save():
    file=filedialog.asksaveasfile(parent=win, mode='w')
    if file!=None:
        lines=text.get('1.0', END+'-1c')
        file.write(lines)
        file.close()
def exit():
    if messagebox.askokcancel('Quit', '종료하시겠습니까?'):
        win.destroy()
def about():
    label=messagebox.showinfo('about', '메모장 프로그램')

win=Tk()
text=Text(win, height=30, width=80)
text.pack()
menubar=Menu(win)
win.config(menu=menubar)
filemenu=Menu(menubar)
menubar.add_cascade(label='파일', menu=filemenu)
filemenu.add_command(label='열기', command=open)
filemenu.add_command(label='저장하기', command=save)
filemenu.add_command(label='종료', command=exit)
helpmenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label='도움말', menu=helpmenu)
helpmenu.add_command(label='프로그램 정보', command=about)

win.mainloop()
