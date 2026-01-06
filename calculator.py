import tkinter as tk
import math

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        clear()
        entry.insert(0, result)
    except:
        clear()
        entry.insert(0, "Error")

def sin():
    value = float(entry.get())
    clear()
    entry.insert(0, math.sin(math.radians(value)))

def cos():
    value = float(entry.get())
    clear()
    entry.insert(0, math.cos(math.radians(value)))

def tan():
    value = float(entry.get())
    clear()
    entry.insert(0, math.tan(math.radians(value)))

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("320x420")

entry = tk.Entry(root, font=("Arial", 18), bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, padx=10, pady=10)

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

frame = tk.Frame(root)
frame.pack()

row = 0
col = 0
for b in buttons:
    action = lambda x=b: click(x) if x != "=" else calculate()
    tk.Button(frame, text=b, width=5, height=2, command=action).grid(row=row, column=col)
    col += 1
    if col == 4:
        col = 0
        row += 1

tk.Button(root, text="sin", width=8, command=sin).pack(side=tk.LEFT, padx=5)
tk.Button(root, text="cos", width=8, command=cos).pack(side=tk.LEFT, padx=5)
tk.Button(root, text="tan", width=8, command=tan).pack(side=tk.LEFT, padx=5)
tk.Button(root, text="C", width=8, command=clear).pack(side=tk.LEFT, padx=5)

root.mainloop()
