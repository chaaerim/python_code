from tkinter import *

mycolor = 'blue'


def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, fill=mycolor, outline=mycolor)


def change_color():
    global mycolor
    mycolor = 'red'


win = Tk()
canvas = Canvas(win);
canvas.pack()
canvas.bind('<B1-Motion>', paint)
b1 = Button(win, text='빨강색', command=change_color);
b1.pack()

win.mainloop()
