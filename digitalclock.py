import tkinter as tk
from time import strftime

def update_time():
    string_time = strftime('%H:%M:%S %p')
    label.config(text=string_time)
    label.after(1000, update_time)  # Update every 1000 milliseconds (1 second)

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

update_time()  # Call the function to initialize the clock

root.mainloop()
