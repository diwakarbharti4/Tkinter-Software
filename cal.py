from tkinter import*

root=Tk()
root.title("diwakar Cal")
e=Entry(root,width=50,borderwidt=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def fun(number):
    #e.delete(0,END)
    a=e.get()
    x=str(a)+str(number)
    e.delete(0,END)
    e.insert(0,x)

def clear():
    e.delete(0,END)

def add():
    num=e.get()
    global fnum
    fnum=num
    e.delete(0,END)

def eq():
    snum=e.get()
    sum=int(snum)+int(fnum)
    e.delete(0,END)
    e.insert(0,sum)

button1=Button(root, text="1",padx=40,pady=20,command=lambda: fun(1))
button2=Button(root, text="2",padx=40,pady=20,command=lambda: fun(2))
button3=Button(root, text="3",padx=40,pady=20,command=lambda: fun(3))
button4=Button(root, text="4",padx=40,pady=20,command=lambda: fun(4))
button5=Button(root, text="5",padx=40,pady=20,command=lambda: fun(5))
button6=Button(root, text="6",padx=40,pady=20,command=lambda: fun(6))
button7=Button(root, text="7",padx=40,pady=20,command=lambda: fun(7))
button8=Button(root, text="8",padx=40,pady=20,command=lambda: fun(8))
button9=Button(root, text="9",padx=40,pady=20,command=lambda: fun(9))
button0=Button(root, text="0",padx=40,pady=20,command=lambda: fun(0))
buttonA=Button(root, text="+",padx=40,pady=20,command=add)
buttonE=Button(root, text="=",padx=100,pady=20,bg="blue",fg="yellow",borderwidth=5,command=eq)
buttonC=Button(root, text="Clear",padx=90,pady=20,bg="olive",fg="yellow",borderwidth=5,command=clear)


button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
buttonA.grid(row=5,column=0)
buttonE.grid(row=5,column=1,columnspan=2)
buttonC.grid(row=4,column=1,columnspan=2)

root.mainloop()