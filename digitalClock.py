import tkinter as tk
from time import strftime
myWindow = tk.Tk()

myWindow.geometry("500x500")
myWindow.title('Time Your Tasks')
def time():
    myTime = strftime('%I:%M:%S %p')
    clock.config(text = myTime)
    clock.after(1000,time)
clock = tk.Label(myWindow, font = ('arial', 40,'bold'), background = 'dark green', foreground = 'white')
clock.place(x="0",y="0", height= 50, width= 500)


#myEntry = tk.Entry(myWindow)
#myEntry.pack()

#button = tk.Button(myWindow,text = 'To Do List', font = ('Arial', 15))
#button.pack(padx = 10, pady = 10)


time()
myWindow.mainloop()