from tkinter import *
from tkinter.ttk import Progressbar
from PIL import Image,ImageTk

# creating tkinter window
root = Tk()
root.title("Are You Ready?")
root.geometry("700x700+500+250")
root.resizable (0, 0)
root.config(bg='plum1')
Label(root,text ="1.Take Care Of Following Hand Gestures",bg="DarkOrange2").pack(pady=2)  

img_How = ImageTk.PhotoImage(Image.open("img/How2.png"))
panel = Label(root, image = img_How)
panel.pack(pady=2)
Label(root,text ="2.Callibration Of the Color                  ",bg="DarkOrange2").pack(pady=1)  
Label(root,text ="3.After Callibration Successful           ",bg="orange2").pack(pady=1)  
Label(root,text ="         Press P - ON/OFF Mouse Simulation",bg="salmon1").pack(pady=3) 
Label(root,text ="Press ESC - Exit",bg="salmon1").pack(pady=2) 




# Progress bar widget
progress = Progressbar(root, orient = HORIZONTAL,
			length = 350, mode = 'determinate')

# Function responsible for the updation
# of the progress bar value
def bar():
	temp=1
	import time
	Label(root,text ="Loding.........",bg="plum3",justify="center").pack(pady=2) 
	progress['value'] = 20
	root.update_idletasks()
	time.sleep(1)

	progress['value'] = 40
	root.update_idletasks()
	time.sleep(1)

	progress['value'] = 50
	root.update_idletasks()
	time.sleep(1)

	progress['value'] = 60
	root.update_idletasks()
	time.sleep(1)

	progress['value'] = 80
	root.update_idletasks()
	time.sleep(1)
	progress['value'] = 100
	if temp==1:
   		import Action

progress.pack(pady = 10)

# This button will initialize
# the progress bar
B1= Button(root, text ="I AM READY",activebackground='cyan2',command = bar,bd=3,bg='plum3')
B1.pack(side="bottom",pady=10)
Cvar=IntVar()
c1 =Checkbutton(root, text='Close this Window',variable=Cvar, onvalue=1, offvalue=0)
c1.pack(side='left')
# infinite loop
root.mainloop()
