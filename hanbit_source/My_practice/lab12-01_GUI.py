from tkinter import *

def clickLeft(e):
    canvas.create_oval(e.x-20, e.y-20 , e.x +20, e.y + 20, width = 5, outline = "green")

def clickRight(e):
    canvas.create_rectangle(e.x -20, e.y -20, e.x + 20, e.y + 20, width=5, outline= "red")



root = Tk()
canvas = Canvas(root, height=500, width=500)
canvas.pack()

canvas.bind("<Button-1>", clickLeft)
canvas.bind("<Button-3>", clickRight)

root.mainloop()