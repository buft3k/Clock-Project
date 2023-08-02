import tkinter as tk
from tkinter import ttk
from time import strftime

myWindow = tk.Tk()
myWindow.geometry("500x500")
myWindow.title('Time Your Tasks')

def time():
    myTime = strftime('%I:%M:%S %p')
    clock.config(text=myTime)
    clock.after(1000, time)

def add_task():
    new_task = new_task_entry.get()
    if new_task:
        tasks['values'] = tasks['values'] + (new_task,)
        tasks.set(new_task)
        new_task_entry.delete(0, tk.END)

def move_up():
    selected_task = tasks.get()
    if selected_task:
        task_index = tasks['values'].index(selected_task)
        if task_index > 0:
            tasks['values'] = tasks['values'][:task_index-1] + (selected_task,) + tasks['values'][task_index-1:task_index] + tasks['values'][task_index+1:]
            tasks.set(selected_task)

def move_down():
    selected_task = tasks.get()
    if selected_task:
        task_index = tasks['values'].index(selected_task)
        if task_index < len(tasks['values']) - 1:
            tasks['values'] = tasks['values'][:task_index] + tasks['values'][task_index+1:task_index+2] + (selected_task,) + tasks['values'][task_index+2:]
            tasks.set(selected_task)

def remove_task():
    selected_task = tasks.get()
    if selected_task:
        tasks['values'] = tuple(task for task in tasks['values'] if task != selected_task)
        completed_tasks.pop(selected_task, None)
        not_completed_tasks.pop(selected_task, None)
        tasks.set('Select Task')

def on_task_selection(event):
    selected_task = tasks.get()
    if selected_task:
        completed.set(completed_tasks.get(selected_task, False))
        not_completed.set(not_completed_tasks.get(selected_task, False))

def update_completed_status():
    selected_task = tasks.get()
    if selected_task:
        completed_tasks[selected_task] = completed.get()
        not_completed_tasks[selected_task] = not_completed.get()

# Rest of the GUI elements
clock = tk.Label(myWindow, font=('arial', 40, 'bold'), background='dark green', foreground='white')
clock.pack(fill=tk.X, padx=10, pady=10)  # Placing the time label at the top and stretching it horizontally

# Entry field to add a new task
new_task_entry = tk.Entry(myWindow, font=('Arial', 15))
new_task_entry.pack(padx=10, pady=5)

# Button to add the task to the dropdown
add_button = tk.Button(myWindow, text='Add Task', font=('Arial', 15), command=add_task)
add_button.pack(padx=10, pady=5)

# Dropdown button for to-do tasks
tasks = ttk.Combobox(myWindow, font=('Arial', 15), state='readonly')
tasks['values'] = ()  # Add your initial tasks here
tasks.set('Select Task')
tasks.pack(padx=10, pady=10)
tasks.bind("<<ComboboxSelected>>", on_task_selection)

# Variables to store the completed and not completed statuses
completed = tk.BooleanVar()
not_completed = tk.BooleanVar()

# Check buttons to indicate task completion
completed_check = ttk.Checkbutton(myWindow, text="Completed", variable=completed)
completed_check.pack(padx=10, pady=5)

not_completed_check = ttk.Checkbutton(myWindow, text="Not Completed", variable=not_completed)
not_completed_check.pack(padx=10, pady=5)

# Dictionaries to keep track of completed and not completed tasks
completed_tasks = {}
not_completed_tasks = {}

# Buttons to rearrange the order of tasks
move_up_button = tk.Button(myWindow, text='Move Up', font=('Arial', 15), command=move_up)
move_up_button.pack(padx=10, pady=5)

move_down_button = tk.Button(myWindow, text='Move Down', font=('Arial', 15), command=move_down)
move_down_button.pack(padx=10, pady=5)

# Button to remove the selected task from the dropdown
remove_button = tk.Button(myWindow, text='Remove Task', font=('Arial', 15), command=remove_task)
remove_button.pack(padx=10, pady=5)

time()
myWindow.mainloop()
