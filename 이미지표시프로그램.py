from tkinter import *


def change_img():
    path = inputBox.get()
    img = PhotoImage(file=path)
    imagel.configure(image=img)
    imagel.inUse = img


win = Tk()
photo = PhotoImage(file='singstreet.png')
imagel = Label(win, image=photo)
imagel.pack()
inputBox = Entry(win)
inputBox.pack()
but = Button(win, text='Submit', command=change_img)
but.pack()
win.mainloop()
