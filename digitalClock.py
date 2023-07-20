import tkinter as tk
from time import strftime
myWindow = tk.Tk()
myWindow.title('Time Your Tasks')
def time():
    myTime = strftime('%I:%M:%S %p')
    clock.config(text = myTime)
    clock.after(1000,time)
clock = tk.Label(myWindow, font = ('arial', 40,'bold'), background = 'dark green', foreground = 'white')

clock.pack(anchor = 'center')
time()
myWindow.mainloop()