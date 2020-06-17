import tkinter
import math
import time


# ------------------------------- DRAW AXIS -------------------------------
def draw_axis(page):
    page.update()  # ACCESS WIDTH AND HEIGHT
    x = page.winfo_width() / 2
    y = page.winfo_height() / 2
    # scrollregion - box with 2 corners
    page.configure(scrollregion=(-x, -y, x, y))
    # DRAW HORIZONTAL AND VERTICAL LINES
    page.create_line(-x, 0, x, 0, fill="blue")
    page.create_line(0, y, 0, -y, fill="blue")


def parabola(page, size):
    for x in range(size):
        y = x * x / size
        page.create_line(x, -y, x + 1, -y + 1, fill="green")
        page.create_line(-x, -y, -x + 1, -y + 1, fill="green")


def circle(page, radius, g, h):
    page.create_oval(g + radius, h + radius, g - radius, h - radius, width=2)


def square(page, side):
    page.create_rectangle(0, 0, side, -side, fill="yellow")


def circle_button_clicked():
    if result1_1.get() != "":
        rad = int(result1_1.get())
        circle(canvas, rad, 100, 100)
        print(result1_1.get())


def parabola_button_clicked():
    if result2_1.get() != "":
        size = int(result2_1.get())
        parabola(canvas, size)


def square_button_clicked():
    if result3_1.get() != "":
        side = int(result3_1.get())
        square(canvas, side)


def clear_button_clicked():
    canvas.delete("all")
    time.sleep(0.1)
    draw_axis(canvas)


mainWindow = tkinter.Tk()
mainWindow.title("Plot A Graph")
mainWindow.geometry("720x480")


# ------------------------------- CANVAS -------------------------------
canvas = tkinter.Canvas(mainWindow, width=480, height=480, bg="pink")   # a6dcef
canvas.grid(row=0, rowspan=20, column=0)


# ------------------------------- CIRCLE -------------------------------
label1 = tkinter.Label(mainWindow, text="Circle Parameters: ")
label1.grid(row=0, column=1, columnspan=2)

# radius
label1_1 = tkinter.Label(mainWindow, text="Radius = ")
result1_1 = tkinter.Entry(mainWindow)
label1_1.grid(row=1, column=1, sticky='w')
result1_1.grid(row=1, column=2, sticky='w')

# button
button1 = tkinter.Button(mainWindow, text="Plot", command=circle_button_clicked)
button1.grid(row=2, column=1, columnspan=3)


# ------------------------------- PARABOLA -------------------------------
label2 = tkinter.Label(mainWindow, text="Parabola Parameters: ")
label2.grid(row=3, column=1, columnspan=2)

# size
label2_1 = tkinter.Label(mainWindow, text="Size = ")
result2_1 = tkinter.Entry(mainWindow)
label2_1.grid(row=4, column=1, sticky='w')
result2_1.grid(row=4, column=2, sticky='w')

# button
button2 = tkinter.Button(mainWindow, text="Plot", command=parabola_button_clicked)
button2.grid(row=5, column=1, columnspan=3)


# ------------------------------- SQUARE -------------------------------
label3 = tkinter.Label(mainWindow, text="Square Parameters: ")
label3.grid(row=6, column=1, columnspan=2)

# size
label3_1 = tkinter.Label(mainWindow, text="Side = ")
result3_1 = tkinter.Entry(mainWindow)
label3_1.grid(row=7, column=1, sticky='w')
result3_1.grid(row=7, column=2, sticky='w')

# button
button3 = tkinter.Button(mainWindow, text="Plot", command=square_button_clicked)
button3.grid(row=8, column=1, columnspan=3)


# ------------------------------- ERASE -------------------------------
# button
button4 = tkinter.Button(mainWindow, text="CLEAR ALL", command=clear_button_clicked)
button4.grid(row=12, column=1, columnspan=5)


# ------------------------------- MAIN -------------------------------
draw_axis(canvas)

# ---
mainWindow.mainloop()

