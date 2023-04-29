from tkinter import *
top=Tk()

x = IntVar()
y = IntVar()

C1 = Checkbutton(top, text = "Music", variable = x, onvalue = 1, offvalue = 0, height=5,  width = 20)
C2 = Checkbutton(top, text = "Video", variable = y, onvalue = 1, offvalue = 0, height=15, width = 50)

C1.pack()
C2.pack()

top.mainloop()