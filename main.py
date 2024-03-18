# import time
# import time
import turtle as tur
import colorsys as cs
from tkinter import *
import messagebox
#
# Full Screen
screen = tur.Screen()
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)
# Close Programme
def close():
    messagebox.showinfo(title="Goodbye", message="See you later...")
    screenTk.destroy()
def Max():
    screenTk.attributes("-fullscreen", True)
def Min():
    result = messagebox.askyesnocancel("Do you want to make the screen minimized?", "Select the chose (Y/N)?")
    if result == True:
        messagebox.showinfo('😃','The screen is minimized !')
        screenTk.attributes("-fullscreen", False)
    elif result == False:
        messagebox.showinfo('😄', 'Minimized!')
        Max()
    elif result == None:
        messagebox.showinfo('😭', 'Bye!')
        close()
    # if result == None:
    #     messagebox.showinfo('', 'Cancel button clicked!')
# btn close
Button(text="Exit",font=('Times New Roman',), height='1', width='4', bg="#EEE2DE",
       fg="#B31312",command=close).place(x=1478, y=4)
Button(text="Max",font=('Times New Roman',), height='1', width='4', bg="#EEE2DE",
       fg="#B31312",command=Max).place(x=1424, y=4)

Button(text="Min",font=('Times New Roman',), height='1', width='4', bg="#EEE2DE",
       fg="#B31312",command=Min).place(x=1375, y=4)
# Label(text="If want exit\nYou should press button",bg='#00004d',fg='red',font=('Times New Roman',20)).place(x=80, y=4)
Label(text="👉",bg='#00004d',fg='red',font=('',20)).place(x=1340, y=4)
# Create Turtle
tur.speed(0)
tur.tracer(10)
tur.width(2)
tur.bgcolor("#00004d")       # Background Page
# tur.pencolor("#00004d")
def screen_1():
    for j in range(25):
        for i in range(15):
            tur.color(cs.hsv_to_rgb(i/15, j/25,1))
            tur.right(90)
            tur.circle(200-j*4, 90)
            tur.left(90)
            tur.circle(200 - j * 4, 90)
            tur.right(180)
            tur.circle(50 ,24)
    tur.reset()
def screen_2():
    for j in range(25):
        for i in range(15):
            tur.color(cs.hsv_to_rgb(i / 80, j / 25, 1))
            tur.right(90)
            tur.circle(200 - j * 4, 90)
            tur.left(90)
            tur.circle(200 - j * 4, 90)
            tur.right(180)
            tur.circle(50, 24)
    tur.reset()
def screen_3():
    colors = ['#11ECFA', '#02A4DB', '#0084F0', '#009DFF', '#0029FF', '#024FDB']
    t = tur.Pen()
    tur.bgcolor('#00004d')
    for x in range(500):
        t.pencolor(colors[x%6])
        t.width(x//100 + 1)
        t.forward(x)
        t.left(59)
    t.reset()
def screen_3_1():
    colors = ['#D7F200', '#FFE000', '#EFB101', '#F56E00', '#FF3200', '#FF1001']
    t = tur.Pen()
    tur.bgcolor('#00004d')
    for x in range(500):
        t.pencolor(colors[x%6])
        t.width(x//100 + 1)
        t.forward(x)
        t.left(59)
    t.reset()
def screen_4():
    tur.hideturtle()
    tur.speed(0)
    c = 0
    x = 0
    colors = [
    #reddish colors
    (1.00, 0.00, 0.00),(1.00, 0.03, 0.00),(1.00, 0.05, 0.00),(1.00, 0.07, 0.00),(1.00, 0.10, 0.00),(1.00, 0.12, 0.00),(1.00, 0.15, 0.00),(1.00, 0.17, 0.00),(1.00, 0.20, 0.00),(1.00, 0.23, 0.00),(1.00, 0.25, 0.00),(1.00, 0.28, 0.00),(1.00, 0.30, 0.00),(1.00, 0.33, 0.00),(1.00, 0.35, 0.00),(1.00, 0.38, 0.00),(1.00, 0.40, 0.00),(1.00, 0.42, 0.00),(1.00, 0.45, 0.00),(1.00, 0.47, 0.00),
    #orangey colors
    (1.00, 0.50, 0.00),(1.00, 0.53, 0.00),(1.00, 0.55, 0.00),(1.00, 0.57, 0.00),(1.00, 0.60, 0.00),(1.00, 0.62, 0.00),(1.00, 0.65, 0.00),(1.00, 0.68, 0.00),(1.00, 0.70, 0.00),(1.00, 0.72, 0.00),(1.00, 0.75, 0.00),(1.00, 0.78, 0.00),(1.00, 0.80, 0.00),(1.00, 0.82, 0.00),(1.00, 0.85, 0.00),(1.00, 0.88, 0.00),(1.00, 0.90, 0.00),(1.00, 0.93, 0.00),(1.00, 0.95, 0.00),(1.00, 0.97, 0.00),
    #yellowy colors
    (1.00, 1.00, 0.00),(0.95, 1.00, 0.00),(0.90, 1.00, 0.00),(0.85, 1.00, 0.00),(0.80, 1.00, 0.00),(0.75, 1.00, 0.00),(0.70, 1.00, 0.00),(0.65, 1.00, 0.00),(0.60, 1.00, 0.00),(0.55, 1.00, 0.00),(0.50, 1.00, 0.00),(0.45, 1.00, 0.00),(0.40, 1.00, 0.00),(0.35, 1.00, 0.00),(0.30, 1.00, 0.00),(0.25, 1.00, 0.00),(0.20, 1.00, 0.00),(0.15, 1.00, 0.00),(0.10, 1.00, 0.00),(0.05, 1.00, 0.00),
    #greenish colors
    (0.00, 1.00, 0.00),(0.00, 0.95, 0.05),(0.00, 0.90, 0.10),(0.00, 0.85, 0.15),(0.00, 0.80, 0.20),(0.00, 0.75, 0.25),(0.00, 0.70, 0.30),(0.00, 0.65, 0.35),(0.00, 0.60, 0.40),(0.00, 0.55, 0.45),(0.00, 0.50, 0.50),(0.00, 0.45, 0.55),(0.00, 0.40, 0.60),(0.00, 0.35, 0.65),(0.00, 0.30, 0.70),(0.00, 0.25, 0.75),(0.00, 0.20, 0.80),(0.00, 0.15, 0.85),(0.00, 0.10, 0.90),(0.00, 0.05, 0.95),
    #blueish colors
    (0.00, 0.00, 1.00),(0.05, 0.00, 1.00),(0.10, 0.00, 1.00),(0.15, 0.00, 1.00),(0.20, 0.00, 1.00),(0.25, 0.00, 1.00),(0.30, 0.00, 1.00),(0.35, 0.00, 1.00),(0.40, 0.00, 1.00),(0.45, 0.00, 1.00),(0.50, 0.00, 1.00),(0.55, 0.00, 1.00),(0.60, 0.00, 1.00),(0.65, 0.00, 1.00),(0.70, 0.00, 1.00),(0.75, 0.00, 1.00),(0.80, 0.00, 1.00),(0.85, 0.00, 1.00),(0.90, 0.00, 1.00),(0.95, 0.00, 1.00)
    ]
    while x < 1000:
        idx = int(c)
        color = colors[idx]
        tur.color(color)
        tur.forward(x)
        tur.right(98)
        x = x + 1
        c = c + 0.1
    tur.reset()
def screen_5():
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    t = tur.Pen()
    tur.bgcolor('#00004d')
    for x in range(500):
        t.pencolor(colors[x%6])
        t.width(x//100 + 1)
        t.forward(x)
        t.left(59)
    t.reset()
# Loop Turtle
while True:
    for s in range(1,100):
        screen_4()
        screen_1()
        screen_5()
        screen_2()
        screen_3()
        screen_3_1()
        continue
    continue

tur.hideturtle()
tur.done()
screenTk.mainloop()