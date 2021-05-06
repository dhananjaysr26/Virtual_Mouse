from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import webbrowser
from tkinter import ttk
from tkinter.ttk import Progressbar

# dictionary of colors:
color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}
app_bg="gray17"
#gif_backcolor="tan2"
gif_backcolor="black"
# setting root window:
root = tk.Tk()
root.title("Virtual Mouse Pro")
root.config(bg=app_bg)
root.geometry("500x650+500+50")
root.resizable (0, 0)
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
def help_plz():
    messagebox.showinfo( "Virtual Mouse", "It Will Open Help Forum Of Virtual Mouse! ")


git_url = "https://github.com/dhananjaysr26/Virtual_Mouse"
def openweb():
    webbrowser.open(git_url,new=1)
def Exiting():
   messagebox.showinfo( "Virtual Mouse", "Thanks for Visiting! ")
   exit()
###main Function
#//////////////////////////////////////////////
def bar():
    temp=1
    if temp==1:
        import Action



def show():
    startWindow = Toplevel(root)
    startWindow.title("Are You Ready?")
    startWindow.geometry("700x700+500+250")
    startWindow.resizable (0, 0)
    startWindow.config(bg='plum1')
    Label(startWindow,text ="1.Take Care Of Following Hand Gestures",bg="DarkOrange2").pack(pady=2)  
    img_How = ImageTk.PhotoImage(Image.open("img/How2.png"))
    panel = Label(startWindow, image = img_How)
    panel.pack(pady=2)
    Label(startWindow,text ="2.Callibration Of the Color                  ",bg="DarkOrange2").pack(pady=1)  
    Label(startWindow,text ="3.After Callibration Successful           ",bg="orange2").pack(pady=1)  
    Label(startWindow,text ="         Press P - ON/OFF Mouse Simulation",bg="salmon1").pack(pady=3) 
    Label(startWindow,text ="Press ESC - Exit",bg="salmon1").pack(pady=2) 
    # Progress bar widget
    progress = Progressbar(startWindow, orient = HORIZONTAL,
            length = 250, mode = 'determinate')
    progress.pack(pady = 10)

    # This button will initialize
    # the progress bar
    B1= Button(startWindow, text ="I AM READY",activebackground='cyan2',command = bar,bd=3,bg='plum3')
    B1.pack(side="bottom",pady=10)
    progress.pack(pady = 10)
    # infinite loop
    Cvar= tk.IntVar()
    c1 = tk.Checkbutton(startWindow, text='Close this Window',variable=Cvar, onvalue=1, offvalue=0)
    c1.pack(side='left')
    startWindow.mainloop()

#////////////////////////////////////////////////
def About():
    newWindow = Toplevel(root)
    newWindow.title("About")
    newWindow.geometry("350x230+500+250")
    newWindow.resizable (0, 0)
    newWindow.config(bg='plum1')
    Label(newWindow,text ="@Virtual Mouse",bg="orange").pack(pady=3)

    Label(newWindow,text ="Virtual Mouse is a Computer vision Application",bg="plum1").pack(pady=0)
    Label(newWindow,text ="It is use for Mouse Functionality using Hand     ",bg="plum1").pack(pady=0)
    Label(newWindow,text ="Gestures with the Help of                                    ",bg="plum1").pack(pady=0)
    Label(newWindow,text ="1.Python\n2.Tkinter3.\n3.OpenCv\n4.Easygui",bg="plum1").pack(pady=0)
    Label(newWindow,text ="----------------------------------------------------------------------------",bg="plum1").pack(pady=0)
    B = Button(newWindow, text ="GitHub",activebackground='cyan2',bd=2,bg='plum3',command=openweb)
    B.pack(side="left",pady=2)
    B1= Button(newWindow, text ="Close",activebackground='cyan2',command = newWindow.destroy,bd=2,bg='plum3')
    B1.pack(side="right",pady=2)

def Tour():
    TourWindow = Toplevel(root)
    TourWindow.title("How To Use")
    TourWindow.geometry("700x700+500+250")
    TourWindow.resizable (0, 0)
    TourWindow.config(bg='plum1')
    Label(TourWindow,text ="@Virtual Mouse",bg="orange").pack(pady=3)  
    Label(TourWindow,text ="Step 1:Take a Yellow, red and blue coloured sticky tape or Plastic or           ",bg="plum2").pack(pady=1) 
    Label(TourWindow,text ="         any material like cloth withut any design and stick it to your finger",bg="plum2").pack(pady=1)
    Label(TourWindow,text ="with duct tape in following colour order.                                   ",bg="plum2").pack(pady=1) 
    Label(TourWindow,text ="Step 2: Learn this following hand Gestures to trigger Mouse Functionality !",bg="plum2").pack(pady=10)  
    img_How = ImageTk.PhotoImage(Image.open("img/How2.png"))
    panel = Label(TourWindow, image = img_How)
    panel.pack(pady=20)
    B1= Button(TourWindow, text ="Close",activebackground='cyan2',command = TourWindow.destroy,bd=3,bg='plum3')
    B1.pack(side="bottom",pady=10)
    TourWindow.mainloop()
#********************************************************************************************

def feed():
    A=1
    if A==1:
        import feedback

#********************************************************************************
# setting switch function:
def switch():
    global btnState
    if btnState is True:
        # create animated Navbar closing:
        for x in range(301):
            navRoot.place(x=-x, y=0)
            topFrame.update()

        # resetting widget colors:
        brandLabel.config(bg="black", fg="green")
        homeLabel.config(bg=color["orange"])
        topFrame.config(bg=color["orange"])
        root.config(bg="gray17")

        # turning button OFF:
        btnState = False
    else:
        # make root dim:
        brandLabel.config(bg='black', fg="#5F5A33")
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
brandLabel = tk.Label(root, font="System 30", bg="black", fg="green")
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

gif_file="img/arrow.gif"
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
B = Button(root, image=img_info,command =Tour,borderwidth=0,activebackground='cyan2',bd='5',bg='orange2')
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
options = ["How to Use","Settings", "Help", "About", "Feedback","Exit"]
Menu_click=[Tour,Exiting,help_plz,About,feed,Exiting]
# Navbar Option Buttons:
for i in range(6):
    tk.Button(navRoot, text=options[i], font="BahnschriftLight 15", bg="gray17", fg=color["orange"],command=Menu_click[i],activebackground="gray17", activeforeground="green", bd=0).place(x=25, y=y)
    y += 40

# Navbar Close Button:
closeBtn = tk.Button(navRoot, image=closeIcon, bg=color["orange"], activebackground=color["orange"], bd=0, command=switch)
closeBtn.place(x=250, y=10)


a = Label(root, text ="Copyright ©2021 All rights reserved")
a.pack(side="bottom",pady=2)

# window in mainloop:
root.mainloop()