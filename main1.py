from tkinter import *

root = Tk()
root.geometry("300x150")

w = Label(root, text="choco and icecreams", font="50")
w.pack()

f1 = Frame(root)
f1.pack()

b1 = Button(f1, text = "choco", fg = "red", bg = "beige")
b1.pack(side=LEFT)
b2 = Button(f1, text = "dark choco", fg = "brown", bg = "beige")
b2.pack(side=LEFT)
b3 = Button(f1, text = "white choco", fg = "blue", bg = "beige")
b3.pack(side=LEFT)

f2 = Frame(root)
f2.pack()

b4 = Button(f2, text = "tiramisu", fg = "white", bg = "black")
b4.pack(side=BOTTOM)
b5 = Button(f2, text = "cake", fg = "red", bg = "pink")
b5.pack(side=BOTTOM)
b6 = Button(f2, text = "cupcake", fg = "pink", bg = "brown")
b6.pack(side=BOTTOM)
root.mainloop()