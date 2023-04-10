from tkinter import *
from random import *

startX = 0
startY = 0
endX = 0
endY = 0

colorlist = ["green", "red" , "black" , "magenta"]
color = choice(colorlist)

def start_drag(event):
    global startX, startY, endX, endY
    # 드래그 시작 위치의 좌표 출력
    startX = event.x 
    startY = event.y

def end_drag(event):
    global startX, startY, endX, endY
    endX = event.x
    endY = event.y
    canvas.create_rectangle(startX, startY, endX, endY, width=5, outline=color)

def colorselect(event):
    global color
    colorlist = ["green", "red" , "black" , "magenta"]
    color = choice(colorlist)
    return color

root = Tk()


canvas = Canvas(root, height=500, width=500)
canvas.pack()

canvas.bind("<Button-1>", start_drag)
canvas.bind("<ButtonRelease-1>", end_drag)
canvas.bind("<Button-3>", colorselect)



root.mainloop()