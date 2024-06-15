import tkinter as tk
from tkinter import ttk
from getWindowHwnd import getWindowIds
from action import getHwndFromName, resizeWindow
from getCoordinate import fightVsStrong
from workScript import get_works

import threading


rootX = 10
root = tk.Tk()
root.title("ngocronght auto")
root.geometry( "1022x630" ) 
padding = {'padx': 10, 'pady': 5}

windowNames = []
windows = []
width = 500
height = 850

def calculatePosX(rootX, widgets):
    x = rootX
    for widget in widgets:
        x += widget.winfo_width()
    
    return x


def calculatePosY(rootY, widgets):
    y = rootY
    for widget in widgets:
        y += widget.winfo_height()
    
    return y

def add_works_fn():
    print('add work')
def showWorkTableViewfn(table):
    works = get_works()
    if len(works) <= 0:
        return
    
    for idx, work in enumerate(works):
        table.insert(parent = '', index = idx, value = ('test', 'test','test', 'test'))


greeting = tk.Label(text="Select window")
greeting.place(x = rootX, y = 10)

def setWindowOptions():
    windowNames.clear()
    windows = getWindowIds()
    
    for window in windows:
        if window.name is not None and window.name != "":
            windowNames.append(window.name)
    
    # windowSeletected.set( windowNames[0] )

    return windowNames

def updateWindowOptions():
    windowSeletected.set("")
    windowMenu.children["menu"].delete(0, 'end')
    windowNames = setWindowOptions()
    for windowName in windowNames:
        windowMenu.children["menu"].add_command(label=windowName, command= tk._setit(windowSeletected, windowName, selectedWindowFn))

def getHwndFromWindowName(name):
    hwnd = getHwndFromName(name)
    return hwnd

root.update()
icon_image = tk.PhotoImage(file="images/reload.png")
button = tk.Button( root, image= icon_image , command = updateWindowOptions )
button.place(x = 20 + greeting.winfo_width(), y = 5)

# Dropdown menu options 



windowNames = setWindowOptions()



  
# datatype of menu text 
windowSeletected = tk.StringVar() 
  
# initial menu text 
# Create Dropdown menu 
root.update()
def selectedWindowFn():
    resizeWindow(windowSeletected.get(), width, height)

windowMenu = tk.OptionMenu( root , windowSeletected , *windowNames,command=selectedWindowFn)
windowMenu.grid(**padding)
windowMenu.place(x=10, y = 20 + button.winfo_height(), width=root.winfo_width() - 20)


root.update()
stateAction = False

def updateStateAction():
    global stateAction
    stateAction = True if stateAction is False else False

    if stateAction is True:
        fightStrongOpBtn.config(image = icon_pause)
        fightStrongOpBtn.image = icon_pause
        threading.Thread(target=loopAction).start()
    else:
        
        fightStrongOpBtn.config(image = icon_play)
        fightStrongOpBtn.image = icon_play
        

    return stateAction;

labelFSOpBtn = tk.Label(root, text="Khiêu chiến cường địch")
labelFSOpBtn.place(x = 10 , y = 20 + button.winfo_height() + windowMenu.winfo_height())
root.update()
icon_play = tk.PhotoImage(file="images/play.png")
icon_pause = tk.PhotoImage(file="images/pause.png")
fightStrongOpBtn = tk.Button(root, image= icon_play if stateAction is False else icon_pause, command= updateStateAction)
fightStrongOpBtn.place(y = 20 + button.winfo_height() + windowMenu.winfo_height(), x = 10 + labelFSOpBtn.winfo_width())
  
# define work
root.update()
work_label = tk.Label(text="Script work")
work_label.place(x = rootX, y = calculatePosY(30, [greeting,fightStrongOpBtn, windowMenu]))

root.update()
icon_add = tk.PhotoImage(file="images/add.png")
addWorkBtn = tk.Button( root, image= icon_add , command = add_works_fn )
addWorkBtn.place(x = calculatePosX(rootX + 10, [work_label]), y = calculatePosY(30, [greeting,fightStrongOpBtn, windowMenu]))

root.update()
workTableView = ttk.Treeview(root, columns=('name', 'posX', 'posY', 'overtime', 'action'), show='headings')
workTableView.heading('name')
workTableView.heading('posX')
workTableView.heading('posY')
workTableView.heading('overtime')
workTableView.place(x = rootX, y = calculatePosY(30, [greeting,fightStrongOpBtn, windowMenu, addWorkBtn]))
showWorkTableViewfn(workTableView)


root.update()
frame1 = tk.Frame(root,bg='lightblue', bd=3, cursor='hand2', height=100, 
                      highlightcolor='red', highlightthickness=2, highlightbackground='black', 
                      relief=tk.RAISED, width=200)
count = 1
for count in range(3):
    label = tk.Label(frame1, text='fuck')
    label.pack()

frame1.place(x = rootX, y = 20 + calculatePosY(30, [greeting,fightStrongOpBtn, windowMenu, workTableView]))


def loopAction():
    global stateAction
    try:
        while stateAction is True:
            fightVsStrong(windowSeletected.get())
    except Exception as err:
        print(err)
        print('stop')
        stateAction = False
        fightStrongOpBtn.config(image = icon_play)
        fightStrongOpBtn.image = icon_play
        # updateStateAction()


def main():
    setWindowOptions()

    tk.mainloop()


main()