from tkinter import *
from PIL import ImageTk, Image

canvas_width = 300
canvas_height =300

master = Tk()

canvas = Canvas(master,
           width=canvas_width,
           height=canvas_height)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("a.png"))
canvas.create_image(20,20, anchor=NW, image=img)

mainloop()
