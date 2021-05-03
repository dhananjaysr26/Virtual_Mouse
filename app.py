from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox

# dictionary of colors:
color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}
app_bg="gray17"
#gif_backcolor="tan2"
gif_backcolor="black"
# setting root window:
root = tk.Tk()
root.title("Virtual Mouse Pro")
root.config(bg=app_bg)
root.geometry("500x600+850+50")
bg = PhotoImage(file = "img/1.png")
w = Label(root, image=bg)
w.place(x=0,y=0,relwidth=1,relheight=1)

# setting switch state:
btnState = False

# loading Navbar icon image:
navIcon = PhotoImage(file="img/menu.png")
closeIcon = PhotoImage(file="img/cut.png")
#button Fuction
#Button
def Exiting():
   messagebox.showinfo( "Virtual Mouse", "Thanks for Visiting! ")
   exit()
###main Function
def show():
   messagebox.showinfo( "Starting.....", "Program will Start")
   A=1
   if A==1:
    import Action
def Info():
   messagebox.showinfo( "Information", "How to USE TOUR")


# setting switch function:
def switch():
    global btnState
    if btnState is True:
        # create animated Navbar closing:
        for x in range(301):
            navRoot.place(x=-x, y=0)
            topFrame.update()

        # resetting widget colors:
        brandLabel.config(bg="gray17", fg="green")
        homeLabel.config(bg=color["orange"])
        topFrame.config(bg=color["orange"])
        root.config(bg="gray17")

        # turning button OFF:
        btnState = False
    else:
        # make root dim:
        brandLabel.config(bg=color["nero"], fg="#5F5A33")
        homeLabel.config(bg=color["nero"])
        topFrame.config(bg=color["nero"])
        root.config(bg=color["nero"])

        # created animated Navbar opening:
        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            topFrame.update()

        # turing button ON:
        btnState = True

# top Navigation bar:
topFrame = tk.Frame(root, bg=color["orange"])
topFrame.pack(side="top", fill=tk.X)

# Header label text:
homeLabel = tk.Label(topFrame, text="Virtual Mouse", font="Bahnschrift 15", bg=color["orange"], fg="gray17", height=2, padx=20)
homeLabel.pack(side="right")

# Main label text:
brandLabel = tk.Label(root, text="", font="System 30", bg="gray17", fg="green")
brandLabel.place(x=100, y=250)
#Logo**********************************************************************

def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2,bg=gif_backcolor)
    count += 1
    if count == frames:
        count = 0
    anim = root.after(50,lambda :animation(count))

gif_file="img/giphy2.gif"
info = Image.open(gif_file)
frames = info.n_frames  # gives total number of frames that gif contains
# creating list of PhotoImage objects for each frames
im = [tk.PhotoImage(file=gif_file,format=f"gif -index {i}") for i in range(frames)]
count = 0
anim = None
gif_label = tk.Label(root,image="")
gif_label.pack()

animation(count)
img_satrt = ImageTk.PhotoImage(Image.open("img/start.png"))
img_label=Label(image=img_satrt)
B1 = Button(root,image=img_satrt ,borderwidth=0,activebackground='purple1',bd='5',bg='gold',justify='center',    
command = show)
B1.pack(pady=10)
img_exit = ImageTk.PhotoImage(Image.open("img/exit.png"))
img_label1=Label(image=img_exit)
B = Button(root, image=img_exit,command = Exiting,borderwidth=0,activebackground='red',bd='5',bg='orange2')
B.pack(pady=10,side = "left")

img_info = ImageTk.PhotoImage(Image.open("img/information.png"))
img_label2=Label(image=img_info)
B = Button(root, image=img_info,command =Info,borderwidth=0,activebackground='cyan2',bd='5',bg='orange2')
B.pack(pady=10,side = "right")
#**************************************************************************



# Navbar button:
navbarBtn = tk.Button(topFrame, image=navIcon, bg=color["orange"], activebackground=color["orange"], bd=0, padx=20, command=switch)
navbarBtn.place(x=10, y=10)

# setting Navbar frame:
navRoot = tk.Frame(root, bg="gray17", height=1000, width=300)
navRoot.place(x=-300, y=0)
tk.Label(navRoot, font="Bahnschrift 15", bg=color["orange"], fg="black", height=2, width=300, padx=20).place(x=0, y=0)

# set y-coordinate of Navbar widgets:
y = 80
# option in the navbar:
options = ["Quick Tour","Settings", "Help", "About", "Feedback","Exit"]
Menu_click=[Exiting,Exiting,Exiting,Exiting,Exiting,Exiting]
# Navbar Option Buttons:
for i in range(6):
    tk.Button(navRoot, text=options[i], font="BahnschriftLight 15", bg="gray17", fg=color["orange"],command=Menu_click[i],activebackground="gray17", activeforeground="green", bd=0).place(x=25, y=y)
    y += 40

# Navbar Close Button:
closeBtn = tk.Button(navRoot, image=closeIcon, bg=color["orange"], activebackground=color["orange"], bd=0, command=switch)
closeBtn.place(x=250, y=10)


a = Label(root, text ="Copyright ©2021 All rights reserved")
b = Label(root, text ="Virtual Mouse")
b.pack(side="bottom",pady=5)
a.pack(side="bottom",pady=2)

# window in mainloop:
root.mainloop()