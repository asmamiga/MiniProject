import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
window.title('To-Do List')
window.geometry("400x270")

task = []
#Functions
def addTask():
    word = input1.get()
    if len(word)==0:
        messagebox.showinfo('Empty Entry', 'Enter task name')
    else:
        task.append(word)
        listUpdate()
        input1.delete(0,'end')

def listUpdate():
    clearList()
    for i in task:
        tList.insert('end', i)
    
def deleteOne():
    try:
        val = tList.get(tList.curselection())
        if val in task:
            task.remove(val)
            listUpdate()
    except:
        messagebox.showinfo('Cannot Delete', 'No Task Item Selected')
        
def deleteAll():
    mBox = messagebox.askyesno('Delete All','Are you sure?')
    if mBox==True:
        while(len(task)!=0):
            task.pop()
        listUpdate()
    
def clearList():
    tList.delete(0,'end')

#Functions
    
label1 = ttk.Label(window, text = 'To-Do List')
label2 = ttk.Label(window, text='Enter task title: ')
input1 = ttk.Entry(window, width=21)
tList = tk.Listbox(window, height=12, width=22, selectmode='SINGLE')
b1 = ttk.Button(window, text='Add task', width=20, command=addTask)
b2 = ttk.Button(window, text='Delete', width=20, command=deleteOne)
b3 = ttk.Button(window, text='Delete all', width=20, command=deleteAll)
listUpdate()
    
#Place geometry
label2.place(x=50, y=50)
input1.place(x=50, y=80)
b1.place(x=50, y=110)
b2.place(x=50, y=140)
b3.place(x=50, y=170)
label1.place(x=50, y=10)
tList.place(x=220, y=50)
window.mainloop()


    