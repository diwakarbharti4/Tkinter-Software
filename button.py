from tkinter import*
root = Tk()
def fun():
    mylebel=Label(root,text="my name is diwakar bharti")
    mylebel.pack()

button=Button(root,text="what is my name", padx=50,pady=50,command=fun,fg="blue",bg="#000000")
button.pack()
root.mainloop()