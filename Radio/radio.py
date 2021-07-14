from tkinter import *

root=Tk()
root.iconbitmap("dd.ico")

frame= LabelFrame(root, text= 'my frame',padx=5,pady=5)
frame.pack()

x= IntVar() 
y=IntVar()
Radiobutton(frame,text='Button 1',variable=x,value=1).pack()
Radiobutton(frame,text='Button 2',variable=y,value=5).pack()

root.mainloop()