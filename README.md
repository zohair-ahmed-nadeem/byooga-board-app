## 📁 Project Structure

Here’s how your files should be organized:

```
byooga/
├── main.py              # Entry point, GUI for canvas configuration
├── start.py             # Drawing window logic
├── pen_icon.png         # Icon for the pen tool
├── colour_icon.png      # Icon for color picker
├── eraser_icon.png      # Icon for eraser tool
├── README.md            # Project documentation (optional but recommended)
```

---

## 🚀 How the App Works

### 1. **Launching the App — `main.py`**
This file provides the launchpad for the whole experience.

- When executed, it opens a **main window** with two buttons:
  - **"Start!!!"** opens a form allowing users to define canvas height, width (in characters), and a background color.
  - **"Exit T_T"** prompts a simple confirmation dialog before exiting.

#### Inside the “Start” Dialog:
You can:
- Enter numeric values for the **canvas height and width**.
- Use a **color chooser** to select a background color for your canvas.
- Click “Create” to launch the drawing interface with those settings.

> Why this design?
This approach keeps the app modular and user-friendly, separating configuration from drawing. It's ideal if you want to build in presets, themes, or additional customization features later.

---

### 2. **Drawing Interface — `start.py`**
Once the user enters valid inputs and hits "Create", the `start_win()` function in `start.py` launches the drawing interface.

#### Canvas Features:
- **Free Drawing** using a virtual pen.
- **Color Picker** to change pen color.
- **Eraser Tool**, toggled separately, which draws over existing strokes with the background color (acts as a visual “undo”).
- **Eraser Size Slider**, giving the user fine control over the size of the erasing area.

> Why use a canvas?
The `tk.Canvas` widget is extremely versatile, letting you draw, move shapes, and respond to mouse events — perfect for a paint app.

---

## 🛠️ How to Run the App

Here are the full steps to get started:

### Step 1: Make sure you have Python installed
Check with:

```bash
python --version
```

If not installed, download from [python.org](https://www.python.org/).

### Step 2: Ensure `Pillow` is installed
Pillow (Python Imaging Library) is used for image manipulation and to support `.png` icons:

```bash
pip install pillow
```

### Step 3: Run the Application

Navigate to the directory where your `main.py` is located and run:

```bash
python main.py
```

> Important:
Ensure the following image files are present in the same directory:
- `pen_icon.png`
- `colour_icon.png`
- `eraser_icon.png`

These icons will be used as buttons for drawing tools. If they’re missing or misnamed, the app will throw an error when trying to load them.

---

## 🧠 Customization Tips

- **Default Background Color**: Change `user_bg = "#ffffff"` in `main.py` to any hex code to set a different default.
- **Canvas Size Scaling**: Although size is currently based on character count, you might switch to pixels for finer control.
- **Add Save Feature**: You can add a save button using `ImageGrab` to capture and export the canvas as an image file.

Example snippet to save the canvas:

```python
x = start_window.winfo_rootx() + canvas.winfo_x()
y = start_window.winfo_rooty() + canvas.winfo_y()
x1 = x + canvas.winfo_width()
y1 = y + canvas.winfo_height()
ImageGrab.grab().crop((x, y, x1, y1)).save("drawing.png")
```

---

## 📝 Final Thoughts

This app is a strong foundation for a creative drawing tool. With the current functionality, it already allows for interactive doodling, color play, and a basic erasing mechanism. From here, you could:

- Add **undo/redo** functionality.
- Introduce **shape tools** (rectangles, circles, etc.).
- Implement **layers** or **opacity settings**.
