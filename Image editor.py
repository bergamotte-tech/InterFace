from tkinter import *
import tkinter.font as tkFont
from tkinter.messagebox import *
from time import *
import numpy as np
from tkinter.colorchooser import *

def actionSquare(event):
    global can
    x = ((int) (event.x/100))
    y = ((int) (event.y/100))
    if x < 9 and y < 9 and x > 0 and y > 0:
        editSquare(event.num, [x, y])
    elif x == 10 and y < 7:
        if y == 1:
            editColor(y-1)
        elif y > 2 and y < 7:
            editColor(y-2)
    elif event.x >= 1000 and event.x <=1150 and event.y >= 900 and event.y <= 950:
        print("-----------------------")
        returnList = "["
        for i in range(len(listOfElement)):
            returnList += "["
            returnList += str(listOfElement[i][0])+","+str(listOfElement[i][1])
            returnList += ",["+str(listOfElement[i][2][0])+","+str(listOfElement[i][2][1])+","+str(listOfElement[i][2][2])+"]"
            returnList += "]"
            if(i < 63):
                returnList += ","
        returnList +="]"
        print(returnList)
    
def editColor(id):
    global colors
    if id == 0:
        color = askcolor()
        if color[0] != None:
            for i in range(4,0, -1):
                colors[i] = colors[i-1]
            colors[0] = color[1]
            reloadColorSelector()
    else:
        tempColor = colors[id]
        for i in range(4,0, -1):
            colors[i] = colors[i-1]
        colors[0] = tempColor
        reloadColorSelector()
            
def editSquare(num, coord):
    global can, colors
    x = coord[0]-1
    y = coord[1]-1
    setColor = "#ffffff"
    if num == 1:
        setColor=colors[0]
    for case in can.find_withtag(str(x)+","+str(y)):
        can.itemconfig(case, fill=setColor)
    listOfElement[x+y*8][2] = hexaToRgb(setColor)

def createArray():
    global listOfElement, colors
    for i in range (0,64):
        x = i%8
        y = (int) ((i-i%8)/8)
        listOfElement[i] = [x, y, [255,255,255]]
    for i in range(5):
        colors[i] = '#ffffff'

def createArea():
    global can, colors
    for i in range(0,64):
        x = i%8
        y = (int) ((i-i%8)/8)
        can.create_rectangle(100+x*100, 100+y*100, 200+x*100, 200+y*100, fill="white", width=5, tag=str(x)+","+str(y))
    for i in range(0,6):
        if i == 0:
            can.create_rectangle(1000,100+i*100,1100,200+i*100, fill=colors[i], width=2, tag="color"+str(i))
        elif i > 1:
            can.create_rectangle(1000,100+i*100,1100,200+i*100, fill=colors[i-1], width=2, tag="color"+str(i-1))
    can.create_rectangle(1000,900,1150,950, fill="white", width=2)
    can.create_text(1075, 925, text="Export", font=tkFont.Font(family='Arial', size=30, weight='bold'));

def reloadColorSelector():
    global colors
    for i in range(5):
        for case in can.find_withtag("color"+str(i)):
            can.itemconfig(case, fill=colors[i])

def hexaToRgb(color):
    return tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

fen=Tk()

haut=999
larg=1200
listOfElement = np.zeros(shape=(64), dtype=object)
colors = np.zeros(shape=(5), dtype=object)

fen.title("Funny face maker")
can=Canvas(fen, bg="white", height=haut,width=larg)
can.pack(expand=YES, fill=BOTH)

createArray()
createArea()

can.focus_set()
can.bind('<Button-1>', actionSquare)
can.bind('<Button-3>', actionSquare)

fen.mainloop()

