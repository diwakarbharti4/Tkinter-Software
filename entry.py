from tkinter import*

root=Tk()
e=Entry(root,borderwidth=5)
e.pack()
e.insert(0,"what is ur name")
def fun():
    b=Label(root,text="hello "+e.get())
    b.pack()
button=Button(root,text="click me",command=fun)
button.pack()
root.mainloop()