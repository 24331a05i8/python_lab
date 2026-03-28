import tkinter as tk

root = tk.Tk()

menu = tk.Menu(root)
file = tk.Menu(menu, tearoff=0)
file.add_command(label="Open")
file.add_command(label="Exit", command=root.quit)

menu.add_cascade(label="File", menu=file)
root.config(menu=menu)

mb = tk.Menubutton(root, text="Options")
mb.menu = tk.Menu(mb, tearoff=0)
mb["menu"] = mb.menu
mb.menu.add_command(label="Option 1")

mb.pack()

root.mainloop()


