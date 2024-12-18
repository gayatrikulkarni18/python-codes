import tkinter
from tkinter import messagebox
parent=tkinter.Tk()
def buttonCallBack():
    messagebox.showinfo("Hello", "My Python")
b=tkinter.Button(parent, text="Click Me", command=buttonCallBack)
b.pack()
#top.mainloop()
