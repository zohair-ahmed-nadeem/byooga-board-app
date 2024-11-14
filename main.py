import tkinter as tk
from tkinter import *
from start import start_win

def start_box():
    root.destroy()
    start_win()

def exit_box():
    top = Toplevel(root)
    top.title("Exit...")
    top.geometry("300x100")
    top.resizable(False,False)

    msg=tk.Label(top,text="Are You Sure You Want To Exit....")
    msg.grid(row=1,column=1,padx=10,pady=10)
    yes_btn = tk.Button(top,text="yes", height=1,width=5, command=root.destroy)
    yes_btn.grid(row=2,column=1,pady=10)
    no_btn = tk.Button(top, text="no", height=1, width=5, command=top.destroy)
    no_btn.grid(row=2,column=2,pady=10)
    top.mainloop()


root = tk.Tk()

root.geometry("1200x700")
root.title("Byooga")

root.minsize(1200,700)

start_btn = tk.Button(root,text="Start!!!",height=5,width=50,command=start_box)
start_btn.place(relx=0.5, rely=0.4,anchor=tk.CENTER)
ext_btn = tk.Button(root,text="Exit T_T ",height=5,width=50,command=exit_box)
ext_btn.place(relx=0.5, rely=0.6,anchor=tk.CENTER)

root.mainloop()
