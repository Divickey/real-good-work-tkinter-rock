from tkinter import *

root = Tk()
root.geometry("300x250")

l1 = Label(root, text="food items", font=50)
l1.pack()

fitems = Listbox(root, height=10, width=15, bg="black", activestyle='dotbox', font="Blackadder", fg="light green")
fitems.insert(1, "[ cheese fondue ]")
fitems.insert(2, "[ griled cheese sandwich ]")
fitems.insert(3, "[ teriyaki chicken rice ]")
fitems.insert(4, "[ wagyu don ]")
fitems.insert(5, "[ wan ton mee ]")
fitems.pack()
root.mainloop()