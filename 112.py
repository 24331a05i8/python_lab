import tkinter as tk

def show():
   lbl.config(text=entry.get())

root = tk.Tk()

tk.Label(root, text="Enter Name").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Submit", command=show).pack()

lbl = tk.Label(root)
lbl.pack()

root.mainloop()



O
