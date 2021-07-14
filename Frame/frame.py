from tkinter import*

root=Tk()
root.title("Frame")
#root.iconbitmap("dd.ico")

label= LabelFrame(root,text="This is Frame",padx=50,pady=20)
label.pack(padx=100,pady=100)

button=Button(label, text='click me')
button.pack()
root.mainloop()