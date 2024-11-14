import tkinter as tk
from tkinter import colorchooser
from PIL import ImageGrab

def start_win(h, w, bg):
    start_window = tk.Tk()
    start_window.geometry("1200x700")
    start_window.title("Byooga")
    start_window.minsize(1200, 700)

    # Initial pen color
    pen_color = "#000000"
    eraser_on = False
    eraser_size = 10  # Default eraser size

    # Add the entry and label for saving the image
    file_name_entry = None
    save_button = None

    def paint(event):
        nonlocal eraser_on, eraser_size
        # Co-ordinates.
        x1, y1, x2, y2 = (event.x - 2), (event.y - 2), (event.x + 2), (event.y + 2)

        if eraser_on:
            # Draw a rectangle with the size of the eraser
            canvas.create_rectangle(event.x - eraser_size // 2, event.y - eraser_size // 2,
                                    event.x + eraser_size // 2, event.y + eraser_size // 2,
                                    fill=bg, outline=bg)
        else:
            # Specify color
            colour = pen_color
            # Specify type of display
            canvas.create_line(x1, y1, x2, y2, fill=colour)

    def choose_color():
        nonlocal pen_color, eraser_on
        eraser_on = False
        color_code = colorchooser.askcolor(title="Choose color")
        pen_color = color_code[1] if color_code[1] else pen_color
        color_button.config(bg=color_code[1] if color_code[1] else color_button.cget("bg"))

    def use_eraser():
        nonlocal eraser_on
        eraser_on = True

    def use_pen():
        nonlocal eraser_on
        eraser_on = False

    def set_eraser_size(val):
        nonlocal eraser_size
        eraser_size = int(val)

    canvas = tk.Canvas(start_window, width=w, height=h, bg=bg)
    canvas.bind("<B1-Motion>", paint)
    canvas.pack(pady=10)

    # Load pen icon (replace 'pen_icon.png' with the actual path to your pen icon)
    pen_icon = tk.PhotoImage(file="pen_icon.png")  # Add your pen icon path here
    pen_button = tk.Button(start_window, image=pen_icon, command=use_pen, height=50, width=50)
    pen_button.image = pen_icon  # Keep a reference to avoid garbage collection
    pen_button.pack(side=tk.LEFT, padx=10)

    # Pen color selection button
    color_icon = tk.PhotoImage(file="colour_icon.png")
    color_button = tk.Button(start_window, image=color_icon, command=choose_color, height=50, width=50)
    color_button.pack(side=tk.LEFT, padx=10)

    # Eraser button
    eraser_icon = tk.PhotoImage(file="eraser_icon.png")
    eraser_button = tk.Button(start_window, image=eraser_icon, text="Eraser", command=use_eraser, height=50, width=50)
    eraser_button.pack(side=tk.LEFT, padx=10)

    # Eraser size scale
    eraser_size_scale = tk.Scale(start_window, from_=2, to=100, orient=tk.HORIZONTAL, label="Eraser Size", command=set_eraser_size)
    eraser_size_scale.set(eraser_size)  # Set default value
    eraser_size_scale.pack(side=tk.LEFT, padx=10)

    start_window.mainloop()