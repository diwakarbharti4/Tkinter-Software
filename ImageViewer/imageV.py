from tkinter import*
from PIL import Image,ImageTk

root=Tk()
root.title("DD")
root.iconbitmap('dd.ico')

myI1=ImageTk.PhotoImage(Image.open('1.jpg'))
myI2=ImageTk.PhotoImage(Image.open('2.jpg'))
myI3=ImageTk.PhotoImage(Image.open('3.jpg'))
myI4=ImageTk.PhotoImage(Image.open('4.jpg'))
myI5=ImageTk.PhotoImage(Image.open('5.jpg'))

ImageList=[myI1,myI2,myI3,myI4,myI5]

mylabel=Label(image=myI1)
mylabel.grid(row=0,column=0,columnspan=3)

def forward(Inum):
    global mylabel
    global forward
    global back
    
    mylabel.grid_forget()
    mylabel=Label(image=ImageList[Inum-1])
    mylabel.grid(row=0,column=0,columnspan=3)
    
    button_forward=Button(root,text='-->',command=lambda: forward(Inum+1))
    button_back=Button(root,text='<--',command=lambda: back(Inum-1))
    
    if Inum ==5:
        button_forward=Button(root,text='XXXXX',state=DISABLED)
    button_forward.grid(row=1,column=2)
    button_back.grid(row=1,column=0)

def back(Inum):
    global mylabel
    global forward
    global back

    mylabel.grid_forget()
    mylabel=Label(image=ImageList[Inum-1])
    mylabel.grid(row=0,column=0,columnspan=3)

    button_forward=Button(root,text='-->',command=lambda: forward(Inum+1))
    button_back=Button(root,text='<--',command=lambda: back(Inum-1))

    if Inum ==1:
        button_back=Button(root,text='XXXXX',state=DISABLED)
    
    button_forward.grid(row=1,column=2)
    button_back.grid(row=1,column=0)


button_back=Button(root,text='XXXX',command=back,state=DISABLED)
button_exit=Button(root,text='Exit',command=root.quit)
button_forward=Button(root,text='>>>>',command=lambda: forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)
root.mainloop()