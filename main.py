import tkinter as tk
from tkinter import *
from start import start_win
from tkinter import colorchooser

def start_box():
    cd = Toplevel(root)
    cd.title("Byooga - canvas details")
    cd.geometry("600x600")
    cd.resizable(False, False)

    h_var = StringVar()
    w_var = StringVar()
    user_bg = "#ffffff"  # Default background color

    def choose_color():
        nonlocal user_bg
        color_code = colorchooser.askcolor(title="Choose background color")
        user_bg = color_code[1] if color_code[1] else user_bg

    def create():
        try:
            user_h = int(h_var.get())
            user_w = int(w_var.get())
            h_var.set("")
            w_var.set("")
            cd.destroy()
            root.destroy()
            start_win(user_h, user_w, user_bg)
        except ValueError:
            error_label.config(text="Please enter valid numbers for height and width.")

    head = tk.Label(cd, text="Enter Canvas Details...", font=16)
    head.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

    u_h_l = tk.Label(cd, text="Height in char", font=16)
    u_h_l.grid(row=2, column=1, padx=5, pady=5)
    u_h_e = tk.Entry(cd, textvariable=h_var, font=16)
    u_h_e.grid(row=2, column=2, padx=5, pady=5)

    u_w_l = tk.Label(cd, text="Width in char", font=16)
    u_w_l.grid(row=3, column=1, padx=5, pady=5)
    u_w_e = tk.Entry(cd, textvariable=w_var, font=16)
    u_w_e.grid(row=3, column=2, padx=5, pady=5)

    u_bg_l = tk.Label(cd, text="Background Colour", font=16)
    u_bg_l.grid(row=4, column=1, padx=5, pady=5)
    u_bg_e = tk.Button(cd, text="select!", font=16, command=choose_color)
    u_bg_e.grid(row=4, column=2, padx=5, pady=5)

    create_btn = tk.Button(cd, text="Create", command=create, font=16)
    create_btn.grid(row=5, column=1, columnspan=2, pady=20)

    error_label = tk.Label(cd, text="", font=16, fg="red")
    error_label.grid(row=6, column=1, columnspan=2)

    cd.mainloop()

def exit_box():
    top = Toplevel(root)
    top.title("Exit...")
    top.geometry("300x100")
    top.resizable(False, False)
    msg = tk.Label(top, text="Are You Sure You Want To Exit...")
    msg.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
    yes_btn = tk.Button(top, text="Yes", height=1, width=5, command=root.destroy)
    yes_btn.grid(row=2, column=1, pady=10)
    no_btn = tk.Button(top, text="No", height=1, width=5, command=top.destroy)
    no_btn.grid(row=2, column=2, pady=10)
    top.mainloop()

root = tk.Tk()

root.geometry("1200x700")
root.title("Byooga")

root.minsize(1200, 700)

start_btn = tk.Button(root, text="Start!!!", height=5, width=50, command=start_box)
start_btn.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
ext_btn = tk.Button(root, text="Exit T_T", height=5, width=50, command=exit_box)
ext_btn.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

root.mainloop()
