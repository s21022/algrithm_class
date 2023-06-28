import tkinter
root = tkinter.Tk()
root.title("")
cvs = tkinter.Canvas(width=600, height=600, bg="white")
cvs.pack()

ox = 300
oy = 300
cvs.create_text(ox+20, oy+10, text="(0,0)")
cvs.create_line(ox, 0, ox, 600, fill="gray")
for y in range(0, 600, 50):
    cvs.create_line(ox-5, y, ox+5, y, fill="silver")
cvs.create_line(0, oy, 600, oy, fill="gray")
for x in range(0, 600, 50):
    cvs.create_line(x, oy-5, x, oy+5, fill="silver")

root.mainloop()