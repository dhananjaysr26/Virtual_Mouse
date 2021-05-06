from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def clear():
    global entry_name
    global entry_email
    global textcomment
    messagebox.showinfo(title='clear', message='Do you want to clear?')
    entry_name.delete(0, END)
    entry_email.delete(0, END)
    textcomment.delete(1.0, END)


def submit():
    global entry_name
    global entry_email
    global textcomment
    print('Name:{}'.format(myvar.get()))
    print('Email:{}'.format(var.get()))
    print('Comment:{}'.format(textcomment.get(1.0, END)))
    messagebox.showinfo(title='Submit', message='Thank you for your Feedback')
    entry_name.delete(0, END)
    entry_email.delete(0, END)
    textcomment.delete(1.0, END)
    feedWindow.destroy()



feedWindow = Tk()
feedWindow.title("Feedback")
feedWindow.geometry("450x300+500+250")
feedWindow.resizable (0, 0)
feedWindow.config(bg='plum1')
myvar = StringVar()
var = StringVar()

namelabel = ttk.Label(feedWindow, text='Name')
namelabel.grid(row=0, column=0, padx=5, sticky='sw')
entry_name = ttk.Entry(feedWindow, width=18, font=('Arial', 14), textvariable=myvar)
entry_name.grid(row=1, column=0)

emaillabel = ttk.Label(feedWindow, text='Email')
emaillabel.grid(row=0, column=1, sticky='sw')
entry_email = ttk.Entry(feedWindow, width=18, font=('Arial', 14), textvariable=var)
entry_email.grid(row=1, column=1)

commentlabel = ttk.Label(feedWindow, text='Comment', font=('Arial', 10))
commentlabel.grid(row=2, column=0, sticky='sw')
textcomment = Text(feedWindow, width=55, height=10)
textcomment.grid(row=3, column=0, columnspan=2)


submitbutton = Button(feedWindow, text='Submit',activebackground='cyan2',bg='plum3',bd=2,padx=5,pady=3, command=submit).grid(row=4, column=0, sticky='e')
clearbutton = Button(feedWindow, text='Clear',activebackground='cyan2',bg='plum3',bd=2,padx=5,pady=3, command=clear).grid(row=4, column=1, sticky='w')


feedWindow.mainloop()